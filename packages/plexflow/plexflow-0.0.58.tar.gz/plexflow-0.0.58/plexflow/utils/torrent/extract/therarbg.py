from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_torrents(html):
    """Extracts torrent information from HTML, resilient to HTML structure changes.

    Args:
        html: The HTML content of the page.

    Returns:
        A list of dictionaries, each containing torrent information:
            - 'title': The title of the torrent.
            - 'link': The link to the torrent detail page.
            - 'category': The category of the torrent.
            - 'added': The date the torrent was added.
            - 'size': The size of the torrent.
            - 'seeders': The number of seeders.
            - 'leechers': The number of leechers.
            - 'thumbnail': The URL of the torrent thumbnail (if available).
    """

    torrents = []
    soup = BeautifulSoup(html, 'html.parser')

    # Find all table rows that likely contain torrent information
    rows = soup.find_all('tr', class_='list-entry')

    for row in rows:
        torrent = {}

        # Extract data from the cells
        cells = row.find_all('td')

        # Title (get full title from link href)
        title_cell = cells[1]
        title_link = title_cell.find('div', class_='wrapper').find('a', recursive=False)
        if title_link:
            # Get the part of the href after the last '/'
            torrent['link'] = urljoin('https://therarbg.com/', title_link['href'])
            torrent['title'] = torrent['link'].rstrip('/').split('/')[-1]  # Use rsplit for last occurrence
        else:
            # If no link is found, get the text of the title cell
            torrent['title'] = title_cell.text.strip()
            torrent['link'] = ''

        # Category
        torrent['category'] = cells[2].find('a').text.strip() if cells[2].find('a') else ''

        # Added
        added_cell = cells[3]
        torrent['added'] = added_cell.text.strip() if added_cell else ''

        # Size
        size_cell = cells[5]
        torrent['size'] = size_cell.text.strip() if size_cell else ''

        # Seeders and Leechers
        seeders_cell = cells[6]
        torrent['seeders'] = int(seeders_cell.text.strip()) if seeders_cell else 0
        leechers_cell = cells[7]
        torrent['leechers'] = int(leechers_cell.text.strip()) if leechers_cell else 0

        # Thumbnail (using a robust approach)
        thumbnail_candidates = row.find_all('img', class_='lazyload')
        if thumbnail_candidates:
            thumbnail = thumbnail_candidates[0]
            torrent['thumbnail'] = thumbnail['data-src'] if thumbnail else ''

        torrents.append(torrent)

    return torrents


