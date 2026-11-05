# Appendix D: Vendor-prefixed CSS properties

Web CSS compatibility and email CSS compatibility are different problem spaces. Email clients may remove `<style>` blocks, rewrite markup, limit selectors, ignore modern layout systems, or render HTML through engines with very different capabilities. Before shipping a campaign, template, or transactional message, check the exact HTML and CSS feature in [Can I Email](https://www.caniemail.com/).

### Can I Email: live email-client compatibility

Use [Can I Email](https://www.caniemail.com/) to check HTML and CSS support across email clients. Scan the QR code in the print edition or use the direct link below to open the current feature tables.

![QR code linking to Can I Email](/qr/caniemail.png)

Direct link: [https://www.caniemail.com/](https://www.caniemail.com/)

### What Can I Email provides

Can I Email is a feature-support reference for HTML and CSS in email clients. Its tables cover client-specific behavior across desktop, mobile, and webmail environments, including Apple Mail, Gmail, Outlook, Yahoo Mail, Samsung Email, Thunderbird, Proton Mail, and others. Use it alongside your own inbox tests and delivery platform documentation; it is a compatibility reference, not a guarantee that a particular template will render identically.

- Can I Email home: https://www.caniemail.com/
- Estimated support methodology: https://www.caniemail.com/support/
- Feature directory: https://www.caniemail.com/features/

### Email-safe baseline

Start with a resilient baseline: table-based structure where necessary, inline styles for critical declarations, explicit dimensions for important assets, descriptive alternative text, a readable fallback font stack, and a plain-text alternative. Add modern enhancements only when the message remains useful without them.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="padding: 24px; font-family: Arial, sans-serif; color: #172033;">
      <h1 style="margin: 0 0 12px; font-size: 28px; line-height: 1.2;">
        A resilient email heading
      </h1>
      <p style="margin: 0; font-size: 16px; line-height: 1.5;">
        The message remains useful when advanced CSS is unavailable.
      </p>
    </td>
  </tr>
</table>
```

### A practical compatibility workflow

1. Identify the feature: for example, `display: grid`, `position: sticky`, `background-image`, `border-radius`, or a media query.
2. Search for the feature on Can I Email and inspect the client-specific notes, not only the headline percentage.
3. Define the fallback first. A single-column layout is often a better email fallback than attempting to simulate a full web layout.
4. Add the enhancement behind a safe condition or in a way that degrades harmlessly.
5. Test representative clients, including the clients that matter to your audience, and inspect both visual output and accessible reading order.

```css
/* Baseline: readable in a simple email renderer. */
.email-columns {
  display: block;
}

/* Enhancement: clients that support the feature can use two columns. */
@media screen and (min-width: 600px) {
  .email-columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }
}
```

### How this appendix fits the book

Use Can I Use for browser compatibility and Can I Email for email-client compatibility. Do not transfer a browser support result directly into an email template decision. When a feature is unavailable, prefer a useful baseline, a progressive enhancement, and a documented test result over a fragile workaround.
