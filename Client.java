import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

public class TcpClient extends Activity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        runTcpClient();
        finish();
    }

    private static final int TCP_SERVER_PORT = 27371;//should be same to the server port

    private void runTcpClient() {
        try {
            Socket s = new Socket("AA:AA:AA:AA:AA:AA", TCP_SERVER_PORT);//Note that the host is changed to the hostname or IP address of your server. < br / >
            BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
            BufferedWriter out = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
            //send output msg
            SimpleDateFormat formatter= new SimpleDateFormat("HH:mm:ss");
            Date date = new Date(System.currentTimeMillis());
            String outMsg = formatter.format(date) + " ";//"TCP connecting to " + TCP_SERVER_PORT + System.getProperty("line.separator");
            out.write(outMsg);//Send data & NBSP; < br / >
            out.flush();
            Log.i("TcpClient", "sent: " + outMsg);
            //accept server response
            String inMsg = in.readLine() + System.getProperty("line.separator");//Gets the data & NBSP; returned by the server; < br / >
            Log.i("TcpClient", "received: " + inMsg);
            //close connection
            s.close();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    //replace runTcpClient() at onCreate with this method if you want to run tcp client as a service
    private void runTcpClientAsService() {
        Intent lIntent = new Intent(this.getApplicationContext(), TcpClientService.class);
        this.startService(lIntent);
    }
}
