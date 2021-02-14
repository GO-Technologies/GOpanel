#!/bin/bash
echo "Content-type: text/html"
echo ''
echo '<title>GOpanel</title>'
echo '<link rel="apple-touch-icon" sizes="57x57" href="/GOpanel/apple-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="/GOpanel/apple-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="/GOpanel/apple-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="/GOpanel/apple-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="/GOpanel/apple-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="/GOpanel/apple-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="/GOpanel/apple-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="/GOpanel/apple-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="/GOpanel/apple-icon-180x180.png">
<link rel="icon" type="image/png" sizes="192x192"  href="/GOpanel/android-icon-192x192.png">
<link rel="icon" type="image/png" sizes="32x32" href="/GOpanel/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="96x96" href="/GOpanel/favicon-96x96.png">
<link rel="icon" type="image/png" sizes="16x16" href="/GOpanel/favicon-16x16.png">
<link rel="manifest" href="/GOpanel/manifest.json">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="msapplication-TileImage" content="/GOpanel/ms-icon-144x144.png">
<meta name="theme-color" content="#ffffff">'
echo '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>pre {
padding:5px;
  font-size: 16px;
} button.navbar-toggler {
display: none;
}</style>'
echo '<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <!-- Container wrapper -->
  <div class="container-fluid">
    <!-- Navbar brand -->
    <a class="navbar-brand" href="#"><img src="./gopanel.png" alt="GO Panel Logo." width="75" height="75"></a>


    <!-- Collapsible wrapper -->
    <div class="navbar navbar-default" id="navbarSupportedContent">
      <!-- Left links -->
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="./index.cgi">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="./ram.cgi">RAMonitor</a>
        </li>
          </ul>
        </li>
 
        </li>
      </ul>
      <!-- Left links -->

    </div>
    <!-- Collapsible wrapper -->
  </div>
  <!-- Container wrapper -->
</nav>
<!-- Navbar -->'
echo '<div class="jumbotron jumbotron-fluid">
  <div class="container">
<h1>Welcome,'
whoami
echo '</h1>
    <p>I&#39;ve gathered the latest analytics on your server for you.</p>
<p>Enjoy your'
date +%A
echo '</p>
  </div>
</div>'
echo '<center><h2>Server Summary</h2><br/><p>I took the liberty to compile some important server stats into a summary, here they are! (Hint: Reload the page to refresh the statistics!)</p><br/><br/>'
echo '<br/><h3>Server Storage</h3><p><small>Disk space is the amount of data that can be stored on your sytem. Below is a list of data on your server.</small></p>'
echo '<pre>'
df -h
echo '</pre>'
echo '<br/>'
echo '<br/><h3>Server Memory</h3><p><small><abbr>RAM</abbr> stands for random access memory, which allows you to run application and programs easily. Below is how much memory your server is using.</small></p>'
echo '<pre>'
free -h
echo '</pre>'
echo '</center>'
exit 0