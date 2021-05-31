<template>
  <div class="cwArea">
    <div class="border">
      <div class="camera">
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
  </div>
</template>

<script>
import { WebCam } from 'vue-web-cam';
import FaceService from '../../service/face';

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
      const [first, ...tail] = this.devices;
      if (first) {
        this.camera = first.deviceId;
        this.deviceId = first.deviceId;
      } else {
        // eslint-disable-next-line
        console.log(tail);
      }
    },
    deviceId() {
      setTimeout(() => {
        this.onCapture();
      }, 500);
    },
  },
  methods: {
    onCapture() {
      let count = 0;
      this.timeInterval = setInterval(() => {
        this.cacheImg = this.$refs.webcam.capture();
        const formData = new FormData();
        formData.append('picture', this.cacheImg);
        // 最多打4次後停住
        if (count === 2) {
          this.user_name = 'Unknown';
          clearInterval(this.timeInterval);
          this.$emit('faceVerify', this.user_name);
        } else {
          count += 1;
          FaceService.faceDetect(formData).then((res) => {
            if (res.data.returnCode === '200') {
              this.user_name = res.data.detail[0].name;
              clearInterval(this.timeInterval);
              this.$emit('faceVerify', this.user_name);
            }
          });
        }
      }, 1000);
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
    onError(error) {
      // eslint-disable-next-line
      console.log('On Error Event', error);
    },
    onCameras(cameras) {
      this.devices = cameras;
    },
  },
};
</script>

<style scoped>
.border {
  -webkit-transform: scaleX(-1);
  transform: scaleX(-1);
  height: 40vh;
}
video {
  padding-bottom: 225px;
  border: none;
}
</style>
