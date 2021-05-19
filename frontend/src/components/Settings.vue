<template>
  <div style="display: flex; flex-direction: column; align-items: center;" class="mt-7">
    <div style="display: flex; flex-direction: column; align-items: center;">

      <SettingsSection name="Security">
        <v-card class="px-7 pt-5 pb-6 ma-2" style="width: 315px; min-height: 300px;
                                                   display: flex; flex-direction: column">
          <div style="font-weight: 500; font-size: 1.3rem" class="mb-2">Change Password</div>
          <div>
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
          </div>
          <div style="flex-grow: 100"></div>
          <div style="display: flex" class="mt-3">
            <v-btn style="flex: 1 1 0;" color="#ff8200"
                   class="mr-2" text
                   @click="$refs.curPassword.reset();
                         $refs.newPassword.reset();
                         $refs.passwordConfirm.reset();
                        ">
              Cancel
            </v-btn>
            <v-btn style="flex: 1 1 0; color: white" color="#ff8200" @click="updatePassword()">
              Update
            </v-btn>
          </div>
        </v-card>
      </SettingsSection>

      <SettingsSection name="Profile" class="mt-10">
        <v-card class="px-7 pt-5 pb-6 ma-2" style="width: 315px; min-height: 300px;
                                                   display: flex; flex-direction: column">
          <div style="font-weight: 500; font-size: 1.3rem">Update Name</div>
          <div style="color: #444444" class="mb-2">Your current name is
                                                   {{ currentUser.first_name }}
                                                   {{ currentUser.last_name }}
          </div>
          <div>
            <v-text-field v-model="firstName" ref="firstName"
                          :rules="firstNameRules" label="First name" required
            ></v-text-field>
            <v-text-field v-model="lastName" ref="lastName"
                          :rules="lastNameRules" label="Last name" required
            ></v-text-field>
          </div>
          <div style="flex-grow: 100"></div>
          <div style="display: flex" class="mt-3">
            <v-btn style="flex: 1 1 0;" color="#ff8200"
                   class="mr-2" text
                   @click="$refs.firstName.reset();
                         $refs.lastName.reset();
                        ">
              Cancel
            </v-btn>
            <v-btn style="flex: 1 1 0; color: white" color="#ff8200" @click="updateName()">
              Update
            </v-btn>
          </div>
        </v-card>
        <v-card class="px-7 pt-5 pb-6 ma-2" style="width: 315px; min-height: 300px;
                                                   display: flex; flex-direction: column">
          <div style="font-weight: 500; font-size: 1.3rem">Update Avatar</div>
          <div class="mb-2"></div>
          <div>
            <v-file-input ref="avatar" v-model="avatarFile"
                          :rules="avatarRules"
                          accept="image/png, image/jpeg, image/gif"
                          placeholder="Choose an avatar"
                          prepend-icon=""
                          append-icon="mdi-camera"
                          label="Avatar"
                          :error-messages="avatarErrorMessage"
            ></v-file-input>
          </div>
          <div style="color: #444444" class="">Maximum allowed size: 500x500 px</div>
          <div style="color: #444444" class="">Available formats: JPG, PNG or GIF</div>

          <div style="flex-grow: 100"></div>
          <div style="display: flex" class="mt-3">
            <v-btn style="flex: 1 1 0;" color="#ff8200"
                   class="mr-2" text
                   @click="$refs.avatar.reset()">
              Cancel
            </v-btn>
            <v-btn style="flex: 1 1 0; color: white" color="#ff8200" @click="updateAvatar()">
              Update
            </v-btn>
          </div>
        </v-card>
      </SettingsSection>
    </div>
  </div>
</template>

<script>
import SettingsSection from '@/components/SettingsSection.vue';
import APIHelper from '@/api/apihelper';

export default {
  name: 'Settings',
  components: { SettingsSection },
  data() {
    return {
      currentUser: {},

      // Password

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
      const valid = this.$refs.curPassword.validate()
        && this.$refs.newPassword.validate()
        && this.$refs.passwordConfirm.validate();
      if (!valid) {
        this.focusFirst(['curPassword', 'newPassword', 'passwordConfirm']);
        return;
      }
      APIHelper.put('/account/changePassword', {
        old_password: this.curPassword,
        new_password: this.newPassword,
        password_confirm: this.passwordConfirm,
      });
    },
    updateName() {
      const valid = this.$refs.firstName.validate() && this.$refs.lastName.validate();
      if (!valid) {
        this.focusFirst(['firstName', 'lastName']);
        return;
      }
      APIHelper.put('/account/updateProfile', {
        first_name: this.firstName,
        last_name: this.lastName,
      });
    },
    resetAvatar() {
      if (!this.avatarFile) {
        this.avatarBinary = undefined;
        this.avatarDimensions = [null, null];
      }
    },
    updateAvatar() {
      const valid = this.$refs.avatar.validate();
      if (!valid) {
        this.focusFirst(['avatar']);
        return;
      }
      this.loadAvatarWidth(() => {
        const validwh = this.avatarDimensions[0] <= 500 && this.avatarDimensions[1] <= 500;
        if (!validwh) {
          this.focusFirst(['avatar']);
          this.avatarErrorMessage = 'Image is bigger than 500x500 px';
          return;
        }
        this.loadAvatarBinary(() => {
          APIHelper.put('/account/updateProfile', this.avatarBinary, {
            headers: {
              contentType: 'multipart/form-data',
            },
          });
        });
      });
    },
    loadAvatarWidth(next) {
      if (!this.avatarFile) {
        this.avatarSrc = '';
        this.avatarDimensions = [null, null];
        return;
      }
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
