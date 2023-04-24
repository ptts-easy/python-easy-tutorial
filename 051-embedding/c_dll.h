#pragma once

#define DLL_EXPORT __declspec(dllexport)
//#define DLL_IMPORT __declspec(dllimport)

#ifdef __cplusplus
extern "C"
{
#endif

struct Passport{
    char*  name;
    char*  surname;
    int var;
};

void DLL_EXPORT SetName(char* new_name);
void DLL_EXPORT SetSurname(char* new_surname);
void DLL_EXPORT SetPassport(Passport* new_passport);
void DLL_EXPORT GetPassport(void);

#ifdef __cplusplus
}
#endif