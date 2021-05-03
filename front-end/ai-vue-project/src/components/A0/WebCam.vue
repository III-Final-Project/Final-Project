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
        </figure>
      </div>
      <div>
        <img :src="newImg" />
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
      img: null,
      camera: null,
      deviceId: null,
      devices: [],
      newImg: null,
      status: true,
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
    onCapture() {
      this.img = this.$refs.webcam.capture();
      const formData = new FormData();
      formData.append('picture', this.img);
      this.axios.post('http://localhost:2204/receive', formData).then((res) => {
        this.newImg = `data:image/jpeg;base64,${res.data}`;
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
      this.$refs.webcam.stop();
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
</style>
