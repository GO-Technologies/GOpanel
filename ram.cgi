#!/bin/bash
echo "Content-type: text/html"
echo ''
echo '<title>GOpanel - RAMonitor</title>'
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
<h1>RAMonitor'
echo '</h1>
    <p>Monitor you&#39;re RAM usage in style.</p>'
echo '
  </div>
</div>'
echo '<center>'
echo '<h2>VM Stats</h2><div style="margin:20px;"><p><small>VM, or Virtual Memory, 
is memory that appears to exist as main storage although most of it is supported by data held in secondary storage, transfer between the two being made automatically as required. Virtual Memory allows you to run so many more apps and programs than your hard drive has space for.</small></p></div>'
echo '<pre>'
vmstat
echo '</pre>'
echo '<hr>'
echo '<h2>Meminfo</h2><div style="margin:20px;overflow: scroll;"><p><small>Meminfo is a file on most linux servers that contains lots of information about your computer&#39;s memory.</small></p></div>'
echo '<pre>'
less /proc/meminfo
echo '</pre>'
echo '</center>'