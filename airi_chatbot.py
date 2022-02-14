import airi
import asyncio

async def test():
    
   

    
  client = airi.Client("a000829197726937c46bc5f0f9b55ecbb932e9a4c92a")
  # above, TOKEN is AIRI API TOKEN
  fact = await client.action('bye')

  print(fact)
    
asyncio.get_event_loop().run_until_complete(test())