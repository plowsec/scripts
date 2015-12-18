
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

        CharSequence cs = "Hi how are u";
        HashMap<String, String> data = new HashMap<String, String>();
        data.put("data", cs.toString());
        AsyncHttpPost asyncHttpPost = new AsyncHttpPost(data);
        asyncHttpPost.execute("http://");
}
public class AsyncHttpPost extends AsyncTask<String, String, String> {
    private HashMap<String, String> mData = null;// post data
    public AsyncHttpPost(HashMap<String, String> data) {
        mData = data;
    }
    @Override
    protected String doInBackground(String... params) {
        byte[] result = null;
        String str = "";
        HttpClient client = new DefaultHttpClient();
        HttpPost post = new HttpPost(params[0]);// in this case, params[0] is URL
        try {
            ArrayList nameValuePair = new ArrayList();
            Iterator it = mData.keySet().iterator();
            while (it.hasNext()) {
                String key = it.next();
                nameValuePair.add(new BasicNameValuePair(key, mData.get(key)));
            }

            post.setEntity(new UrlEncodedFormEntity(nameValuePair, "UTF-8"));
            HttpResponse response = client.execute(post);
            StatusLine statusLine = response.getStatusLine();
            if(statusLine.getStatusCode() == HttpURLConnection.HTTP_OK){
                result = EntityUtils.toByteArray(response.getEntity());
                str = new String(result, "UTF-8");
            }
        }
        catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        catch (Exception e) {
        }
        return str;
    }

    @Override
    protected void onPostExecute(String result) {
// something...
    }
}
