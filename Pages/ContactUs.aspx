<%@ Page Title="" Language="VB" MasterPageFile="~/Master_pages/Main.master" AutoEventWireup="false" CodeFile="ContactUs.aspx.vb" Inherits="Pages_ContactUs" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
    <asp:UpdatePanel runat="server">
        <ContentTemplate runat="server">
            <asp:ScriptManager runat="server"></asp:ScriptManager>
    <section>
        <div class="contact-container">
      <div class="left-col d-none d-md-block"></div>
      <div class="right-col">
        <h1>Contact us</h1>

        <section id="contact-form formPage" method="post">
          <label for="name">Full name</label>
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Your Full Name"
            required
          />
          <label for="email">Email Address</label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Your Email Address"
            required
          />
          <label for="message">Message</label>
          <textarea
            rows="6"
            placeholder="Your Message"
            id="message"
            name="message"
            required
          ></textarea>
          <!--<a href="javascript:void(0)">--><button
            type="submit"
            id="submit"
            name="submit"
          >
            Send</button
          ><!--</a>-->
        </section>
        <div id="error"></div>
        <div id="success-msg"></div>
      </div>
    </div>
    </section>
   
            </ContentTemplate>
        </asp:UpdatePanel>
</asp:Content>

