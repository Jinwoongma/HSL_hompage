<template>
  <div>
    <h3 class="pb-4">About us</h3>
    <h5>Mission</h5><hr>
    <h6>우리의 사명(Mission)은 모든 분야의 지식과 기술을 사용하여 인류의 행복한 삶을 진일보시키기 위한 기술적 해답-특히 건강한 삶을 통한 해답-을 제공하고, 이러한 추구를 지속할 수 있는 창조적이고 도전적인 전문가를 양성하는 데에 있다.</h6>

    <h5>Vision</h5><hr>
    <h6>헬스케어솔루션연구실의 비젼(vision)은 크게 세 가지이다. 첫째, 핵심적인 건강 문제 해결을 위한 효율적/실용적 기술을 개발하여 인류의 삶의 질(Quality of Life, QoL)을 향상 시키는 것이다. 둘째, 미래 의료 혁신에 대한 새로운 기술적, 이론적 토대를 마련하여 새로운 미래가치를 창출하는데에 기여하는 것이다. 셋째, 행복추구에 대한 정신적, 영적, 기술적 가치 및 정의(righteousness), 관용(tolerance), 사랑(love)에 대한 행동양식을 공유하고 어디에서든 실천하는 전문가를 양성하는 것이다.</h6>

    <div>
      <!-- <ul>
        <li v-for="member in ungraduatedMembers" :key="`member_${member.id}`">
          {{ member.name }}
        </li>
      </ul> -->

      <div class=" row row-cols-2 row-cols-md-4 pt-5"> 
        <div v-for="member in ungraduatedMembers" :key="`member_${member.id}`" class='col mb-4'>
          <div class="card">
            <img :src="`http://localhost:8000${member.photo}`" class="card-img-top">
            <div class="card-body px-0 text-center">
              <h5 class="card-title">{{ member.name }}</h5>
              <p class="card-text"> {{ member.course }} </p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>

</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
    name: 'AboutVeiw',
    data() {
      return {
        members: [],
      }
    },
    methods: {
      fetchMembers() {
        axios.get(SERVER_URL + '/members/')
          .then( res => {
            console.log(res)
            this.members = res.data
          })
          .catch( err => console.error(err) )
      }
    },
    created() {
      this.fetchMembers()
    },
    computed: {
      ungraduatedMembers() {
        return this.members.filter(function(member) {
          return member.is_graduate === false
        })
      },
      photoUrl() {
        const url = this.member.photo
        return `http://localhost:8000/${url}`
      }
    }
}
</script>

<style>
  .card {
    border: none;
  }
  .card-title {
    font-size: 18px;
  }
  .card-text {
    font-size: small;
  }
</style>