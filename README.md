# LaravelDebugModeEnabled
![image](https://user-images.githubusercontent.com/91685640/153610818-2085eb64-209f-43ff-9d43-2cbc7ebaed26.png)



<h1>Note</h1>
You need to have shodan Api key and type "shodan init XXXXXXXXapikeyXXXXX" to activate your account

<h1>Description</h1>
Laravel.py find the laravel debug mode enabled server with the help of shodan 
Here you provide list of domain you want to search for 
domain list should be in specific format --> www.google.com[Invalid] || google[valid]

<h1>Usage</h1>

<table>
<thead>
<tr>
<th>Argument</th>
<th>Description</th>
<th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
<td>-d</td>
<td>provide path to the wordlist</td>
<td>'C:\\Users\\AVADH\\Desktop\\Automation\\domain.txt'</td>
</tr>
<tr>
<td>-s</td>
<td>Provide Shodan API key</td>
<td>TnJ92ZwOblwDxxxxxxxxx</td>
</tr>
</tbody>
</table>
  
  
<h2>Usage1</h2><h4>python Laravel.py  -d  'C:\\Users\\AVADH\\Desktop\\Automation\\domain.txt'  -s  "TnJ92ZwOblwDbq7jbrRUxxxxxxxxx"</h4>
  
  
<h1>OUTPUT</h1>
You will get two files with the name domainIpFile.txt [maps Ip with the domain name]
second is Finalresponse which is the final output which contains server response which may contain redis cache uri or mongoDB URI 
You will get above two file in same directory you provide as argument
you could also add Regular expression for AWSAccessKey -- > A[SK]IA\w{16}
you could also add Regular expression for SectetKey -[a-zA-Z0-9\/\=]{40} in the source code for further finding

  
<h1>Installation</h1>
 
    Clone the repository to your machine. git clone https://github.com/Aviack/DjangoBango.git
    cd DjangoBango
    Install required modules by running the code pip install -r requirements.txt
    READY!
