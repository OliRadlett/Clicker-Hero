package oli.clicker_hero;

import android.app.VoiceInteractor;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;

// TODO Add POST response listener to get returned amount of money

public class MainActivity extends AppCompatActivity {

    public void POST(RequestQueue rq, final String key, final String value) {

        // String url = "http://51.140.230.235:1234"; /* Address for remote server */
        String url = "http://192.168.1.144:1234"; /* Address for PC (Carsington) */
        StringRequest request = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                System.out.println(response);
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                System.out.println(error);
            }
        }) {

            protected Map<String, String> getParams() {

                Map<String, String> data = new HashMap<String, String>();
                data.put(key, value);
                return data;

            }

        };

        rq.add(request);

    }

    public void GET(RequestQueue rq, String param, final VolleyCallback callback) {

        // String url = "http://51.140.230.235:1234"; /* Address for remote server */
        String url = "http://192.168.1.144:1234" + param; /* Address for PC (Carsington) */
        StringRequest request = new StringRequest(Request.Method.GET, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                callback.onSuccess(response);
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                System.out.println(error);
            }
        });

        rq.add(request);

    }

    public interface VolleyCallback {
        void onSuccess(String result);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final RequestQueue queue = Volley.newRequestQueue(this);

        final Button getTest = findViewById(R.id.get_test);
        final TextView getTestReturn = findViewById(R.id.getTestReturn);

        getTest.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {

                GET(queue, "/test", new VolleyCallback() {
                    @Override
                    public void onSuccess(String result) {
                        getTestReturn.setText(result);
                    }
                });

            }

        });

    }

}
