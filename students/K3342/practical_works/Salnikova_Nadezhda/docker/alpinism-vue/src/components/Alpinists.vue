<template>
    <div>
        <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="goHome">Home</mu-button>
        </mu-container>

        <mu-container class="table-wrapper">
            <mu-row gutter>
                <mu-col>
                    <mu-paper :z-depth="1">
                        <mu-data-table stripe :columns="columns" :data="list.data">
                            <template slot-scope="dt">
                                <td class="is-center">{{ dt.row.id }}</td>
                                <td class="is-center">{{ dt.row.name }}</td>
                                <td class="is-center">{{ dt.row.birth_date }}</td>
                                <td class="is-center">{{ dt.row.club_name.id }}</td>
                                <td class="is-center">{{ dt.row.club_name.club_name}}</td>
                                <td class="is-center">{{ dt.row.telephone }}</td>
                                <td class="is-center">{{ dt.row.email }}</td>
                                <td class="is-center">{{ dt.row.address }}</td>
                            </template>
                        </mu-data-table>
                    </mu-paper>
                </mu-col>
            </mu-row>
        </mu-container>
        <br/>
        <br/>

        <h3>Add new alpinist</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="name" placeholder="Alpinist Name" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="birth_date" placeholder="Birth date (yyyy-mm-dd)" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="telephone" placeholder="Telephone number" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="email" placeholder="E-mail" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <mu-text-field v-model="address" placeholder="Address (city, street, house, flat)" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
                <h4>Select club of the alpinist</h4>
                <mu-select v-model="club">
                <mu-option v-for="club, index in club_list" :key="club.club_name" :label="club.club_name"
                       :value="club.id"></mu-option>
                </mu-select>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="addAlpinist">Add</mu-button>
        </mu-container>

        <h3>Delete a record</h3>
        <mu-container>
            <mu-paper :z-depth="1">
                <mu-text-field v-model="pk" placeholder="Alpinist ID" solo full-width
                               class="demo-divider-form"></mu-text-field>
                <mu-divider></mu-divider>
            </mu-paper>
        </mu-container>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#2c3e50" textColor="white" @click="deleteAlpinist">Delete</mu-button>
        </mu-container>

    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Alpinists",
        data() {
            return {
                pk: '',
                id: '',
                name: '',
                birth_date: '',
                club_name_id: '',
                club_name: '',
                telephone: '',
                email: '',
                address: '',
                columns: [
                    { title: "Alpinist ID", name: 'id', width: 70, align: 'center' },
                    { title: "Name", name: 'name', width: 170, align: 'center' },
                    { title: "Birth date", name: 'birth_date', width: 150, align: 'center' },
                    { title: "Club ID", name: 'club_name_id', width: 70, align: 'center' },
                    { title: "Club Name", name: 'club_name', width: 120, align: 'center' },
                    { title: "Telephone", name: 'telephone', width: 140, align: 'center' },
                    { title: "Email", name: 'email', width: 170, align: 'center' },
                    { title: "Address", name: 'address', width: 234, align: 'center' }
                ],
                list: {},
                club_list: {},
                club: ''
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            })
            this.loadAlpinists()
            this.loadClubs()
        },
        methods: {
            goHome() {
                this.$router.push({name: "main_page"})
            },
            loadAlpinists() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/alpinists/',
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            loadClubs() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/clubs/',
                    type: 'GET',
                    success: (response) => {
                        this.club_list = response.data.data
                    }
                })
            },
            addAlpinist() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/alpinists/',
                    type: 'POST',
                    data: {
                        id: this.id,
                        name: this.name,
                        birth_date: this.birth_date,
                        club_name: this.club,
                        telephone: this.telephone,
                        email: this.email,
                        address: this.address,
                    },
                    success: (response) => {
                        alert('Alpinist has been added'),
                        this.loadAlpinists()
                    },
                    error: (response) => {
                        alert('Alpinist was not added. Input is not correct')
                    }
                })
            },
            deleteAlpinist() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/alp/alpinists/',
                    type: 'DELETE',
                    data: {
                        pk: this.pk,
                    },
                    success: (response) => {
                        this.loadAlpinists()
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert('No alpinist was found')
                        }
                    }
                })
            },
        }
    }

</script>

<style scoped>

</style>
