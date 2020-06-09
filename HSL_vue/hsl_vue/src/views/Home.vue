<template>
  <div >
    <!-- carousel -->
    <div id="carouselExampleInterval" class="carousel slide carousel py-3" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
      </ol>
      
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../assets/main/carousel/img1.jpg" class="d-block w-100 " alt="...">
        </div>
        <div class="carousel-item">
          <img src="../assets/main/carousel/img2.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="../assets/main/carousel/img3.jpg" class="d-block w-100" alt="...">
        </div>
      </div>

      <a class="carousel-control-prev" href="#carouselExampleInterval" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleInterval" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    <div class="discription text-center">
      <h1>헬스케어솔루션연구실</h1>
      <h2>(Healthcare Solution Laboratory)</h2>
      <p>헬스케어솔루션연구실은 건강 및 의료분야 당면 과제 해결 및 미지의 영역 접근을 위한 기술과 제품 개발을 추구하며, 의학과 공학 중심 다학제 연구 수행을 통해 새로운 시각으로 문제를 바라보고 해결할 수 있는 인재를 양성합니다.</p>
    </div>
      
    <!--  -->
    <div class='pt-3'>
      <div class=" row row-cols-1 row-cols-md-3"> 
        <div class='col mb-4'>
          <div class="card">
            <img src="../assets/main/biosignal.jpg" class="card-img-top" alt="...">
            <div class="card-body px-0">
              <h5 class="card-title">BIO-SIGNAL ANALYSIS</h5>
              <p class="card-text">생체신호 측정을 위한 생체계측시스템, 잡음 제거와 특징 검출을 위한 생체신호처리, 자동 진단 및 의사결정을 위한 생체신호 분석 및 분류 기술을 연구 합니다.</p>
            </div>
          </div>
        </div>
        
        <div class='col mb-4'>
          <div class="card">
            <img src="../assets/main/wellness.jpg" class="card-img-top" alt="...">
            <div class="card-body px-0">
              <h5 class="card-title">u-HEALTH & WELLNESS</h5>
              <p class="card-text">언제, 어디서나 편리하게 건강상태를 모니터링하고 관리하기 위한 기술로 무구속(Unconstrained), 무자각(Unconsciousness), 무공백(Blankless) 측정 및 분석기술을 연구합니다.</p>
            </div>
          </div>
        </div>

        <div class='col mb-4'>
          <div class="card">
            <img src="../assets/main/model.jpg" class="card-img-top" alt="...">
            <div class="card-body px-0">
              <h5 class="card-title">MODELING & SIMULATION</h5>
              <p class="card-text">인체의 세포, 조직, 장기 등을 수학적으로 모델링하고 컴퓨터로 구현하여 가상으로 시뮬레이션 함으로 안전하고 정교한 개인맞춤형 정밀의료(Precision Medicine)를 구현합니다.</p>
            </div>
          </div>
        </div>
        
        <div class='col mb-4'>
          <div class="card">
            <img src="../assets/main/achievement.jpg" class="card-img-top" alt="...">
            <div class="card-body px-0">
              <h5 class="card-title">ACHIEVEMENTS</h5>
              <p class="card-text">국내외 논문, 책, 강연, 학술대회, 출원되거나 등록된 특허 등 연구실의 연구 업적을 소개합니다.</p>
            </div>
          </div>
        </div>

        <div class='col mb-4'>
          <div class="card">
            <img src="../assets/main/member.jpg" class="card-img-top" alt="...">
            <div class="card-body px-0">
              <h5 class="card-title">MEMBERS</h5>
              <p class="card-text">헬스케어솔루션연구실의 풀타임, 파트타임 연구원 들과 여러 협력연구원 및 기관을 소개합니다.</p>
            </div>
          </div>
        </div>

        <div class='col mb-4'>
          <div class="card">
            <img src="../assets/main/news.jpg" class="card-img-top" alt="...">
            <div class="card-body px-0">
              <h5 class="card-title">NEWS</h5>
              <p class="card-text">헬스케어솔루션연구실에서의 최근 소식을 알 수 있습니다.</p>
            </div>
          </div>
        </div>
      </div>   
    </div>

    <section class='more-info d-flex flex-column justify-content-center'> 
      <div class="bg"></div> 
      <h1>Would you like to see more?</h1> 
      <h3>헬스케어솔루션실험실을 더 알고 싶은가요?</h3> 
      <div>
        <button type="button" class="btn">더 알아보기(More info)</button>
      </div>
    </section>

    <hr>
    <div class='footer'>
      <p>59626 전라남도 여수시 대학로 50 전남대학교 여수캠퍼스 제3공학관 502호 헬스케어솔루션 연구실</p>
      <p>Healthcare Solution Laboratory, 502, 3rd Eng. Bldg., Chonnam National University, 50 Daehak-ro, Yeosu, Republic of Korea (59626) </p>
      <p>TEL: +82-61-659-7872 / FAX: +82-61-659-7369</p>
      <p>ⓒ Healthcare Solution Laboratory, 2016.</p>
    </div>  
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
  components: {

  }
}
</script>

<style scoped>
  .card {
    border: 0;
  }
  .card-title {
    font-size: 16px
  }
   .card-body {
    font-size: 14px
  }
  .discription p {
    color: #666666;
    font-weight: 500;
    line-height: 1.4em;
    font-size: 18px;
  }

  .more-info {
    background: linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url(../assets/main/more.jpg) no-repeat bottom center;;
    background-size: cover;
    height:600px;
    max-height: 460px;
    max-width: 1110px;
    margin-bottom: 20px;
    padding-left: 20px;
  }

  .more-info h1, h3{
    color: white;
    text-shadow: 1px 1px 1px black;
  }
  .more-info button {
    color: white;
    font-weight: 600;
    border: solid 2px white;
  }

  .footer {
    font-size: 12px;
    color: #333333;
    margin-bottom: 20px;
  }
  .footer p{
    margin: 0;
  }
</style>
