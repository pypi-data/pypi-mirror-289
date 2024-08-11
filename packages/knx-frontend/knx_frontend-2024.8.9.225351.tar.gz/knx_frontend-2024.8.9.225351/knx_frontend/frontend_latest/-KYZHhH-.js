export const id=9184;export const ids=[9184];export const modules={80106:(e,i,t)=>{t.d(i,{d:()=>o});const o=e=>{switch(e.language){case"cz":case"de":case"fi":case"fr":case"sk":case"sv":return" ";default:return""}}},96287:(e,i,t)=>{var o=t(85461),a=t(69534),n=(t(8774),t(98597)),r=t(196),s=t(69760),l=t(33167),d=(t(66494),t(89874),t(80106)),c=t(96041);const h="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z",p="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M13.5,16V19H10.5V16H8L12,12L16,16H13.5M13,9V3.5L18.5,9H13Z";(0,o.A)([(0,r.EM)("ha-file-upload")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"accept",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"icon",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"secondary",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"supports",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Object})],key:"value",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"multiple",value(){return!1}},{kind:"field",decorators:[(0,r.MZ)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"uploading",value(){return!1}},{kind:"field",decorators:[(0,r.MZ)({type:Number})],key:"progress",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean,attribute:"auto-open-file-dialog"})],key:"autoOpenFileDialog",value(){return!1}},{kind:"field",decorators:[(0,r.wk)()],key:"_drag",value(){return!1}},{kind:"field",decorators:[(0,r.P)("#input")],key:"_input",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){(0,a.A)(t,"firstUpdated",this,3)([e]),this.autoOpenFileDialog&&this._openFilePicker()}},{kind:"method",key:"render",value:function(){return n.qy`
      ${this.uploading?n.qy`<div class="container">
            <div class="row">
              <span class="header"
                >${this.value?this.hass?.localize("ui.components.file-upload.uploading_name",{name:this.value.toString()}):this.hass?.localize("ui.components.file-upload.uploading")}</span
              >
              ${this.progress?n.qy`<span class="progress"
                    >${this.progress}${(0,d.d)(this.hass.locale)}%</span
                  >`:""}
            </div>
            <mwc-linear-progress
              .indeterminate=${!this.progress}
              .progress=${this.progress?this.progress/100:void 0}
            ></mwc-linear-progress>
          </div>`:n.qy`<label
            for=${this.value?"":"input"}
            class="container ${(0,s.H)({dragged:this._drag,multiple:this.multiple,value:Boolean(this.value)})}"
            @drop=${this._handleDrop}
            @dragenter=${this._handleDragStart}
            @dragover=${this._handleDragStart}
            @dragleave=${this._handleDragEnd}
            @dragend=${this._handleDragEnd}
            >${this.value?"string"==typeof this.value?n.qy`<div class="row">
                    <div class="value" @click=${this._openFilePicker}>
                      <ha-svg-icon
                        .path=${this.icon||p}
                      ></ha-svg-icon>
                      ${this.value}
                    </div>
                    <ha-icon-button
                      @click=${this._clearValue}
                      .label=${this.hass?.localize("ui.common.delete")||"Delete"}
                      .path=${h}
                    ></ha-icon-button>
                  </div>`:(this.value instanceof FileList?Array.from(this.value):(0,c.e)(this.value)).map((e=>n.qy`<div class="row">
                        <div class="value" @click=${this._openFilePicker}>
                          <ha-svg-icon
                            .path=${this.icon||p}
                          ></ha-svg-icon>
                          ${e.name} - ${((e=0,i=2)=>{if(0===e)return"0 Bytes";i=i<0?0:i;const t=Math.floor(Math.log(e)/Math.log(1024));return`${parseFloat((e/1024**t).toFixed(i))} ${["Bytes","KB","MB","GB","TB","PB","EB","ZB","YB"][t]}`})(e.size)}
                        </div>
                        <ha-icon-button
                          @click=${this._clearValue}
                          .label=${this.hass?.localize("ui.common.delete")||"Delete"}
                          .path=${h}
                        ></ha-icon-button>
                      </div>`)):n.qy`<ha-svg-icon
                    class="big-icon"
                    .path=${this.icon||p}
                  ></ha-svg-icon>
                  <ha-button unelevated @click=${this._openFilePicker}>
                    ${this.label||this.hass?.localize("ui.components.file-upload.label")}
                  </ha-button>
                  <span class="secondary"
                    >${this.secondary||this.hass?.localize("ui.components.file-upload.secondary")}</span
                  >
                  <span class="supports">${this.supports}</span>`}
            <input
              id="input"
              type="file"
              class="file"
              .accept=${this.accept}
              .multiple=${this.multiple}
              @change=${this._handleFilePicked}
          /></label>`}
    `}},{kind:"method",key:"_openFilePicker",value:function(){this._input?.click()}},{kind:"method",key:"_handleDrop",value:function(e){e.preventDefault(),e.stopPropagation(),e.dataTransfer?.files&&(0,l.r)(this,"file-picked",{files:this.multiple||1===e.dataTransfer.files.length?Array.from(e.dataTransfer.files):[e.dataTransfer.files[0]]}),this._drag=!1}},{kind:"method",key:"_handleDragStart",value:function(e){e.preventDefault(),e.stopPropagation(),this._drag=!0}},{kind:"method",key:"_handleDragEnd",value:function(e){e.preventDefault(),e.stopPropagation(),this._drag=!1}},{kind:"method",key:"_handleFilePicked",value:function(e){0!==e.target.files.length&&(this.value=e.target.files,(0,l.r)(this,"file-picked",{files:e.target.files}))}},{kind:"method",key:"_clearValue",value:function(e){e.preventDefault(),this._input.value="",this.value=void 0,(0,l.r)(this,"change")}},{kind:"get",static:!0,key:"styles",value:function(){return n.AH`
      :host {
        display: block;
        height: 240px;
      }
      :host([disabled]) {
        pointer-events: none;
        color: var(--disabled-text-color);
      }
      .container {
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border: solid 1px
          var(--mdc-text-field-idle-line-color, rgba(0, 0, 0, 0.42));
        border-radius: var(--mdc-shape-small, 4px);
        height: 100%;
      }
      label.container {
        border: dashed 1px
          var(--mdc-text-field-idle-line-color, rgba(0, 0, 0, 0.42));
        cursor: pointer;
      }
      :host([disabled]) .container {
        border-color: var(--disabled-color);
      }
      label.dragged {
        border-color: var(--primary-color);
      }
      .dragged:before {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background-color: var(--primary-color);
        content: "";
        opacity: var(--dark-divider-opacity);
        pointer-events: none;
        border-radius: var(--mdc-shape-small, 4px);
      }
      label.value {
        cursor: default;
      }
      label.value.multiple {
        justify-content: unset;
        overflow: auto;
      }
      .highlight {
        color: var(--primary-color);
      }
      .row {
        display: flex;
        width: 100%;
        align-items: center;
        justify-content: space-between;
        padding: 0 16px;
        box-sizing: border-box;
      }
      ha-button {
        margin-bottom: 4px;
      }
      .supports {
        color: var(--secondary-text-color);
        font-size: 12px;
      }
      :host([disabled]) .secondary {
        color: var(--disabled-text-color);
      }
      input.file {
        display: none;
      }
      .value {
        cursor: pointer;
      }
      .value ha-svg-icon {
        margin-right: 8px;
        margin-inline-end: 8px;
        margin-inline-start: initial;
      }
      .big-icon {
        --mdc-icon-size: 48px;
        margin-bottom: 8px;
      }
      ha-button {
        --mdc-button-outline-color: var(--primary-color);
        --mdc-icon-button-size: 24px;
      }
      mwc-linear-progress {
        width: 100%;
        padding: 16px;
        box-sizing: border-box;
      }
      .header {
        font-weight: 500;
      }
      .progress {
        color: var(--secondary-text-color);
      }
    `}}]}}),n.WF)},18966:(e,i,t)=>{t.d(i,{Q:()=>o,n:()=>a});const o=async(e,i)=>{const t=new FormData;t.append("file",i);const o=await e.fetchWithAuth("/api/file_upload",{method:"POST",body:t});if(413===o.status)throw new Error(`Uploaded file is too large (${i.name})`);if(200!==o.status)throw new Error("Unknown error");return(await o.json()).file_id},a=async(e,i)=>e.callApi("DELETE","file_upload",{file_id:i})},12263:(e,i,t)=>{t.d(i,{PS:()=>o,VR:()=>a});const o=e=>e.data,a=e=>"object"==typeof e?"object"==typeof e.body?e.body.message||"Unknown error, see supervisor logs":e.body||e.message||"Unknown error, see supervisor logs":e;new Set([502,503,504])},31447:(e,i,t)=>{t.d(i,{K$:()=>r,an:()=>l,dk:()=>s});var o=t(33167);const a=()=>Promise.all([t.e(2658),t.e(4475)]).then(t.bind(t,94475)),n=(e,i,t)=>new Promise((n=>{const r=i.cancel,s=i.confirm;(0,o.r)(e,"show-dialog",{dialogTag:"dialog-box",dialogImport:a,dialogParams:{...i,...t,cancel:()=>{n(!!t?.prompt&&null),r&&r()},confirm:e=>{n(!t?.prompt||e),s&&s(e)}}})})),r=(e,i)=>n(e,i),s=(e,i)=>n(e,i,{confirmation:!0}),l=(e,i)=>n(e,i,{prompt:!0})},69184:(e,i,t)=>{t.r(i),t.d(i,{KNXInfo:()=>u});var o=t(85461),a=t(98597),n=t(196),r=t(13314),s=(t(94392),t(7341),t(66494),t(96287),t(74259),t(73279),t(18966)),l=t(12263),d=t(31447),c=t(39987),h=t(61328);const p=new h.Q("info");let u=(0,o.A)([(0,n.EM)("knx-info")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.MZ)({type:Object})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"knx",value:void 0},{kind:"field",decorators:[(0,n.MZ)({type:Boolean,reflect:!0})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.MZ)({type:Object})],key:"route",value:void 0},{kind:"field",decorators:[(0,n.MZ)({type:Array,reflect:!1})],key:"tabs",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"knxInfoData",value(){return null}},{kind:"field",decorators:[(0,n.wk)()],key:"_projectPassword",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_uploading",value(){return!1}},{kind:"field",decorators:[(0,n.wk)()],key:"_projectFile",value:void 0},{kind:"method",key:"firstUpdated",value:function(){this.loadKnxInfo()}},{kind:"method",key:"render",value:function(){return a.qy`
      <hass-tabs-subpage
        .hass=${this.hass}
        .narrow=${this.narrow}
        .route=${this.route}
        .tabs=${this.tabs}
        .localizeFunc=${this.knx.localize}
      >
        <div class="columns">
          ${this.knxInfoData?a.qy`
                ${this._renderInfoCard()}
                ${this.knxInfoData?.project?this._renderProjectDataCard(this.knxInfoData.project):a.s6}
                ${this._renderProjectUploadCard()}
              `:a.qy`
                <ha-circular-progress alt="Loading..." size="large" active></ha-circular-progress>
              `}
        </div>
      </hass-tabs-subpage>
    `}},{kind:"method",key:"_renderInfoCard",value:function(){return a.qy` <ha-card class="knx-info">
      <div class="card-content knx-info-section">
        <div class="knx-content-row header">${this.knx.localize("info_information_header")}</div>

        <div class="knx-content-row">
          <div>XKNX Version</div>
          <div>${this.knxInfoData?.version}</div>
        </div>

        <div class="knx-content-row">
          <div>KNX-Frontend Version</div>
          <div>${"2024.8.9.225351"}</div>
        </div>

        <div class="knx-content-row">
          <div>${this.knx.localize("info_connected_to_bus")}</div>
          <div>
            ${this.hass.localize(this.knxInfoData?.connected?"ui.common.yes":"ui.common.no")}
          </div>
        </div>

        <div class="knx-content-row">
          <div>${this.knx.localize("info_individual_address")}</div>
          <div>${this.knxInfoData?.current_address}</div>
        </div>

        <div class="knx-bug-report">
          <div>${this.knx.localize("info_issue_tracker")}</div>
          <ul>
            <li>
              <a href="https://github.com/XKNX/knx-frontend/issues" target="_blank"
                >${this.knx.localize("info_issue_tracker_knx_frontend")}</a
              >
            </li>
            <li>
              <a href="https://github.com/XKNX/xknxproject/issues" target="_blank"
                >${this.knx.localize("info_issue_tracker_xknxproject")}</a
              >
            </li>
            <li>
              <a href="https://github.com/XKNX/xknx/issues" target="_blank"
                >${this.knx.localize("info_issue_tracker_xknx")}</a
              >
            </li>
          </ul>
        </div>
      </div>
    </ha-card>`}},{kind:"method",key:"_renderProjectDataCard",value:function(e){return a.qy`
      <ha-card class="knx-info">
          <div class="card-content knx-content">
            <div class="header knx-content-row">
              ${this.knx.localize("info_project_data_header")}
            </div>
            <div class="knx-content-row">
              <div>${this.knx.localize("info_project_data_name")}</div>
              <div>${e.name}</div>
            </div>
            <div class="knx-content-row">
              <div>${this.knx.localize("info_project_data_last_modified")}</div>
              <div>${new Date(e.last_modified).toUTCString()}</div>
            </div>
            <div class="knx-content-row">
              <div>${this.knx.localize("info_project_data_tool_version")}</div>
              <div>${e.tool_version}</div>
            </div>
            <div class="knx-content-row">
              <div>${this.knx.localize("info_project_data_xknxproject_version")}</div>
              <div>${e.xknxproject_version}</div>
            </div>
            <div class="knx-button-row">
              <ha-button
                class="knx-warning push-right"
                @click=${this._removeProject}
                .disabled=${this._uploading||!this.knxInfoData?.project}
                >
                ${this.knx.localize("info_project_delete")}
              </ha-button>
            </div>
          </div>
        </div>
      </ha-card>
    `}},{kind:"method",key:"_renderProjectUploadCard",value:function(){return a.qy` <ha-card class="knx-info">
      <div class="card-content knx-content">
        <div class="knx-content-row header">${this.knx.localize("info_project_file_header")}</div>
        <div class="knx-content-row">${this.knx.localize("info_project_upload_description")}</div>
        <div class="knx-content-row">
          <ha-file-upload
            .hass=${this.hass}
            accept=".knxproj, .knxprojarchive"
            .icon=${"M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M13.5,16V19H10.5V16H8L12,12L16,16H13.5M13,9V3.5L18.5,9H13Z"}
            .label=${this.knx.localize("info_project_file")}
            .value=${this._projectFile?.name}
            .uploading=${this._uploading}
            @file-picked=${this._filePicked}
          ></ha-file-upload>
        </div>
        <div class="knx-content-row">
          <ha-selector-text
            .hass=${this.hass}
            .value=${this._projectPassword||""}
            .label=${this.hass.localize("ui.login-form.password")}
            .selector=${{text:{multiline:!1,type:"password"}}}
            .required=${!1}
            @value-changed=${this._passwordChanged}
          >
          </ha-selector-text>
        </div>
        <div class="knx-button-row">
          <ha-button
            class="push-right"
            @click=${this._uploadFile}
            .disabled=${this._uploading||!this._projectFile}
            >${this.hass.localize("ui.common.submit")}</ha-button
          >
        </div>
      </div>
    </ha-card>`}},{kind:"method",key:"loadKnxInfo",value:function(){(0,c.qn)(this.hass).then((e=>{this.knxInfoData=e,this.requestUpdate()}),(e=>{p.error("getKnxInfoData",e),(0,r.o)("/knx/error",{replace:!0,data:e})}))}},{kind:"method",key:"_filePicked",value:function(e){this._projectFile=e.detail.files[0]}},{kind:"method",key:"_passwordChanged",value:function(e){this._projectPassword=e.detail.value}},{kind:"method",key:"_uploadFile",value:async function(e){const i=this._projectFile;if(void 0===i)return;let t;this._uploading=!0;try{const e=await(0,s.Q)(this.hass,i);await(0,c.dc)(this.hass,e,this._projectPassword||"")}catch(o){t=o,(0,d.K$)(this,{title:"Upload failed",text:(0,l.VR)(o)})}finally{t||(this._projectFile=void 0,this._projectPassword=void 0),this._uploading=!1,this.loadKnxInfo()}}},{kind:"method",key:"_removeProject",value:async function(e){if(await(0,d.dk)(this,{text:this.knx.localize("info_project_delete")}))try{await(0,c.gV)(this.hass)}catch(i){(0,d.K$)(this,{title:"Deletion failed",text:(0,l.VR)(i)})}finally{this.loadKnxInfo()}else p.debug("User cancelled deletion")}},{kind:"get",static:!0,key:"styles",value:function(){return a.AH`
      .columns {
        display: flex;
        justify-content: center;
      }

      @media screen and (max-width: 1232px) {
        .columns {
          flex-direction: column;
        }

        .knx-button-row {
          margin-top: 20px;
        }

        .knx-info {
          margin-right: 8px;
        }
      }

      @media screen and (min-width: 1233px) {
        .knx-button-row {
          margin-top: auto;
        }

        .knx-info {
          width: 400px;
        }
      }

      .knx-info {
        margin-left: 8px;
        margin-top: 8px;
      }

      .knx-content {
        display: flex;
        flex-direction: column;
        height: 100%;
        box-sizing: border-box;
      }

      .knx-content-row {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
      }

      .knx-content-row > div:nth-child(2) {
        margin-left: 1rem;
      }

      .knx-button-row {
        display: flex;
        flex-direction: row;
        vertical-align: bottom;
        padding-top: 16px;
      }

      .push-left {
        margin-right: auto;
      }

      .push-right {
        margin-left: auto;
      }

      .knx-warning {
        --mdc-theme-primary: var(--error-color);
      }

      .knx-project-description {
        margin-top: -8px;
        padding: 0px 16px 16px;
      }

      .knx-delete-project-button {
        position: absolute;
        bottom: 0;
        right: 0;
      }

      .knx-bug-report {
        margin-top: 20px;
      }

      .knx-bug-report > ul > li > a {
        text-decoration: none;
        color: var(--mdc-theme-primary);
      }

      .header {
        color: var(--ha-card-header-color, --primary-text-color);
        font-family: var(--ha-card-header-font-family, inherit);
        font-size: var(--ha-card-header-font-size, 24px);
        letter-spacing: -0.012em;
        line-height: 48px;
        padding: -4px 16px 16px;
        display: inline-block;
        margin-block-start: 0px;
        margin-block-end: 4px;
        font-weight: normal;
      }

      ha-file-upload,
      ha-selector-text {
        width: 100%;
        margin-top: 8px;
      }

      ha-circular-progress {
        margin-top: 32px;
      }
    `}}]}}),a.WF)}};
//# sourceMappingURL=-KYZHhH-.js.map