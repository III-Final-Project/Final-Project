<template>
  <div class="cwArea">
    <div class="row">
      <div class="col-md-6">
        <h4>Current Camera</h4>
        <code v-if="device">{{ device.label }}</code>
        <div class="border">
          <div v-if="status">
            <vue-web-cam
              ref="webcam"
              :device-id="deviceId"
              width="100%"
              @started="onStarted"
              @stopped="onStopped"
              @error="onError"
              @cameras="onCameras"
            />
          </div>
        </div>
        <div class="row">
          <div class="col-md-12 fotoArea">
            <select v-model="camera">
              <option>-- Select Device --</option>
              <option
                v-for="device in devices"
                :key="device.deviceId"
                :value="device.deviceId"
              >
                {{ device.label }}
              </option>
            </select>
          </div>
          <div class="col-md-12">
            <button type="button" class="btn btn-primary" @click="onCapture">
              Capture Photo
            </button>
            <button type="button" class="btn btn-danger" @click="onStop">
              Stop Camera
            </button>
            <button type="button" class="btn btn-success" @click="onStart">
              Start Camera
            </button>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <h4>Captured Image</h4>
        <figure class="figure">
          <img :src="img" class="img-responsive" />
          <h4>{{ user_name }}</h4>
        </figure>
      </div>
      <div><button @click="testing">test</button></div>
      <div>
        <!-- <img :src="newImg" /> -->
        <!-- <h1>{{ user_name }}</h1> -->
      </div>
    </div>
  </div>
</template>

<script>
import { WebCam } from 'vue-web-cam';

export default {
  name: 'webcam',
  components: {
    'vue-web-cam': WebCam,
  },
  data() {
    return {
      camera: null,
      deviceId: null,
      devices: [],
      newImg: null,
      status: true,
      cacheImg: null,
      timeInterval: null,
      // canvus
      img: null,
      user_name: null,
      face_location: null,
    };
  },
  computed: {
    device() {
      return this.devices.find((n) => n.deviceId === this.deviceId);
    },
  },
  watch: {
    camera(id) {
      this.deviceId = id;
    },
    devices() {
      // Once we have a list select the first one
      const [first, ...tail] = this.devices;
      if (first) {
        this.camera = first.deviceId;
        this.deviceId = first.deviceId;
      } else {
        // eslint-disable-next-line
        console.log(tail);
      }
    },
  },
  methods: {
    async onCapture() {
      let count = 0;
      this.timeInterval = await setInterval(() => {
        this.cacheImg = this.$refs.webcam.capture();
        const formData = new FormData();
        formData.append('picture', this.cacheImg);
        // 最多打4次後停住
        count += 1;
        if (count === 4) {
          this.user_name = 'Unknown';
          clearInterval(this.timeInterval);
        }
        this.axios.post('http://localhost:5000/face', formData).then((res) => {
          // this.newImg = `data:image/jpeg;base64,${res.data}`;
          // eslint-disable-next-line no-console
          // console.log(res.data);
          if (
            res.data.returnCode === '200' &&
            res.data.details[0].user_name !== 'Unknown'
          ) {
            this.user_name = res.data.details[0].user_name;
            clearInterval(this.timeInterval);
          }
        });
      }, 1000);
    },
    async testing() {
      this.img = this.$refs.webcam.capture();
      const formData = new FormData();
      formData.append('picture', this.img);
      this.axios.post('http://localhost:5000/face', formData).then((res) => {
        // this.user_name = res.data.details[0].name;
        // this.face_location = res.data.details[0].face_location;
        console.log(res.data);
      });
    },
    onStarted(stream) {
      // eslint-disable-next-line
      console.log('On Started Event', stream);
    },
    onStopped(stream) {
      // eslint-disable-next-line
      console.log('On Stopped Event', stream);
    },
    onStop() {
      this.$refs.webcam.stop();
    },
    async onStart() {
      this.status = true;
      this.$refs.webcam.start();
    },
    onError(error) {
      // eslint-disable-next-line
      console.log('On Error Event', error);
    },
    onCameras(cameras) {
      this.devices = cameras;
      // this.$refs.webcam.stop();
      // eslint-disable-next-line
      console.log('On Cameras Event', cameras);
    },
    // onCameraChange(deviceId) {
    //   this.deviceId = deviceId;
    //   this.camera = deviceId;
    //   // eslint-disable-next-line
    //   console.log('On Camera Change Event', deviceId);
    // },
  },
};
</script>

<style scoped>
.border {
  -webkit-transform: scaleX(-1);
  transform: scaleX(-1);
  height: 30vh;
}

.fotoArea {
  height: 30vh;
}

.img-responsive {
  object-fit: contain;
  max-width: 100%;
}
</style>
