# SNMP MIB module (ZhoneProductRegistrations) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/ZhoneProductRegistrations.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:10:21 2025
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

(zhoneModules,
 zhoneRegCpe,
 zhoneRegMalc,
 zhoneRegMux,
 zhoneRegPls,
 zhoneRegSechtor,
 zhoneRegistrations) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneRegCpe",
    "zhoneRegMalc",
    "zhoneRegMux",
    "zhoneRegPls",
    "zhoneRegSechtor",
    "zhoneRegistrations")


# MODULE-IDENTITY

zhoneRegistrationsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 1)
)
if mibBuilder.loadTexts:
    zhoneRegistrationsModule.setRevisions(
        ("2003-02-11 14:58",
         "2002-10-23 10:18",
         "2002-10-10 09:43",
         "2002-10-10 09:42",
         "2001-06-26 17:04",
         "2001-06-07 11:59",
         "2001-05-15 11:53",
         "2001-02-01 13:10",
         "2000-09-28 16:48",
         "2000-09-12 10:55")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ban_2000_ObjectIdentity = ObjectIdentity
ban_2000 = _Ban_2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ban_2000.setStatus("current")
_Zedge64_ObjectIdentity = ObjectIdentity
zedge64 = _Zedge64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zedge64.setStatus("current")
_Zedge64_SHDSL_FXS_ObjectIdentity = ObjectIdentity
zedge64_SHDSL_FXS = _Zedge64_SHDSL_FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    zedge64_SHDSL_FXS.setStatus("current")
_Zedge64_SHDSL_BRI_ObjectIdentity = ObjectIdentity
zedge64_SHDSL_BRI = _Zedge64_SHDSL_BRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    zedge64_SHDSL_BRI.setStatus("current")
_Zedge64_T1_FXS_ObjectIdentity = ObjectIdentity
zedge64_T1_FXS = _Zedge64_T1_FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    zedge64_T1_FXS.setStatus("current")
_Zedge64_E1_FXS_ObjectIdentity = ObjectIdentity
zedge64_E1_FXS = _Zedge64_E1_FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    zedge64_E1_FXS.setStatus("current")
_Z_plex10B_ObjectIdentity = ObjectIdentity
z_plex10B = _Z_plex10B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 3, 1)
)
if mibBuilder.loadTexts:
    z_plex10B.setStatus("current")
_Z_plex10B_FXS_FXO_ObjectIdentity = ObjectIdentity
z_plex10B_FXS_FXO = _Z_plex10B_FXS_FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    z_plex10B_FXS_FXO.setStatus("current")
_Z_plex10B_FXS_ObjectIdentity = ObjectIdentity
z_plex10B_FXS = _Z_plex10B_FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    z_plex10B_FXS.setStatus("current")
_Sechtor_100_ObjectIdentity = ObjectIdentity
sechtor_100 = _Sechtor_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sechtor_100.setStatus("current")
_S100_ATM_SM_16T1_ObjectIdentity = ObjectIdentity
s100_ATM_SM_16T1 = _S100_ATM_SM_16T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    s100_ATM_SM_16T1.setStatus("current")
_S100_ATM_SM_16E1_ObjectIdentity = ObjectIdentity
s100_ATM_SM_16E1 = _S100_ATM_SM_16E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    s100_ATM_SM_16E1.setStatus("current")
_Sechtor_300_ObjectIdentity = ObjectIdentity
sechtor_300 = _Sechtor_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sechtor_300.setStatus("current")
_ZhoneRegWtn_ObjectIdentity = ObjectIdentity
zhoneRegWtn = _ZhoneRegWtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5)
)
if mibBuilder.loadTexts:
    zhoneRegWtn.setStatus("current")
_Node5700Mhz_ObjectIdentity = ObjectIdentity
node5700Mhz = _Node5700Mhz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 1)
)
if mibBuilder.loadTexts:
    node5700Mhz.setStatus("current")
_SkyZhone45_ObjectIdentity = ObjectIdentity
skyZhone45 = _SkyZhone45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    skyZhone45.setStatus("current")
_OduTypeA_ObjectIdentity = ObjectIdentity
oduTypeA = _OduTypeA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    oduTypeA.setStatus("current")
_OduTypeB_ObjectIdentity = ObjectIdentity
oduTypeB = _OduTypeB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    oduTypeB.setStatus("current")
_Node23000Mhz_ObjectIdentity = ObjectIdentity
node23000Mhz = _Node23000Mhz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2)
)
if mibBuilder.loadTexts:
    node23000Mhz.setStatus("current")
