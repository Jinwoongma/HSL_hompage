

<template>
  <div id="app">
    <nav class="d-flex flex-column navbar navbar-expand-sm navbar-light bg-white">
			<div class="w-100 d-flex align-items-center justify-content-between justify-content-sm-center">
				<a class="navbar-brand" href="/">
					<img src="./assets/logo.png" height="100" alt="" loading="lazy">
				</a>
				<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
			</div>
			<div class="w-100">				
				<div class="collapse navbar-collapse" id="navbarNav" >
					<ul class="navbar-nav mx-auto mt-2">
						<li class="nav-item dropdown"> <router-link class="nav-link dropdown-toggle" to="/aboutus" id="navbardrop" data-toggle="dropdown">ABOUT US</router-link>
							<div class="dropdown-menu"> 
								<router-link class="dropdown-item" to="/aboutus">Members</router-link>
								<router-link class="dropdown-item" to="/">What's New?</router-link>
							</div>
						</li>
						<li class="nav-item dropdown"> <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown"> RESEARCH </a>
							<div class="dropdown-menu"> 
								<router-link class="dropdown-item" to="/">Biomedical Signal Processing & Analysis</router-link>
								<router-link class="dropdown-item" to="/">Physiological Modeling & Simulation</router-link>
								<router-link class="dropdown-item" to="/">u-Health & Wellness Technology</router-link>
							</div>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="#">PUBLICATION</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="#">PRESENTATION</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="#">PATENT</a>
						</li>
					</ul>
				</div>
			</div>
		</nav>


		<div class='container'>
			<router-view/>
		</div>
    


  </div>
  
</template>
<script>
export default {
  
}
</script>

<style>
#app {
  font-family: Arial, Helvetica, Geneva, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.nav-item {
	margin-left: 15px;
	font-size: 14px;
	font-weight: 600;
  color: black;
	}
.nav-link {

}

.dropdown:hover .dropdown-menu {display: block;}

@media (min-width: 576px)  {
	.navbar .nav-item .dropdown-menu{  display:block; opacity: 0;  visibility: hidden; transition:.3s; margin-top:0;  }
	.navbar .nav-item:hover .nav-link{ color: black;  }
	.navbar .dropdown-menu.fade-down{ top:80%; transform: rotateX(-75deg); transform-origin: 0% 0%; }
	.navbar .dropdown-menu.fade-up{ top:180%;  }
	.navbar .nav-item:hover .dropdown-menu{ transition: .3s; opacity:1; visibility:visible; top:100%; transform: rotateX(0deg); }
}		
</style>
