/*#include <Windows.h>
#include <WinInet.h>
#include <iostream>
#include <string>*/

#include <Windows.h>
#include <WinInet.h>
#include <iostream>
#include <string>
//#pragma comment (lib, "Wininet.lib") for gcc, delete .lib at the end. 
//#pragma comment (lib, "urlmon.lib")
#define POST 1
#define GET 0


//link wininet


std::string sendRequest(int Method, LPCSTR Host, LPCSTR url, LPCSTR header, LPSTR data
{
    char m[5];

    if(Method == GET)
        strcpy(m, "GET");
	else
		strcpy(m, "POST");
		
  HINTERNET hInternet = InternetOpenW(L"PONEY OF DOOM", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);

  if( hInternet==NULL )
  {
    std::cout << "InternetOpenW failed with error code " << GetLastError() << std::endl;
  }
  else
  {
    HINTERNET hConnect = InternetConnectW(hInternet, Host, INTERNET_DEFAULT_HTTP_PORT, NULL, NULL, INTERNET_SERVICE_HTTP, 0, 0);

    if( hConnect==NULL )
    {
      std::cout << "InternetConnectW failed with error code " << GetLastError() << std::endl;
    }
    else
    {
      //const wchar_t* parrAcceptTypes[] = { L"text/*", NULL };
      HINTERNET hRequest = HttpOpenRequestW(hConnect, m, url, "HTTP/1.1", NULL, NULL, INTERNET_FLAG_HYPERLINK | INTERNET_FLAG_IGNORE_CERT_CN_INVALID |
					INTERNET_FLAG_IGNORE_CERT_DATE_INVALID |
					INTERNET_FLAG_IGNORE_REDIRECT_TO_HTTP  |
					INTERNET_FLAG_IGNORE_REDIRECT_TO_HTTPS |
					INTERNET_FLAG_NO_AUTH |
					INTERNET_FLAG_NO_CACHE_WRITE |
					INTERNET_FLAG_NO_UI |
					INTERNET_FLAG_PRAGMA_NOCACHE |
					INTERNET_FLAG_RELOAD, NULL);

      if( hRequest==NULL )
      {
        std::cout << "HttpOpenRequestW failed with error code " << GetLastError() << std::endl;
      }
      else
      {
        int datalen = 0;
        if(data != NULL) 
            datalen = strlen(data);
        int headerlen = 0;
	    if(header != NULL) 
	        headerlen = strlen(header);
        
        BOOL bRequestSent = HttpSendRequestW(hRequest, header, headerlen, data, datalen);

        if( !bRequestSent )
        {
          std::cout << "HttpSendRequestW failed with error code " << GetLastError() << std::endl;
        }
        else
        {
          std::string strResponse;
          const int nBuffSize = 1024;
          char buff[nBuffSize];

          BOOL bKeepReading = true;
          DWORD dwBytesRead = -1;

          while(bKeepReading && dwBytesRead!=0)
          {
            bKeepReading = InternetReadFile( hRequest, buff, nBuffSize, &dwBytesRead );
            strResponse.append(buff, dwBytesRead);
          }

          std::cout << strResponse << std::endl;
        }

        InternetCloseHandle(hRequest);
      }

      InternetCloseHandle(hConnect);
    }

    InternetCloseHandle(hInternet);
  }

  return 0;
}