_SkyZhone8e1_ObjectIdentity = ObjectIdentity
skyZhone8e1 = _SkyZhone8e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    skyZhone8e1.setStatus("current")
_OduTypeE1A_ObjectIdentity = ObjectIdentity
oduTypeE1A = _OduTypeE1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    oduTypeE1A.setStatus("current")
_OduTypeE1B_ObjectIdentity = ObjectIdentity
oduTypeE1B = _OduTypeE1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    oduTypeE1B.setStatus("current")
_SkyZhone8e2_ObjectIdentity = ObjectIdentity
skyZhone8e2 = _SkyZhone8e2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    skyZhone8e2.setStatus("current")
_OduTypeE2A_ObjectIdentity = ObjectIdentity
oduTypeE2A = _OduTypeE2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oduTypeE2A.setStatus("current")
_OduTypeE2B_ObjectIdentity = ObjectIdentity
oduTypeE2B = _OduTypeE2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    oduTypeE2B.setStatus("current")
_SkyZhone8e3_ObjectIdentity = ObjectIdentity
skyZhone8e3 = _SkyZhone8e3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    skyZhone8e3.setStatus("current")
_OduTypeE3A_ObjectIdentity = ObjectIdentity
oduTypeE3A = _OduTypeE3A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    oduTypeE3A.setStatus("current")
_OduTypeE3B_ObjectIdentity = ObjectIdentity
oduTypeE3B = _OduTypeE3B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    oduTypeE3B.setStatus("current")
_SkyZhone8e4_ObjectIdentity = ObjectIdentity
skyZhone8e4 = _SkyZhone8e4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    skyZhone8e4.setStatus("current")
_OduTypeE4A_ObjectIdentity = ObjectIdentity
oduTypeE4A = _OduTypeE4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    oduTypeE4A.setStatus("current")
_OduTypeE4B_ObjectIdentity = ObjectIdentity
oduTypeE4B = _OduTypeE4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 4, 2)
)
if mibBuilder.loadTexts:
    oduTypeE4B.setStatus("current")
_SkyZhone8t1_ObjectIdentity = ObjectIdentity
skyZhone8t1 = _SkyZhone8t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    skyZhone8t1.setStatus("current")
_OduTypeT1A_ObjectIdentity = ObjectIdentity
oduTypeT1A = _OduTypeT1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 5, 1)
)
if mibBuilder.loadTexts:
    oduTypeT1A.setStatus("current")
_OduTypeT1B_ObjectIdentity = ObjectIdentity
oduTypeT1B = _OduTypeT1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 5, 2)
)
if mibBuilder.loadTexts:
    oduTypeT1B.setStatus("current")
_SkyZhone8t2_ObjectIdentity = ObjectIdentity
skyZhone8t2 = _SkyZhone8t2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    skyZhone8t2.setStatus("current")
_OduTypeT2A_ObjectIdentity = ObjectIdentity
oduTypeT2A = _OduTypeT2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 6, 1)
)
if mibBuilder.loadTexts:
    oduTypeT2A.setStatus("current")
_OduTypeT2B_ObjectIdentity = ObjectIdentity
oduTypeT2B = _OduTypeT2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 6, 2)
)
if mibBuilder.loadTexts:
    oduTypeT2B.setStatus("current")
_SkyZhone8t3_ObjectIdentity = ObjectIdentity
skyZhone8t3 = _SkyZhone8t3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    skyZhone8t3.setStatus("current")
_OduTypeT3A_ObjectIdentity = ObjectIdentity
oduTypeT3A = _OduTypeT3A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 7, 1)
)
if mibBuilder.loadTexts:
    oduTypeT3A.setStatus("current")
_OduTypeT3B_ObjectIdentity = ObjectIdentity
oduTypeT3B = _OduTypeT3B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 7, 2)
)
if mibBuilder.loadTexts:
    oduTypeT3B.setStatus("current")
