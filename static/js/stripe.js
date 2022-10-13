// let stripe, elements;
// const stripeSubmit = document.getElementById('stripe-submit');
//
// async function createStripeSession() {
//
//   switchPaymentMethod('stripe', '')
//
//   const form = document.getElementById('form-user-info');
//   const formData = new FormData(form);
//
//   stripeSubmit.disabled = true;
//   try {
//     const { data } = await axios.post("/checkout/stripe", formData) // يتم الإستعلام عن المفتاح السري للعميل
//     const { client_secret } = data; // ثم جلب المفتاح
//   //  console.log(client_secret);
//     const stripe = Stripe("pk_test_51LrkCWLfmxyYAt6xIV8Y94ZyPjfsQ4HlbFP571eBjUZS83RtoEwOESaXREEGtxYTZO6c7W7WrlgcNDTJicldGWzp00iSj2A6t5");// هنا يتم تعريف الكائن سترايب مع إسناد قيمة المفتاح العام الخاص بك
//     elements = stripe.elements({ appearance, clientSecret: client_secret}); // ثم تعريف العناصر مع اسناد قيمة المفتاح السري للعميل
//     const paymentElement = elements.create("payment")
//     paymentElement.mount("#payment-element");
//
//     document
//     .querySelector("#payment-form")
//     .addEventListener("submit", _stripeFormSubmit);
//
//     document.getElementById('stripe-card').style.display = 'block'
//     stripeSubmit.disabled = false;
//   } catch (e) {
//     console.log(e)
//     notyf.error(e);
//   }
//
// async function _stripeFormSubmit(e) {
//   e.preventDefault();
//   stripeSubmit.disabled = true;
//   const host = window.location.protocol + "//" + window.location.host;
//   const stripe = new Stripe("pk_test_51LrkCWLfmxyYAt6xIV8Y94ZyPjfsQ4HlbFP571eBjUZS83RtoEwOESaXREEGtxYTZO6c7W7WrlgcNDTJicldGWzp00iSj2A6t5"); // قمت بإضافة هذا السطر للتعريف عن كائن سترايب
//
//   const { error } = await stripe.confirmPayment({
//     elements,
//     confirmParams: {
//       return_url: `${host}/checkout/complete`,
//     },
//   });
//
//   if (error.type === "card_error" || error.type === "validation_error") {
//     notyf.error(error.message);
//   } else {
//     notyf.error("عذرًا، هنالك خطأ ما حصل خلال عملية الدفع.");
//   }
//   stripeSubmit.disabled = false;
// }
//
// async function _checkStripePaymentStatus() {
//   const clientSecret = new URLSearchParams(window.location.search).get(
//     "payment_intent_client_secret"
//   );
//   if (!clientSecret) {
//     return;
//   }
//   const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);
//   switch (paymentIntent.status) {
//     case "succeeded":
//       notyf.success("لقد تمت عملية الدفع بنجاح!");
//       break;
//     case "processing":
//       notyf.success("عملية الدفع قيد المعالجة");
//       break;
//     default:
//       notyf.error("عذرًا، هنالك خطأ ما حصل خلال عملية الدفع.");
//       break;
//   }
// // }
//
// async function _stripeInit() {
//     const { data } = await axios("/checkout/stripe/config");
//     stripe = Stripe(data.public_key, { locale: 'ar' });
//     _checkStripePaymentStatus();
// }
//
// // _stripeInit();


var stripe, elements;
const stripeSubmit = document.getElementById('stripe-submit');
async function _stripeInit() {
  const { data } = await axios("/checkout/stripe/config");
  stripe = Stripe(data.public_key, { locale: 'ar' });
  _checkStripePaymentStatus();
}

async function createStripeSession() {
  switchPaymentMethod('stripe', '')
  const form = document.getElementById('form-user-info');
  const formData = new FormData(form);
  stripeSubmit.disabled = true;
  try {
    const { data } = await axios.post("/checkout/stripe", formData)
    const { client_secret } = data;
    console.log(client_secret);
    const appearance = { theme: 'flat' };
    const stripe = new Stripe("pk_test_51LrkCWLfmxyYAt6xIV8Y94ZyPjfsQ4HlbFP571eBjUZS83RtoEwOESaXREEGtxYTZO6c7W7WrlgcNDTJicldGWzp00iSj2A6t5");
    elements = stripe.elements({ appearance, clientSecret: client_secret});
    const paymentElement = elements.create("payment")
    paymentElement.mount("#payment-element");

    document
    .querySelector("#payment-form")
    .addEventListener("submit", _stripeFormSubmit);

    document.getElementById('stripe-card').style.display = 'block'
    stripeSubmit.disabled = false;
  } catch (e) {
    console.log(e)
    notyf.error(e);
  }
}

async function _stripeFormSubmit(e) {
  e.preventDefault();
  stripeSubmit.disabled = true;
  const host = window.location.protocol + "//" + window.location.host;
  const stripe = new Stripe("pk_test_51LrkCWLfmxyYAt6xIV8Y94ZyPjfsQ4HlbFP571eBjUZS83RtoEwOESaXREEGtxYTZO6c7W7WrlgcNDTJicldGWzp00iSj2A6t5");

  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: {
      return_url: `${host}/checkout/complete`,
    },
  });

  if (error.type === "card_error" || error.type === "validation_error") {
    notyf.error(error.message);
  } else {
    notyf.error("عذرًا، هنالك خطأ ما حصل خلال عملية الدفع.");
  }
  stripeSubmit.disabled = false;
}

async function _checkStripePaymentStatus() {
  const clientSecret = new URLSearchParams(window.location.search).get(
    "payment_intent_client_secret"
  );
  if (!clientSecret) {
    return;
  }
  const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);
  switch (paymentIntent.status) {
    case "succeeded":
      notyf.success("لقد تمت عملية الدفع بنجاح!");
      break;
    case "processing":
      notyf.success("عملية الدفع قيد المعالجة");
      break;
    default:
      notyf.error("عذرًا، هنالك خطأ ما حصل خلال عملية الدفع.");
      break;
  }
}


//_stripeInit();