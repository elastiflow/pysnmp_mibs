# SNMP MIB module (RUIJIE-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-PRODUCTS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ruijieGatewayProducts,) = mibBuilder.importSymbols(
    "RUIJIE-GATEWAY-SMI",
    "ruijieGatewayProducts")

(ruijieRouterProducts,) = mibBuilder.importSymbols(
    "RUIJIE-ROUTER-SMI",
    "ruijieRouterProducts")

(ruijieSmartClassProducts,) = mibBuilder.importSymbols(
    "RUIJIE-SMARTCLASS-SMI",
    "ruijieSmartClassProducts")

(ruijieModules,
 ruijieSwitchProducts) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieModules",
    "ruijieSwitchProducts")

(ruijieSoftwareProducts,) = mibBuilder.importSymbols(
    "RUIJIE-SOFTWARE-SMI",
    "ruijieSoftwareProducts")

(ruijieWirelessProducts,) = mibBuilder.importSymbols(
    "RUIJIE-WIRELESS-SMI",
    "ruijieWirelessProducts")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieProductsMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S2126G_ObjectIdentity = ObjectIdentity
s2126G = _S2126G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 1)
)
_S2126GL3_ObjectIdentity = ObjectIdentity
s2126GL3 = _S2126GL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 2)
)
_S2150G_ObjectIdentity = ObjectIdentity
s2150G = _S2150G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 3)
)
_S2150GL3_ObjectIdentity = ObjectIdentity
s2150GL3 = _S2150GL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 4)
)
_S4909_ObjectIdentity = ObjectIdentity
s4909 = _S4909_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 5)
)
_S3550_12G_ObjectIdentity = ObjectIdentity
s3550_12G = _S3550_12G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 6)
)
_S3550_24G_ObjectIdentity = ObjectIdentity
s3550_24G = _S3550_24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 8)
)
_S21_STACKING_ObjectIdentity = ObjectIdentity
s21_STACKING = _S21_STACKING_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 11)
)
_S3550_24_ObjectIdentity = ObjectIdentity
s3550_24 = _S3550_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 12)
)
_S3550_48_ObjectIdentity = ObjectIdentity
s3550_48 = _S3550_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 13)
)
_S3550_12SFP_GT_ObjectIdentity = ObjectIdentity
s3550_12SFP_GT = _S3550_12SFP_GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 15)
)
_S6806_ObjectIdentity = ObjectIdentity
s6806 = _S6806_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 16)
)
_S6810_ObjectIdentity = ObjectIdentity
s6810 = _S6810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 17)
)
_S2126S_ObjectIdentity = ObjectIdentity
s2126S = _S2126S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 18)
)
_S2126S_STACKING_ObjectIdentity = ObjectIdentity
s2126S_STACKING = _S2126S_STACKING_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 19)
)
_S1908PLUS_ObjectIdentity = ObjectIdentity
s1908PLUS = _S1908PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 20)
)
_S1916PLUS_ObjectIdentity = ObjectIdentity
s1916PLUS = _S1916PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 21)
)
_S6506_ObjectIdentity = ObjectIdentity
s6506 = _S6506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 22)
)
_S2126S_08_ObjectIdentity = ObjectIdentity
s2126S_08 = _S2126S_08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 23)
)
_S2126S_16_ObjectIdentity = ObjectIdentity
s2126S_16 = _S2126S_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 24)
)
_S6806E_ObjectIdentity = ObjectIdentity
s6806E = _S6806E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 25)
)
_S6810E_ObjectIdentity = ObjectIdentity
s6810E = _S6810E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 26)
)
_S2026G_ObjectIdentity = ObjectIdentity
s2026G = _S2026G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 27)
)
_S3750_24_ObjectIdentity = ObjectIdentity
s3750_24 = _S3750_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 28)
)
_S3750_48_ObjectIdentity = ObjectIdentity
s3750_48 = _S3750_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 29)
)
_S2126_ObjectIdentity = ObjectIdentity
s2126 = _S2126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 30)
)
_S2126_STACKING_ObjectIdentity = ObjectIdentity
s2126_STACKING = _S2126_STACKING_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 31)
)
_S2026F_ObjectIdentity = ObjectIdentity
s2026F = _S2026F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 33)
)
_S3760_12SFP_GT_ObjectIdentity = ObjectIdentity
s3760_12SFP_GT = _S3760_12SFP_GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 34)
)
_S4009_ObjectIdentity = ObjectIdentity
s4009 = _S4009_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 35)
)
_S3526_ObjectIdentity = ObjectIdentity
s3526 = _S3526_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 36)
)
_S3512G_ObjectIdentity = ObjectIdentity
s3512G = _S3512G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 37)
)
_Hcl_12GCS_L3_ObjectIdentity = ObjectIdentity
hcl_12GCS_L3 = _Hcl_12GCS_L3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 38)
)
_Hcl_24GS_L3_ObjectIdentity = ObjectIdentity
hcl_24GS_L3 = _Hcl_24GS_L3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 39)
)
_Hcl_48TMS_2S_S_ObjectIdentity = ObjectIdentity
hcl_48TMS_2S_S = _Hcl_48TMS_2S_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 40)
)
_S5750_24GT_12SFP_ObjectIdentity = ObjectIdentity
s5750_24GT_12SFP = _S5750_24GT_12SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 41)
)
_S5750P_24GT_12SFP_ObjectIdentity = ObjectIdentity
s5750P_24GT_12SFP = _S5750P_24GT_12SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 42)
)
_S8606_ObjectIdentity = ObjectIdentity
s8606 = _S8606_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 43)
)
_S8610_ObjectIdentity = ObjectIdentity
s8610 = _S8610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 44)
)
_S8606B_ObjectIdentity = ObjectIdentity
s8606B = _S8606B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 45)
)
_S9620_ObjectIdentity = ObjectIdentity
s9620 = _S9620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 46)
)
_S2924G_ObjectIdentity = ObjectIdentity
s2924G = _S2924G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 47)
)
_S3760_24_ObjectIdentity = ObjectIdentity
s3760_24 = _S3760_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 48)
)
_S3760_48_ObjectIdentity = ObjectIdentity
s3760_48 = _S3760_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 49)
)
_S3750E_24_ObjectIdentity = ObjectIdentity
s3750E_24 = _S3750E_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 50)
)
_S3750E_48_ObjectIdentity = ObjectIdentity
s3750E_48 = _S3750E_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 51)
)
_S5750S_24GT_12SFP_ObjectIdentity = ObjectIdentity
s5750S_24GT_12SFP = _S5750S_24GT_12SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 53)
)
_S2128G_ObjectIdentity = ObjectIdentity
s2128G = _S2128G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 54)
)
_S2927XG_ObjectIdentity = ObjectIdentity
s2927XG = _S2927XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 55)
)
_S3512GPLUS_ObjectIdentity = ObjectIdentity
s3512GPLUS = _S3512GPLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 56)
)
_S7604_ObjectIdentity = ObjectIdentity
s7604 = _S7604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 57)
)
_S7606_ObjectIdentity = ObjectIdentity
s7606 = _S7606_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 58)
)
_S7610_ObjectIdentity = ObjectIdentity
s7610 = _S7610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 59)
)
_S5750_24SFP_12GT_ObjectIdentity = ObjectIdentity
s5750_24SFP_12GT = _S5750_24SFP_12GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 60)
)
_S5750_48GT_4SFP_ObjectIdentity = ObjectIdentity
s5750_48GT_4SFP = _S5750_48GT_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 61)
)
_S5750S_48GT_4SFP_ObjectIdentity = ObjectIdentity
s5750S_48GT_4SFP = _S5750S_48GT_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 62)
)
_S3250_24_ObjectIdentity = ObjectIdentity
s3250_24 = _S3250_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 63)
)
_S3250_48_ObjectIdentity = ObjectIdentity
s3250_48 = _S3250_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 64)
)
_S2724G_ObjectIdentity = ObjectIdentity
s2724G = _S2724G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 65)
)
_S2951XG_ObjectIdentity = ObjectIdentity
s2951XG = _S2951XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 66)
)
_S3750_24_UB_ObjectIdentity = ObjectIdentity
s3750_24_UB = _S3750_24_UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 67)
)
_S3750_48_UB_ObjectIdentity = ObjectIdentity
s3750_48_UB = _S3750_48_UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 68)
)
_Scg5510_ObjectIdentity = ObjectIdentity
scg5510 = _Scg5510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 69)
)
_S2052G_ObjectIdentity = ObjectIdentity
s2052G = _S2052G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 70)
)
_S2328G_ObjectIdentity = ObjectIdentity
s2328G = _S2328G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 71)
)
_S8614_ObjectIdentity = ObjectIdentity
s8614 = _S8614_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 72)
)
_S5760_24GT_4SFP_ObjectIdentity = ObjectIdentity
s5760_24GT_4SFP = _S5760_24GT_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 73)
)
_S5760_48GT_4SFP_ObjectIdentity = ObjectIdentity
s5760_48GT_4SFP = _S5760_48GT_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 75)
)
_S3250P_24_ObjectIdentity = ObjectIdentity
s3250P_24 = _S3250P_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 78)
)
_S2628G_ObjectIdentity = ObjectIdentity
s2628G = _S2628G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 82)
)
_S2652G_ObjectIdentity = ObjectIdentity
s2652G = _S2652G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 83)
)
_S5750P_48GT_4SFP_ObjectIdentity = ObjectIdentity
s5750P_48GT_4SFP = _S5750P_48GT_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 85)
)
_S5750_48GT_4SFP_A_ObjectIdentity = ObjectIdentity
s5750_48GT_4SFP_A = _S5750_48GT_4SFP_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 92)
)
_S5750_48GT_4SFP_AP_ObjectIdentity = ObjectIdentity
s5750_48GT_4SFP_AP = _S5750_48GT_4SFP_AP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 93)
)
_S2352G_ObjectIdentity = ObjectIdentity
s2352G = _S2352G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 94)
)
_S3760E_24_ObjectIdentity = ObjectIdentity
s3760E_24 = _S3760E_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 98)
)
_S3760E_48_ObjectIdentity = ObjectIdentity
s3760E_48 = _S3760E_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 99)
)
_S3250E_24_ObjectIdentity = ObjectIdentity
s3250E_24 = _S3250E_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 100)
)
_S2628G_P_ObjectIdentity = ObjectIdentity
s2628G_P = _S2628G_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 101)
)
_S3250E_48_ObjectIdentity = ObjectIdentity
s3250E_48 = _S3250E_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 102)
)
_S2652G_P_ObjectIdentity = ObjectIdentity
s2652G_P = _S2652G_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 103)
)
_S3760E_24P_ObjectIdentity = ObjectIdentity
S3760E_24P = _S3760E_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 104)
)
_S3760E_48P_ObjectIdentity = ObjectIdentity
S3760E_48P = _S3760E_48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 105)
)
_S2628G_E_ObjectIdentity = ObjectIdentity
s2628G_E = _S2628G_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 106)
)
_S2652G_E_ObjectIdentity = ObjectIdentity
s2652G_E = _S2652G_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 107)
)
_S5750_24GT8SFP_E_ObjectIdentity = ObjectIdentity
S5750_24GT8SFP_E = _S5750_24GT8SFP_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 111)
)
_S5750_24GT8SFP_P_ObjectIdentity = ObjectIdentity
S5750_24GT8SFP_P = _S5750_24GT8SFP_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 112)
)
_S5750_48GT4SFP_E_ObjectIdentity = ObjectIdentity
S5750_48GT4SFP_E = _S5750_48GT4SFP_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 113)
)
_S5750_48GT4SFP_P_ObjectIdentity = ObjectIdentity
S5750_48GT4SFP_P = _S5750_48GT4SFP_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 114)
)
_S2928G_E_ObjectIdentity = ObjectIdentity
S2928G_E = _S2928G_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 117)
)
_S2952G_E_ObjectIdentity = ObjectIdentity
S2952G_E = _S2952G_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 118)
)
_S2924GT8SFP_XS_P_ObjectIdentity = ObjectIdentity
S2924GT8SFP_XS_P = _S2924GT8SFP_XS_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 120)
)
_S6200_48XS_ObjectIdentity = ObjectIdentity
S6200_48XS = _S6200_48XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 123)
)
_S2628G_I_ObjectIdentity = ObjectIdentity
S2628G_I = _S2628G_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 126)
)
_S2652G_I_ObjectIdentity = ObjectIdentity
S2652G_I = _S2652G_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 127)
)
_S6000_48GT4XS_ObjectIdentity = ObjectIdentity
S6000_48GT4XS = _S6000_48GT4XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 128)
)
_S6210_32XS8QXS_ObjectIdentity = ObjectIdentity
S6210_32XS8QXS = _S6210_32XS8QXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 129)
)
_S6210_48XS_ObjectIdentity = ObjectIdentity
S6210_48XS = _S6210_48XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 130)
)
_S15010_ObjectIdentity = ObjectIdentity
S15010 = _S15010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 131)
)
_S12006_ObjectIdentity = ObjectIdentity
S12006 = _S12006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 132)
)
_S12010_ObjectIdentity = ObjectIdentity
S12010 = _S12010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 133)
)
_S5750_28GT_L_ObjectIdentity = ObjectIdentity
S5750_28GT_L = _S5750_28GT_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 137)
)
_S5750_52GT_L_ObjectIdentity = ObjectIdentity
S5750_52GT_L = _S5750_52GT_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 138)
)
_S5750_24SFP8GT_E_ObjectIdentity = ObjectIdentity
S5750_24SFP8GT_E = _S5750_24SFP8GT_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 139)
)
_S6000_86GT10XS_ObjectIdentity = ObjectIdentity
S6000_86GT10XS = _S6000_86GT10XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 141)
)
_S2928G_S_ObjectIdentity = ObjectIdentity
S2928G_S = _S2928G_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 142)
)
_S2950G_S_ObjectIdentity = ObjectIdentity
S2950G_S = _S2950G_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 143)
)
_S5750_28GT_S_ObjectIdentity = ObjectIdentity
S5750_28GT_S = _S5750_28GT_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 144)
)
_S2628G_S_ObjectIdentity = ObjectIdentity
S2628G_S = _S2628G_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 146)
)
_S2652G_S_ObjectIdentity = ObjectIdentity
S2652G_S = _S2652G_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 147)
)
_S6220_24XS_ObjectIdentity = ObjectIdentity
S6220_24XS = _S6220_24XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 148)
)
_S6220_48XS4QXS_ObjectIdentity = ObjectIdentity
S6220_48XS4QXS = _S6220_48XS4QXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 150)
)
_S6220_48XT4QXS_ObjectIdentity = ObjectIdentity
S6220_48XT4QXS = _S6220_48XT4QXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 151)
)
_S6000_24GT8SFP_ObjectIdentity = ObjectIdentity
S6000_24GT8SFP = _S6000_24GT8SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 153)
)
_S6000_48GT4SFP_ObjectIdentity = ObjectIdentity
S6000_48GT4SFP = _S6000_48GT4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 154)
)
_S2928G_24P_ObjectIdentity = ObjectIdentity
S2928G_24P = _S2928G_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 155)
)
_S2928G_12P_ObjectIdentity = ObjectIdentity
S2928G_12P = _S2928G_12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 156)
)
_S5750_24GT8SFP_S_ObjectIdentity = ObjectIdentity
S5750_24GT8SFP_S = _S5750_24GT8SFP_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 157)
)
_S5750_48GT4SFP_S_ObjectIdentity = ObjectIdentity
S5750_48GT4SFP_S = _S5750_48GT4SFP_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 158)
)
_RG_S7805E_ObjectIdentity = ObjectIdentity
RG_S7805E = _RG_S7805E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 159)
)
_RG_S7807E_ObjectIdentity = ObjectIdentity
RG_S7807E = _RG_S7807E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 160)
)
_RG_S7810E_ObjectIdentity = ObjectIdentity
RG_S7810E = _RG_S7810E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 161)
)
_RG_S8605E_ObjectIdentity = ObjectIdentity
RG_S8605E = _RG_S8605E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 162)
)
_RG_S8607E_ObjectIdentity = ObjectIdentity
RG_S8607E = _RG_S8607E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 163)
)
_RG_S8610E_ObjectIdentity = ObjectIdentity
RG_S8610E = _RG_S8610E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 164)
)
_RG_N18010_ObjectIdentity = ObjectIdentity
RG_N18010 = _RG_N18010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 165)
)
_RG_N18014_ObjectIdentity = ObjectIdentity
RG_N18014 = _RG_N18014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 166)
)
_S2528G_24P_ObjectIdentity = ObjectIdentity
S2528G_24P = _S2528G_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 169)
)
_RG_N18007_ObjectIdentity = ObjectIdentity
RG_N18007 = _RG_N18007_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 170)
)
_S2910_24GT4XS_E_ObjectIdentity = ObjectIdentity
S2910_24GT4XS_E = _S2910_24GT4XS_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 174)
)
_S2910_48GT4XS_E_ObjectIdentity = ObjectIdentity
S2910_48GT4XS_E = _S2910_48GT4XS_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 175)
)
_S2910C_24GT2XS_P_E_ObjectIdentity = ObjectIdentity
S2910C_24GT2XS_P_E = _S2910C_24GT2XS_P_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 176)
)
_S2910C_24GT2XS_HP_E_ObjectIdentity = ObjectIdentity
S2910C_24GT2XS_HP_E = _S2910C_24GT2XS_HP_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 177)
)
_S2910C_48GT2XS_HP_E_ObjectIdentity = ObjectIdentity
S2910C_48GT2XS_HP_E = _S2910C_48GT2XS_HP_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 178)
)
_S5750_24GT4XS_L_ObjectIdentity = ObjectIdentity
S5750_24GT4XS_L = _S5750_24GT4XS_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 179)
)
_S5750_48GT4XS_L_ObjectIdentity = ObjectIdentity
S5750_48GT4XS_L = _S5750_48GT4XS_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 180)
)
_S6220_48XS6QXS_H_ObjectIdentity = ObjectIdentity
S6220_48XS6QXS_H = _S6220_48XS6QXS_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 184)
)
_S6220_48XT6QXS_H_ObjectIdentity = ObjectIdentity
S6220_48XT6QXS_H = _S6220_48XT6QXS_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 185)
)
_S2910_24GT4SFP_UP_H_ObjectIdentity = ObjectIdentity
S2910_24GT4SFP_UP_H = _S2910_24GT4SFP_UP_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 186)
)
_S5750_48GT4SFP_PV50_ObjectIdentity = ObjectIdentity
S5750_48GT4SFP_PV50 = _S5750_48GT4SFP_PV50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 188)
)
_S5750_24GT4XS_H_ObjectIdentity = ObjectIdentity
S5750_24GT4XS_H = _S5750_24GT4XS_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 190)
)
_S5750_48GT4XS_H_ObjectIdentity = ObjectIdentity
S5750_48GT4XS_H = _S5750_48GT4XS_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 191)
)
_S5750C_28GT4XS_H_ObjectIdentity = ObjectIdentity
S5750C_28GT4XS_H = _S5750C_28GT4XS_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 192)
)
_S5750C_28SFP4XS_H_ObjectIdentity = ObjectIdentity
S5750C_28SFP4XS_H = _S5750C_28SFP4XS_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 193)
)
_S5750C_48GT4XS_H_ObjectIdentity = ObjectIdentity
S5750C_48GT4XS_H = _S5750C_48GT4XS_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 194)
)
_S5750C_28GT4XS_HP_H_ObjectIdentity = ObjectIdentity
S5750C_28GT4XS_HP_H = _S5750C_28GT4XS_HP_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 195)
)
_S5750C_48GT4XS_HP_H_ObjectIdentity = ObjectIdentity
S5750C_48GT4XS_HP_H = _S5750C_48GT4XS_HP_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 196)
)
_S6000C_28GT4XS_E_ObjectIdentity = ObjectIdentity
S6000C_28GT4XS_E = _S6000C_28GT4XS_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 197)
)
_S6000C_48GT4XS_E_ObjectIdentity = ObjectIdentity
S6000C_48GT4XS_E = _S6000C_48GT4XS_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 198)
)
_RG_S7808C_ObjectIdentity = ObjectIdentity
RG_S7808C = _RG_S7808C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 199)
)
_S2320G_P_ObjectIdentity = ObjectIdentity
S2320G_P = _S2320G_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 202)
)
_NBS5552XG_ObjectIdentity = ObjectIdentity
NBS5552XG = _NBS5552XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 206)
)
_NBS2009G_P_ObjectIdentity = ObjectIdentity
NBS2009G_P = _NBS2009G_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 208)
)
_NBS5628XG_ObjectIdentity = ObjectIdentity
NBS5628XG = _NBS5628XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 210)
)
_NBS5652XG_ObjectIdentity = ObjectIdentity
NBS5652XG = _NBS5652XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 211)
)
_RG_AS224T_ObjectIdentity = ObjectIdentity
RG_AS224T = _RG_AS224T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 220)
)
_RG_AS248T_ObjectIdentity = ObjectIdentity
RG_AS248T = _RG_AS248T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 221)
)
_RG_AS224GT_ObjectIdentity = ObjectIdentity
RG_AS224GT = _RG_AS224GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 222)
)
_RG_AS224GT_P_ObjectIdentity = ObjectIdentity
RG_AS224GT_P = _RG_AS224GT_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 223)
)
_RG_AS248GT_ObjectIdentity = ObjectIdentity
RG_AS248GT = _RG_AS248GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 224)
)
_RG_AS324GT_ObjectIdentity = ObjectIdentity
RG_AS324GT = _RG_AS324GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 225)
)
_RG_AS324GF_ObjectIdentity = ObjectIdentity
RG_AS324GF = _RG_AS324GF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 226)
)
_RG_AS348GT_ObjectIdentity = ObjectIdentity
RG_AS348GT = _RG_AS348GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 227)
)
_RG_AS216T_ObjectIdentity = ObjectIdentity
RG_AS216T = _RG_AS216T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 228)
)
_RG_AS216GT_ObjectIdentity = ObjectIdentity
RG_AS216GT = _RG_AS216GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 229)
)
_NBS228F_ObjectIdentity = ObjectIdentity
NBS228F = _NBS228F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 232)
)
_NBS252F_ObjectIdentity = ObjectIdentity
NBS252F = _NBS252F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 233)
)
_RG_N18018_X_ObjectIdentity = ObjectIdentity
RG_N18018_X = _RG_N18018_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 234)
)
_RG_N18010_X_ObjectIdentity = ObjectIdentity
RG_N18010_X = _RG_N18010_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 235)
)
_S2910_10GT2SFP_P_E_ObjectIdentity = ObjectIdentity
S2910_10GT2SFP_P_E = _S2910_10GT2SFP_P_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 238)
)
_S2910_10GT2SFP_UP_H_ObjectIdentity = ObjectIdentity
S2910_10GT2SFP_UP_H = _S2910_10GT2SFP_UP_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 239)
)
_S6220_32QXS_H_ObjectIdentity = ObjectIdentity
S6220_32QXS_H = _S6220_32QXS_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 241)
)
_S2910_24GT4XS_UP_H_ObjectIdentity = ObjectIdentity
S2910_24GT4XS_UP_H = _S2910_24GT4XS_UP_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 286)
)
_S2710G_P_ObjectIdentity = ObjectIdentity
S2710G_P = _S2710G_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 294)
)
_S2900_8GT2SFP_L_ObjectIdentity = ObjectIdentity
S2900_8GT2SFP_L = _S2900_8GT2SFP_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 822)
)
_S2900_24GT4SFP2GT_P_L_ObjectIdentity = ObjectIdentity
S2900_24GT4SFP2GT_P_L = _S2900_24GT4SFP2GT_P_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 823)
)
_S2900_8GT2SFP_P_L_ObjectIdentity = ObjectIdentity
S2900_8GT2SFP_P_L = _S2900_8GT2SFP_P_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 824)
)
_S2900_24GT4SFP2GT_L_ObjectIdentity = ObjectIdentity
S2900_24GT4SFP2GT_L = _S2900_24GT4SFP2GT_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 825)
)
_S2900_18GT2SFP_L_ObjectIdentity = ObjectIdentity
S2900_18GT2SFP_L = _S2900_18GT2SFP_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 826)
)
_SF2900_8GT2SFP_S_ObjectIdentity = ObjectIdentity
SF2900_8GT2SFP_S = _SF2900_8GT2SFP_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 827)
)
_SF2900_8GT2SFP_P_S_ObjectIdentity = ObjectIdentity
SF2900_8GT2SFP_P_S = _SF2900_8GT2SFP_P_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1, 828)
)
_R2620_ObjectIdentity = ObjectIdentity
r2620 = _R2620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 1)
)
_R2624_ObjectIdentity = ObjectIdentity
r2624 = _R2624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 2)
)
_R2690_ObjectIdentity = ObjectIdentity
r2690 = _R2690_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 3)
)
_R2692_ObjectIdentity = ObjectIdentity
r2692 = _R2692_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 4)
)
_R3642_ObjectIdentity = ObjectIdentity
r3642 = _R3642_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 5)
)
_R3662_ObjectIdentity = ObjectIdentity
r3662 = _R3662_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 6)
)
_Nbr1000_ObjectIdentity = ObjectIdentity
nbr1000 = _Nbr1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 7)
)
_Nbr200_ObjectIdentity = ObjectIdentity
nbr200 = _Nbr200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 8)
)
_Secvpn100_ObjectIdentity = ObjectIdentity
secvpn100 = _Secvpn100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 9)
)
_R2632_ObjectIdentity = ObjectIdentity
r2632 = _R2632_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 10)
)
_R1762_ObjectIdentity = ObjectIdentity
r1762 = _R1762_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 11)
)
_Rcms_ObjectIdentity = ObjectIdentity
rcms = _Rcms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 12)
)
_Hcl_r1762_ObjectIdentity = ObjectIdentity
hcl_r1762 = _Hcl_r1762_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 13)
)
_Hcl_r2632_ObjectIdentity = ObjectIdentity
hcl_r2632 = _Hcl_r2632_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 14)
)
_Hcl_r2692_ObjectIdentity = ObjectIdentity
hcl_r2692 = _Hcl_r2692_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 15)
)
_Hcl_r3642_ObjectIdentity = ObjectIdentity
hcl_r3642 = _Hcl_r3642_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 16)
)
_Hcl_r3662_ObjectIdentity = ObjectIdentity
hcl_r3662 = _Hcl_r3662_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 17)
)
_R3740_ObjectIdentity = ObjectIdentity
r3740 = _R3740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 18)
)
_Nbr2000_ObjectIdentity = ObjectIdentity
nbr2000 = _Nbr2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 19)
)
_Nbr300_ObjectIdentity = ObjectIdentity
nbr300 = _Nbr300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 20)
)
_Nbr1200_ObjectIdentity = ObjectIdentity
nbr1200 = _Nbr1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 21)
)
_Nbr1500_ObjectIdentity = ObjectIdentity
nbr1500 = _Nbr1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 22)
)
_R2716_ObjectIdentity = ObjectIdentity
r2716 = _R2716_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 23)
)
_R2724_ObjectIdentity = ObjectIdentity
r2724 = _R2724_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 24)
)
_R3802_ObjectIdentity = ObjectIdentity
r3802 = _R3802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 25)
)
_R3804_ObjectIdentity = ObjectIdentity
r3804 = _R3804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 26)
)
_Rsr50_20_ObjectIdentity = ObjectIdentity
rsr50_20 = _Rsr50_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 27)
)
_Rsr50_40_ObjectIdentity = ObjectIdentity
rsr50_40 = _Rsr50_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 28)
)
_Rsr50_80_ObjectIdentity = ObjectIdentity
rsr50_80 = _Rsr50_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 29)
)
_Npe50_20_ObjectIdentity = ObjectIdentity
npe50_20 = _Npe50_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 30)
)
_Rsr10_02_ObjectIdentity = ObjectIdentity
rsr10_02 = _Rsr10_02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 31)
)
_Rsr20_04_ObjectIdentity = ObjectIdentity
rsr20_04 = _Rsr20_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 32)
)
_Vpn120_ObjectIdentity = ObjectIdentity
vpn120 = _Vpn120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 33)
)
_Rsr20_24_ObjectIdentity = ObjectIdentity
rsr20_24 = _Rsr20_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 35)
)
_Rsr20_14_ObjectIdentity = ObjectIdentity
rsr20_14 = _Rsr20_14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 41)
)
_Rsr30_44_ObjectIdentity = ObjectIdentity
rsr30_44 = _Rsr30_44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 42)
)
_R2700v2v3_ObjectIdentity = ObjectIdentity
r2700v2v3 = _R2700v2v3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 43)
)
_R2700v5_ObjectIdentity = ObjectIdentity
r2700v5 = _R2700v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 44)
)
_Npe50_40_ObjectIdentity = ObjectIdentity
npe50_40 = _Npe50_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 45)
)
_Rsr20_18_ObjectIdentity = ObjectIdentity
rsr20_18 = _Rsr20_18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 46)
)
_Rsr50E_80_ObjectIdentity = ObjectIdentity
rsr50E_80 = _Rsr50E_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 47)
)
_Npe50e_80_ObjectIdentity = ObjectIdentity
npe50e_80 = _Npe50e_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 49)
)
_Rsr7708_ObjectIdentity = ObjectIdentity
rsr7708 = _Rsr7708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 50)
)
_Dnmx_48esw_ObjectIdentity = ObjectIdentity
dnmx_48esw = _Dnmx_48esw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 51)
)
_Rsr7704_ObjectIdentity = ObjectIdentity
rsr7704 = _Rsr7704_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 52)
)
_Rsr7716_ObjectIdentity = ObjectIdentity
rsr7716 = _Rsr7716_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 53)
)
_Rsr20_14e_ObjectIdentity = ObjectIdentity
rsr20_14e = _Rsr20_14e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 54)
)
_Rsr20_14f_ObjectIdentity = ObjectIdentity
rsr20_14f = _Rsr20_14f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 55)
)
_Rsr10_01g_w_ObjectIdentity = ObjectIdentity
rsr10_01g_w = _Rsr10_01g_w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 56)
)
_Rsr10_01g_c_ObjectIdentity = ObjectIdentity
rsr10_01g_c = _Rsr10_01g_c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 57)
)
_Rsr10_01g_td_ObjectIdentity = ObjectIdentity
rsr10_01g_td = _Rsr10_01g_td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 58)
)
_Rsr50e_40_ObjectIdentity = ObjectIdentity
rsr50e_40 = _Rsr50e_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1, 66)
)
_WS5708_V10_ObjectIdentity = ObjectIdentity
WS5708_V10 = _WS5708_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 1)
)
_AP220_SE_V10_ObjectIdentity = ObjectIdentity
AP220_SE_V10 = _AP220_SE_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 2)
)
_WS5302_V10_ObjectIdentity = ObjectIdentity
WS5302_V10 = _WS5302_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 3)
)
_AP220_E_V10_ObjectIdentity = ObjectIdentity
AP220_E_V10 = _AP220_E_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 4)
)
_AP620_H_V10_ObjectIdentity = ObjectIdentity
AP620_H_V10 = _AP620_H_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 5)
)
_AP220_SH_V10_ObjectIdentity = ObjectIdentity
AP220_SH_V10 = _AP220_SH_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 8)
)
_M8600_WS_V10_ObjectIdentity = ObjectIdentity
M8600_WS_V10 = _M8600_WS_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 14)
)
_AP620_H_S_V10_ObjectIdentity = ObjectIdentity
AP620_H_S_V10 = _AP620_H_S_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 17)
)
_AP220_SH_V20_ObjectIdentity = ObjectIdentity
AP220_SH_V20 = _AP220_SH_V20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 18)
)
_AP220_E_V11_ObjectIdentity = ObjectIdentity
AP220_E_V11 = _AP220_E_V11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 19)
)
_AP220_SE_V11_ObjectIdentity = ObjectIdentity
AP220_SE_V11 = _AP220_SE_V11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 20)
)
_AP220_SH_V11_ObjectIdentity = ObjectIdentity
AP220_SH_V11 = _AP220_SH_V11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 23)
)
_AP220_E_V20_ObjectIdentity = ObjectIdentity
AP220_E_V20 = _AP220_E_V20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 24)
)
_AP220_SE_V20_ObjectIdentity = ObjectIdentity
AP220_SE_V20 = _AP220_SE_V20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 25)
)
_AP220_E_V199_ObjectIdentity = ObjectIdentity
AP220_E_V199 = _AP220_E_V199_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 26)
)
_AP220_I_V10_ObjectIdentity = ObjectIdentity
AP220_I_V10 = _AP220_I_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 27)
)
_AP220_SI_V10_ObjectIdentity = ObjectIdentity
AP220_SI_V10 = _AP220_SI_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 28)
)
_AP220_E_M_V15_ObjectIdentity = ObjectIdentity
AP220_E_M_V15 = _AP220_E_M_V15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 29)
)
_AP220_SH_V30_ObjectIdentity = ObjectIdentity
AP220_SH_V30 = _AP220_SH_V30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 30)
)
_AP620_H_V20_ObjectIdentity = ObjectIdentity
AP620_H_V20 = _AP620_H_V20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 31)
)
_AP220_E_V30_ObjectIdentity = ObjectIdentity
AP220_E_V30 = _AP220_E_V30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 34)
)
_AP220_E_M_V20_ObjectIdentity = ObjectIdentity
AP220_E_M_V20 = _AP220_E_M_V20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1, 35)
)
_EG1000S_ObjectIdentity = ObjectIdentity
EG1000S = _EG1000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 1)
)
_EG1000C_ObjectIdentity = ObjectIdentity
EG1000C = _EG1000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 2)
)
_EG1000M_ObjectIdentity = ObjectIdentity
EG1000M = _EG1000M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 3)
)
_EG1000E_ObjectIdentity = ObjectIdentity
EG1000E = _EG1000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 5)
)
_NPE40_ObjectIdentity = ObjectIdentity
NPE40 = _NPE40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 6)
)
_NPE50E_ObjectIdentity = ObjectIdentity
NPE50E = _NPE50E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 7)
)
_NPE60_ObjectIdentity = ObjectIdentity
NPE60 = _NPE60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 8)
)
_NPE80_ObjectIdentity = ObjectIdentity
NPE80 = _NPE80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 9)
)
_NBR2000G_ObjectIdentity = ObjectIdentity
NBR2000G = _NBR2000G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 10)
)
_NBR2500G_ObjectIdentity = ObjectIdentity
NBR2500G = _NBR2500G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 11)
)
_NPE60E_ObjectIdentity = ObjectIdentity
NPE60E = _NPE60E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 13)
)
_NBR1300G_ObjectIdentity = ObjectIdentity
NBR1300G = _NBR1300G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 18)
)
_NBR1500G_ObjectIdentity = ObjectIdentity
NBR1500G = _NBR1500G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 19)
)
_EG1000L_ObjectIdentity = ObjectIdentity
EG1000L = _EG1000L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 20)
)
_EG2000K_ObjectIdentity = ObjectIdentity
EG2000K = _EG2000K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 21)
)
_NBR2000D_ObjectIdentity = ObjectIdentity
NBR2000D = _NBR2000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 22)
)
_NBR1000G_ObjectIdentity = ObjectIdentity
NBR1000G = _NBR1000G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 23)
)
_EG2000D_ObjectIdentity = ObjectIdentity
EG2000D = _EG2000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 24)
)
_EG2000T_ObjectIdentity = ObjectIdentity
EG2000T = _EG2000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 25)
)
_EG2000G_ObjectIdentity = ObjectIdentity
EG2000G = _EG2000G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 26)
)
_EG2000X_ObjectIdentity = ObjectIdentity
EG2000X = _EG2000X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 27)
)
_EG2000XE_ObjectIdentity = ObjectIdentity
EG2000XE = _EG2000XE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 28)
)
_EG2000CE_ObjectIdentity = ObjectIdentity
EG2000CE = _EG2000CE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 29)
)
_EG2000SE_ObjectIdentity = ObjectIdentity
EG2000SE = _EG2000SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 30)
)
_EG2000GE_ObjectIdentity = ObjectIdentity
EG2000GE = _EG2000GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 31)
)
_NBR2020G_ObjectIdentity = ObjectIdentity
NBR2020G = _NBR2020G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 33)
)
_EG2000P_ObjectIdentity = ObjectIdentity
EG2000P = _EG2000P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 35)
)
_EG2000UE_ObjectIdentity = ObjectIdentity
EG2000UE = _EG2000UE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 36)
)
_DDI3000_ObjectIdentity = ObjectIdentity
DDI3000 = _DDI3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 67)
)
_DDI2000_ObjectIdentity = ObjectIdentity
DDI2000 = _DDI2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 5, 1, 1, 74)
)
_RG_ESS1000_ObjectIdentity = ObjectIdentity
RG_ESS1000 = _RG_ESS1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 7, 1, 1, 1)
)
_RG_eLog2_ObjectIdentity = ObjectIdentity
RG_eLog2 = _RG_eLog2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 7, 1, 1, 2)
)
_RG_SCC600_ObjectIdentity = ObjectIdentity
RG_SCC600 = _RG_SCC600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 8, 1, 1, 1)
)
_RG_ITC1000_ObjectIdentity = ObjectIdentity
RG_ITC1000 = _RG_ITC1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 8, 1, 1, 100)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-PRODUCTS-MIB",
    **{"s2126G": s2126G,
       "s2126GL3": s2126GL3,
       "s2150G": s2150G,
       "s2150GL3": s2150GL3,
       "s4909": s4909,
       "s3550-12G": s3550_12G,
       "s3550-24G": s3550_24G,
       "s21-STACKING": s21_STACKING,
       "s3550-24": s3550_24,
       "s3550-48": s3550_48,
       "s3550-12SFP-GT": s3550_12SFP_GT,
       "s6806": s6806,
       "s6810": s6810,
       "s2126S": s2126S,
       "s2126S-STACKING": s2126S_STACKING,
       "s1908PLUS": s1908PLUS,
       "s1916PLUS": s1916PLUS,
       "s6506": s6506,
       "s2126S-08": s2126S_08,
       "s2126S-16": s2126S_16,
       "s6806E": s6806E,
       "s6810E": s6810E,
       "s2026G": s2026G,
       "s3750-24": s3750_24,
       "s3750-48": s3750_48,
       "s2126": s2126,
       "s2126-STACKING": s2126_STACKING,
       "s2026F": s2026F,
       "s3760-12SFP-GT": s3760_12SFP_GT,
       "s4009": s4009,
       "s3526": s3526,
       "s3512G": s3512G,
       "hcl-12GCS-L3": hcl_12GCS_L3,
       "hcl-24GS-L3": hcl_24GS_L3,
       "hcl-48TMS-2S-S": hcl_48TMS_2S_S,
       "s5750-24GT-12SFP": s5750_24GT_12SFP,
       "s5750P-24GT-12SFP": s5750P_24GT_12SFP,
       "s8606": s8606,
       "s8610": s8610,
       "s8606B": s8606B,
       "s9620": s9620,
       "s2924G": s2924G,
       "s3760-24": s3760_24,
       "s3760-48": s3760_48,
       "s3750E-24": s3750E_24,
       "s3750E-48": s3750E_48,
       "s5750S-24GT-12SFP": s5750S_24GT_12SFP,
       "s2128G": s2128G,
       "s2927XG": s2927XG,
       "s3512GPLUS": s3512GPLUS,
       "s7604": s7604,
       "s7606": s7606,
       "s7610": s7610,
       "s5750-24SFP-12GT": s5750_24SFP_12GT,
       "s5750-48GT-4SFP": s5750_48GT_4SFP,
       "s5750S-48GT-4SFP": s5750S_48GT_4SFP,
       "s3250-24": s3250_24,
       "s3250-48": s3250_48,
       "s2724G": s2724G,
       "s2951XG": s2951XG,
       "s3750-24-UB": s3750_24_UB,
       "s3750-48-UB": s3750_48_UB,
       "scg5510": scg5510,
       "s2052G": s2052G,
       "s2328G": s2328G,
       "s8614": s8614,
       "s5760-24GT-4SFP": s5760_24GT_4SFP,
       "s5760-48GT-4SFP": s5760_48GT_4SFP,
       "s3250P-24": s3250P_24,
       "s2628G": s2628G,
       "s2652G": s2652G,
       "s5750P-48GT-4SFP": s5750P_48GT_4SFP,
       "s5750-48GT-4SFP-A": s5750_48GT_4SFP_A,
       "s5750-48GT-4SFP-AP": s5750_48GT_4SFP_AP,
       "s2352G": s2352G,
       "s3760E-24": s3760E_24,
       "s3760E-48": s3760E_48,
       "s3250E-24": s3250E_24,
       "s2628G-P": s2628G_P,
       "s3250E-48": s3250E_48,
       "s2652G-P": s2652G_P,
       "S3760E-24P": S3760E_24P,
       "S3760E-48P": S3760E_48P,
       "s2628G-E": s2628G_E,
       "s2652G-E": s2652G_E,
       "S5750-24GT8SFP-E": S5750_24GT8SFP_E,
       "S5750-24GT8SFP-P": S5750_24GT8SFP_P,
       "S5750-48GT4SFP-E": S5750_48GT4SFP_E,
       "S5750-48GT4SFP-P": S5750_48GT4SFP_P,
       "S2928G-E": S2928G_E,
       "S2952G-E": S2952G_E,
       "S2924GT8SFP-XS-P": S2924GT8SFP_XS_P,
       "S6200-48XS": S6200_48XS,
       "S2628G-I": S2628G_I,
       "S2652G-I": S2652G_I,
       "S6000-48GT4XS": S6000_48GT4XS,
       "S6210-32XS8QXS": S6210_32XS8QXS,
       "S6210-48XS": S6210_48XS,
       "S15010": S15010,
       "S12006": S12006,
       "S12010": S12010,
       "S5750-28GT-L": S5750_28GT_L,
       "S5750-52GT-L": S5750_52GT_L,
       "S5750-24SFP8GT-E": S5750_24SFP8GT_E,
       "S6000-86GT10XS": S6000_86GT10XS,
       "S2928G-S": S2928G_S,
       "S2950G-S": S2950G_S,
       "S5750-28GT-S": S5750_28GT_S,
       "S2628G-S": S2628G_S,
       "S2652G-S": S2652G_S,
       "S6220-24XS": S6220_24XS,
       "S6220-48XS4QXS": S6220_48XS4QXS,
       "S6220-48XT4QXS": S6220_48XT4QXS,
       "S6000-24GT8SFP": S6000_24GT8SFP,
       "S6000-48GT4SFP": S6000_48GT4SFP,
       "S2928G-24P": S2928G_24P,
       "S2928G-12P": S2928G_12P,
       "S5750-24GT8SFP-S": S5750_24GT8SFP_S,
       "S5750-48GT4SFP-S": S5750_48GT4SFP_S,
       "RG-S7805E": RG_S7805E,
       "RG-S7807E": RG_S7807E,
       "RG-S7810E": RG_S7810E,
       "RG-S8605E": RG_S8605E,
       "RG-S8607E": RG_S8607E,
       "RG-S8610E": RG_S8610E,
       "RG-N18010": RG_N18010,
       "RG-N18014": RG_N18014,
       "S2528G-24P": S2528G_24P,
       "RG-N18007": RG_N18007,
       "S2910-24GT4XS-E": S2910_24GT4XS_E,
       "S2910-48GT4XS-E": S2910_48GT4XS_E,
       "S2910C-24GT2XS-P-E": S2910C_24GT2XS_P_E,
       "S2910C-24GT2XS-HP-E": S2910C_24GT2XS_HP_E,
       "S2910C-48GT2XS-HP-E": S2910C_48GT2XS_HP_E,
       "S5750-24GT4XS-L": S5750_24GT4XS_L,
       "S5750-48GT4XS-L": S5750_48GT4XS_L,
       "S6220-48XS6QXS-H": S6220_48XS6QXS_H,
       "S6220-48XT6QXS-H": S6220_48XT6QXS_H,
       "S2910-24GT4SFP-UP-H": S2910_24GT4SFP_UP_H,
       "S5750-48GT4SFP-PV50": S5750_48GT4SFP_PV50,
       "S5750-24GT4XS-H": S5750_24GT4XS_H,
       "S5750-48GT4XS-H": S5750_48GT4XS_H,
       "S5750C-28GT4XS-H": S5750C_28GT4XS_H,
       "S5750C-28SFP4XS-H": S5750C_28SFP4XS_H,
       "S5750C-48GT4XS-H": S5750C_48GT4XS_H,
       "S5750C-28GT4XS-HP-H": S5750C_28GT4XS_HP_H,
       "S5750C-48GT4XS-HP-H": S5750C_48GT4XS_HP_H,
       "S6000C-28GT4XS-E": S6000C_28GT4XS_E,
       "S6000C-48GT4XS-E": S6000C_48GT4XS_E,
       "RG-S7808C": RG_S7808C,
       "S2320G-P": S2320G_P,
       "NBS5552XG": NBS5552XG,
       "NBS2009G-P": NBS2009G_P,
       "NBS5628XG": NBS5628XG,
       "NBS5652XG": NBS5652XG,
       "RG-AS224T": RG_AS224T,
       "RG-AS248T": RG_AS248T,
       "RG-AS224GT": RG_AS224GT,
       "RG-AS224GT-P": RG_AS224GT_P,
       "RG-AS248GT": RG_AS248GT,
       "RG-AS324GT": RG_AS324GT,
       "RG-AS324GF": RG_AS324GF,
       "RG-AS348GT": RG_AS348GT,
       "RG-AS216T": RG_AS216T,
       "RG-AS216GT": RG_AS216GT,
       "NBS228F": NBS228F,
       "NBS252F": NBS252F,
       "RG-N18018-X": RG_N18018_X,
       "RG-N18010-X": RG_N18010_X,
       "S2910-10GT2SFP-P-E": S2910_10GT2SFP_P_E,
       "S2910-10GT2SFP-UP-H": S2910_10GT2SFP_UP_H,
       "S6220-32QXS-H": S6220_32QXS_H,
       "S2910-24GT4XS-UP-H": S2910_24GT4XS_UP_H,
       "S2710G-P": S2710G_P,
       "S2900-8GT2SFP-L": S2900_8GT2SFP_L,
       "S2900-24GT4SFP2GT-P-L": S2900_24GT4SFP2GT_P_L,
       "S2900-8GT2SFP-P-L": S2900_8GT2SFP_P_L,
       "S2900-24GT4SFP2GT-L": S2900_24GT4SFP2GT_L,
       "S2900-18GT2SFP-L": S2900_18GT2SFP_L,
       "SF2900-8GT2SFP-S": SF2900_8GT2SFP_S,
       "SF2900-8GT2SFP-P-S": SF2900_8GT2SFP_P_S,
       "ruijieProductsMIB": ruijieProductsMIB,
       "r2620": r2620,
       "r2624": r2624,
       "r2690": r2690,
       "r2692": r2692,
       "r3642": r3642,
       "r3662": r3662,
       "nbr1000": nbr1000,
       "nbr200": nbr200,
       "secvpn100": secvpn100,
       "r2632": r2632,
       "r1762": r1762,
       "rcms": rcms,
       "hcl-r1762": hcl_r1762,
       "hcl-r2632": hcl_r2632,
       "hcl-r2692": hcl_r2692,
       "hcl-r3642": hcl_r3642,
       "hcl-r3662": hcl_r3662,
       "r3740": r3740,
       "nbr2000": nbr2000,
       "nbr300": nbr300,
       "nbr1200": nbr1200,
       "nbr1500": nbr1500,
       "r2716": r2716,
       "r2724": r2724,
       "r3802": r3802,
       "r3804": r3804,
       "rsr50-20": rsr50_20,
       "rsr50-40": rsr50_40,
       "rsr50-80": rsr50_80,
       "npe50-20": npe50_20,
       "rsr10-02": rsr10_02,
       "rsr20-04": rsr20_04,
       "vpn120": vpn120,
       "rsr20-24": rsr20_24,
       "rsr20-14": rsr20_14,
       "rsr30-44": rsr30_44,
       "r2700v2v3": r2700v2v3,
       "r2700v5": r2700v5,
       "npe50-40": npe50_40,
       "rsr20-18": rsr20_18,
       "rsr50E-80": rsr50E_80,
       "npe50e-80": npe50e_80,
       "rsr7708": rsr7708,
       "dnmx-48esw": dnmx_48esw,
       "rsr7704": rsr7704,
       "rsr7716": rsr7716,
       "rsr20-14e": rsr20_14e,
       "rsr20-14f": rsr20_14f,
       "rsr10-01g-w": rsr10_01g_w,
       "rsr10-01g-c": rsr10_01g_c,
       "rsr10-01g-td": rsr10_01g_td,
       "rsr50e-40": rsr50e_40,
       "WS5708-V10": WS5708_V10,
       "AP220-SE-V10": AP220_SE_V10,
       "WS5302-V10": WS5302_V10,
       "AP220-E-V10": AP220_E_V10,
       "AP620-H-V10": AP620_H_V10,
       "AP220-SH-V10": AP220_SH_V10,
       "M8600-WS-V10": M8600_WS_V10,
       "AP620-H-S-V10": AP620_H_S_V10,
       "AP220-SH-V20": AP220_SH_V20,
       "AP220-E-V11": AP220_E_V11,
       "AP220-SE-V11": AP220_SE_V11,
       "AP220-SH-V11": AP220_SH_V11,
       "AP220-E-V20": AP220_E_V20,
       "AP220-SE-V20": AP220_SE_V20,
       "AP220-E-V199": AP220_E_V199,
       "AP220-I-V10": AP220_I_V10,
       "AP220-SI-V10": AP220_SI_V10,
       "AP220-E-M-V15": AP220_E_M_V15,
       "AP220-SH-V30": AP220_SH_V30,
       "AP620-H-V20": AP620_H_V20,
       "AP220-E-V30": AP220_E_V30,
       "AP220-E-M-V20": AP220_E_M_V20,
       "EG1000S": EG1000S,
       "EG1000C": EG1000C,
       "EG1000M": EG1000M,
       "EG1000E": EG1000E,
       "NPE40": NPE40,
       "NPE50E": NPE50E,
       "NPE60": NPE60,
       "NPE80": NPE80,
       "NBR2000G": NBR2000G,
       "NBR2500G": NBR2500G,
       "NPE60E": NPE60E,
       "NBR1300G": NBR1300G,
       "NBR1500G": NBR1500G,
       "EG1000L": EG1000L,
       "EG2000K": EG2000K,
       "NBR2000D": NBR2000D,
       "NBR1000G": NBR1000G,
       "EG2000D": EG2000D,
       "EG2000T": EG2000T,
       "EG2000G": EG2000G,
       "EG2000X": EG2000X,
       "EG2000XE": EG2000XE,
       "EG2000CE": EG2000CE,
       "EG2000SE": EG2000SE,
       "EG2000GE": EG2000GE,
       "NBR2020G": NBR2020G,
       "EG2000P": EG2000P,
       "EG2000UE": EG2000UE,
       "DDI3000": DDI3000,
       "DDI2000": DDI2000,
       "RG-ESS1000": RG_ESS1000,
       "RG-eLog2": RG_eLog2,
       "RG-SCC600": RG_SCC600,
       "RG-ITC1000": RG_ITC1000}
)