_SkyZhone8t4_ObjectIdentity = ObjectIdentity
skyZhone8t4 = _SkyZhone8t4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    skyZhone8t4.setStatus("current")
_OduTypeT4A_ObjectIdentity = ObjectIdentity
oduTypeT4A = _OduTypeT4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 8, 1)
)
if mibBuilder.loadTexts:
    oduTypeT4A.setStatus("current")
_OduTypeT4B_ObjectIdentity = ObjectIdentity
oduTypeT4B = _OduTypeT4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 8, 2)
)
if mibBuilder.loadTexts:
    oduTypeT4B.setStatus("current")
_SkyZhone155s1_ObjectIdentity = ObjectIdentity
skyZhone155s1 = _SkyZhone155s1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 9)
)
if mibBuilder.loadTexts:
    skyZhone155s1.setStatus("current")
_OduTypeS1A_ObjectIdentity = ObjectIdentity
oduTypeS1A = _OduTypeS1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 9, 1)
)
if mibBuilder.loadTexts:
    oduTypeS1A.setStatus("current")
_OduTypeS1B_ObjectIdentity = ObjectIdentity
oduTypeS1B = _OduTypeS1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 9, 2)
)
if mibBuilder.loadTexts:
    oduTypeS1B.setStatus("current")
_SkyZhone155s2_ObjectIdentity = ObjectIdentity
skyZhone155s2 = _SkyZhone155s2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 10)
)
if mibBuilder.loadTexts:
    skyZhone155s2.setStatus("current")
_OduTypeS2A_ObjectIdentity = ObjectIdentity
oduTypeS2A = _OduTypeS2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 10, 1)
)
if mibBuilder.loadTexts:
    oduTypeS2A.setStatus("current")
_OduTypeS2B_ObjectIdentity = ObjectIdentity
oduTypeS2B = _OduTypeS2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 10, 2)
)
if mibBuilder.loadTexts:
    oduTypeS2B.setStatus("current")
_SkyZhone155s3_ObjectIdentity = ObjectIdentity
skyZhone155s3 = _SkyZhone155s3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 11)
)
if mibBuilder.loadTexts:
    skyZhone155s3.setStatus("current")
_OduTypeS3A_ObjectIdentity = ObjectIdentity
oduTypeS3A = _OduTypeS3A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 11, 1)
)
if mibBuilder.loadTexts:
    oduTypeS3A.setStatus("current")
_OduTypeS3B_ObjectIdentity = ObjectIdentity
oduTypeS3B = _OduTypeS3B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 11, 2)
)
if mibBuilder.loadTexts:
    oduTypeS3B.setStatus("current")
_SkyZhone155s4_ObjectIdentity = ObjectIdentity
skyZhone155s4 = _SkyZhone155s4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 12)
)
if mibBuilder.loadTexts:
    skyZhone155s4.setStatus("current")
_OduTypeS4A_ObjectIdentity = ObjectIdentity
oduTypeS4A = _OduTypeS4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 12, 1)
)
if mibBuilder.loadTexts:
    oduTypeS4A.setStatus("current")
_OduTypeS4B_ObjectIdentity = ObjectIdentity
oduTypeS4B = _OduTypeS4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 12, 2)
)
if mibBuilder.loadTexts:
    oduTypeS4B.setStatus("current")
_Malc19_ObjectIdentity = ObjectIdentity
malc19 = _Malc19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 1)
)
if mibBuilder.loadTexts:
    malc19.setStatus("current")
_Malc23_ObjectIdentity = ObjectIdentity
malc23 = _Malc23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 2)
)
if mibBuilder.loadTexts:
    malc23.setStatus("current")
_Malc319_ObjectIdentity = ObjectIdentity
malc319 = _Malc319_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 3)
)
if mibBuilder.loadTexts:
    malc319.setStatus("current")
_Raptor319A_ObjectIdentity = ObjectIdentity
raptor319A = _Raptor319A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 4)
)
if mibBuilder.loadTexts:
    raptor319A.setStatus("current")
_Raptor319I_ObjectIdentity = ObjectIdentity
raptor319I = _Raptor319I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 5)
)
if mibBuilder.loadTexts:
    raptor319I.setStatus("current")
_Raptor719A_ObjectIdentity = ObjectIdentity
raptor719A = _Raptor719A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 6)
)
if mibBuilder.loadTexts:
    raptor719A.setStatus("current")
_Raptor719I_ObjectIdentity = ObjectIdentity
raptor719I = _Raptor719I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 7)
)
if mibBuilder.loadTexts:
    raptor719I.setStatus("current")
