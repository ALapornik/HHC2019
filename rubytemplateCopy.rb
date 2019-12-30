KEY_LENGTH = 8 # TODO: What is the length of the key?

def super_secure_random(seed)
 
  seed = seed >> 16
  seed = seed & 0x7fff
  
  return seed
end  


def generate_key(seed)
  key = ""
  1.upto(KEY_LENGTH) do
    seed *= 214013
    seed += 2531011
    
    # puts("seed: #{seed>>16 & 0x7fff}")
    


    key += ((seed >>16 & 0x7fff )& 0x0FF).chr # TODO: How's the RNG work?
    
  end

  return key
end


# main

file = File.open("keysarr.txt","w")
seed = 1575658800
1.upto(7200) do
  key = generate_key(seed)
  file.puts "#{key.unpack('H*')}"
  seed+=1
end

file.close
