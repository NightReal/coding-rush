<template>
  <div style="display: flex; flex-direction: column; align-items: center;" class="mt-3">
    <div style="display: flex; justify-content: space-between;
                max-width: 1000px; min-width: 800px; width: 90vw">
      <v-btn class="text-capitalize mt-3" color="#ff8200"
             style="color: white; font-size: 0.95rem; width: 110px"
             @click="$router.push(`/profile/${$store.getters.user.username}`)">
        <v-icon class="ml-n2 mr-1">mdi-chevron-left</v-icon>
        Profile
      </v-btn>
      <div style="font-size: 2.5rem; font-weight: 600" class="mb-3">Settings</div>
      <div style="width: 110px"></div>
    </div>
    <div style="color: #444444; font-size: 1.2rem; max-width: 500px; text-align: center;">
      Here you can set up your account.
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;" class="mt-7">

      <SettingsSection name="Security">
        <SettingsCard title="Change Password" :error-box="passwordErrorBox"
                      @update="updatePassword()"
                      @cancel="cancelPassword()">
          <v-form class="pa-0 ma-0" ref="formPassword" lazy-validation autocomplete="off">
            <v-text-field v-model="curPassword" ref="curPassword"
                          :rules="curPasswordRules" label="Current password" required
                          autocomplete="password"
                          :append-icon="showCurPassword ? 'mdi-eye' : 'mdi-eye-off'"
                          :type="showCurPassword ? 'text' : 'password'"
                          @click:append="showCurPassword = !showCurPassword"
            ></v-text-field>
            <v-text-field v-model="newPassword" ref="newPassword"
                          :rules="newPasswordRules" label="New password" required
                          autocomplete="new-password"
                          :append-icon="showNewPassword ? 'mdi-eye' : 'mdi-eye-off'"
                          :type="showNewPassword ? 'text' : 'password'"
                          @click:append="showNewPassword = !showNewPassword"
            ></v-text-field>
            <v-text-field v-model="passwordConfirm" ref="passwordConfirm"
                          :rules="passwordConfirmRules" label="Confirm password" required
                          :append-icon="showPasswordConfirm ? 'mdi-eye' : 'mdi-eye-off'"
                          :type="showPasswordConfirm ? 'text' : 'password'"
                          @click:append="showPasswordConfirm = !showPasswordConfirm"
            ></v-text-field>
          </v-form>
        </SettingsCard>
      </SettingsSection>

      <SettingsSection name="Profile" class="mt-7">
        <SettingsCard title="Update Name" :error-box="nameErrorBox"
                      :caption="`Your current name is
                                ${currentUser.first_name} ${currentUser.last_name}`"
                      @update="updateName()"
                      @cancel="cancelName">
          <v-form class="pa-0 ma-0" ref="formName" lazy-validation autocomplete="off">
            <v-text-field v-model="firstName" ref="firstName"
                          :rules="firstNameRules" label="First name" required
            ></v-text-field>
            <v-text-field v-model="lastName" ref="lastName"
                          :rules="lastNameRules" label="Last name" required
            ></v-text-field>
          </v-form>
        </SettingsCard>
        <SettingsCard title="Update Avatar" :error-box="avatarErrorBox"
                      @update="updateAvatar()"
                      @cancel="cancelAvatar()">
          <v-form class="pa-0 ma-0" ref="formAvatar" lazy-validation autocomplete="off">
            <v-file-input ref="avatar" v-model="avatarFile" class="mt-3"
                          :rules="avatarRules"
                          accept="image/png, image/jpeg, image/gif"
                          placeholder="Choose an avatar"
                          prepend-icon=""
                          append-icon="mdi-camera"
                          label="Avatar"
                          :error-messages="avatarErrorMessage"
            ></v-file-input>
          </v-form>
          <div style="color: #444444" class="mt-1">Maximum allowed size: 500x500 px</div>
          <div style="color: #444444" class="">Available formats: JPG, PNG or GIF</div>
        </SettingsCard>
      </SettingsSection>
    </div>
  </div>
</template>

<script>
import SettingsSection from '@/components/Settings/SettingsSection.vue';
import APIHelper from '@/api/apihelper';
import SettingsCard from '@/components/Settings/SettingsCard.vue';

export default {
  name: 'Settings',
  components: { SettingsCard, SettingsSection },
  data() {
    return {
      currentUser: {},

      // Password

      passwordErrorBox: '',

      curPassword: '',
      showCurPassword: false,
      curPasswordRules: [
        (v) => !!v || 'Current password is required',
      ],

      newPassword: '',
      showNewPassword: false,
      newPasswordRules: [
        (v) => !!v || 'New password is required',
        (v) => (v && v.length <= 64) || 'Password must be less than 64 characters',
        (v) => (v && v.length >= 8) || 'Password must be more than 8 characters',
      ],

      passwordConfirm: '',
      showPasswordConfirm: false,
      passwordConfirmRules: [
        (v) => !!v || 'Password confirmation is required',
        (v) => (v === this.newPassword) || 'Passwords didn\'t match',

      ],

      // First Name and Last Name

      nameErrorBox: '',

      firstName: '',
      lastName: '',
      firstNameRules: [
        (v) => !!v || 'First name required',
        (v) => /^[a-zA-Z0-9 _.-]*$/.test(v)
          || 'Only Latin letters, digits and symbols . - _ are allowed',
        (v) => !v || v.replace(/[^a-zA-Z]/g, '').length >= 3
          || 'First name must contain at least 3 letters',
        (v) => !v || v.length <= 40 || 'First name must be less than 40 characters',
      ],
      lastNameRules: [
        (v) => !!v || 'Last name required',
        (v) => /^[a-zA-Z0-9 _.-]*$/.test(v)
          || 'Only Latin letters, digits and symbols . - _ are allowed',
        (v) => !v || v.replace(/[^a-zA-Z]/g, '').length >= 3
          || 'Last name must contain at least 3 letters',
        (v) => !v || v.length <= 40 || 'Last name must be less than 40 characters',
      ],

      // Avatar

      avatarErrorBox: '',

      avatarFile: undefined,
      avatarBinary: undefined,
      avatarDimensions: [null, null],
      avatarErrorMessage: '',
      avatarRules: [
        (v) => {
          this.avatarErrorMessage = '';
          if (!v) this.resetAvatar();
          return true;
        },
        (v) => !!v || 'Image is required',
        (v) => !v || v.size < 2000000 || 'Avatar size should be less than 2 MB',
      ],
    };
  },

  mounted() {
    if (!this.$store.getters.user.username) {
      this.$store.dispatch('getUser').then(this.loadUser);
    } else {
      this.loadUser();
    }
  },

  methods: {
    loadUser() {
      this.currentUser = this.$store.getters.user;
    },
    focusFirst(fields) {
      // eslint-disable-next-line guard-for-in,no-restricted-syntax
      for (const i in fields) {
        const element = this.$refs[fields[i]];
        if (!element.valid) {
          element.focus();
          break;
        }
      }
    },

    updatePassword() {
      const valid = this.$refs.formPassword.validate();
      if (!valid) {
        this.focusFirst(['curPassword', 'newPassword', 'passwordConfirm']);
        return;
      }
      APIHelper.put('/account/changePassword', {
        old_password: this.curPassword,
        new_password: this.newPassword,
        new_password_confirm: this.passwordConfirm,
      })
        .then(() => this.successPassword())
        .catch((e) => this.errorPassword(e));
    },
    cancelPassword() {
      this.$refs.curPassword.reset();
      this.$refs.newPassword.reset();
      this.$refs.passwordConfirm.reset();
      this.passwordErrorBox = '';
    },
    errorPassword(err) {
      if (err.response && err.response.data) {
        const e = err.response.data;
        if (e.old_password && e.old_password.includes('Current password does not match')) {
          this.passwordErrorBox = 'Current password is incorrect.';
          return;
        }
        if (e.new_password && e.new_password.includes('This password is too common.')) {
          this.passwordErrorBox = 'New password is too common.';
          return;
        }
        const order = ['old_password', 'new_password', 'new_password_confirm'];
        for (const sec of order) { // eslint-disable-line no-restricted-syntax
          if (e[sec] && e[sec].length) {
            this.passwordErrorBox = e[sec][0]; // eslint-disable-line prefer-destructuring
            return;
          }
        }
      }
      this.passwordErrorBox = 'Something went wrong.';
      console.log(err);
      console.log(err.response);
    },
    successPassword() {
      this.cancelPassword();
      this.passwordErrorBox = '!Password Updated!';
    },

    updateName() {
      this.nameErrorBox = '';
      const valid = this.$refs.formName.validate();
      if (!valid) {
        this.focusFirst(['firstName', 'lastName']);
        return;
      }
      APIHelper.put('/account/updateProfile', {
        first_name: this.firstName,
        last_name: this.lastName,
      })
        .then(() => this.successName())
        .catch((e) => this.errorName(e));
    },
    cancelName() {
      this.$refs.firstName.reset();
      this.$refs.lastName.reset();
      this.nameErrorBox = '';
    },
    errorName(err) {
      if (err.response && err.response.data) {
        const e = err.response.data;
        for (const sec in e) { // eslint-disable-line no-restricted-syntax
          if (e[sec] && e[sec].length) {
            this.nameErrorBox = e[sec][0]; // eslint-disable-line prefer-destructuring
            return;
          }
        }
      }
      this.passwordErrorBox = 'Something went wrong.';
      console.log(err);
      console.log(err.response);
    },
    successName() {
      this.currentUser.first_name = this.firstName;
      this.currentUser.last_name = this.lastName;
      this.cancelName();
      this.nameErrorBox = '!Name Updated!';
      this.$store.dispatch('getUser');
    },

    updateAvatar() {
      this.avatarErrorBox = '';
      const valid = this.$refs.formAvatar.validate();
      if (!valid) {
        this.focusFirst(['avatar']);
        return;
      }
      this.loadAvatarWidth(() => {
        let error = '';
        const [w, h] = this.avatarDimensions;
        if (w > 500 || h > 500) {
          error = 'Image is bigger than 500x500 px';
        } else if (w / h > 2) {
          error = 'Image width is more than twice the height';
        } else if (w / h < 0.5) {
          error = 'Image height is more than twice the width';
        }
        if (error) {
          this.avatarErrorMessage = error;
          return;
        }
        this.loadAvatarBinary(() => {
          APIHelper.put('/account/updateProfile', this.avatarBinary, {
            headers: {
              contentType: 'multipart/form-data',
            },
          })
            .then(() => this.successAvatar())
            .catch((e) => this.errorAvatar(e));
        });
      });
    },
    cancelAvatar() {
      this.$refs.avatar.reset();
      this.avatarErrorBox = '';
    },
    errorAvatar(err) {
      if (err.response && err.response.data) {
        const e = err.response.data;
        for (const sec in e) { // eslint-disable-line no-restricted-syntax
          if (e[sec] && e[sec].length) {
            this.nameErrorBox = e[sec][0]; // eslint-disable-line prefer-destructuring
            return;
          }
        }
      }
      this.passwordErrorBox = 'Something went wrong.';
      console.log(err);
      console.log(err.response);
    },
    successAvatar() {
      this.cancelAvatar();
      this.avatarErrorBox = '!Avatar updated!';
      this.$store.dispatch('getUser');
    },
    resetAvatar() {
      if (!this.avatarFile) {
        this.avatarBinary = undefined;
        this.avatarDimensions = [null, null];
      }
    },
    loadAvatarWidth(next) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const img = new Image();
        img.onload = () => {
          this.avatarDimensions = [img.width, img.height];
          next();
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(this.avatarFile);
    },
    loadAvatarBinary(next) {
      const formData = new FormData();
      formData.append('avatar', this.avatarFile);
      this.avatarBinary = formData;
      next();
    },

  },
};
</script>

<style scoped>

</style>