_Raptor723A_ObjectIdentity = ObjectIdentity
raptor723A = _Raptor723A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 8)
)
if mibBuilder.loadTexts:
    raptor723A.setStatus("current")
_Raptor723I_ObjectIdentity = ObjectIdentity
raptor723I = _Raptor723I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 9)
)
if mibBuilder.loadTexts:
    raptor723I.setStatus("current")
_Raptor100A_ObjectIdentity = ObjectIdentity
raptor100A = _Raptor100A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 10)
)
if mibBuilder.loadTexts:
    raptor100A.setStatus("current")
_Raptor100I_ObjectIdentity = ObjectIdentity
raptor100I = _Raptor100I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 11)
)
if mibBuilder.loadTexts:
    raptor100I.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZhoneProductRegistrations",
    **{"ban-2000": ban_2000,
       "zedge64": zedge64,
       "zedge64-SHDSL-FXS": zedge64_SHDSL_FXS,
       "zedge64-SHDSL-BRI": zedge64_SHDSL_BRI,
       "zedge64-T1-FXS": zedge64_T1_FXS,
       "zedge64-E1-FXS": zedge64_E1_FXS,
       "z-plex10B": z_plex10B,
       "z-plex10B-FXS-FXO": z_plex10B_FXS_FXO,
       "z-plex10B-FXS": z_plex10B_FXS,
       "sechtor-100": sechtor_100,
       "s100-ATM-SM-16T1": s100_ATM_SM_16T1,
       "s100-ATM-SM-16E1": s100_ATM_SM_16E1,
       "sechtor-300": sechtor_300,
       "zhoneRegWtn": zhoneRegWtn,
       "node5700Mhz": node5700Mhz,
       "skyZhone45": skyZhone45,
       "oduTypeA": oduTypeA,
       "oduTypeB": oduTypeB,
       "node23000Mhz": node23000Mhz,
       "skyZhone8e1": skyZhone8e1,
       "oduTypeE1A": oduTypeE1A,
       "oduTypeE1B": oduTypeE1B,
       "skyZhone8e2": skyZhone8e2,
       "oduTypeE2A": oduTypeE2A,
       "oduTypeE2B": oduTypeE2B,
       "skyZhone8e3": skyZhone8e3,
       "oduTypeE3A": oduTypeE3A,
       "oduTypeE3B": oduTypeE3B,
       "skyZhone8e4": skyZhone8e4,
       "oduTypeE4A": oduTypeE4A,
       "oduTypeE4B": oduTypeE4B,
       "skyZhone8t1": skyZhone8t1,
       "oduTypeT1A": oduTypeT1A,
       "oduTypeT1B": oduTypeT1B,
       "skyZhone8t2": skyZhone8t2,
       "oduTypeT2A": oduTypeT2A,
       "oduTypeT2B": oduTypeT2B,
       "skyZhone8t3": skyZhone8t3,
       "oduTypeT3A": oduTypeT3A,
       "oduTypeT3B": oduTypeT3B,
       "skyZhone8t4": skyZhone8t4,
       "oduTypeT4A": oduTypeT4A,
       "oduTypeT4B": oduTypeT4B,
       "skyZhone155s1": skyZhone155s1,
       "oduTypeS1A": oduTypeS1A,
       "oduTypeS1B": oduTypeS1B,
       "skyZhone155s2": skyZhone155s2,
       "oduTypeS2A": oduTypeS2A,
       "oduTypeS2B": oduTypeS2B,
       "skyZhone155s3": skyZhone155s3,
       "oduTypeS3A": oduTypeS3A,
       "oduTypeS3B": oduTypeS3B,
       "skyZhone155s4": skyZhone155s4,
       "oduTypeS4A": oduTypeS4A,
       "oduTypeS4B": oduTypeS4B,
       "malc19": malc19,
       "malc23": malc23,
       "malc319": malc319,
       "raptor319A": raptor319A,
       "raptor319I": raptor319I,
       "raptor719A": raptor719A,
       "raptor719I": raptor719I,
       "raptor723A": raptor723A,
       "raptor723I": raptor723I,
       "raptor100A": raptor100A,
       "raptor100I": raptor100I,
       "zhoneRegistrationsModule": zhoneRegistrationsModule}
)
