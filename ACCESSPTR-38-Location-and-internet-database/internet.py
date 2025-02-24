import speedtest   
  
print("Running speed test... ")
st = speedtest.Speedtest() 
servernames =[]
st.get_servers(servernames)     

print(f"Download Speed: {st.download()/1e6:.2f}  Mbps") 
print(f"Upload Speed: {st.upload()/1e6:.2f}  Mbps") 
print("Ping: " + str(st.results.ping)) 

  
       
  
    
  


#https://www.geeksforgeeks.org/test-internet-speed-using-python/