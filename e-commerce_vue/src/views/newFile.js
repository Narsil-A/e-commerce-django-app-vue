export default (await import('vue')).defineComponent({
name: 'Search',
components: {
ProductBox
},
data() {
return {
products: [],
query: ''
};
},
mounted() {
document.title = ' Search | Petstore';
}
});
