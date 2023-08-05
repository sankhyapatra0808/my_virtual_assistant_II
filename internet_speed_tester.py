def speed_check():
    import speedtest
    try:
        test = speedtest.Speedtest()
        down = test.download()
        # upload = test.upload()
        print("DOWNLOADING SPEED RIGHT NOW IS ...", (down / 1024) / 1024)
        # print("Uploading speedtest...", upload)
    except:
        print("YOUR NETWORK SPEED IS REALLY SLOW AND YOU CAN FACE NETWORK ISSUE...")

# c150208
