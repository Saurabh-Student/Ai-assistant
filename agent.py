from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
    noise_cancellation,
)
from jarvis_prompt import _Behavoiur_prompts,Reply_prompts
from jarvis_search import google_search

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=_Behavoiur_prompts, tools=[google_search])


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            voice="charon"
            
            
        )
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
            video_enabled=True
        ),
    )
    await ctx.connect()

    await session.generate_reply(
        instructions=Reply_prompts
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))