html = r"""

<!DOCTYPE html>

<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Search for tt12584954, Free Fast, Download. Torrent The RarBg</title>
        <script src="/cdn-cgi/apps/head/esopnMC-ZcP4Rx5x4pcSP3OrjXQ.js"></script><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
          integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
          crossorigin="anonymous"
          referrerpolicy="no-referrer"
        />
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
        <link rel="stylesheet" type="text/css" href="/static/rarbg/css/slick.css?v=1.04">

        <meta name="description"
            content="Search The RarBg, Torrents, movies, download, music, games, free, XXX, Best Search, The RarBg Torrents, film, download">
        <meta name="keywords"
            content="Search, The RarBg, Torrents , film , download, The RarBg Torrents , Best Search, XXX, Alternative, film , download">
          
    
        <link rel="icon" type="image/png" href="/static/rarbg/image/rbg.png">
        <link href="/static/rarbg/image/rbg.png" rel="apple-touch-icon" />
    
        <link rel="stylesheet" href="/static/rarbg/css/index.css?v=1.04" />
        <link rel="stylesheet" href="/static/rarbg/css/snow.css?v=1.01" />
       
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js" type="a821953e36abcb9cb469edf3-text/javascript"></script>
        <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js" type="a821953e36abcb9cb469edf3-text/javascript"></script>

        
    
    </head>
    <body class="postBody container">
    <!-- enable in christmas -->
    <!-- <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div> -->
     <div
          style="
            background-image: url(/static/rarbg/image/bknd_body.jpg);
            background-repeat: repeat-x;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
          "
        ></div>
       

    

<body>
  <div class="topnav">
    
    <div >
      <a href="/"> 
        <img  class="logo" src="/static/rarbg/image/therarbg.svg" />
      </a>
   
    
    <a href="javascript:void(0);" class="icon showMob  d-block d-md-none" onclick="if (!window.__cfRLUnblockHandlers) return false; myFunction()" data-cf-modified-a821953e36abcb9cb469edf3-="">
      <i class="fa fa-bars"></i>
    </a>
    <div id="myLinks">
<button class="Home"  style="width:100%;"><a href="/"><i class="fas fa-house"></i> Home</a></button>
<button class="Movies" style="width:100%;"><a href="/get-posts/category:Movies:time:10D/"><i class="fa-solid fa-film"></i> Movies</a></button>
<!-- enable in christmas -->
<!-- <button class="Christmas" style="width:100%; background: #B11E31;"><a href="/catalog/movie/christmas/"><i class="fa-solid fa-tree"></i> X-mas</a></button> -->
<button class="TV" style="width:100%;"><a href="/get-posts/category:TV:time:10D/"><i class="fa-solid fa-tv"></i> TV</a></button>
<button class="Games" style="width:100%;"><a href="/get-posts/category:Games:time:10D/"><i class="fa-solid fa-gamepad"></i> Games</a></button>
<button class="Music" style="width:100%;"><a href="/get-posts/category:Music:time:10D/"><i class="fa-solid fa-music"></i> Music</a></button>
<button class="Anime" style="width:100%;"><a href="/get-posts/category:Anime:time:10D/"><i class="fa-solid fa-a"></i> Anime</a></button>
<button class="Apps" style="width:100%;"><a href="/get-posts/category:Apps:time:10D/"><i class="fa-brands fa-app-store-ios"></i> Apps</a></button>
<button class="Other" style="width:100%;"><a href="/get-posts/category:Other:time:10D/"><i class="fa-solid fa-box-open"></i> Other</a></button>
<button class="Books" style="width:100%;"><a href="/get-posts/category:Books:time:10D/"><i class="fa-solid fa-book"></i> Books</a></button>
<button class="XXX isXXX" style="width:100%;"><a href="/get-posts/category:XXX:time:6D/"><i class="fa-solid fa-x"></i> XXX</a></button>
<button class="Pages" style="width:100%;"><a href="/main-page-list/"><i class="fa-solid fa-ghost"></i> Pages</a></button>

<script type="a821953e36abcb9cb469edf3-text/javascript">
   $(document).ready(function(){
    if (window.location.pathname == '/'){
      $('.Home').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Movies') != -1){
      $('.Movies').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':TV') != -1){
      $('.TV').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Games') != -1){
      $('.Games').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Music') != -1){
      $('.Music').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Anime') != -1){
      $('.Anime').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Apps') != -1){
      $('.Apps').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Other') != -1){
      $('.Other').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Books') != -1){
      $('.Books').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':XXX') != -1){
      $('.XXX').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search('/christmas/') != -1){
      $('.Christmas').addClass("btn btn-secondary");
    }
    })
</script>
</div>
    <div class="postContUp">
      <button id="logi-btn"  ><a href="/auth/login/"> Login</a></button>
      <button id="home-btn"><a href="/">Home</a></button>
      <button id="catalog-btn"><a href="/catalog/">Catalog</a></button>

      <button id="box-office-btn">
        <a href="/box-office/">Box Office</a>
      </button>

      <button id="latest-trailer-btn">
        <a href="/latest-trailer/">New Selection</a>
      </button>

      <button id="latest-100-m-btn">
        <a href="/get-posts/keywords:2160p:category:Movies:time:30D/">4K Movies</a>
      </button>
      <button id="latest-100-xxx-4k-btn" class="isXXX">
        <a href="/top/100/XXX/4K/">4K XXX</a>
      </button>
    </div>
  </div>
  <script type="a821953e36abcb9cb469edf3-text/javascript">
      $(document).ready(function () {
              // executes when HTML-Document is loaded and DOM is ready
              const userProfile = JSON.parse(localStorage.getItem("userProfile"));
             if(userProfile?.username){
              document.getElementById("logi-btn").innerHTML = `Logout(${userProfile?.username})`;
              document.getElementById("logi-btn").className = "logout-btn"
             }
             $(".logout-btn").click(function(){
     localStorage.removeItem("token")
     localStorage.removeItem("userProfile")
     window.location.reload()
    }); 
            });
    function myFunction() {
      var x = document.getElementById("myLinks");
      if (x.style.display === "block") {
        x.style.display = "none";
      } else {
        x.style.display = "block";
      }
    }
    // Active
    let pathname = window.location.pathname;
    if (pathname == '/'){
        $('#home-btn').addClass("btn btn-secondary");
    }
    else if (pathname.search('/catalog/') != -1){
        $('#catalog-btn').addClass("btn btn-secondary");
    }
    else if (pathname.search('/box-office/') != -1){
        $('#box-office-btn').addClass("btn btn-secondary");
    }
    else if (pathname.search('/latest-trailer/') != -1){
        $('#latest-trailer-btn').addClass("btn btn-secondary");
    }
    else if (pathname.search('/top/100/Movies/latest/') != -1){
        $('#latest-100-m-btn').addClass("btn btn-secondary");
    }
    else if (pathname.search('/top/100/XXX/4K/') != -1){
        $('#latest-100-xxx-4k-btn').addClass("btn btn-secondary");
    }
  </script>
<script src="/cdn-cgi/scripts/7d0fa10a/cloudflare-static/rocket-loader.min.js" data-cf-settings="a821953e36abcb9cb469edf3-|49" defer></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon='{"rayId":"8b078c33b888b708","version":"2024.7.0","r":1,"token":"77a6085657eb4b2fabd792a0fe5574aa","serverTiming":{"name":{"cfL4":true}}}' crossorigin="anonymous"></script>
</body>

   
    <div class="row">
        <div class="leftNav d-none d-md-block col-md-3 col-lg-1">
        
<button class="Home"  style="width:100%;"><a href="/"><i class="fas fa-house"></i> Home</a></button>
<button class="Movies" style="width:100%;"><a href="/get-posts/category:Movies:time:10D/"><i class="fa-solid fa-film"></i> Movies</a></button>
<!-- enable in christmas -->
<!-- <button class="Christmas" style="width:100%; background: #B11E31;"><a href="/catalog/movie/christmas/"><i class="fa-solid fa-tree"></i> X-mas</a></button> -->
<button class="TV" style="width:100%;"><a href="/get-posts/category:TV:time:10D/"><i class="fa-solid fa-tv"></i> TV</a></button>
<button class="Games" style="width:100%;"><a href="/get-posts/category:Games:time:10D/"><i class="fa-solid fa-gamepad"></i> Games</a></button>
<button class="Music" style="width:100%;"><a href="/get-posts/category:Music:time:10D/"><i class="fa-solid fa-music"></i> Music</a></button>
<button class="Anime" style="width:100%;"><a href="/get-posts/category:Anime:time:10D/"><i class="fa-solid fa-a"></i> Anime</a></button>
<button class="Apps" style="width:100%;"><a href="/get-posts/category:Apps:time:10D/"><i class="fa-brands fa-app-store-ios"></i> Apps</a></button>
<button class="Other" style="width:100%;"><a href="/get-posts/category:Other:time:10D/"><i class="fa-solid fa-box-open"></i> Other</a></button>
<button class="Books" style="width:100%;"><a href="/get-posts/category:Books:time:10D/"><i class="fa-solid fa-book"></i> Books</a></button>
<button class="XXX isXXX" style="width:100%;"><a href="/get-posts/category:XXX:time:6D/"><i class="fa-solid fa-x"></i> XXX</a></button>
<button class="Pages" style="width:100%;"><a href="/main-page-list/"><i class="fa-solid fa-ghost"></i> Pages</a></button>

<script type="a821953e36abcb9cb469edf3-text/javascript">
   $(document).ready(function(){
    if (window.location.pathname == '/'){
      $('.Home').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Movies') != -1){
      $('.Movies').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':TV') != -1){
      $('.TV').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Games') != -1){
      $('.Games').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Music') != -1){
      $('.Music').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Anime') != -1){
      $('.Anime').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Apps') != -1){
      $('.Apps').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Other') != -1){
      $('.Other').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':Books') != -1){
      $('.Books').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search(':XXX') != -1){
      $('.XXX').addClass("btn btn-secondary");
    }
    else if (window.location.pathname.search('/christmas/') != -1){
      $('.Christmas').addClass("btn btn-secondary");
    }
    })
</script>

        </div>
      <div class="postCont col-12 col-md-9 col-lg-11">
       
       
        <!-- <h3><b>Recommended Torrents:</b></h3> -->
        
    <!-- movies slide -->
   
    <div class="banner-box movie">
        <ul id="mySlides1" class="slider">
        
        </ul>
    </div>

    <script type="a821953e36abcb9cb469edf3-text/javascript">
        function stoperror() {
            return true;
        }
    //window.onerror = stoperror;
        var category_init = "None"
        if (category_init == 'XXX'){
            category = 'XXX'
        }
        else if (category_init == 'TV'){
            category = 'tv'
        }
        else{
            category = 'Movies'
        }
        var recommendation_url = `/api/v1/recommendation-list/${category}/`
        $( document ).ready(function() {
            $.get(recommendation_url, (data, status) => {
            if (data) {
              allData(data);
            }
        });
        });
       

        function allData(list) {
        let inhtml = "";
        if (list.length > 0) {
          list.map(
            (post) =>
              (inhtml =
                inhtml +
                ` <li class="most-popular-poster">
                    <a  title="${post?.name}" href=${String(post?.url)} tabindex="-1"> 
                        <img style="max-height:180px" src="${post?.thumbnail}" alt="${post?.name}"/>
                      
                      <div class="most-popular-rating ${Number(post?.rating)>=7?'green':'yellow'}"><a href="https://www.imdb.com/title/${String(post?.imdb)}/" target="_blank">${String(post?.rating)}</a></div>  
                    
                    </a>
                  </li>
                `)
          );
          document.getElementById("mySlides1").innerHTML = inhtml;
          $(".movie .slider").slick({
            infinite: true,
            slidesToShow: 8,
            slidesToScroll: 4,
            autoplay: true,
            autoplaySpeed: 8000,
            responsive: [
              {
                breakpoint: 1024,
                settings: {
                  slidesToShow: 6,
                  slidesToScroll: 4,
                },
              },
              {
                breakpoint: 768,
                settings: {
                  slidesToShow: 4,
                  slidesToScroll: 4,
                },
              },
              // You can unslick at a given breakpoint now by adding:
              // settings: "unslick"
              // instead of a settings object
            ],
          });

        }
        }
       

        let blocked = false;
let blockTimeout = null;
let prevDeltaY = 0;

$("#mySlides1").on('mousewheel DOMMouseScroll wheel', (function(e) {
    let deltaY = e.originalEvent.deltaX;
    e.preventDefault();
    e.stopPropagation();

    clearTimeout(blockTimeout);
    blockTimeout = setTimeout(function(){
        blocked = false;
    }, 50);

    
    if (deltaY > 0 && deltaY > prevDeltaY || deltaY < 0 && deltaY < prevDeltaY || !blocked) {
        blocked = true;
        prevDeltaY = deltaY;
        if (deltaY > 0) {
            $(this).slick('slickNext');
        } else {
            $(this).slick('slickPrev');
        }
    }
}));
    </script>


        <br /><br />

        <div class="row justify-content-md-center">
           
<div class="row" style="text-align: right;">
  <div class="form-check form-switch">
   <label class="form-check-label" for="adultContentToggle" style="margin-right: 10px;">XXX content<input class="form-check-input" type="checkbox" role="switch" onchange="if (!window.__cfRLUnblockHandlers) return false; {localStorage.setItem('adultContentToggle',this.checked);(this.checked?$('.isXXX').css('display', 'block'):$('.isXXX').css('display', 'none'))}" id="adultContentToggle" checked data-cf-modified-a821953e36abcb9cb469edf3-=""></label>
  </div>
 </div>
<div class="searchSec mb-4">
  <form action="/get-posts/" method="GET" id="form_search">
    <div class="search mb-3">
      <input name="keywords" id="keywords" type="text" class="searchTerm" value="" placeholder="Search title or IMDB ID like tt27932269 ..." onkeyup="if (!window.__cfRLUnblockHandlers) return false; fetchData(String(this.value).replaceAll(':',' ').replaceAll(',',' ').replaceAll('.',' ').replaceAll('[',' ').replaceAll(']',' ').replaceAll('(',' ').replaceAll(')',' '))" autocomplete="off" data-cf-modified-a821953e36abcb9cb469edf3-="" />
      <button type="submit" class="searchButton">
        <i class="fa fa-search sIcon" style="display: block"></i>
        <img width="12px" class="lIcon" style="display: none" src="/static/rarbg/image/loader.svg" />
      </button>
      <button id="filterBtn" class="closed filterButton" onclick="if (!window.__cfRLUnblockHandlers) return false; if(this.classList.contains('closed')){this.innerHTML='«';this.classList.remove('closed');this.classList.add('open');localStorage.setItem('filterBtn', 'open');this.parentElement.nextElementSibling.style.display='grid';}else{this.innerHTML='»';this.classList.remove('open');this.classList.add('closed');localStorage.setItem('filterBtn', 'close');this.parentElement.nextElementSibling.style.display='none';}return false;" data-cf-modified-a821953e36abcb9cb469edf3-="">
        »
      </button>
    </div>
    <div id="filterOption" style="display: none" class="filtOptn">
      <div>
        <input type="checkbox" name="Movies" id="radMovies" />
        <label for="radMovies" class="one">
          <a href="/get-posts/category:Movies:time:2D/">Movies</a>
        </label>
      </div>
      <div>
        <input type="checkbox" name="TV" id="radTV" />
        <label for="radTV" class="one">
          <a href="/get-posts/category:TV:time:2D/">TV-Shows</a>
        </label>
      </div>
      <div>
        <input type="checkbox" name="Games" id="radGames" />
        <label for="radGames" class="one">
          <a href="/get-posts/category:Games:time:2D/">Games</a>
        </label>
      </div>
      <div>
        <input type="checkbox" name="one" id="radMusic" />
        <label for="radMusic" class="one">
          <a href="/get-posts/category:Music:time:2D/">Music</a>
        </label>
      </div>
      <div>
        <input type="checkbox" name="Anime" id="radAnime" />
        <label for="radAnime" class="two">
          <a href="/get-posts/category:Anime:time:2D/">Anime</a>
        </label>
      </div>
      <div>
        <input type="checkbox" name="Apps" id="radApps" />
        <label for="radApps" class="two">
          <a href="/get-posts/category:Apps:time:2D/">Apps</a>
        </label>
      </div>
      <div>
        <input type="checkbox" id="radOther" name="Other" />
        <label for="radOther" class="two">
          <a href="/get-posts/category:Other:time:2D/">Other</a>
        </label>
      </div>
      <div>
        <input type="checkbox" name="XXX" id="radXXX" />
        <label for="radXXX" class="two">
          <a href="/get-posts/category:XXX:time:2D/">XXX</a>
        </label>
      </div>
      <div>
        <label for="sizeMin" class="two" style="position: relative;display: inline-flex;">
          <span style="position: absolute;top: 2px;left: 2px;color: #3760bb;"> Min</span>
          <input placeholder="size" type="number" name="size" id="sizeMin" style="width: 120px; padding: 0px 25px;">
          <span style="position: absolute;top: 2px;right: 4px;color: #3760bb;"> MB</span>
        </label> 
      </div>
      <div>
        <label for="sizeMax" class="two" style="position: relative;display: inline-flex;">
          <span style="position: absolute;top: 2px;left: 2px;color: #3760bb;"> Max</span>
          <input placeholder="size" type="number" name="size" id="sizeMax" style="width: 120px; padding: 0px 26px;">
          <span style="position: absolute;top: 2px;right: 4px;color: #3760bb;"> MB</span>
        </label> 
      </div>
    </div>
    <div style="margin-top: 10px;text-align: left;">
      <button class="filterButton" type="reset" onclick="if (!window.__cfRLUnblockHandlers) return false; {this.parentElement.parentElement.reset();localStorage.removeItem('checkedSearches')}" data-cf-modified-a821953e36abcb9cb469edf3-="">
        Reset
      </button>
    </div>
  </form>
  <div class="nav search-result-pop" id="search-suggest" style="display: none">
    <!-- <div
      class="loading-relative"
      id="search-loading"
      style="display: none"
      bis_skin_checked="1"
    >
      <div class="loading" bis_skin_checked="1">
        <div class="span1" bis_skin_checked="1"></div>
        <div class="span2" bis_skin_checked="1"></div>
        <div class="span3" bis_skin_checked="1"></div>
      </div>
    </div> -->
    <div class="result" id="searchList"></div>
  </div>
  <script type="a821953e36abcb9cb469edf3-text/javascript">
    $(document).ready(function () {
      if(localStorage.getItem("adultContentToggle")==="false"){
        document.getElementById("adultContentToggle").checked = false;
        $('.isXXX').css('display', 'none')

      }
      if (localStorage.getItem('filterBtn') == 'open') {
        $('#filterBtn').removeClass('closed');
        $('#filterBtn').addClass('open');
        $('#filterBtn').html('«');
        $('#filterOption').css("display", "grid");
      }
      let chkObj = JSON.parse(localStorage.getItem('checkedSearches'))
      if (chkObj?.movies === "true") {
        document.getElementById("radMovies").checked = true;
      }
      if (chkObj?.tv === "true") {
        document.getElementById("radTV").checked = true;
      }
      if (chkObj?.games === "true") {
        document.getElementById("radGames").checked = true;
      }
      if (chkObj?.music === "true") {
        document.getElementById("radMusic").checked = true;
      }
      if (chkObj?.anime === "true") {
        document.getElementById("radAnime").checked = true;
      }
      if (chkObj?.apps === "true") {
        document.getElementById("radApps").checked = true;
      }
      if (chkObj?.other === "true") {
        document.getElementById("radOther").checked = true;
      }
      if (chkObj?.xxx === "true") {
        document.getElementById("radXXX").checked = true;
      }
      if (chkObj?.sizeMin) {
        document.getElementById("sizeMin").value = chkObj?.sizeMin;
      }
      if (chkObj?.sizeMax) {
        document.getElementById("sizeMax").value = chkObj?.sizeMax;
      }

      $("#form_search").submit(function (event) {
        event.preventDefault(); // <-- add this
        var searchValue = encodeURI(document.getElementById("keywords").value.replace(':', ' '));
        var sizeMinMb = encodeURI(document.getElementById("sizeMin").value);
        var sizeMaxMb = encodeURI(document.getElementById("sizeMax").value);
        var radMovies = encodeURI(document.getElementById("radMovies").checked);
        var radTV = encodeURI(document.getElementById("radTV").checked);
        var radGames = encodeURI(document.getElementById("radGames").checked);
        var radMusic = encodeURI(document.getElementById("radMusic").checked);
        var radAnime = encodeURI(document.getElementById("radAnime").checked);
        var radApps = encodeURI(document.getElementById("radApps").checked);
        var radOther = encodeURI(document.getElementById("radOther").checked);
        var radXXX = encodeURI(document.getElementById("radXXX").checked);

        if (searchValue) {
          let checked = {
            movies: radMovies,
            tv: radTV,
            games: radGames,
            music: radMusic,
            anime: radAnime,
            apps: radApps,
            other: radOther,
            xxx: radXXX,
            sizeMin:sizeMinMb,
            sizeMax:sizeMaxMb,
          }
          localStorage.setItem("checkedSearches", JSON.stringify(checked))
          let showAdultCon = localStorage.getItem("adultContentToggle")||"true";
          document.location =
            "/get-posts/keywords:" +
            searchValue +
            (radMovies === "true" ? `:category:Movies` : "") +
            (radTV === "true" ? `:category:TV` : "") +
            (radGames === "true" ? `:category:Games` : "") +
            (radMusic === "true" ? `:category:Music` : "") +
            (radAnime === "true" ? `:category:Anime` : "") +
            (radApps === "true" ? `:category:Apps` : "") +
            (radOther === "true" ? `:category:Other` : "") +
            (radXXX === "true" ? `:category:XXX` : "") +
            (showAdultCon === "false" ? `:ncategory:XXX` : "") +
            (Number(sizeMinMb) > 0 ? `:size__gte:${Number(sizeMinMb)*1000000}` : "") +
            (Number(sizeMaxMb) > 0 ? `:size__lte:${Number(sizeMaxMb)*1000000}` : "") +
            "/";
        }
      });
      $(".searchTerm").blur(function () {
        $("#search-suggest").slideUp("fast");
      });
      $(".searchTerm").focus(function () {
        $("#search-suggest").slideDown("fast");
      });
      $(".nav-item").click(function () {
        $(".searchTerm").focus();

      });
      $(".searchTerm").val(sessionStorage.getItem("search"));
      $('.sortableTable').DataTable({
        paging: false,
        language: {
          search: "_INPUT_",
          searchPlaceholder: "Search table..."
        }
      });
    });
    function showHide(val, cls) {
      $(cls).css("display", val);
    }
    function fetchData(search) {
      sessionStorage.setItem("search", search);
      $.get(
        `${window.location.origin}/get-posts/keywords:${search}:format:json:ncategory:XXX/`,
        (data, status) => {
          if (data?.results) {
            createHtml(data?.results, search);
          }
        }
      );
    }

    const units = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'];

    function niceBytes(x) {

      let l = 0, n = parseInt(x, 10) || 0;

      while (n >= 1024 && ++l) {
        n = n / 1024;
      }

      return (n.toFixed(n < 10 && l > 0 ? 1 : 0) + ' ' + units[l]);
    };

    function createHtml(list, search) {
      let inhtml = ` <a href="/get-posts/keywords:${search}/" class="nav-item nav-bottom">
        View all results<i class="fa fa-angle-right ml-2"></i>
      </a>`;
      if (list.length > 0) {
        list.map((post, index) =>
          index < 5
            ? (inhtml =
              `<a  href="/post-detail/${post.pk}/${String(post.n)
                .replaceAll(" ", ".")
                .replaceAll(".", "-")
                .toLowerCase()}/" class="nav-item">
        <div class="film-poster" bis_skin_checked="1">
          <img
            class="film-poster-img lazyloaded"
            src="${post.t ? post.t : "https://i.therarbg.com/np.jpg"
              }"
          />
        </div>
        <div class="srp-detail" bis_skin_checked="1">
          <p class="film-name" >
            ${post.n}
          </p>

          <div class="alias-name" bis_skin_checked="1">${post.c}</div>

          <div class="film-infor" bis_skin_checked="1">
            <span>Leechers:${post.se}</span> | <span>Seeders:${post.le
              }</span> | <span>Size:${niceBytes(post.s)}</span>
          </div>
        </div>
        <div class="clearfix" bis_skin_checked="1"></div>
      </a>` + inhtml)
            : ""
        );
        document.getElementById("searchList").innerHTML = inhtml;
      } else if (list.length === 0) {
        document.getElementById("searchList").innerHTML = "";
      }
    }
    // Animation
    let i = 0;
    let placeholder = "";
    const txt = document.getElementById("keywords").placeholder;
    const speed = 120;
    function typeAnimation() {
      placeholder += txt.charAt(i);
      document.getElementById("keywords").setAttribute("placeholder", placeholder);
      i++;
      setTimeout(typeAnimation, speed);
    }
    typeAnimation();
  </script>
</div>
        </div>

        <div class="row justify-content-md-center mb-3">
          <!-- Tags -->

<div id="searchTags">
      <a href="/top/100/Movies/latest/"><span class='badge rounded-pill bg-info'>Latest 100 Movies</span></a>

      <a href="/trending/10/ALL/1D/"><span class='badge rounded-pill bg-danger'>Trending 10 in all category</span></a>
      <a href="/get-posts/keywords:2160p:category:Movies:time:60D/"><span class='badge rounded-pill bg-info'>4K Movies</span></a>
      <a href="/get-posts/keywords:Remux 2160p:category:Movies:time:60D/"><span class='badge rounded-pill bg-info'>Remux 4K Movies</span></a>
      <a href="/get-posts/keywords:1080p:category:Movies:time:60D/"><span class='m-1 badge rounded-pill bg-info'>1080p Movies</span></a>
      <a href="/get-posts/keywords:Remux 1080p:category:Movies:time:60D/"><span class='m-1 badge rounded-pill bg-info'>Remux 1080p Movies</span></a>
      <a href="/get-posts/keywords:720p:category:Movies:time:60D/"><span class='badge rounded-pill bg-info'>720p Movies</span></a>
      <a href="/get-posts/keywords:480p:category:Movies:time:60D/"><span class='m-1 badge rounded-pill bg-info'>480p Movies</span></a>
      <a href="/get-posts/keywords:x265:category:Movies:time:60D/"><span class='m-1 badge rounded-pill bg-info'>x265 Movies</span></a>
      <a href="/get-posts/keywords:Remux x265:category:Movies:time:60D/"><span class='m-1 badge rounded-pill bg-info'>Remux x265 Movies</span></a>
      <a href="/get-posts/keywords:x264:category:Movies:time:60D/"><span class='m-1 badge rounded-pill bg-info'>x264 Movies</span></a>
      <a href="/get-posts/keywords:Remux Bluray:category:Movies:time:60D/"><span class='m-1 badge rounded-pill bg-info'>Remux BluRay Movies</span></a>
      <a href="/get-posts/keywords:Bluray:category:Movies:time:60D/"><span class='m-1 badge rounded-pill bg-info'>BluRay Movies</span></a>
      <a href="/get-posts/keywords:60FPS/"><span class='m-1 badge rounded-pill bg-info'>60FPS</span></a>
      <a href="/trending/100/Movies/3D/"><span class='badge rounded-pill bg-danger'>Trending 100 Movies</span></a>

      <a href="/get-posts/keywords:ita 2160p:category:Movies/"><span class='badge rounded-pill bg-primary'>4K ITA Movies</span></a>
      <a href="/get-posts/keywords:ita 1080p:category:Movies/"><span class='m-1 badge rounded-pill bg-primary'>ITA 1080p Movies</span></a>
      <a href="/get-posts/keywords:ita 720p:category:Movies/"><span class='badge rounded-pill bg-primary'>ITA 720p Movies</span></a>
      <a href="/get-posts/keywords:ita 480p:category:Movies/"><span class='m-1 badge rounded-pill bg-primary'>ITA 480p Movies</span></a>

      <a href="/get-posts/keywords:evilangel:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>EvilAngel XXX</span></a>
      <a href="/get-posts/keywords:24 08 09:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>24 08 09 XXX</span></a>
      <a href="/get-posts/keywords:TonightsGirlfriend:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>TonightsGirlfriend XXX</span></a>
      <a href="/get-posts/keywords:blacked:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>blacked XXX</span></a>
      <a href="/get-posts/keywords:TushyRaw:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>TushyRaw XXX</span></a>
      <a href="/get-posts/keywords:Vixen:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>Vixen XXX</span></a>
      <a href="/trending/100/XXX/3D/"><span class='badge rounded-pill bg-danger'>Trending 100 XXX</span></a>

      <a href="/get-posts/keywords:2160p:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>4K XXX</span></a>
      <a href="/get-posts/keywords:1080p:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>1080p XXX</span></a>
      <a href="/get-posts/keywords:720p:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>720p XXX</span></a>
      <a href="/get-posts/keywords:480p:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>480p XXX</span></a>
      <a href="/get-posts/keywords:x265:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>x265 XXX</span></a>
      <a href="/get-posts/keywords:x264:category:XXX:time:60D/"><span class='m-1 badge rounded-pill bg-secondary'>x264 XXX</span></a>

      <a href="/get-posts/keywords:WWE:category:TV:time:90D/"><span class='m-1 badge rounded-pill bg-warning'>WWE TV Show</span></a>
      <a href="/get-posts/keywords:UFC:category:TV:time:90D/"><span class='m-1 badge rounded-pill bg-warning'>UFC TV Show</span></a>
      <a href="/get-posts/keywords:2160p:category:TV:time:60D/"><span class='m-1 badge rounded-pill bg-warning'>4K TV</span></a>
      <a href="/get-posts/keywords:1080p:category:TV/"><span class='m-1 badge rounded-pill bg-warning'>1080p TV</span></a>
      <a href="/get-posts/keywords:720p:category:TV:time:60D/"><span class='m-1 badge rounded-pill bg-warning'>720p TV</span></a>
      <a href="/get-posts/keywords:480p:category:TV:time:60D/"><span class='m-1 badge rounded-pill bg-warning'>480p TV</span></a>
      <a href="/get-posts/keywords:x265:category:TV:time:60D/"><span class='m-1 badge rounded-pill bg-warning'>x265 TV</span></a>
      <a href="/get-posts/keywords:x264:category:TV:time:60D/"><span class='m-1 badge rounded-pill bg-warning'>x264 TV</span></a>
      <a href="/get-posts/keywords:Bluray:category:TV:time:60D/"><span class='m-1 badge rounded-pill bg-warning'>BluRay TV</span></a>
      <a href="/trending/100/TV/3D/"><span class='badge rounded-pill bg-danger'>Trending 100 TV</span></a>

      <a href="/get-posts/keywords:FLAC:category:Music:time:60D/"><span class='m-1 badge rounded-pill bg-success'>FLAC Quality Music</span></a>
      <a href="/get-posts/keywords:320:category:Music:time:60D/"><span class='m-1 badge rounded-pill bg-success'>320kbps Music</span></a>
      <a href="/get-posts/keywords:pop:category:Music:time:60D/"><span class='m-1 badge rounded-pill bg-success'>POP Music</span></a>
      <a href="/trending/100/Music/3D/"><span class='badge rounded-pill bg-danger'>Trending 100 Music</span></a>
</div>

        </div>

        <div class="row justify-content-md-center">
          
    <!-- movies slide -->
   
    <div id="recentSearch"></div>
    <script async type="a821953e36abcb9cb469edf3-text/javascript">
      $.get("/api/v1/recent-search/", (data, status) => {
        RsData(data);
      });
      function RsData(list) {
        let inhtml = "";
        if (list.length > 0) {
          list.map(
            (post) =>
              (inhtml =
                inhtml +
                `<a class="recent-search" href="${'/get-posts/' + post?.search_keywords + '/'}" >${String(post.search_keywords.replace('keywords:','').replace('user', ''))} </a>`)
          );
          document.getElementById("recentSearch").innerHTML = inhtml;

            const fonts = ['Helvetica', 'Arial', 'Verdana', 'Courier', 'Courier New'];
            const elements = document.querySelectorAll('.recent-search');
            Array.from(elements).forEach((element, index) => {
                let s = Math.floor(11 + Math.random() * 8)
                const randomfont = fonts[Math.floor(Math.random() * fonts.length)];
                element.style.fontFamily = randomfont;
                element.style.fontSize = s + 'px'
            });

        }
      }

    </script>

        </div>

        <br />
                


<div class="row">
  <nav>
    <ul class="pagination justify-content-center">
      <li class="page-item">
        
     
        
          
          <li class="page-item active">  <a class="page-link" href="?page=1">1</a>   </li>
          
        
   
    
        
     
    </ul>
  </nav>
</div>





        <br />
        <div class="row p-1">
          <div style="display:flex; justify-content:space-between; flex-wrap: wrap;">
            <input type="text" id="flist" onkeyup="if (!window.__cfRLUnblockHandlers) return false; filter_list2()" placeholder="Search table.." style="height:26px" data-cf-modified-a821953e36abcb9cb469edf3-="">
            <div style="margin-top: 6px;">
              Quick Filters: <label title="720p"><input name="720p" id="f_720p" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">720p</label>&nbsp;&nbsp;<label title="1080p"><input name="1080p" id="f_1080p" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">1080p</label>&nbsp;&nbsp;<label title="2160p"><input name="2160p" id="f_2160p" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">2160p</label>&nbsp;&nbsp;<label title="x264"><input name="x264" id="f_x264" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">x264</label>&nbsp;&nbsp;<label title="h264"><input name="h264" id="f_h264" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">h264</label>&nbsp;&nbsp;<label title="x265"><input name="x265" id="f_x265" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">x265</label>&nbsp;&nbsp;<label title="h265"><input name="h265" id="f_h265" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">h265</label>&nbsp;&nbsp;<label title="WEBRip"><input name="webrip" id="f_webrip" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">WEBRip</label>&nbsp;&nbsp;<label title="BluRay"><input name="bluray" id="f_bluray" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">BluRay</label>&nbsp;&nbsp;<label title="HDR"><input name="hdr" id="f_hdr" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">HDR</label>&nbsp;&nbsp;<label title="HEVC"><input name="hevc" id="f_hevc" onclick="if (!window.__cfRLUnblockHandlers) return false; filter_list2();" type="checkbox" data-cf-modified-a821953e36abcb9cb469edf3-="">HEVC</label><ol id="torrents" class="view-single"></ol>
             </div>
             
            <form action="#" novalidate="true">
              <select class="form-select" style="background-color: #fff; color:#464646; width:163px" onchange="if (!window.__cfRLUnblockHandlers) return false; top.location.href=this.options[this.selectedIndex].value;" data-cf-modified-a821953e36abcb9cb469edf3-="">
            <option   value="#" >All Categories</option>
            <option   value="/get-posts/category:Movies:keywords:tt12584954/">Movies Only</option>
            <option   value="/get-posts/category:TV:keywords:tt12584954/">TV Only</option>
            <option   value="/get-posts/category:Games:keywords:tt12584954/">Games Only</option>
            <option   value="/get-posts/category:Music:keywords:tt12584954/">Music Only</option>
            <option   value="/get-posts/category:Apps:keywords:tt12584954/">Applications Only</option>
            <option   value="/get-posts/category:Documentaries:keywords:tt12584954/">Documentaries Only</option>
            <option   value="/get-posts/category:Anime:keywords:tt12584954/">Anime Only</option>
            <option   value="/get-posts/category:Other:keywords:tt12584954/">Other Only</option>
            <option   value="/get-posts/category:XXX:keywords:tt12584954/">XXX Only</option>
            </select>
            </form>
            <form action="#" novalidate="true">
              <select class="form-select" style="background-color: #fff; color:#464646; width:163px" onchange="if (!window.__cfRLUnblockHandlers) return false; top.location.href=this.options[this.selectedIndex].value;" data-cf-modified-a821953e36abcb9cb469edf3-="">
               <option   value="#">Sort by...</option>
               <option selected  value="/get-posts/order:-a:keywords:tt12584954/">Sort by Time</option>
               <option   value="/get-posts/order:-s:keywords:tt12584954/">Sort by Size</option>
               <option   value="/get-posts/order:-se:keywords:tt12584954/">Sort by Seeders</option>
               <option   value="/get-posts/order:-le:keywords:tt12584954/">Sort by Leechers</option>
               </select>
               </form>
              
          </div>
          
          <table class="sortableTable2 compact cell-border hover stripe" style="width:100%">
            <thead class="table1head">
              <th class="hideCell">C.</th>
              <th class="cellName">File</th>
              <th class="hideCell">Category</th>
              <th id="added" class="hideCell">Added</th>
              <th class="hideCell">Time Since</th>
              <th id="size">Size</th>
              <th id="seeders">S.</th>
              <th id="leechers">L.</th>
            </thead>
            <tbody>
              
              <tr class="list-entry">
                <td class="hideCell">
                  <img width="35" src="/static/rarbg/image/categories/cat_new44.gif"
                  />
                </td>
                <td class="cellName">
                  <div class="wrapper">
                    <a
                      href="/post-detail/75d730/twisters-2024-v3-1080p-clean-hdts-new-video-audio-x264-collective/"
                      style="font-weight: 700"
                      >Twisters 2024 V3 1080p CLEAN HDTS New Video Audio X264 COLLECTiVE</a>  <a href="/imdb-detail/tt12584954/"><span class="badge rounded-pill bg-info">M.Q.A</span></a>
                    <span class="tooltip" id="fade">
                        <img class="lazyload" data-src="https://i.therarbg.com/np.jpg" width="100px" alt="thumbnail"/></span>
                  </div>
                </td>
                <td class="hideCell">
                  <a
                    href="/get-posts/category:Movies/"
                    style="font-weight: 700"
                  >
                    Movies</a
                  >
                </td>
                <td class="hideCell" data-order="1721677508">
                  <div style="display: inline-block">
                    2024-07-22
                  </div>
                </td>
                <td class="hideCell" data-order="1721677508">
                  <div style="display: inline-block">
                    2 weeks, 3 days
                  </div>
                </td>
                <td style="text-align: left;" class="sizeCell" data-order="5583457484">5.2 GB</td>
                <td style="color: green">4</td>
                <td style="color: red">12</td>
              </tr>
              
              <tr class="list-entry">
                <td class="hideCell">
                  <img width="35" src="/static/rarbg/image/categories/cat_new44.gif"
                  />
                </td>
                <td class="cellName">
                  <div class="wrapper">
                    <a
                      href="/post-detail/75ce89/twisters-2024-1080p-camrip-v3-hindi-x264-1xbet/"
                      style="font-weight: 700"
                      >Twisters 2024 1080p CAMRip V3 Hindi x264 1XBET</a>  <a href="/imdb-detail/tt12584954/"><span class="badge rounded-pill bg-info">M.Q.A</span></a>
                    <span class="tooltip" id="fade">
                        <img class="lazyload" data-src="https://a.therarbg.com/006/e2c7ec9359f862095b60898a5fb8bfd3.jpg" width="100px" alt="thumbnail"/></span>
                  </div>
                </td>
                <td class="hideCell">
                  <a
                    href="/get-posts/category:Movies/"
                    style="font-weight: 700"
                  >
                    Movies</a
                  >
                </td>
                <td class="hideCell" data-order="1721546419">
                  <div style="display: inline-block">
                    2024-07-21
                  </div>
                </td>
                <td class="hideCell" data-order="1721546419">
                  <div style="display: inline-block">
                    2 weeks, 5 days
                  </div>
                </td>
                <td style="text-align: left;" class="sizeCell" data-order="4219805368">3.9 GB</td>
                <td style="color: green">8</td>
                <td style="color: red">20</td>
              </tr>
              
              <tr class="list-entry">
                <td class="hideCell">
                  <img width="35" src="/static/rarbg/image/categories/cat_new44.gif"
                  />
                </td>
                <td class="cellName">
                  <div class="wrapper">
                    <a
                      href="/post-detail/75c337/twisters-2024-v3-1080p-clean-cam-new-video-audio-x264-collective/"
                      style="font-weight: 700"
                      >Twisters 2024 V3 1080p CLEAN CAM New Video Audio X264 COLLECTiVE</a>  <a href="/imdb-detail/tt12584954/"><span class="badge rounded-pill bg-info">M.Q.A</span></a>
                    <span class="tooltip" id="fade">
                        <img class="lazyload" data-src="https://a.therarbg.com/006/23f3796a0e1f97d150e4f91248f7e794.jpg" width="100px" alt="thumbnail"/></span>
                  </div>
                </td>
                <td class="hideCell">
                  <a
                    href="/get-posts/category:Movies/"
                    style="font-weight: 700"
                  >
                    Movies</a
                  >
                </td>
                <td class="hideCell" data-order="1721427191">
                  <div style="display: inline-block">
                    2024-07-19
                  </div>
                </td>
                <td class="hideCell" data-order="1721427191">
                  <div style="display: inline-block">
                    2 weeks, 6 days
                  </div>
                </td>
                <td style="text-align: left;" class="sizeCell" data-order="5529770393">5.1 GB</td>
                <td style="color: green">8</td>
                <td style="color: red">38</td>
              </tr>
              
              <tr class="list-entry">
                <td class="hideCell">
                  <img width="35" src="/static/rarbg/image/categories/cat_new44.gif"
                  />
                </td>
                <td class="cellName">
                  <div class="wrapper">
                    <a
                      href="/post-detail/75bd75/twisters-1080p-v2-clean-cam-multi-audio-x264-collective/"
                      style="font-weight: 700"
                      >Twisters 1080p V2 CLEAN CAM Multi Audio X264 COLLECTiVE</a>  <a href="/imdb-detail/tt12584954/"><span class="badge rounded-pill bg-info">M.Q.A</span></a>
                    <span class="tooltip" id="fade">
                        <img class="lazyload" data-src="https://a.therarbg.com/006/23f3796a0e1f97d150e4f91248f7e794.jpg" width="100px" alt="thumbnail"/></span>
                  </div>
                </td>
                <td class="hideCell">
                  <a
                    href="/get-posts/category:Movies/"
                    style="font-weight: 700"
                  >
                    Movies</a
                  >
                </td>
                <td class="hideCell" data-order="1721265615">
                  <div style="display: inline-block">
                    2024-07-18
                  </div>
                </td>
                <td class="hideCell" data-order="1721265615">
                  <div style="display: inline-block">
                    3 weeks, 1 day
                  </div>
                </td>
                <td style="text-align: left;" class="sizeCell" data-order="4681514352">4.4 GB</td>
                <td style="color: green">11</td>
                <td style="color: red">38</td>
              </tr>
              
              <tr class="list-entry">
                <td class="hideCell">
                  <img width="35" src="/static/rarbg/image/categories/cat_new44.gif"
                  />
                </td>
                <td class="cellName">
                  <div class="wrapper">
                    <a
                      href="/post-detail/75afed/twisters-1080p-clean-cam-dual-audio-x264-collective/"
                      style="font-weight: 700"
                      >Twisters 1080p CLEAN CAM Dual Audio X264 COLLECTiVE</a>  <a href="/imdb-detail/tt12584954/"><span class="badge rounded-pill bg-info">M.Q.A</span></a>
                    <span class="tooltip" id="fade">
                        <img class="lazyload" data-src="https://a.therarbg.com/006/23f3796a0e1f97d150e4f91248f7e794.jpg" width="100px" alt="thumbnail"/></span>
                  </div>
                </td>
                <td class="hideCell">
                  <a
                    href="/get-posts/category:Movies/"
                    style="font-weight: 700"
                  >
                    Movies</a
                  >
                </td>
                <td class="hideCell" data-order="1720924222">
                  <div style="display: inline-block">
                    2024-07-14
                  </div>
                </td>
                <td class="hideCell" data-order="1720924222">
                  <div style="display: inline-block">
                    3 weeks, 5 days
                  </div>
                </td>
                <td style="text-align: left;" class="sizeCell" data-order="4380866641">4.1 GB</td>
                <td style="color: green">12</td>
                <td style="color: red">44</td>
              </tr>
              
              <tr class="list-entry">
                <td class="hideCell">
                  <img width="35" src="/static/rarbg/image/categories/cat_new44.gif"
                  />
                </td>
                <td class="cellName">
                  <div class="wrapper">
                    <a
                      href="/post-detail/75af8d/twisters-2024-v2-hdcam-c1nem4-x264-sunscreen-tgx/"
                      style="font-weight: 700"
                      >Twisters 2024 V2 HDCAM c1nem4 x264 SUNSCREEN TGx</a>  <a href="/imdb-detail/tt12584954/"><span class="badge rounded-pill bg-info">M.Q.A</span></a>
                    <span class="tooltip" id="fade">
                        <img class="lazyload" data-src="https://a.therarbg.com/006/23f3796a0e1f97d150e4f91248f7e794.jpg" width="100px" alt="thumbnail"/></span>
                  </div>
                </td>
                <td class="hideCell">
                  <a
                    href="/get-posts/category:Movies/"
                    style="font-weight: 700"
                  >
                    Movies</a
                  >
                </td>
                <td class="hideCell" data-order="1720909217">
                  <div style="display: inline-block">
                    2024-07-13
                  </div>
                </td>
                <td class="hideCell" data-order="1720909217">
                  <div style="display: inline-block">
                    3 weeks, 5 days
                  </div>
                </td>
                <td style="text-align: left;" class="sizeCell" data-order="1043637207">995.3 MB</td>
                <td style="color: green">41</td>
                <td style="color: red">82</td>
              </tr>
              
              <tr class="list-entry">
                <td class="hideCell">
                  <img width="35" src="/static/rarbg/image/categories/cat_new44.gif"
                  />
                </td>
                <td class="cellName">
                  <div class="wrapper">
                    <a
                      href="/post-detail/75a027/twisters-2024-hdcam-c1nem4-x264-sunscreen-tgx/"
                      style="font-weight: 700"
                      >Twisters 2024 HDCAM c1nem4 x264 SUNSCREEN TGx</a>  <a href="/imdb-detail/tt12584954/"><span class="badge rounded-pill bg-info">M.Q.A</span></a>
                    <span class="tooltip" id="fade">
                        <img class="lazyload" data-src="https://a.therarbg.com/006/751111132fc22d8d045f104ece0f6a0d.jpg" width="100px" alt="thumbnail"/></span>
                  </div>
                </td>
                <td class="hideCell">
                  <a
                    href="/get-posts/category:Movies/"
                    style="font-weight: 700"
                  >
                    Movies</a
                  >
                </td>
                <td class="hideCell" data-order="1720870837">
                  <div style="display: inline-block">
                    2024-07-13
                  </div>
                </td>
                <td class="hideCell" data-order="1720870837">
                  <div style="display: inline-block">
                    3 weeks, 6 days
                  </div>
                </td>
                <td style="text-align: left;" class="sizeCell" data-order="1043637207">995.3 MB</td>
                <td style="color: green">12</td>
                <td style="color: red">35</td>
              </tr>
              
              <tr class="list-entry">
                <td class="hideCell">
                  <img width="35" src="/static/rarbg/image/categories/cat_new44.gif"
                  />
                </td>
                <td class="cellName">
                  <div class="wrapper">
                    <a
                      href="/post-detail/75a01f/twisters-2024-720p-hdcam-c1nem4/"
                      style="font-weight: 700"
                      >Twisters 2024 720p HDCAM C1NEM4</a>  <a href="/imdb-detail/tt12584954/"><span class="badge rounded-pill bg-info">M.Q.A</span></a>
                    <span class="tooltip" id="fade">
                        <img class="lazyload" data-src="https://a.therarbg.com/006/c2615aabdd035b6fb5d5e7a5f064fb93.jpg" width="100px" alt="thumbnail"/></span>
                  </div>
                </td>
                <td class="hideCell">
                  <a
                    href="/get-posts/category:Movies/"
                    style="font-weight: 700"
                  >
                    Movies</a
                  >
                </td>
                <td class="hideCell" data-order="1720869621">
                  <div style="display: inline-block">
                    2024-07-13
                  </div>
                </td>
                <td class="hideCell" data-order="1720869621">
                  <div style="display: inline-block">
                    3 weeks, 6 days
                  </div>
                </td>
                <td style="text-align: left;" class="sizeCell" data-order="1803886264">1.7 GB</td>
                <td style="color: green">31</td>
                <td style="color: red">22</td>
              </tr>
              
            </tbody>
          </table>
              
        </div>

        <br />

                


<div class="row">
  <nav>
    <ul class="pagination justify-content-center">
      <li class="page-item">
        
     
        
          
          <li class="page-item active">  <a class="page-link" href="?page=1">1</a>   </li>
          
        
   
    
        
     
    </ul>
  </nav>
</div>




        <br />
        <br />
          <script type="a821953e36abcb9cb469edf3-text/javascript">
            $(document).ready(function() {
             // executes when HTML-Document is loaded and DOM is ready
            
            current_url = window.location.href
            let se = '-a' == '-se'? 'se':'-se';
            let le = '-a' == '-le'? 'le':'-le';
            let a = '-a' == 'a'? '-a':'a';
            let s = '-a' == '-s'? 's':'-s';
              let seedersUrl = current_url.replace(/\/$/, ':order:' + se + '/');
              let leechersUrl = current_url.replace(/\/$/, ':order:' + le + '/');
              let addedUrl = current_url.replace(/\/$/, ':order:' + a +'/');
              let sizeUrl = current_url.replace(/\/$/, ':order:' + s + '/');

              $("#seeders").html('<a href="' + seedersUrl + '"><i class="fa-solid fa-arrow-down"></i>S.</a>');
              $("#leechers").html('<a href="' + leechersUrl + '"><i class="fa-solid fa-arrow-down"></i>L.</a>');
              $("#added").html('<a href="' + addedUrl + '"><i class="fa-solid fa-arrow-down"></i>Added</a>');
              $("#size").html('<a href="' + sizeUrl + '"><i class="fa-solid fa-arrow-down"></i>Size</a>');

              $("#seeders a").css("color", "white");
              $("#leechers a").css("color", "white");
              $("#added a").css("color", "white");
              $("#size a").css("color", "white");

              $('.sortableTable2').DataTable({
               paging: false,
               bFilter: false
              // language: {
              // search: "_INPUT_",
              //  searchPlaceholder: "Search table..."
              //    }
               });
            });
            const images = document.querySelectorAll("img.lazyload");
            images.forEach(img => {
                img.src = img.dataset.src;
            });

            function filter_list2() {
    let input, filter, ul, li, a, i, txtValue;
    let f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12;
    let show, qshow, txtv, do_qshow = 1;
    f1 = '';
    if (document.getElementById('f_720p').checked)
        f2 = '720P';
    else
        f2 = '';
    if (document.getElementById('f_1080p').checked)
        f3 = '1080P';
    else
        f3 = '';
    if (document.getElementById('f_2160p').checked)
        f4 = '2160P';
    else
        f4 = '';
    if (document.getElementById('f_x264').checked)
        f5 = 'X264';
    else
        f5 = '';
    if (document.getElementById('f_h264').checked)
        f6 = 'H264';
    else
        f6 = '';
    if (document.getElementById('f_x265').checked)
        f7 = 'X265';
    else
        f7 = '';
    if (document.getElementById('f_h265').checked)
        f8 = 'H265';
    else
        f8 = '';
    if (document.getElementById('f_hdr').checked)
        f9 = 'HDR ';
    else
        f9 = '';
    if (document.getElementById('f_hevc').checked)
        f10 = 'HEVC';
    else
        f10 = '';
    if (document.getElementById('f_webrip').checked)
        f11 = 'WEBRIP';
    else
        f11 = '';
    if (document.getElementById('f_bluray').checked)
        f12 = 'BLURAY';
    else
        f12 = '';
    if ((f1.length == 0) && (f2.length == 0) && (f3.length == 0) && (f4.length == 0) && (f5.length == 0) && (f6.length == 0) && (f7.length == 0) && (f8.length == 0) && (f9.length == 0) && (f10.length == 0) && (f11.length == 0) && (f12.length == 0))
        do_qshow = 0;
    input = document.getElementById('flist');
    filter = input.value.toUpperCase();
    li = document.getElementsByClassName('list-entry');
    for (i = 0; i < li.length; i++) {
        show = 0;
        qshow = 0;
        a = li[i].getElementsByTagName('td')[1];
        txtv = a.textContent || a.innerText;
        txtValue = txtv.toUpperCase();
        if (do_qshow) {
            if (f1.length > 0)
                if (txtValue.indexOf(f1, 0) !== -1)
                    qshow = 1;
            if (f2.length > 0)
                if (txtValue.indexOf(f2, 0) !== -1)
                    qshow = 1;
            if (f3.length > 0)
                if (txtValue.indexOf(f3, 0) !== -1)
                    qshow = 1;
            if (f4.length > 0)
                if (txtValue.indexOf(f4, 0) !== -1)
                    qshow = 1;
            if (f5.length > 0)
                if (txtValue.indexOf(f5, 0) !== -1)
                    qshow = 1;
            if (f6.length > 0)
                if (txtValue.indexOf(f6, 0) !== -1)
                    qshow = 1;
            if (f7.length > 0)
                if (txtValue.indexOf(f7, 0) !== -1)
                    qshow = 1;
            if (f8.length > 0)
                if (txtValue.indexOf(f8, 0) !== -1)
                    qshow = 1;
            if (f9.length > 0)
                if (txtValue.indexOf(f9, 0) !== -1)
                    qshow = 1;
            if (f10.length > 0)
                if (txtValue.indexOf(f10, 0) !== -1)
                    qshow = 1;
            if (f11.length > 0)
                if (txtValue.indexOf(f11, 0) !== -1)
                    qshow = 1;
            if (f12.length > 0)
                if (txtValue.indexOf(f12, 0) !== -1)
                    qshow = 1;
        } else {
            qshow = 1;
        }
        if (txtValue.indexOf(filter) > -1)
            show = 1
        if ((qshow == 1) && (show == 1)) {
            li[i].style.display = '';
        } else {
            li[i].style.display = 'none';
        }
    }
}

          </script>

      </div>
        <div class="adCont row">
            <div class="me-auto text-center">
                
<script async type="a821953e36abcb9cb469edf3-text/javascript">
  function findValidDate(val) {
    let d =   new Date(val);;
    let date = d.getFullYear() + "-" + d.getMonth()+"-"+d.getDate()+" "+d.getHours()+":"+d.getMinutes()+":"+d.getSeconds();
  
    var d1 = new Date(date); //yyyy-mm-dd hh:mm:ss

    var currentdate = new Date(); //fetch the current date value
 
    if (d1.getTime() < currentdate.getTime()) {
      return false;
    
    } else {

      return true;
    }
  }
  const userProfile = JSON.parse(localStorage.getItem("userProfile"));
  if (findValidDate(userProfile?.ads_free_till)) {
  
    atOptions = {
      key: "4439e3c279bee065536d153688548a10",
      format: "iframe",
      height: window.innerWidth < 600 ? 40 : 90,
      width: window.innerWidth < 600 ? 300 : 728,
      params: {},
    };
    document.write(
      "<scr" +
        'ipt async type="text/javascript" src="http' +
        (location.protocol === "https:" ? "s" : "") +
        '://whiteinflammablejaws.com/41/a3/47/41a347e3e4cd3f7d448317dd8f7b963c.js"></scr' +
        "ipt>"
    );
  }
</script>



            <div>
        </div>
    </div>
    

       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous" type="a821953e36abcb9cb469edf3-text/javascript"></script>
       <script src="/static/rarbg/css/jquery-ui.js?v=1.04" type="a821953e36abcb9cb469edf3-text/javascript"></script>
       <script src="/static/rarbg/css/slick.min.js?v=1.04" type="a821953e36abcb9cb469edf3-text/javascript"></script>

    </body>
       
       
        
       

            <footer class="row align-center">
                    <div style="text-align: center; color: white;margin-top: 20px;">
        <a
        class="anal tdlinkfull"
        href="/"
        target="_blank"
        style="color: white; text-decoration: underline"
        >Home</a
      >
      |
      <a
        class="anal tdlinkfull"
        href="/about-us/"
        style="color: white; text-decoration: underline"
        >About us</a
      >

      |
      <a
        class="anal tdlinkfull"
        href="/latest/rss/"
        target="_blank"
        style="color: white; text-decoration: underline"
        >RSS</a
      >
      


      
      |
      <a
        class="anal tdlinkfull"
        href="https://thepiratebayproxy.github.io/"
        target="_blank"
        style="color: white; text-decoration: underline"
        >TPB Proxy</a
      >
      |
      <a
        class="anal tdlinkfull"
        href="https://therarbg.com/discord/"
        target="_blank"
        style="color: white; text-decoration: underline"
        >Discord</a
      >
      |
      <a
        class="anal tdlinkfull"
        href="https://www.reddit.com/r/TheRarBg/"
        target="_blank"
        style="color: white; text-decoration: underline"
        >Reddit</a
      >
      

      <br />
    </div>
    <br />

    <div style="text-align: center; color: white; font-size: 11px;">
      Donation ETH Address: 0x5C8Ba662A48811B52D8A24074569A10B03245bf9
    </div>
    <br />
    <div style="text-align: center; color: white">
        <p>© 2023 The RarBg. All rights reserved.</p>
    </div>

            </footer>
       
</html>
"""

# Extract torrent information
torrents = extract_torrents(html)

# Print the extracted data
for torrent in torrents:
    print(torrent)