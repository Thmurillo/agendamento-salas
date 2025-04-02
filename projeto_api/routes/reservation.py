from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import select, func
from datetime import date, time ,timedelta, datetime
from models.reservation import Reservation
from models.room import Room
from models.user import User
from models.block import Block
from database import get_session
from schemas.reservation import ReservationCreate, ReservationResponse, ReservationSequencialCreate
from schemas.report import ReportResponse
from copy import deepcopy
import logging

router = APIRouter()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def log_upcoming_reservation(reservation, room, block):
                future_date = datetime.combine(reservation.date, reservation.start_time) - timedelta(hours=1)
                logging.info(f"[Notificação] Reserva para a sala {room.number} disposta no bloco {block.block_name} às {reservation.start_time} no dia {reservation.date}. Enviar alerta em {future_date}")


async def verification_of_reservation_date( base_Reservation, new_reservation, date_with_conflict, session ):
        result = await session.execute(select(base_Reservation).where((base_Reservation.room_id == new_reservation.room_id)& (base_Reservation.date == new_reservation.date)))
        existance_reservation = result.scalars().all()

        for existance in existance_reservation:
            if (existance.start_time <= new_reservation.end_time and existance.end_time>= new_reservation.start_time):
                date_with_conflict.append(new_reservation.date)
                return False
        return True

async def multi_reservation(base_Reservation, new_reservation, date_with_conflict,room, block, session):
    if await verification_of_reservation_date(base_Reservation, new_reservation, date_with_conflict, session):
        new_instance_reservation = deepcopy(new_reservation)
        session.add(new_instance_reservation)
        await session.commit()
        log_upcoming_reservation(new_reservation, room,block)
        new_reservation.date = new_reservation.date + timedelta(days= 7)
    else:
        new_reservation.date = new_reservation.date + timedelta(days= 7)

        
        
        
    

async def multi_reservation_recursion(base_Reservation, new_reservation, end_date_reservation, date_with_conflict,room, block, session):
    await multi_reservation(base_Reservation, new_reservation, date_with_conflict,room, block, session)
    if(new_reservation.date <= end_date_reservation):
        await multi_reservation_recursion(base_Reservation, new_reservation, end_date_reservation, date_with_conflict,room, block, session)
    

            


@router.post("/reservation", response_model=ReservationResponse, status_code=status.HTTP_201_CREATED)
async def create_reservation(reservation: ReservationCreate, session: AsyncSession = Depends(get_session)):
     
    result_block = await session.execute(select(Block).where(Block.block_name == reservation.block_name))
    block = result_block.scalars().first()

    if not block:
        raise HTTPException(status_code=404, detail="Bloco não encontrado.")

    result_room = await session.execute(select(Room).where(Room.number == reservation.room_number, Room.block_id == block.id))
    room = result_room.scalars().first()


    if not room:
        raise HTTPException(status_code=404, detail="Sala não encontrada.")

    
    result_user = await session.execute(select(User).where(User.user_name == reservation.user_name))
    user = result_user.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    
    new_reservation = Reservation(
        block_id=block.id,
        room_id=room.id,
        user_id=user.id,
        date=reservation.date,
        start_time=reservation.start_time,
        end_time=reservation.end_time,
        requester_course = reservation.requester_course,
        confirmation=reservation.confirmation,
        reason=reservation.reason
    )

    restriction_result = await session.execute(select(Room.restriction).where(new_reservation.room_id == Room.id))
    room_restriction = restriction_result.scalars().first()

    if (room_restriction == "Geral" or new_reservation.requester_course == room_restriction):

        result = await session.execute(select(Reservation).where(
            Reservation.room_id == room.id,
            Reservation.date == reservation.date))
        existing_reservations = result.scalars().all()

        for existing in existing_reservations:
            if (reservation.start_time < existing.end_time and reservation.end_time > existing.start_time):
                raise HTTPException(status_code=400, detail="Horário já reservado para essa sala.")
        else:

            session.add(new_reservation)
            await session.commit()
            log_upcoming_reservation(new_reservation, room,block)
            await session.refresh(new_reservation)
            return new_reservation

        

    else:
        raise HTTPException(status_code=442, detail="Curso incopativel")
    
@router.post("/reservation/sequence", status_code=status.HTTP_201_CREATED)
async def reservation_more_days(reservation: ReservationSequencialCreate, session:AsyncSession= Depends(get_session)):
    date_with_conflict = []
    user_result = await session.execute(select(User).where(User.user_name == reservation.user_name))
    user = user_result.scalars().first()
    if not user:
        raise(HTTPException(status_code=404, detail= "User not found"))
    
    block_result = await session.execute(select(Block).where(Block.block_name == reservation.block_name))
    block = block_result.scalars().first()
    if not block:
        raise HTTPException(status_code=404, detail="block not found")
    
    room_result = await session.execute(select(Room).where ((Room.number == reservation.room_number) & (Room.block_id == block.id)))
    room = room_result.scalars().first()
    if not room:
        raise HTTPException(status_code= 404, detail="Room not found")

    new_reservation = Reservation(
        block_id = block.id,
        room_id = room.id,
        user_id = user.id,
        date = reservation.start_date,
        start_time = reservation.start_time,
        end_time = reservation.end_time,
        requester_course = reservation.requester_course,
        confirmation = reservation.confirmation,
        reason = reservation.reason
    )

    if (room.restriction == "Geral" or room.restriction == new_reservation.requester_course):
        
        await multi_reservation_recursion(Reservation, new_reservation, reservation.end_date, date_with_conflict, room, block, session)
    else:
        raise HTTPException(status_code=400, detail="Room have restricition")
    
    return {
        "Reservation concluded": "...",
        "Reservation for the following days conflicted": date_with_conflict
    }

                



@router.get("/reservation/{data_search}/{time_search}", response_model= list[ReservationResponse], status_code=status.HTTP_200_OK)
async def search_reservation_for_data(data_search: date, time_search: time,session: AsyncSession = Depends(get_session)):
    data_result = await session.execute(select(Reservation).where((Reservation.date == data_search) & (Reservation.start_time <= time_search) & (time_search <= Reservation.end_time )))
    reservation = data_result.scalars().all()

    if not reservation:
        return "All rooms avaliable"
    
    return reservation

@router.get("/reservation", response_model=list[ReservationResponse], status_code=status.HTTP_200_OK)
async def show_reservations(session: AsyncSession = Depends(get_session)):
    data_result = await session.execute(select(Reservation))
    reservation = data_result.scalars().all()

    if not reservation:
        return "All rooms avaliable"
    
    return reservation

@router.delete("/reseration/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_reservation(reservation_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Reservation).where(Reservation.id == reservation_id))
    reservation_delete = result.scalars().first()

    if not reservation_delete:
        raise HTTPException(status_code=404, details="Reservation not found")

    await session.delete(reservation_delete)
    await session.commit()


@router.get("/report")
async def generate_report(session: AsyncSession = Depends(get_session)):
    
    result = await session.execute(
        select(Reservation.room_id, func.count().label("total"))
        .group_by(Reservation.room_id)
        .order_by(func.count().desc())
    )
    most_reserved = [{"room_id": row[0], "total": row[1]} for row in result.all()]

    
    result = await session.execute(
        select(Reservation.start_time, func.count().label("total"))
        .group_by(Reservation.start_time)
        .order_by(func.count().desc())
    )
    peak_hours = [{"start_time": row[0], "total": row[1]} for row in result.all()]

    return ReportResponse(room_mensage= "The room most reported:", most_reserved_room= most_reserved, hour_mensage= "The peak_hours:", peak_hour= peak_hours)
