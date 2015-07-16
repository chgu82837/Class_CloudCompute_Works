PythonHW2_s101056017
==========================

### Server

To start the server, use following command to open the GUI console:

```
python ./PythonHW2_s101056017_server.py
```

This will bring up a GUI server console, change the `ADDRESS TO BIND`, `PORT` and `MAX_CLIENT_NUMBER` on your own need (`127.0.0.1` to restrict client to be the same computer). Press the `Start` Button to start the server  

After service started, you can press the button again to stop the server.  

The People list will list the peoples (accounts) in the bank:  

```
<is_login?*><name>:<money>
```

### Client GUI

To start the client, use following command to open the GUI login console:

```
python ./PythonHW2_s101056017_client.py
```

This will bring up a GUI login console, input `HOST TO CONNECT`, `PORT`, `Username` and `Password` on demand (There is a default user `user` with password `12345`), left `Password` blank if a user has no password. Press `Connect` to enter client console.  

If you login to a non-exist user, system will create one for you. If you have `Password` entered, system will insert the password you entered to the new user.  

#### Client console

There are some function I implemented:

 1. Logout (and relogin)
 2. Blance inquriries
 3. Deposit
 4. Withdraw
 5. Fund transfer
 6. PASSWD (change password)
