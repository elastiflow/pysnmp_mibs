# SNMP MIB module (EKINOPS-Pm1004m-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1004m-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:47 2025
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

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

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

modulePm1004m = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29)
)
if mibBuilder.loadTexts:
    modulePm1004m.setRevisions(
        ("2007-12-14 00:00",
         "2009-03-19 00:00",
         "2009-04-06 00:00",
         "2009-04-09 00:00",
         "2009-09-30 00:00",
         "2010-02-18 00:00",
         "2010-06-14 00:00",
         "2010-11-09 00:00",
         "2012-07-03 00:00",
         "2013-04-02 00:00",
         "2014-03-27 00:00",
         "2014-12-22 00:00",
         "2016-05-19 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1004mOtxMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("otx80mode", 1),
          ("otx60mode", 2),
          ("otxadjustmode", 4))
    )



class Pm1004mOtxGrid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("otxgrid50", 50),
          ("otxgrid100", 100),
          ("otxgrid200", 200))
    )



class Pm1004mAdjustValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("otxadjustvalue0", 0),
          ("otxadjustvalue1", 1),
          ("otxadjustvalue2", 2),
          ("otxadjustvalue3", 3),
          ("otxadjustvalue4", 4),
          ("otxadjustvalue5", 5),
          ("otxadjustvalue6", 6),
          ("otxadjustvalue7", 7),
          ("otxadjustvalue8", 8),
          ("otxadjustvalue9", 9),
          ("otxadjustvalue10", 10))
    )



class Pm1004mOtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm1004malarms_ObjectIdentity = ObjectIdentity
pm1004malarms = _Pm1004malarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2)
)
_Pm1004mAlmOther_ObjectIdentity = ObjectIdentity
pm1004mAlmOther = _Pm1004mAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1)
)
_Pm1004mAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1004mAlmOtherNurg = _Pm1004mAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 1)
)
_Pm1004mAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm1004mAlmsynthAlm2 = _Pm1004mAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 1, 2)
)
_Pm1004mAlmConfTableSave_Type = EkiOnOff
_Pm1004mAlmConfTableSave_Object = MibScalar
pm1004mAlmConfTableSave = _Pm1004mAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 1, 2, 1),
    _Pm1004mAlmConfTableSave_Type()
)
pm1004mAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmConfTableSave.setStatus("current")
_Pm1004mAlmInvUpload_Type = EkiOnOff
_Pm1004mAlmInvUpload_Object = MibScalar
pm1004mAlmInvUpload = _Pm1004mAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 1, 2, 2),
    _Pm1004mAlmInvUpload_Type()
)
pm1004mAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmInvUpload.setStatus("current")
_Pm1004mAlmConfTableLoad_Type = EkiOnOff
_Pm1004mAlmConfTableLoad_Object = MibScalar
pm1004mAlmConfTableLoad = _Pm1004mAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 1, 2, 3),
    _Pm1004mAlmConfTableLoad_Type()
)
pm1004mAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmConfTableLoad.setStatus("current")
_Pm1004mAlmCorrelatOff_Type = EkiOnOff
_Pm1004mAlmCorrelatOff_Object = MibScalar
pm1004mAlmCorrelatOff = _Pm1004mAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 1, 2, 4),
    _Pm1004mAlmCorrelatOff_Type()
)
pm1004mAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmCorrelatOff.setStatus("current")
_Pm1004mAlmMaintenanceOn_Type = EkiOnOff
_Pm1004mAlmMaintenanceOn_Object = MibScalar
pm1004mAlmMaintenanceOn = _Pm1004mAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 1, 2, 5),
    _Pm1004mAlmMaintenanceOn_Type()
)
pm1004mAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmMaintenanceOn.setStatus("current")
_Pm1004mAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1004mAlmOtherUrg = _Pm1004mAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2)
)
_Pm1004mAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm1004mAlmmodInitFailLevel2 = _Pm1004mAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 194)
)
_Pm1004mAlmLedFail_Type = EkiOnOff
_Pm1004mAlmLedFail_Object = MibScalar
pm1004mAlmLedFail = _Pm1004mAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 194, 1),
    _Pm1004mAlmLedFail_Type()
)
pm1004mAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLedFail.setStatus("current")
_Pm1004mAlmNextColdBootForced_Type = EkiOnOff
_Pm1004mAlmNextColdBootForced_Object = MibScalar
pm1004mAlmNextColdBootForced = _Pm1004mAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 194, 2),
    _Pm1004mAlmNextColdBootForced_Type()
)
pm1004mAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmNextColdBootForced.setStatus("current")
_Pm1004mAlmBootUndone_Type = EkiOnOff
_Pm1004mAlmBootUndone_Object = MibScalar
pm1004mAlmBootUndone = _Pm1004mAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 194, 3),
    _Pm1004mAlmBootUndone_Type()
)
pm1004mAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmBootUndone.setStatus("current")
_Pm1004mAlmResetHwInitFail_Type = EkiOnOff
_Pm1004mAlmResetHwInitFail_Object = MibScalar
pm1004mAlmResetHwInitFail = _Pm1004mAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 194, 4),
    _Pm1004mAlmResetHwInitFail_Type()
)
pm1004mAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmResetHwInitFail.setStatus("current")
_Pm1004mAlmSwInitFail_Type = EkiOnOff
_Pm1004mAlmSwInitFail_Object = MibScalar
pm1004mAlmSwInitFail = _Pm1004mAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 194, 5),
    _Pm1004mAlmSwInitFail_Type()
)
pm1004mAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmSwInitFail.setStatus("current")
_Pm1004mAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm1004mAlmmodInitFailLevel3 = _Pm1004mAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195)
)
_Pm1004mAlmGwIdentFail_Type = EkiOnOff
_Pm1004mAlmGwIdentFail_Object = MibScalar
pm1004mAlmGwIdentFail = _Pm1004mAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 1),
    _Pm1004mAlmGwIdentFail_Type()
)
pm1004mAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmGwIdentFail.setStatus("current")
_Pm1004mAlmObmTypeReadFail_Type = EkiOnOff
_Pm1004mAlmObmTypeReadFail_Object = MibScalar
pm1004mAlmObmTypeReadFail = _Pm1004mAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 2),
    _Pm1004mAlmObmTypeReadFail_Type()
)
pm1004mAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmObmTypeReadFail.setStatus("current")
_Pm1004mAlmInitModuleFail_Type = EkiOnOff
_Pm1004mAlmInitModuleFail_Object = MibScalar
pm1004mAlmInitModuleFail = _Pm1004mAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 3),
    _Pm1004mAlmInitModuleFail_Type()
)
pm1004mAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmInitModuleFail.setStatus("current")
_Pm1004mAlmXfp1InitFail_Type = EkiOnOff
_Pm1004mAlmXfp1InitFail_Object = MibScalar
pm1004mAlmXfp1InitFail = _Pm1004mAlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 5),
    _Pm1004mAlmXfp1InitFail_Type()
)
pm1004mAlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmXfp1InitFail.setStatus("current")
_Pm1004mAlmXfp2InitFail_Type = EkiOnOff
_Pm1004mAlmXfp2InitFail_Object = MibScalar
pm1004mAlmXfp2InitFail = _Pm1004mAlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 6),
    _Pm1004mAlmXfp2InitFail_Type()
)
pm1004mAlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmXfp2InitFail.setStatus("current")
_Pm1004mAlmLine1InitFail_Type = EkiOnOff
_Pm1004mAlmLine1InitFail_Object = MibScalar
pm1004mAlmLine1InitFail = _Pm1004mAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 7),
    _Pm1004mAlmLine1InitFail_Type()
)
pm1004mAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLine1InitFail.setStatus("current")
_Pm1004mAlmLine2InitFail_Type = EkiOnOff
_Pm1004mAlmLine2InitFail_Object = MibScalar
pm1004mAlmLine2InitFail = _Pm1004mAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 8),
    _Pm1004mAlmLine2InitFail_Type()
)
pm1004mAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLine2InitFail.setStatus("current")
_Pm1004mAlmClient1InitFail_Type = EkiOnOff
_Pm1004mAlmClient1InitFail_Object = MibScalar
pm1004mAlmClient1InitFail = _Pm1004mAlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 9),
    _Pm1004mAlmClient1InitFail_Type()
)
pm1004mAlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmClient1InitFail.setStatus("current")
_Pm1004mAlmClient2InitFail_Type = EkiOnOff
_Pm1004mAlmClient2InitFail_Object = MibScalar
pm1004mAlmClient2InitFail = _Pm1004mAlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 10),
    _Pm1004mAlmClient2InitFail_Type()
)
pm1004mAlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmClient2InitFail.setStatus("current")
_Pm1004mAlmClient3InitFail_Type = EkiOnOff
_Pm1004mAlmClient3InitFail_Object = MibScalar
pm1004mAlmClient3InitFail = _Pm1004mAlmClient3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 11),
    _Pm1004mAlmClient3InitFail_Type()
)
pm1004mAlmClient3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmClient3InitFail.setStatus("current")
_Pm1004mAlmClient4InitFail_Type = EkiOnOff
_Pm1004mAlmClient4InitFail_Object = MibScalar
pm1004mAlmClient4InitFail = _Pm1004mAlmClient4InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 2, 195, 12),
    _Pm1004mAlmClient4InitFail_Type()
)
pm1004mAlmClient4InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmClient4InitFail.setStatus("current")
_Pm1004mAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1004mAlmOtherCrit = _Pm1004mAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 3)
)
_Pm1004mAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1004mAlmsynthAlm0 = _Pm1004mAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 3, 0)
)
_Pm1004mAlmModGlobFail_Type = EkiOnOff
_Pm1004mAlmModGlobFail_Object = MibScalar
pm1004mAlmModGlobFail = _Pm1004mAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 3, 0, 9),
    _Pm1004mAlmModGlobFail_Type()
)
pm1004mAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmModGlobFail.setStatus("current")
_Pm1004mAlmDefFuseA_Type = EkiOnOff
_Pm1004mAlmDefFuseA_Object = MibScalar
pm1004mAlmDefFuseA = _Pm1004mAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 3, 0, 15),
    _Pm1004mAlmDefFuseA_Type()
)
pm1004mAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDefFuseA.setStatus("current")
_Pm1004mAlmDefFuseB_Type = EkiOnOff
_Pm1004mAlmDefFuseB_Object = MibScalar
pm1004mAlmDefFuseB = _Pm1004mAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 1, 3, 0, 16),
    _Pm1004mAlmDefFuseB_Type()
)
pm1004mAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDefFuseB.setStatus("current")
_Pm1004mAlmClient_ObjectIdentity = ObjectIdentity
pm1004mAlmClient = _Pm1004mAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2)
)
_Pm1004mAlmClientNurg_ObjectIdentity = ObjectIdentity
pm1004mAlmClientNurg = _Pm1004mAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1)
)
_Pm1004mAlmsfpWarnDdmTable_Object = MibTable
pm1004mAlmsfpWarnDdmTable = _Pm1004mAlmsfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pm1004mAlmsfpWarnDdmTable.setStatus("current")
_Pm1004mAlmsfpWarnDdmEntry_Object = MibTableRow
pm1004mAlmsfpWarnDdmEntry = _Pm1004mAlmsfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1)
)
pm1004mAlmsfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmsfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmsfpWarnDdmEntry.setStatus("current")


class _Pm1004mAlmsfpWarnDdmIndex_Type(Integer32):
    """Custom type pm1004mAlmsfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmsfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm1004mAlmsfpWarnDdmIndex_Object = MibTableColumn
pm1004mAlmsfpWarnDdmIndex = _Pm1004mAlmsfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 1),
    _Pm1004mAlmsfpWarnDdmIndex_Type()
)
pm1004mAlmsfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmsfpWarnDdmIndex.setStatus("current")
_Pm1004mAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm1004mAlmTxPwLowWngPortn_Object = MibTableColumn
pm1004mAlmTxPwLowWngPortn = _Pm1004mAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 2),
    _Pm1004mAlmTxPwLowWngPortn_Type()
)
pm1004mAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxPwLowWngPortn.setStatus("current")
_Pm1004mAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm1004mAlmTxPwrHighWngPortn_Object = MibTableColumn
pm1004mAlmTxPwrHighWngPortn = _Pm1004mAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 3),
    _Pm1004mAlmTxPwrHighWngPortn_Type()
)
pm1004mAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxPwrHighWngPortn.setStatus("current")
_Pm1004mAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm1004mAlmTxBiasLowWngPortn_Object = MibTableColumn
pm1004mAlmTxBiasLowWngPortn = _Pm1004mAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 4),
    _Pm1004mAlmTxBiasLowWngPortn_Type()
)
pm1004mAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxBiasLowWngPortn.setStatus("current")
_Pm1004mAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm1004mAlmTxBiasHighWngPortn_Object = MibTableColumn
pm1004mAlmTxBiasHighWngPortn = _Pm1004mAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 5),
    _Pm1004mAlmTxBiasHighWngPortn_Type()
)
pm1004mAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxBiasHighWngPortn.setStatus("current")
_Pm1004mAlmVccLowWngPortn_Type = EkiOnOff
_Pm1004mAlmVccLowWngPortn_Object = MibTableColumn
pm1004mAlmVccLowWngPortn = _Pm1004mAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 6),
    _Pm1004mAlmVccLowWngPortn_Type()
)
pm1004mAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVccLowWngPortn.setStatus("current")
_Pm1004mAlmVccHighWngPortn_Type = EkiOnOff
_Pm1004mAlmVccHighWngPortn_Object = MibTableColumn
pm1004mAlmVccHighWngPortn = _Pm1004mAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 7),
    _Pm1004mAlmVccHighWngPortn_Type()
)
pm1004mAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVccHighWngPortn.setStatus("current")
_Pm1004mAlmTempLowWngPortn_Type = EkiOnOff
_Pm1004mAlmTempLowWngPortn_Object = MibTableColumn
pm1004mAlmTempLowWngPortn = _Pm1004mAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 8),
    _Pm1004mAlmTempLowWngPortn_Type()
)
pm1004mAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTempLowWngPortn.setStatus("current")
_Pm1004mAlmTempHighWngPortn_Type = EkiOnOff
_Pm1004mAlmTempHighWngPortn_Object = MibTableColumn
pm1004mAlmTempHighWngPortn = _Pm1004mAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 9),
    _Pm1004mAlmTempHighWngPortn_Type()
)
pm1004mAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTempHighWngPortn.setStatus("current")
_Pm1004mAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm1004mAlmRxPwrLowWngPortn_Object = MibTableColumn
pm1004mAlmRxPwrLowWngPortn = _Pm1004mAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 16),
    _Pm1004mAlmRxPwrLowWngPortn_Type()
)
pm1004mAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxPwrLowWngPortn.setStatus("current")
_Pm1004mAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm1004mAlmRxPwrHighWngPortn_Object = MibTableColumn
pm1004mAlmRxPwrHighWngPortn = _Pm1004mAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 48, 1, 17),
    _Pm1004mAlmRxPwrHighWngPortn_Type()
)
pm1004mAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxPwrHighWngPortn.setStatus("current")
_Pm1004mAlmk1K2ClientTable_Object = MibTable
pm1004mAlmk1K2ClientTable = _Pm1004mAlmk1K2ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 96)
)
if mibBuilder.loadTexts:
    pm1004mAlmk1K2ClientTable.setStatus("current")
_Pm1004mAlmk1K2ClientEntry_Object = MibTableRow
pm1004mAlmk1K2ClientEntry = _Pm1004mAlmk1K2ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 96, 1)
)
pm1004mAlmk1K2ClientEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmk1K2ClientIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmk1K2ClientEntry.setStatus("current")


class _Pm1004mAlmk1K2ClientIndex_Type(Integer32):
    """Custom type pm1004mAlmk1K2ClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmk1K2ClientIndex_Type.__name__ = "Integer32"
_Pm1004mAlmk1K2ClientIndex_Object = MibTableColumn
pm1004mAlmk1K2ClientIndex = _Pm1004mAlmk1K2ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 96, 1, 1),
    _Pm1004mAlmk1K2ClientIndex_Type()
)
pm1004mAlmk1K2ClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmk1K2ClientIndex.setStatus("current")


class _Pm1004mAlmk1K2ClientPortn_Type(Integer32):
    """Custom type pm1004mAlmk1K2ClientPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mAlmk1K2ClientPortn_Type.__name__ = "Integer32"
_Pm1004mAlmk1K2ClientPortn_Object = MibTableColumn
pm1004mAlmk1K2ClientPortn = _Pm1004mAlmk1K2ClientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 1, 96, 1, 2),
    _Pm1004mAlmk1K2ClientPortn_Type()
)
pm1004mAlmk1K2ClientPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmk1K2ClientPortn.setStatus("current")
_Pm1004mAlmClientUrg_ObjectIdentity = ObjectIdentity
pm1004mAlmClientUrg = _Pm1004mAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2)
)
_Pm1004mAlmsfpAlmDdmTable_Object = MibTable
pm1004mAlmsfpAlmDdmTable = _Pm1004mAlmsfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004mAlmsfpAlmDdmTable.setStatus("current")
_Pm1004mAlmsfpAlmDdmEntry_Object = MibTableRow
pm1004mAlmsfpAlmDdmEntry = _Pm1004mAlmsfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1)
)
pm1004mAlmsfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmsfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmsfpAlmDdmEntry.setStatus("current")


class _Pm1004mAlmsfpAlmDdmIndex_Type(Integer32):
    """Custom type pm1004mAlmsfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmsfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm1004mAlmsfpAlmDdmIndex_Object = MibTableColumn
pm1004mAlmsfpAlmDdmIndex = _Pm1004mAlmsfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 1),
    _Pm1004mAlmsfpAlmDdmIndex_Type()
)
pm1004mAlmsfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmsfpAlmDdmIndex.setStatus("current")
_Pm1004mAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm1004mAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm1004mAlmTxPwrLowAlaPortn = _Pm1004mAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 2),
    _Pm1004mAlmTxPwrLowAlaPortn_Type()
)
pm1004mAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxPwrLowAlaPortn.setStatus("current")
_Pm1004mAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm1004mAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm1004mAlmTxPwrHighAlaPortn = _Pm1004mAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 3),
    _Pm1004mAlmTxPwrHighAlaPortn_Type()
)
pm1004mAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxPwrHighAlaPortn.setStatus("current")
_Pm1004mAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm1004mAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm1004mAlmTxBiasLowAlaPortn = _Pm1004mAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 4),
    _Pm1004mAlmTxBiasLowAlaPortn_Type()
)
pm1004mAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxBiasLowAlaPortn.setStatus("current")
_Pm1004mAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm1004mAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm1004mAlmTxBiasHighAlaPortn = _Pm1004mAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 5),
    _Pm1004mAlmTxBiasHighAlaPortn_Type()
)
pm1004mAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxBiasHighAlaPortn.setStatus("current")
_Pm1004mAlmVccLowAlaPortn_Type = EkiOnOff
_Pm1004mAlmVccLowAlaPortn_Object = MibTableColumn
pm1004mAlmVccLowAlaPortn = _Pm1004mAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 6),
    _Pm1004mAlmVccLowAlaPortn_Type()
)
pm1004mAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVccLowAlaPortn.setStatus("current")
_Pm1004mAlmVccHighAlaPortn_Type = EkiOnOff
_Pm1004mAlmVccHighAlaPortn_Object = MibTableColumn
pm1004mAlmVccHighAlaPortn = _Pm1004mAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 7),
    _Pm1004mAlmVccHighAlaPortn_Type()
)
pm1004mAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVccHighAlaPortn.setStatus("current")
_Pm1004mAlmTempLowAlaPortn_Type = EkiOnOff
_Pm1004mAlmTempLowAlaPortn_Object = MibTableColumn
pm1004mAlmTempLowAlaPortn = _Pm1004mAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 8),
    _Pm1004mAlmTempLowAlaPortn_Type()
)
pm1004mAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTempLowAlaPortn.setStatus("current")
_Pm1004mAlmTempHighAlaPortn_Type = EkiOnOff
_Pm1004mAlmTempHighAlaPortn_Object = MibTableColumn
pm1004mAlmTempHighAlaPortn = _Pm1004mAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 9),
    _Pm1004mAlmTempHighAlaPortn_Type()
)
pm1004mAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTempHighAlaPortn.setStatus("current")
_Pm1004mAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm1004mAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm1004mAlmRxPwrLowAlaPortn = _Pm1004mAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 16),
    _Pm1004mAlmRxPwrLowAlaPortn_Type()
)
pm1004mAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxPwrLowAlaPortn.setStatus("current")
_Pm1004mAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm1004mAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm1004mAlmRxPwrHighAlaPortn = _Pm1004mAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 2, 32, 1, 17),
    _Pm1004mAlmRxPwrHighAlaPortn_Type()
)
pm1004mAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxPwrHighAlaPortn.setStatus("current")
_Pm1004mAlmClientCrit_ObjectIdentity = ObjectIdentity
pm1004mAlmClientCrit = _Pm1004mAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3)
)
_Pm1004mAlmsynthAlmPortTable_Object = MibTable
pm1004mAlmsynthAlmPortTable = _Pm1004mAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm1004mAlmsynthAlmPortTable.setStatus("current")
_Pm1004mAlmsynthAlmPortEntry_Object = MibTableRow
pm1004mAlmsynthAlmPortEntry = _Pm1004mAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1)
)
pm1004mAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmsynthAlmPortEntry.setStatus("current")


class _Pm1004mAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm1004mAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm1004mAlmsynthAlmPortIndex_Object = MibTableColumn
pm1004mAlmsynthAlmPortIndex = _Pm1004mAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 1),
    _Pm1004mAlmsynthAlmPortIndex_Type()
)
pm1004mAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmsynthAlmPortIndex.setStatus("current")
_Pm1004mAlmSfpAbsentPortn_Type = EkiOnOff
_Pm1004mAlmSfpAbsentPortn_Object = MibTableColumn
pm1004mAlmSfpAbsentPortn = _Pm1004mAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 2),
    _Pm1004mAlmSfpAbsentPortn_Type()
)
pm1004mAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmSfpAbsentPortn.setStatus("current")
_Pm1004mAlmDdmAbsentPortn_Type = EkiOnOff
_Pm1004mAlmDdmAbsentPortn_Object = MibTableColumn
pm1004mAlmDdmAbsentPortn = _Pm1004mAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 3),
    _Pm1004mAlmDdmAbsentPortn_Type()
)
pm1004mAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDdmAbsentPortn.setStatus("current")
_Pm1004mAlmHwFailAccPortn_Type = EkiOnOff
_Pm1004mAlmHwFailAccPortn_Object = MibTableColumn
pm1004mAlmHwFailAccPortn = _Pm1004mAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 5),
    _Pm1004mAlmHwFailAccPortn_Type()
)
pm1004mAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmHwFailAccPortn.setStatus("current")
_Pm1004mAlmDwLsdPortn_Type = EkiOnOff
_Pm1004mAlmDwLsdPortn_Object = MibTableColumn
pm1004mAlmDwLsdPortn = _Pm1004mAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 6),
    _Pm1004mAlmDwLsdPortn_Type()
)
pm1004mAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwLsdPortn.setStatus("current")
_Pm1004mAlmClientLocalOosPortn_Type = EkiOnOff
_Pm1004mAlmClientLocalOosPortn_Object = MibTableColumn
pm1004mAlmClientLocalOosPortn = _Pm1004mAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 7),
    _Pm1004mAlmClientLocalOosPortn_Type()
)
pm1004mAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmClientLocalOosPortn.setStatus("current")
_Pm1004mAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm1004mAlmClientRemoteOosPortn_Object = MibTableColumn
pm1004mAlmClientRemoteOosPortn = _Pm1004mAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 8),
    _Pm1004mAlmClientRemoteOosPortn_Type()
)
pm1004mAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmClientRemoteOosPortn.setStatus("current")
_Pm1004mAlmDwCaisPortn_Type = EkiOnOff
_Pm1004mAlmDwCaisPortn_Object = MibTableColumn
pm1004mAlmDwCaisPortn = _Pm1004mAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 9),
    _Pm1004mAlmDwCaisPortn_Type()
)
pm1004mAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwCaisPortn.setStatus("current")
_Pm1004mAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm1004mAlmSfpDdmWarningPortn_Object = MibTableColumn
pm1004mAlmSfpDdmWarningPortn = _Pm1004mAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 10),
    _Pm1004mAlmSfpDdmWarningPortn_Type()
)
pm1004mAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmSfpDdmWarningPortn.setStatus("current")
_Pm1004mAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm1004mAlmSfpDdmAlmPortn_Object = MibTableColumn
pm1004mAlmSfpDdmAlmPortn = _Pm1004mAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 11),
    _Pm1004mAlmSfpDdmAlmPortn_Type()
)
pm1004mAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmSfpDdmAlmPortn.setStatus("current")
_Pm1004mAlmFailAccPortn_Type = EkiOnOff
_Pm1004mAlmFailAccPortn_Object = MibTableColumn
pm1004mAlmFailAccPortn = _Pm1004mAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 13),
    _Pm1004mAlmFailAccPortn_Type()
)
pm1004mAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmFailAccPortn.setStatus("current")
_Pm1004mAlmUpCsfPortn_Type = EkiOnOff
_Pm1004mAlmUpCsfPortn_Object = MibTableColumn
pm1004mAlmUpCsfPortn = _Pm1004mAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 8, 1, 17),
    _Pm1004mAlmUpCsfPortn_Type()
)
pm1004mAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmUpCsfPortn.setStatus("current")
_Pm1004mAlmaccessioAlmTable_Object = MibTable
pm1004mAlmaccessioAlmTable = _Pm1004mAlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm1004mAlmaccessioAlmTable.setStatus("current")
_Pm1004mAlmaccessioAlmEntry_Object = MibTableRow
pm1004mAlmaccessioAlmEntry = _Pm1004mAlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 16, 1)
)
pm1004mAlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmaccessioAlmEntry.setStatus("current")


class _Pm1004mAlmaccessioAlmIndex_Type(Integer32):
    """Custom type pm1004mAlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pm1004mAlmaccessioAlmIndex_Object = MibTableColumn
pm1004mAlmaccessioAlmIndex = _Pm1004mAlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 16, 1, 1),
    _Pm1004mAlmaccessioAlmIndex_Type()
)
pm1004mAlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmaccessioAlmIndex.setStatus("current")
_Pm1004mAlmDwLasFailPortn_Type = EkiOnOff
_Pm1004mAlmDwLasFailPortn_Object = MibTableColumn
pm1004mAlmDwLasFailPortn = _Pm1004mAlmDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 16, 1, 2),
    _Pm1004mAlmDwLasFailPortn_Type()
)
pm1004mAlmDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwLasFailPortn.setStatus("current")
_Pm1004mAlmUpLosPortn_Type = EkiOnOff
_Pm1004mAlmUpLosPortn_Object = MibTableColumn
pm1004mAlmUpLosPortn = _Pm1004mAlmUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 16, 1, 5),
    _Pm1004mAlmUpLosPortn_Type()
)
pm1004mAlmUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmUpLosPortn.setStatus("current")
_Pm1004mAlmmapperDeAlmTable_Object = MibTable
pm1004mAlmmapperDeAlmTable = _Pm1004mAlmmapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pm1004mAlmmapperDeAlmTable.setStatus("current")
_Pm1004mAlmmapperDeAlmEntry_Object = MibTableRow
pm1004mAlmmapperDeAlmEntry = _Pm1004mAlmmapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 72, 1)
)
pm1004mAlmmapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmmapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmmapperDeAlmEntry.setStatus("current")


class _Pm1004mAlmmapperDeAlmIndex_Type(Integer32):
    """Custom type pm1004mAlmmapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmmapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm1004mAlmmapperDeAlmIndex_Object = MibTableColumn
pm1004mAlmmapperDeAlmIndex = _Pm1004mAlmmapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 72, 1, 1),
    _Pm1004mAlmmapperDeAlmIndex_Type()
)
pm1004mAlmmapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmmapperDeAlmIndex.setStatus("current")
_Pm1004mAlmUpAccOosPortn_Type = EkiOnOff
_Pm1004mAlmUpAccOosPortn_Object = MibTableColumn
pm1004mAlmUpAccOosPortn = _Pm1004mAlmUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 72, 1, 2),
    _Pm1004mAlmUpAccOosPortn_Type()
)
pm1004mAlmUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmUpAccOosPortn.setStatus("current")
_Pm1004mAlmUpBufferOvlPortn_Type = EkiOnOff
_Pm1004mAlmUpBufferOvlPortn_Object = MibTableColumn
pm1004mAlmUpBufferOvlPortn = _Pm1004mAlmUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 72, 1, 11),
    _Pm1004mAlmUpBufferOvlPortn_Type()
)
pm1004mAlmUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmUpBufferOvlPortn.setStatus("current")
_Pm1004mAlmDwCsfDetPortn_Type = EkiOnOff
_Pm1004mAlmDwCsfDetPortn_Object = MibTableColumn
pm1004mAlmDwCsfDetPortn = _Pm1004mAlmDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 72, 1, 12),
    _Pm1004mAlmDwCsfDetPortn_Type()
)
pm1004mAlmDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwCsfDetPortn.setStatus("current")
_Pm1004mAlmDwBufferOvlPortn_Type = EkiOnOff
_Pm1004mAlmDwBufferOvlPortn_Object = MibTableColumn
pm1004mAlmDwBufferOvlPortn = _Pm1004mAlmDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 72, 1, 15),
    _Pm1004mAlmDwBufferOvlPortn_Type()
)
pm1004mAlmDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwBufferOvlPortn.setStatus("current")
_Pm1004mAlmaccessioSdhAlarmTable_Object = MibTable
pm1004mAlmaccessioSdhAlarmTable = _Pm1004mAlmaccessioSdhAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 104)
)
if mibBuilder.loadTexts:
    pm1004mAlmaccessioSdhAlarmTable.setStatus("current")
_Pm1004mAlmaccessioSdhAlarmEntry_Object = MibTableRow
pm1004mAlmaccessioSdhAlarmEntry = _Pm1004mAlmaccessioSdhAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 104, 1)
)
pm1004mAlmaccessioSdhAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmaccessioSdhAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmaccessioSdhAlarmEntry.setStatus("current")


class _Pm1004mAlmaccessioSdhAlarmIndex_Type(Integer32):
    """Custom type pm1004mAlmaccessioSdhAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmaccessioSdhAlarmIndex_Type.__name__ = "Integer32"
_Pm1004mAlmaccessioSdhAlarmIndex_Object = MibTableColumn
pm1004mAlmaccessioSdhAlarmIndex = _Pm1004mAlmaccessioSdhAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 104, 1, 1),
    _Pm1004mAlmaccessioSdhAlarmIndex_Type()
)
pm1004mAlmaccessioSdhAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmaccessioSdhAlarmIndex.setStatus("current")
_Pm1004mAlmFifoErrPortn_Type = EkiOnOff
_Pm1004mAlmFifoErrPortn_Object = MibTableColumn
pm1004mAlmFifoErrPortn = _Pm1004mAlmFifoErrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 104, 1, 3),
    _Pm1004mAlmFifoErrPortn_Type()
)
pm1004mAlmFifoErrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmFifoErrPortn.setStatus("current")
_Pm1004mAlmRxLossOfLockPortn_Type = EkiOnOff
_Pm1004mAlmRxLossOfLockPortn_Object = MibTableColumn
pm1004mAlmRxLossOfLockPortn = _Pm1004mAlmRxLossOfLockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 104, 1, 4),
    _Pm1004mAlmRxLossOfLockPortn_Type()
)
pm1004mAlmRxLossOfLockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxLossOfLockPortn.setStatus("current")
_Pm1004mAlmTxLossOfLockPortn_Type = EkiOnOff
_Pm1004mAlmTxLossOfLockPortn_Object = MibTableColumn
pm1004mAlmTxLossOfLockPortn = _Pm1004mAlmTxLossOfLockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 104, 1, 5),
    _Pm1004mAlmTxLossOfLockPortn_Type()
)
pm1004mAlmTxLossOfLockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxLossOfLockPortn.setStatus("current")
_Pm1004mAlmClientAisDetPortn_Type = EkiOnOff
_Pm1004mAlmClientAisDetPortn_Object = MibTableColumn
pm1004mAlmClientAisDetPortn = _Pm1004mAlmClientAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 104, 1, 6),
    _Pm1004mAlmClientAisDetPortn_Type()
)
pm1004mAlmClientAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmClientAisDetPortn.setStatus("current")
_Pm1004mAlmClientRdiDetPortn_Type = EkiOnOff
_Pm1004mAlmClientRdiDetPortn_Object = MibTableColumn
pm1004mAlmClientRdiDetPortn = _Pm1004mAlmClientRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 104, 1, 7),
    _Pm1004mAlmClientRdiDetPortn_Type()
)
pm1004mAlmClientRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmClientRdiDetPortn.setStatus("current")
_Pm1004mAlmClientOofPortn_Type = EkiOnOff
_Pm1004mAlmClientOofPortn_Object = MibTableColumn
pm1004mAlmClientOofPortn = _Pm1004mAlmClientOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 2, 3, 104, 1, 8),
    _Pm1004mAlmClientOofPortn_Type()
)
pm1004mAlmClientOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmClientOofPortn.setStatus("current")
_Pm1004mAlmLine_ObjectIdentity = ObjectIdentity
pm1004mAlmLine = _Pm1004mAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3)
)
_Pm1004mAlmLineNurg_ObjectIdentity = ObjectIdentity
pm1004mAlmLineNurg = _Pm1004mAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1)
)
_Pm1004mAlmlineXfp1WarningsTable_Object = MibTable
pm1004mAlmlineXfp1WarningsTable = _Pm1004mAlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1WarningsTable.setStatus("current")
_Pm1004mAlmlineXfp1WarningsEntry_Object = MibTableRow
pm1004mAlmlineXfp1WarningsEntry = _Pm1004mAlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1)
)
pm1004mAlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1WarningsEntry.setStatus("current")


class _Pm1004mAlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pm1004mAlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pm1004mAlmlineXfp1WarningsIndex_Object = MibTableColumn
pm1004mAlmlineXfp1WarningsIndex = _Pm1004mAlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1, 1),
    _Pm1004mAlmlineXfp1WarningsIndex_Type()
)
pm1004mAlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1WarningsIndex.setStatus("current")
_Pm1004mAlmTxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004mAlmTxPowerLowWarningPortn_Object = MibTableColumn
pm1004mAlmTxPowerLowWarningPortn = _Pm1004mAlmTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1, 2),
    _Pm1004mAlmTxPowerLowWarningPortn_Type()
)
pm1004mAlmTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxPowerLowWarningPortn.setStatus("current")
_Pm1004mAlmTxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004mAlmTxPowerHighWarningPortn_Object = MibTableColumn
pm1004mAlmTxPowerHighWarningPortn = _Pm1004mAlmTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1, 3),
    _Pm1004mAlmTxPowerHighWarningPortn_Type()
)
pm1004mAlmTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxPowerHighWarningPortn.setStatus("current")
_Pm1004mAlmTxBiasLowWarningPortn_Type = EkiOnOff
_Pm1004mAlmTxBiasLowWarningPortn_Object = MibTableColumn
pm1004mAlmTxBiasLowWarningPortn = _Pm1004mAlmTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1, 4),
    _Pm1004mAlmTxBiasLowWarningPortn_Type()
)
pm1004mAlmTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxBiasLowWarningPortn.setStatus("current")
_Pm1004mAlmTxBiasHighWarningPortn_Type = EkiOnOff
_Pm1004mAlmTxBiasHighWarningPortn_Object = MibTableColumn
pm1004mAlmTxBiasHighWarningPortn = _Pm1004mAlmTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1, 5),
    _Pm1004mAlmTxBiasHighWarningPortn_Type()
)
pm1004mAlmTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxBiasHighWarningPortn.setStatus("current")
_Pm1004mAlmTempLowWarningPortn_Type = EkiOnOff
_Pm1004mAlmTempLowWarningPortn_Object = MibTableColumn
pm1004mAlmTempLowWarningPortn = _Pm1004mAlmTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1, 8),
    _Pm1004mAlmTempLowWarningPortn_Type()
)
pm1004mAlmTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTempLowWarningPortn.setStatus("current")
_Pm1004mAlmTempHighWarningPortn_Type = EkiOnOff
_Pm1004mAlmTempHighWarningPortn_Object = MibTableColumn
pm1004mAlmTempHighWarningPortn = _Pm1004mAlmTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1, 9),
    _Pm1004mAlmTempHighWarningPortn_Type()
)
pm1004mAlmTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTempHighWarningPortn.setStatus("current")
_Pm1004mAlmRxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004mAlmRxPowerLowWarningPortn_Object = MibTableColumn
pm1004mAlmRxPowerLowWarningPortn = _Pm1004mAlmRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1, 16),
    _Pm1004mAlmRxPowerLowWarningPortn_Type()
)
pm1004mAlmRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxPowerLowWarningPortn.setStatus("current")
_Pm1004mAlmRxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004mAlmRxPowerHighWarningPortn_Object = MibTableColumn
pm1004mAlmRxPowerHighWarningPortn = _Pm1004mAlmRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 209, 1, 17),
    _Pm1004mAlmRxPowerHighWarningPortn_Type()
)
pm1004mAlmRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxPowerHighWarningPortn.setStatus("current")
_Pm1004mAlmlineOtx1TlhWarningsTable_Object = MibTable
pm1004mAlmlineOtx1TlhWarningsTable = _Pm1004mAlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pm1004mAlmlineOtx1TlhWarningsTable.setStatus("current")
_Pm1004mAlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pm1004mAlmlineOtx1TlhWarningsEntry = _Pm1004mAlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 225, 1)
)
pm1004mAlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pm1004mAlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pm1004mAlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pm1004mAlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pm1004mAlmlineOtx1TlhWarningsIndex = _Pm1004mAlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 225, 1, 1),
    _Pm1004mAlmlineOtx1TlhWarningsIndex_Type()
)
pm1004mAlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pm1004mAlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pm1004mAlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pm1004mAlmLineModulatorAgingHighWarningPortn = _Pm1004mAlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 225, 1, 6),
    _Pm1004mAlmLineModulatorAgingHighWarningPortn_Type()
)
pm1004mAlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pm1004mAlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pm1004mAlmLineAgingHighWarningPortn_Object = MibTableColumn
pm1004mAlmLineAgingHighWarningPortn = _Pm1004mAlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 225, 1, 7),
    _Pm1004mAlmLineAgingHighWarningPortn_Type()
)
pm1004mAlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineAgingHighWarningPortn.setStatus("current")
_Pm1004mAlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pm1004mAlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pm1004mAlmLineFreqDevHighWarningPortn = _Pm1004mAlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 225, 1, 13),
    _Pm1004mAlmLineFreqDevHighWarningPortn_Type()
)
pm1004mAlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineFreqDevHighWarningPortn.setStatus("current")
_Pm1004mAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm1004mAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm1004mAlmLineLaserTempHighWarningPortn = _Pm1004mAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 1, 225, 1, 15),
    _Pm1004mAlmLineLaserTempHighWarningPortn_Type()
)
pm1004mAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm1004mAlmLineUrg_ObjectIdentity = ObjectIdentity
pm1004mAlmLineUrg = _Pm1004mAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2)
)
_Pm1004mAlmdfrmBerTable_Object = MibTable
pm1004mAlmdfrmBerTable = _Pm1004mAlmdfrmBerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 129)
)
if mibBuilder.loadTexts:
    pm1004mAlmdfrmBerTable.setStatus("current")
_Pm1004mAlmdfrmBerEntry_Object = MibTableRow
pm1004mAlmdfrmBerEntry = _Pm1004mAlmdfrmBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 129, 1)
)
pm1004mAlmdfrmBerEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmdfrmBerIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmdfrmBerEntry.setStatus("current")


class _Pm1004mAlmdfrmBerIndex_Type(Integer32):
    """Custom type pm1004mAlmdfrmBerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmdfrmBerIndex_Type.__name__ = "Integer32"
_Pm1004mAlmdfrmBerIndex_Object = MibTableColumn
pm1004mAlmdfrmBerIndex = _Pm1004mAlmdfrmBerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 129, 1, 1),
    _Pm1004mAlmdfrmBerIndex_Type()
)
pm1004mAlmdfrmBerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmdfrmBerIndex.setStatus("current")
_Pm1004mAlmLineSignalDegradePortn_Type = EkiOnOff
_Pm1004mAlmLineSignalDegradePortn_Object = MibTableColumn
pm1004mAlmLineSignalDegradePortn = _Pm1004mAlmLineSignalDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 129, 1, 2),
    _Pm1004mAlmLineSignalDegradePortn_Type()
)
pm1004mAlmLineSignalDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineSignalDegradePortn.setStatus("current")
_Pm1004mAlmLineSignalFailPortn_Type = EkiOnOff
_Pm1004mAlmLineSignalFailPortn_Object = MibTableColumn
pm1004mAlmLineSignalFailPortn = _Pm1004mAlmLineSignalFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 129, 1, 3),
    _Pm1004mAlmLineSignalFailPortn_Type()
)
pm1004mAlmLineSignalFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineSignalFailPortn.setStatus("current")
_Pm1004mAlmLineDegradePortn_Type = EkiOnOff
_Pm1004mAlmLineDegradePortn_Object = MibTableColumn
pm1004mAlmLineDegradePortn = _Pm1004mAlmLineDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 129, 1, 6),
    _Pm1004mAlmLineDegradePortn_Type()
)
pm1004mAlmLineDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineDegradePortn.setStatus("current")
_Pm1004mAlmlineXfp1AlarmTable_Object = MibTable
pm1004mAlmlineXfp1AlarmTable = _Pm1004mAlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1AlarmTable.setStatus("current")
_Pm1004mAlmlineXfp1AlarmEntry_Object = MibTableRow
pm1004mAlmlineXfp1AlarmEntry = _Pm1004mAlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1)
)
pm1004mAlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1AlarmEntry.setStatus("current")


class _Pm1004mAlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pm1004mAlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pm1004mAlmlineXfp1AlarmIndex_Object = MibTableColumn
pm1004mAlmlineXfp1AlarmIndex = _Pm1004mAlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1, 1),
    _Pm1004mAlmlineXfp1AlarmIndex_Type()
)
pm1004mAlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1AlarmIndex.setStatus("current")
_Pm1004mAlmTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004mAlmTxPowerLowAlarmPortn_Object = MibTableColumn
pm1004mAlmTxPowerLowAlarmPortn = _Pm1004mAlmTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1, 2),
    _Pm1004mAlmTxPowerLowAlarmPortn_Type()
)
pm1004mAlmTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxPowerLowAlarmPortn.setStatus("current")
_Pm1004mAlmTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004mAlmTxPowerHighAlarmPortn_Object = MibTableColumn
pm1004mAlmTxPowerHighAlarmPortn = _Pm1004mAlmTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1, 3),
    _Pm1004mAlmTxPowerHighAlarmPortn_Type()
)
pm1004mAlmTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxPowerHighAlarmPortn.setStatus("current")
_Pm1004mAlmTxBiasLowAlarmPortn_Type = EkiOnOff
_Pm1004mAlmTxBiasLowAlarmPortn_Object = MibTableColumn
pm1004mAlmTxBiasLowAlarmPortn = _Pm1004mAlmTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1, 4),
    _Pm1004mAlmTxBiasLowAlarmPortn_Type()
)
pm1004mAlmTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxBiasLowAlarmPortn.setStatus("current")
_Pm1004mAlmTxBiasHighAlarmPortn_Type = EkiOnOff
_Pm1004mAlmTxBiasHighAlarmPortn_Object = MibTableColumn
pm1004mAlmTxBiasHighAlarmPortn = _Pm1004mAlmTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1, 5),
    _Pm1004mAlmTxBiasHighAlarmPortn_Type()
)
pm1004mAlmTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxBiasHighAlarmPortn.setStatus("current")
_Pm1004mAlmTempLowAlarmPortn_Type = EkiOnOff
_Pm1004mAlmTempLowAlarmPortn_Object = MibTableColumn
pm1004mAlmTempLowAlarmPortn = _Pm1004mAlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1, 8),
    _Pm1004mAlmTempLowAlarmPortn_Type()
)
pm1004mAlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTempLowAlarmPortn.setStatus("current")
_Pm1004mAlmTempHighAlarmPortn_Type = EkiOnOff
_Pm1004mAlmTempHighAlarmPortn_Object = MibTableColumn
pm1004mAlmTempHighAlarmPortn = _Pm1004mAlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1, 9),
    _Pm1004mAlmTempHighAlarmPortn_Type()
)
pm1004mAlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTempHighAlarmPortn.setStatus("current")
_Pm1004mAlmRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004mAlmRxPowerLowAlarmPortn_Object = MibTableColumn
pm1004mAlmRxPowerLowAlarmPortn = _Pm1004mAlmRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1, 16),
    _Pm1004mAlmRxPowerLowAlarmPortn_Type()
)
pm1004mAlmRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxPowerLowAlarmPortn.setStatus("current")
_Pm1004mAlmRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004mAlmRxPowerHighAlarmPortn_Object = MibTableColumn
pm1004mAlmRxPowerHighAlarmPortn = _Pm1004mAlmRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 208, 1, 17),
    _Pm1004mAlmRxPowerHighAlarmPortn_Type()
)
pm1004mAlmRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxPowerHighAlarmPortn.setStatus("current")
_Pm1004mAlmlineXfp1SupplyAlarmTable_Object = MibTable
pm1004mAlmlineXfp1SupplyAlarmTable = _Pm1004mAlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pm1004mAlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pm1004mAlmlineXfp1SupplyAlarmEntry = _Pm1004mAlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1)
)
pm1004mAlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pm1004mAlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pm1004mAlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pm1004mAlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pm1004mAlmlineXfp1SupplyAlarmIndex = _Pm1004mAlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 1),
    _Pm1004mAlmlineXfp1SupplyAlarmIndex_Type()
)
pm1004mAlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pm1004mAlmVee5LowAlarmPortn_Type = EkiOnOff
_Pm1004mAlmVee5LowAlarmPortn_Object = MibTableColumn
pm1004mAlmVee5LowAlarmPortn = _Pm1004mAlmVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 2),
    _Pm1004mAlmVee5LowAlarmPortn_Type()
)
pm1004mAlmVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVee5LowAlarmPortn.setStatus("current")
_Pm1004mAlmVee5HighAlarmPortn_Type = EkiOnOff
_Pm1004mAlmVee5HighAlarmPortn_Object = MibTableColumn
pm1004mAlmVee5HighAlarmPortn = _Pm1004mAlmVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 3),
    _Pm1004mAlmVee5HighAlarmPortn_Type()
)
pm1004mAlmVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVee5HighAlarmPortn.setStatus("current")
_Pm1004mAlmVcc2LowAlarmPortn_Type = EkiOnOff
_Pm1004mAlmVcc2LowAlarmPortn_Object = MibTableColumn
pm1004mAlmVcc2LowAlarmPortn = _Pm1004mAlmVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 4),
    _Pm1004mAlmVcc2LowAlarmPortn_Type()
)
pm1004mAlmVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc2LowAlarmPortn.setStatus("current")
_Pm1004mAlmVcc2HighAlarmPortn_Type = EkiOnOff
_Pm1004mAlmVcc2HighAlarmPortn_Object = MibTableColumn
pm1004mAlmVcc2HighAlarmPortn = _Pm1004mAlmVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 5),
    _Pm1004mAlmVcc2HighAlarmPortn_Type()
)
pm1004mAlmVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc2HighAlarmPortn.setStatus("current")
_Pm1004mAlmVcc3LowAlarmPortn_Type = EkiOnOff
_Pm1004mAlmVcc3LowAlarmPortn_Object = MibTableColumn
pm1004mAlmVcc3LowAlarmPortn = _Pm1004mAlmVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 6),
    _Pm1004mAlmVcc3LowAlarmPortn_Type()
)
pm1004mAlmVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc3LowAlarmPortn.setStatus("current")
_Pm1004mAlmVcc3HighAlarmPortn_Type = EkiOnOff
_Pm1004mAlmVcc3HighAlarmPortn_Object = MibTableColumn
pm1004mAlmVcc3HighAlarmPortn = _Pm1004mAlmVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 7),
    _Pm1004mAlmVcc3HighAlarmPortn_Type()
)
pm1004mAlmVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc3HighAlarmPortn.setStatus("current")
_Pm1004mAlmVcc5LowAlarmPortn_Type = EkiOnOff
_Pm1004mAlmVcc5LowAlarmPortn_Object = MibTableColumn
pm1004mAlmVcc5LowAlarmPortn = _Pm1004mAlmVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 8),
    _Pm1004mAlmVcc5LowAlarmPortn_Type()
)
pm1004mAlmVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc5LowAlarmPortn.setStatus("current")
_Pm1004mAlmVcc5HighAlarmPortn_Type = EkiOnOff
_Pm1004mAlmVcc5HighAlarmPortn_Object = MibTableColumn
pm1004mAlmVcc5HighAlarmPortn = _Pm1004mAlmVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 9),
    _Pm1004mAlmVcc5HighAlarmPortn_Type()
)
pm1004mAlmVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc5HighAlarmPortn.setStatus("current")
_Pm1004mAlmVee5LowWarningPortn_Type = EkiOnOff
_Pm1004mAlmVee5LowWarningPortn_Object = MibTableColumn
pm1004mAlmVee5LowWarningPortn = _Pm1004mAlmVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 10),
    _Pm1004mAlmVee5LowWarningPortn_Type()
)
pm1004mAlmVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVee5LowWarningPortn.setStatus("current")
_Pm1004mAlmVee5HighWarningPortn_Type = EkiOnOff
_Pm1004mAlmVee5HighWarningPortn_Object = MibTableColumn
pm1004mAlmVee5HighWarningPortn = _Pm1004mAlmVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 11),
    _Pm1004mAlmVee5HighWarningPortn_Type()
)
pm1004mAlmVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVee5HighWarningPortn.setStatus("current")
_Pm1004mAlmVcc2LowWarningPortn_Type = EkiOnOff
_Pm1004mAlmVcc2LowWarningPortn_Object = MibTableColumn
pm1004mAlmVcc2LowWarningPortn = _Pm1004mAlmVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 12),
    _Pm1004mAlmVcc2LowWarningPortn_Type()
)
pm1004mAlmVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc2LowWarningPortn.setStatus("current")
_Pm1004mAlmVcc2HighWarningPortn_Type = EkiOnOff
_Pm1004mAlmVcc2HighWarningPortn_Object = MibTableColumn
pm1004mAlmVcc2HighWarningPortn = _Pm1004mAlmVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 13),
    _Pm1004mAlmVcc2HighWarningPortn_Type()
)
pm1004mAlmVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc2HighWarningPortn.setStatus("current")
_Pm1004mAlmVcc3LowWarningPortn_Type = EkiOnOff
_Pm1004mAlmVcc3LowWarningPortn_Object = MibTableColumn
pm1004mAlmVcc3LowWarningPortn = _Pm1004mAlmVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 14),
    _Pm1004mAlmVcc3LowWarningPortn_Type()
)
pm1004mAlmVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc3LowWarningPortn.setStatus("current")
_Pm1004mAlmVcc3HighWarningPortn_Type = EkiOnOff
_Pm1004mAlmVcc3HighWarningPortn_Object = MibTableColumn
pm1004mAlmVcc3HighWarningPortn = _Pm1004mAlmVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 15),
    _Pm1004mAlmVcc3HighWarningPortn_Type()
)
pm1004mAlmVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc3HighWarningPortn.setStatus("current")
_Pm1004mAlmVcc5LowWarningPortn_Type = EkiOnOff
_Pm1004mAlmVcc5LowWarningPortn_Object = MibTableColumn
pm1004mAlmVcc5LowWarningPortn = _Pm1004mAlmVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 16),
    _Pm1004mAlmVcc5LowWarningPortn_Type()
)
pm1004mAlmVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc5LowWarningPortn.setStatus("current")
_Pm1004mAlmVcc5HighWarningPortn_Type = EkiOnOff
_Pm1004mAlmVcc5HighWarningPortn_Object = MibTableColumn
pm1004mAlmVcc5HighWarningPortn = _Pm1004mAlmVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 212, 1, 17),
    _Pm1004mAlmVcc5HighWarningPortn_Type()
)
pm1004mAlmVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmVcc5HighWarningPortn.setStatus("current")
_Pm1004mAlmlineOtx1TlhAlarmsTable_Object = MibTable
pm1004mAlmlineOtx1TlhAlarmsTable = _Pm1004mAlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pm1004mAlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pm1004mAlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pm1004mAlmlineOtx1TlhAlarmsEntry = _Pm1004mAlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 224, 1)
)
pm1004mAlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pm1004mAlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pm1004mAlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004mAlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pm1004mAlmlineOtx1TlhAlarmsIndex = _Pm1004mAlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 224, 1, 1),
    _Pm1004mAlmlineOtx1TlhAlarmsIndex_Type()
)
pm1004mAlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pm1004mAlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pm1004mAlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pm1004mAlmLineModulatorAgingHighAlaPortn = _Pm1004mAlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 224, 1, 6),
    _Pm1004mAlmLineModulatorAgingHighAlaPortn_Type()
)
pm1004mAlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pm1004mAlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pm1004mAlmLineAgingHighAlaPortn_Object = MibTableColumn
pm1004mAlmLineAgingHighAlaPortn = _Pm1004mAlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 224, 1, 7),
    _Pm1004mAlmLineAgingHighAlaPortn_Type()
)
pm1004mAlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineAgingHighAlaPortn.setStatus("current")
_Pm1004mAlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pm1004mAlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pm1004mAlmLineFreqDevHighAlaPortn = _Pm1004mAlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 224, 1, 13),
    _Pm1004mAlmLineFreqDevHighAlaPortn_Type()
)
pm1004mAlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineFreqDevHighAlaPortn.setStatus("current")
_Pm1004mAlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pm1004mAlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pm1004mAlmLineLaserTempHighAlaPortn = _Pm1004mAlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 2, 224, 1, 15),
    _Pm1004mAlmLineLaserTempHighAlaPortn_Type()
)
pm1004mAlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineLaserTempHighAlaPortn.setStatus("current")
_Pm1004mAlmLineCrit_ObjectIdentity = ObjectIdentity
pm1004mAlmLineCrit = _Pm1004mAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3)
)
_Pm1004mAlmsynthAlmLineTable_Object = MibTable
pm1004mAlmsynthAlmLineTable = _Pm1004mAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm1004mAlmsynthAlmLineTable.setStatus("current")
_Pm1004mAlmsynthAlmLineEntry_Object = MibTableRow
pm1004mAlmsynthAlmLineEntry = _Pm1004mAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1)
)
pm1004mAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmsynthAlmLineEntry.setStatus("current")


class _Pm1004mAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm1004mAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm1004mAlmsynthAlmLineIndex_Object = MibTableColumn
pm1004mAlmsynthAlmLineIndex = _Pm1004mAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 1),
    _Pm1004mAlmsynthAlmLineIndex_Type()
)
pm1004mAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmsynthAlmLineIndex.setStatus("current")
_Pm1004mAlmXfpAbsentPortn_Type = EkiOnOff
_Pm1004mAlmXfpAbsentPortn_Object = MibTableColumn
pm1004mAlmXfpAbsentPortn = _Pm1004mAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 2),
    _Pm1004mAlmXfpAbsentPortn_Type()
)
pm1004mAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmXfpAbsentPortn.setStatus("current")
_Pm1004mAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm1004mAlmXfpInitNotComplPortn_Object = MibTableColumn
pm1004mAlmXfpInitNotComplPortn = _Pm1004mAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 3),
    _Pm1004mAlmXfpInitNotComplPortn_Type()
)
pm1004mAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmXfpInitNotComplPortn.setStatus("current")
_Pm1004mAlmLineHwFailPortn_Type = EkiOnOff
_Pm1004mAlmLineHwFailPortn_Object = MibTableColumn
pm1004mAlmLineHwFailPortn = _Pm1004mAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 5),
    _Pm1004mAlmLineHwFailPortn_Type()
)
pm1004mAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineHwFailPortn.setStatus("current")
_Pm1004mAlmXfpTxOffPortn_Type = EkiOnOff
_Pm1004mAlmXfpTxOffPortn_Object = MibTableColumn
pm1004mAlmXfpTxOffPortn = _Pm1004mAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 6),
    _Pm1004mAlmXfpTxOffPortn_Type()
)
pm1004mAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmXfpTxOffPortn.setStatus("current")
_Pm1004mAlmLineLocalOosPortn_Type = EkiOnOff
_Pm1004mAlmLineLocalOosPortn_Object = MibTableColumn
pm1004mAlmLineLocalOosPortn = _Pm1004mAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 7),
    _Pm1004mAlmLineLocalOosPortn_Type()
)
pm1004mAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineLocalOosPortn.setStatus("current")
_Pm1004mAlmUpRdiInsPortn_Type = EkiOnOff
_Pm1004mAlmUpRdiInsPortn_Object = MibTableColumn
pm1004mAlmUpRdiInsPortn = _Pm1004mAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 9),
    _Pm1004mAlmUpRdiInsPortn_Type()
)
pm1004mAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmUpRdiInsPortn.setStatus("current")
_Pm1004mAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm1004mAlmLineDdmWarningPortn_Object = MibTableColumn
pm1004mAlmLineDdmWarningPortn = _Pm1004mAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 10),
    _Pm1004mAlmLineDdmWarningPortn_Type()
)
pm1004mAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineDdmWarningPortn.setStatus("current")
_Pm1004mAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm1004mAlmLineDdmAlmPortn_Object = MibTableColumn
pm1004mAlmLineDdmAlmPortn = _Pm1004mAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 11),
    _Pm1004mAlmLineDdmAlmPortn_Type()
)
pm1004mAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineDdmAlmPortn.setStatus("current")
_Pm1004mAlmLineFailPortn_Type = EkiOnOff
_Pm1004mAlmLineFailPortn_Object = MibTableColumn
pm1004mAlmLineFailPortn = _Pm1004mAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 13),
    _Pm1004mAlmLineFailPortn_Type()
)
pm1004mAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineFailPortn.setStatus("current")
_Pm1004mAlmLineActivePortn_Type = EkiOnOff
_Pm1004mAlmLineActivePortn_Object = MibTableColumn
pm1004mAlmLineActivePortn = _Pm1004mAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 7, 1, 17),
    _Pm1004mAlmLineActivePortn_Type()
)
pm1004mAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmLineActivePortn.setStatus("current")
_Pm1004mAlmdfrmAlmTable_Object = MibTable
pm1004mAlmdfrmAlmTable = _Pm1004mAlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm1004mAlmdfrmAlmTable.setStatus("current")
_Pm1004mAlmdfrmAlmEntry_Object = MibTableRow
pm1004mAlmdfrmAlmEntry = _Pm1004mAlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 128, 1)
)
pm1004mAlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmdfrmAlmEntry.setStatus("current")


class _Pm1004mAlmdfrmAlmIndex_Type(Integer32):
    """Custom type pm1004mAlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pm1004mAlmdfrmAlmIndex_Object = MibTableColumn
pm1004mAlmdfrmAlmIndex = _Pm1004mAlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 128, 1, 1),
    _Pm1004mAlmdfrmAlmIndex_Type()
)
pm1004mAlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmdfrmAlmIndex.setStatus("current")
_Pm1004mAlmDwAisDetPortn_Type = EkiOnOff
_Pm1004mAlmDwAisDetPortn_Object = MibTableColumn
pm1004mAlmDwAisDetPortn = _Pm1004mAlmDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 128, 1, 2),
    _Pm1004mAlmDwAisDetPortn_Type()
)
pm1004mAlmDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwAisDetPortn.setStatus("current")
_Pm1004mAlmDwRdiDetPortn_Type = EkiOnOff
_Pm1004mAlmDwRdiDetPortn_Object = MibTableColumn
pm1004mAlmDwRdiDetPortn = _Pm1004mAlmDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 128, 1, 3),
    _Pm1004mAlmDwRdiDetPortn_Type()
)
pm1004mAlmDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwRdiDetPortn.setStatus("current")
_Pm1004mAlmDwOofPortn_Type = EkiOnOff
_Pm1004mAlmDwOofPortn_Object = MibTableColumn
pm1004mAlmDwOofPortn = _Pm1004mAlmDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 128, 1, 4),
    _Pm1004mAlmDwOofPortn_Type()
)
pm1004mAlmDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwOofPortn.setStatus("current")
_Pm1004mAlmDwLofPortn_Type = EkiOnOff
_Pm1004mAlmDwLofPortn_Object = MibTableColumn
pm1004mAlmDwLofPortn = _Pm1004mAlmDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 128, 1, 5),
    _Pm1004mAlmDwLofPortn_Type()
)
pm1004mAlmDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwLofPortn.setStatus("current")
_Pm1004mAlmlineSyncAlarmsTable_Object = MibTable
pm1004mAlmlineSyncAlarmsTable = _Pm1004mAlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pm1004mAlmlineSyncAlarmsTable.setStatus("current")
_Pm1004mAlmlineSyncAlarmsEntry_Object = MibTableRow
pm1004mAlmlineSyncAlarmsEntry = _Pm1004mAlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 133, 1)
)
pm1004mAlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmlineSyncAlarmsEntry.setStatus("current")


class _Pm1004mAlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pm1004mAlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004mAlmlineSyncAlarmsIndex_Object = MibTableColumn
pm1004mAlmlineSyncAlarmsIndex = _Pm1004mAlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 133, 1, 1),
    _Pm1004mAlmlineSyncAlarmsIndex_Type()
)
pm1004mAlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmlineSyncAlarmsIndex.setStatus("current")
_Pm1004mAlmDwLockerrPortn_Type = EkiOnOff
_Pm1004mAlmDwLockerrPortn_Object = MibTableColumn
pm1004mAlmDwLockerrPortn = _Pm1004mAlmDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 133, 1, 13),
    _Pm1004mAlmDwLockerrPortn_Type()
)
pm1004mAlmDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwLockerrPortn.setStatus("current")
_Pm1004mAlmUpLockerrPortn_Type = EkiOnOff
_Pm1004mAlmUpLockerrPortn_Object = MibTableColumn
pm1004mAlmUpLockerrPortn = _Pm1004mAlmUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 133, 1, 14),
    _Pm1004mAlmUpLockerrPortn_Type()
)
pm1004mAlmUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmUpLockerrPortn.setStatus("current")
_Pm1004mAlmDwLosPortn_Type = EkiOnOff
_Pm1004mAlmDwLosPortn_Object = MibTableColumn
pm1004mAlmDwLosPortn = _Pm1004mAlmDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 133, 1, 17),
    _Pm1004mAlmDwLosPortn_Type()
)
pm1004mAlmDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmDwLosPortn.setStatus("current")
_Pm1004mAlmlineXfp1AlarmsTable_Object = MibTable
pm1004mAlmlineXfp1AlarmsTable = _Pm1004mAlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1AlarmsTable.setStatus("current")
_Pm1004mAlmlineXfp1AlarmsEntry_Object = MibTableRow
pm1004mAlmlineXfp1AlarmsEntry = _Pm1004mAlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1)
)
pm1004mAlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1AlarmsEntry.setStatus("current")


class _Pm1004mAlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pm1004mAlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pm1004mAlmlineXfp1AlarmsIndex_Object = MibTableColumn
pm1004mAlmlineXfp1AlarmsIndex = _Pm1004mAlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 1),
    _Pm1004mAlmlineXfp1AlarmsIndex_Type()
)
pm1004mAlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmlineXfp1AlarmsIndex.setStatus("current")
_Pm1004mAlmModNrPortn_Type = EkiOnOff
_Pm1004mAlmModNrPortn_Object = MibTableColumn
pm1004mAlmModNrPortn = _Pm1004mAlmModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 3),
    _Pm1004mAlmModNrPortn_Type()
)
pm1004mAlmModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmModNrPortn.setStatus("current")
_Pm1004mAlmRxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004mAlmRxCdrNotLockedPortn_Object = MibTableColumn
pm1004mAlmRxCdrNotLockedPortn = _Pm1004mAlmRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 4),
    _Pm1004mAlmRxCdrNotLockedPortn_Type()
)
pm1004mAlmRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxCdrNotLockedPortn.setStatus("current")
_Pm1004mAlmRxNrPortn_Type = EkiOnOff
_Pm1004mAlmRxNrPortn_Object = MibTableColumn
pm1004mAlmRxNrPortn = _Pm1004mAlmRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 6),
    _Pm1004mAlmRxNrPortn_Type()
)
pm1004mAlmRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmRxNrPortn.setStatus("current")
_Pm1004mAlmTxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004mAlmTxCdrNotLockedPortn_Object = MibTableColumn
pm1004mAlmTxCdrNotLockedPortn = _Pm1004mAlmTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 7),
    _Pm1004mAlmTxCdrNotLockedPortn_Type()
)
pm1004mAlmTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxCdrNotLockedPortn.setStatus("current")
_Pm1004mAlmTxFaultPortn_Type = EkiOnOff
_Pm1004mAlmTxFaultPortn_Object = MibTableColumn
pm1004mAlmTxFaultPortn = _Pm1004mAlmTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 8),
    _Pm1004mAlmTxFaultPortn_Type()
)
pm1004mAlmTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxFaultPortn.setStatus("current")
_Pm1004mAlmTxNrPortn_Type = EkiOnOff
_Pm1004mAlmTxNrPortn_Object = MibTableColumn
pm1004mAlmTxNrPortn = _Pm1004mAlmTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 9),
    _Pm1004mAlmTxNrPortn_Type()
)
pm1004mAlmTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTxNrPortn.setStatus("current")
_Pm1004mAlmWavelengthUnlockedPortn_Type = EkiOnOff
_Pm1004mAlmWavelengthUnlockedPortn_Object = MibTableColumn
pm1004mAlmWavelengthUnlockedPortn = _Pm1004mAlmWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 15),
    _Pm1004mAlmWavelengthUnlockedPortn_Type()
)
pm1004mAlmWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmWavelengthUnlockedPortn.setStatus("current")
_Pm1004mAlmTecFaultPortn_Type = EkiOnOff
_Pm1004mAlmTecFaultPortn_Object = MibTableColumn
pm1004mAlmTecFaultPortn = _Pm1004mAlmTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 16),
    _Pm1004mAlmTecFaultPortn_Type()
)
pm1004mAlmTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmTecFaultPortn.setStatus("current")
_Pm1004mAlmApdSupplyFaultPortn_Type = EkiOnOff
_Pm1004mAlmApdSupplyFaultPortn_Object = MibTableColumn
pm1004mAlmApdSupplyFaultPortn = _Pm1004mAlmApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 2, 3, 3, 211, 1, 17),
    _Pm1004mAlmApdSupplyFaultPortn_Type()
)
pm1004mAlmApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmApdSupplyFaultPortn.setStatus("current")
_Pm1004mmeasures_ObjectIdentity = ObjectIdentity
pm1004mmeasures = _Pm1004mmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3)
)
_Pm1004mMesrOther_ObjectIdentity = ObjectIdentity
pm1004mMesrOther = _Pm1004mMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 1)
)
_Pm1004mMesrsynth0_Type = EkiMeasureType
_Pm1004mMesrsynth0_Object = MibScalar
pm1004mMesrsynth0 = _Pm1004mMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 1, 0),
    _Pm1004mMesrsynth0_Type()
)
pm1004mMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrsynth0.setStatus("deprecated")
_Pm1004mMesrsynth1_Type = EkiMeasureType
_Pm1004mMesrsynth1_Object = MibScalar
pm1004mMesrsynth1 = _Pm1004mMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 1, 1),
    _Pm1004mMesrsynth1_Type()
)
pm1004mMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrsynth1.setStatus("deprecated")
_Pm1004mMesrClient_ObjectIdentity = ObjectIdentity
pm1004mMesrClient = _Pm1004mMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2)
)
_Pm1004mMesrtempMeasTable_Object = MibTable
pm1004mMesrtempMeasTable = _Pm1004mMesrtempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004mMesrtempMeasTable.setStatus("current")
_Pm1004mMesrtempMeasEntry_Object = MibTableRow
pm1004mMesrtempMeasEntry = _Pm1004mMesrtempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 16, 1)
)
pm1004mMesrtempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrtempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrtempMeasEntry.setStatus("current")


class _Pm1004mMesrtempMeasIndex_Type(Integer32):
    """Custom type pm1004mMesrtempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrtempMeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrtempMeasIndex_Object = MibTableColumn
pm1004mMesrtempMeasIndex = _Pm1004mMesrtempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 16, 1, 1),
    _Pm1004mMesrtempMeasIndex_Type()
)
pm1004mMesrtempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrtempMeasIndex.setStatus("current")


class _Pm1004mMesrtempMeasPortn_Type(Integer32):
    """Custom type pm1004mMesrtempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrtempMeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrtempMeasPortn_Object = MibTableColumn
pm1004mMesrtempMeasPortn = _Pm1004mMesrtempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 16, 1, 2),
    _Pm1004mMesrtempMeasPortn_Type()
)
pm1004mMesrtempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrtempMeasPortn.setStatus("current")
_Pm1004mMesrvoltMeasTable_Object = MibTable
pm1004mMesrvoltMeasTable = _Pm1004mMesrvoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm1004mMesrvoltMeasTable.setStatus("current")
_Pm1004mMesrvoltMeasEntry_Object = MibTableRow
pm1004mMesrvoltMeasEntry = _Pm1004mMesrvoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 24, 1)
)
pm1004mMesrvoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrvoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrvoltMeasEntry.setStatus("current")


class _Pm1004mMesrvoltMeasIndex_Type(Integer32):
    """Custom type pm1004mMesrvoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrvoltMeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrvoltMeasIndex_Object = MibTableColumn
pm1004mMesrvoltMeasIndex = _Pm1004mMesrvoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 24, 1, 1),
    _Pm1004mMesrvoltMeasIndex_Type()
)
pm1004mMesrvoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrvoltMeasIndex.setStatus("current")


class _Pm1004mMesrvoltMeasPortn_Type(Integer32):
    """Custom type pm1004mMesrvoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrvoltMeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrvoltMeasPortn_Object = MibTableColumn
pm1004mMesrvoltMeasPortn = _Pm1004mMesrvoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 24, 1, 2),
    _Pm1004mMesrvoltMeasPortn_Type()
)
pm1004mMesrvoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrvoltMeasPortn.setStatus("current")
_Pm1004mMesrbiasMeasTable_Object = MibTable
pm1004mMesrbiasMeasTable = _Pm1004mMesrbiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004mMesrbiasMeasTable.setStatus("current")
_Pm1004mMesrbiasMeasEntry_Object = MibTableRow
pm1004mMesrbiasMeasEntry = _Pm1004mMesrbiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 32, 1)
)
pm1004mMesrbiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrbiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrbiasMeasEntry.setStatus("current")


class _Pm1004mMesrbiasMeasIndex_Type(Integer32):
    """Custom type pm1004mMesrbiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrbiasMeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrbiasMeasIndex_Object = MibTableColumn
pm1004mMesrbiasMeasIndex = _Pm1004mMesrbiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 32, 1, 1),
    _Pm1004mMesrbiasMeasIndex_Type()
)
pm1004mMesrbiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrbiasMeasIndex.setStatus("current")


class _Pm1004mMesrbiasMeasPortn_Type(Integer32):
    """Custom type pm1004mMesrbiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrbiasMeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrbiasMeasPortn_Object = MibTableColumn
pm1004mMesrbiasMeasPortn = _Pm1004mMesrbiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 32, 1, 2),
    _Pm1004mMesrbiasMeasPortn_Type()
)
pm1004mMesrbiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrbiasMeasPortn.setStatus("current")
_Pm1004mMesrtxpwrMeasTable_Object = MibTable
pm1004mMesrtxpwrMeasTable = _Pm1004mMesrtxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm1004mMesrtxpwrMeasTable.setStatus("current")
_Pm1004mMesrtxpwrMeasEntry_Object = MibTableRow
pm1004mMesrtxpwrMeasEntry = _Pm1004mMesrtxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 40, 1)
)
pm1004mMesrtxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrtxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrtxpwrMeasEntry.setStatus("current")


class _Pm1004mMesrtxpwrMeasIndex_Type(Integer32):
    """Custom type pm1004mMesrtxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrtxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrtxpwrMeasIndex_Object = MibTableColumn
pm1004mMesrtxpwrMeasIndex = _Pm1004mMesrtxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 40, 1, 1),
    _Pm1004mMesrtxpwrMeasIndex_Type()
)
pm1004mMesrtxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrtxpwrMeasIndex.setStatus("current")


class _Pm1004mMesrtxpwrMeasPortn_Type(Integer32):
    """Custom type pm1004mMesrtxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrtxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrtxpwrMeasPortn_Object = MibTableColumn
pm1004mMesrtxpwrMeasPortn = _Pm1004mMesrtxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 40, 1, 2),
    _Pm1004mMesrtxpwrMeasPortn_Type()
)
pm1004mMesrtxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrtxpwrMeasPortn.setStatus("current")
_Pm1004mMesrrxpwrMeasTable_Object = MibTable
pm1004mMesrrxpwrMeasTable = _Pm1004mMesrrxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm1004mMesrrxpwrMeasTable.setStatus("current")
_Pm1004mMesrrxpwrMeasEntry_Object = MibTableRow
pm1004mMesrrxpwrMeasEntry = _Pm1004mMesrrxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 48, 1)
)
pm1004mMesrrxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrrxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrrxpwrMeasEntry.setStatus("current")


class _Pm1004mMesrrxpwrMeasIndex_Type(Integer32):
    """Custom type pm1004mMesrrxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrrxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrrxpwrMeasIndex_Object = MibTableColumn
pm1004mMesrrxpwrMeasIndex = _Pm1004mMesrrxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 48, 1, 1),
    _Pm1004mMesrrxpwrMeasIndex_Type()
)
pm1004mMesrrxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrrxpwrMeasIndex.setStatus("current")


class _Pm1004mMesrrxpwrMeasPortn_Type(Integer32):
    """Custom type pm1004mMesrrxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrrxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrrxpwrMeasPortn_Object = MibTableColumn
pm1004mMesrrxpwrMeasPortn = _Pm1004mMesrrxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 2, 48, 1, 2),
    _Pm1004mMesrrxpwrMeasPortn_Type()
)
pm1004mMesrrxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrrxpwrMeasPortn.setStatus("current")
_Pm1004mMesrLine_ObjectIdentity = ObjectIdentity
pm1004mMesrLine = _Pm1004mMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3)
)
_Pm1004mMesrxfp1LxModTempMeasTable_Object = MibTable
pm1004mMesrxfp1LxModTempMeasTable = _Pm1004mMesrxfp1LxModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxModTempMeasTable.setStatus("current")
_Pm1004mMesrxfp1LxModTempMeasEntry_Object = MibTableRow
pm1004mMesrxfp1LxModTempMeasEntry = _Pm1004mMesrxfp1LxModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 208, 1)
)
pm1004mMesrxfp1LxModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrxfp1LxModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxModTempMeasEntry.setStatus("current")


class _Pm1004mMesrxfp1LxModTempMeasIndex_Type(Integer32):
    """Custom type pm1004mMesrxfp1LxModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrxfp1LxModTempMeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LxModTempMeasIndex_Object = MibTableColumn
pm1004mMesrxfp1LxModTempMeasIndex = _Pm1004mMesrxfp1LxModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 208, 1, 1),
    _Pm1004mMesrxfp1LxModTempMeasIndex_Type()
)
pm1004mMesrxfp1LxModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxModTempMeasIndex.setStatus("current")


class _Pm1004mMesrxfp1LxModTempMeasPortn_Type(Integer32):
    """Custom type pm1004mMesrxfp1LxModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrxfp1LxModTempMeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LxModTempMeasPortn_Object = MibTableColumn
pm1004mMesrxfp1LxModTempMeasPortn = _Pm1004mMesrxfp1LxModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 208, 1, 2),
    _Pm1004mMesrxfp1LxModTempMeasPortn_Type()
)
pm1004mMesrxfp1LxModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxModTempMeasPortn.setStatus("current")
_Pm1004mMesrxfp1ReservedTable_Object = MibTable
pm1004mMesrxfp1ReservedTable = _Pm1004mMesrxfp1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1ReservedTable.setStatus("deprecated")
_Pm1004mMesrxfp1ReservedEntry_Object = MibTableRow
pm1004mMesrxfp1ReservedEntry = _Pm1004mMesrxfp1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 209, 1)
)
pm1004mMesrxfp1ReservedEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrxfp1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1ReservedEntry.setStatus("deprecated")


class _Pm1004mMesrxfp1ReservedIndex_Type(Integer32):
    """Custom type pm1004mMesrxfp1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrxfp1ReservedIndex_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1ReservedIndex_Object = MibTableColumn
pm1004mMesrxfp1ReservedIndex = _Pm1004mMesrxfp1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 209, 1, 1),
    _Pm1004mMesrxfp1ReservedIndex_Type()
)
pm1004mMesrxfp1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1ReservedIndex.setStatus("deprecated")


class _Pm1004mMesrxfp1ReservedPortn_Type(Integer32):
    """Custom type pm1004mMesrxfp1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrxfp1ReservedPortn_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1ReservedPortn_Object = MibTableColumn
pm1004mMesrxfp1ReservedPortn = _Pm1004mMesrxfp1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 209, 1, 2),
    _Pm1004mMesrxfp1ReservedPortn_Type()
)
pm1004mMesrxfp1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1ReservedPortn.setStatus("deprecated")
_Pm1004mMesrxfp1LoBiasCurrentMeasTable_Object = MibTable
pm1004mMesrxfp1LoBiasCurrentMeasTable = _Pm1004mMesrxfp1LoBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LoBiasCurrentMeasTable.setStatus("current")
_Pm1004mMesrxfp1LoBiasCurrentMeasEntry_Object = MibTableRow
pm1004mMesrxfp1LoBiasCurrentMeasEntry = _Pm1004mMesrxfp1LoBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 210, 1)
)
pm1004mMesrxfp1LoBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrxfp1LoBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LoBiasCurrentMeasEntry.setStatus("current")


class _Pm1004mMesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pm1004mMesrxfp1LoBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrxfp1LoBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LoBiasCurrentMeasIndex_Object = MibTableColumn
pm1004mMesrxfp1LoBiasCurrentMeasIndex = _Pm1004mMesrxfp1LoBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 210, 1, 1),
    _Pm1004mMesrxfp1LoBiasCurrentMeasIndex_Type()
)
pm1004mMesrxfp1LoBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LoBiasCurrentMeasIndex.setStatus("current")


class _Pm1004mMesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pm1004mMesrxfp1LoBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrxfp1LoBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LoBiasCurrentMeasPortn_Object = MibTableColumn
pm1004mMesrxfp1LoBiasCurrentMeasPortn = _Pm1004mMesrxfp1LoBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 210, 1, 2),
    _Pm1004mMesrxfp1LoBiasCurrentMeasPortn_Type()
)
pm1004mMesrxfp1LoBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LoBiasCurrentMeasPortn.setStatus("current")
_Pm1004mMesrxfp1LoTxPowerMeasTable_Object = MibTable
pm1004mMesrxfp1LoTxPowerMeasTable = _Pm1004mMesrxfp1LoTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LoTxPowerMeasTable.setStatus("current")
_Pm1004mMesrxfp1LoTxPowerMeasEntry_Object = MibTableRow
pm1004mMesrxfp1LoTxPowerMeasEntry = _Pm1004mMesrxfp1LoTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 211, 1)
)
pm1004mMesrxfp1LoTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrxfp1LoTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LoTxPowerMeasEntry.setStatus("current")


class _Pm1004mMesrxfp1LoTxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004mMesrxfp1LoTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrxfp1LoTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LoTxPowerMeasIndex_Object = MibTableColumn
pm1004mMesrxfp1LoTxPowerMeasIndex = _Pm1004mMesrxfp1LoTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 211, 1, 1),
    _Pm1004mMesrxfp1LoTxPowerMeasIndex_Type()
)
pm1004mMesrxfp1LoTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LoTxPowerMeasIndex.setStatus("current")


class _Pm1004mMesrxfp1LoTxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004mMesrxfp1LoTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrxfp1LoTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LoTxPowerMeasPortn_Object = MibTableColumn
pm1004mMesrxfp1LoTxPowerMeasPortn = _Pm1004mMesrxfp1LoTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 211, 1, 2),
    _Pm1004mMesrxfp1LoTxPowerMeasPortn_Type()
)
pm1004mMesrxfp1LoTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LoTxPowerMeasPortn.setStatus("current")
_Pm1004mMesrxfp1LiRxPowerMeasTable_Object = MibTable
pm1004mMesrxfp1LiRxPowerMeasTable = _Pm1004mMesrxfp1LiRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LiRxPowerMeasTable.setStatus("current")
_Pm1004mMesrxfp1LiRxPowerMeasEntry_Object = MibTableRow
pm1004mMesrxfp1LiRxPowerMeasEntry = _Pm1004mMesrxfp1LiRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 212, 1)
)
pm1004mMesrxfp1LiRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrxfp1LiRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LiRxPowerMeasEntry.setStatus("current")


class _Pm1004mMesrxfp1LiRxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004mMesrxfp1LiRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrxfp1LiRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LiRxPowerMeasIndex_Object = MibTableColumn
pm1004mMesrxfp1LiRxPowerMeasIndex = _Pm1004mMesrxfp1LiRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 212, 1, 1),
    _Pm1004mMesrxfp1LiRxPowerMeasIndex_Type()
)
pm1004mMesrxfp1LiRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LiRxPowerMeasIndex.setStatus("current")


class _Pm1004mMesrxfp1LiRxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004mMesrxfp1LiRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrxfp1LiRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LiRxPowerMeasPortn_Object = MibTableColumn
pm1004mMesrxfp1LiRxPowerMeasPortn = _Pm1004mMesrxfp1LiRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 212, 1, 2),
    _Pm1004mMesrxfp1LiRxPowerMeasPortn_Type()
)
pm1004mMesrxfp1LiRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LiRxPowerMeasPortn.setStatus("current")
_Pm1004mMesrxfp1LxAux1MeasTable_Object = MibTable
pm1004mMesrxfp1LxAux1MeasTable = _Pm1004mMesrxfp1LxAux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxAux1MeasTable.setStatus("deprecated")
_Pm1004mMesrxfp1LxAux1MeasEntry_Object = MibTableRow
pm1004mMesrxfp1LxAux1MeasEntry = _Pm1004mMesrxfp1LxAux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 213, 1)
)
pm1004mMesrxfp1LxAux1MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrxfp1LxAux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxAux1MeasEntry.setStatus("deprecated")


class _Pm1004mMesrxfp1LxAux1MeasIndex_Type(Integer32):
    """Custom type pm1004mMesrxfp1LxAux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrxfp1LxAux1MeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LxAux1MeasIndex_Object = MibTableColumn
pm1004mMesrxfp1LxAux1MeasIndex = _Pm1004mMesrxfp1LxAux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 213, 1, 1),
    _Pm1004mMesrxfp1LxAux1MeasIndex_Type()
)
pm1004mMesrxfp1LxAux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxAux1MeasIndex.setStatus("deprecated")


class _Pm1004mMesrxfp1LxAux1MeasPortn_Type(Integer32):
    """Custom type pm1004mMesrxfp1LxAux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrxfp1LxAux1MeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LxAux1MeasPortn_Object = MibTableColumn
pm1004mMesrxfp1LxAux1MeasPortn = _Pm1004mMesrxfp1LxAux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 213, 1, 2),
    _Pm1004mMesrxfp1LxAux1MeasPortn_Type()
)
pm1004mMesrxfp1LxAux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxAux1MeasPortn.setStatus("deprecated")
_Pm1004mMesrxfp1LxAux2MeasTable_Object = MibTable
pm1004mMesrxfp1LxAux2MeasTable = _Pm1004mMesrxfp1LxAux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxAux2MeasTable.setStatus("deprecated")
_Pm1004mMesrxfp1LxAux2MeasEntry_Object = MibTableRow
pm1004mMesrxfp1LxAux2MeasEntry = _Pm1004mMesrxfp1LxAux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 214, 1)
)
pm1004mMesrxfp1LxAux2MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrxfp1LxAux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxAux2MeasEntry.setStatus("deprecated")


class _Pm1004mMesrxfp1LxAux2MeasIndex_Type(Integer32):
    """Custom type pm1004mMesrxfp1LxAux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrxfp1LxAux2MeasIndex_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LxAux2MeasIndex_Object = MibTableColumn
pm1004mMesrxfp1LxAux2MeasIndex = _Pm1004mMesrxfp1LxAux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 214, 1, 1),
    _Pm1004mMesrxfp1LxAux2MeasIndex_Type()
)
pm1004mMesrxfp1LxAux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxAux2MeasIndex.setStatus("deprecated")


class _Pm1004mMesrxfp1LxAux2MeasPortn_Type(Integer32):
    """Custom type pm1004mMesrxfp1LxAux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrxfp1LxAux2MeasPortn_Type.__name__ = "Integer32"
_Pm1004mMesrxfp1LxAux2MeasPortn_Object = MibTableColumn
pm1004mMesrxfp1LxAux2MeasPortn = _Pm1004mMesrxfp1LxAux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 214, 1, 2),
    _Pm1004mMesrxfp1LxAux2MeasPortn_Type()
)
pm1004mMesrxfp1LxAux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrxfp1LxAux2MeasPortn.setStatus("deprecated")
_Pm1004mMesrotx1AgingTable_Object = MibTable
pm1004mMesrotx1AgingTable = _Pm1004mMesrotx1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pm1004mMesrotx1AgingTable.setStatus("current")
_Pm1004mMesrotx1AgingEntry_Object = MibTableRow
pm1004mMesrotx1AgingEntry = _Pm1004mMesrotx1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 224, 1)
)
pm1004mMesrotx1AgingEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrotx1AgingIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrotx1AgingEntry.setStatus("current")


class _Pm1004mMesrotx1AgingIndex_Type(Integer32):
    """Custom type pm1004mMesrotx1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrotx1AgingIndex_Type.__name__ = "Integer32"
_Pm1004mMesrotx1AgingIndex_Object = MibTableColumn
pm1004mMesrotx1AgingIndex = _Pm1004mMesrotx1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 224, 1, 1),
    _Pm1004mMesrotx1AgingIndex_Type()
)
pm1004mMesrotx1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrotx1AgingIndex.setStatus("current")


class _Pm1004mMesrotx1AgingPortn_Type(Integer32):
    """Custom type pm1004mMesrotx1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrotx1AgingPortn_Type.__name__ = "Integer32"
_Pm1004mMesrotx1AgingPortn_Object = MibTableColumn
pm1004mMesrotx1AgingPortn = _Pm1004mMesrotx1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 224, 1, 2),
    _Pm1004mMesrotx1AgingPortn_Type()
)
pm1004mMesrotx1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrotx1AgingPortn.setStatus("current")
_Pm1004mMesrotx1LaserTemperatureTable_Object = MibTable
pm1004mMesrotx1LaserTemperatureTable = _Pm1004mMesrotx1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pm1004mMesrotx1LaserTemperatureTable.setStatus("deprecated")
_Pm1004mMesrotx1LaserTemperatureEntry_Object = MibTableRow
pm1004mMesrotx1LaserTemperatureEntry = _Pm1004mMesrotx1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 225, 1)
)
pm1004mMesrotx1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrotx1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrotx1LaserTemperatureEntry.setStatus("deprecated")


class _Pm1004mMesrotx1LaserTemperatureIndex_Type(Integer32):
    """Custom type pm1004mMesrotx1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrotx1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pm1004mMesrotx1LaserTemperatureIndex_Object = MibTableColumn
pm1004mMesrotx1LaserTemperatureIndex = _Pm1004mMesrotx1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 225, 1, 1),
    _Pm1004mMesrotx1LaserTemperatureIndex_Type()
)
pm1004mMesrotx1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrotx1LaserTemperatureIndex.setStatus("deprecated")


class _Pm1004mMesrotx1LaserTemperaturePortn_Type(Integer32):
    """Custom type pm1004mMesrotx1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrotx1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pm1004mMesrotx1LaserTemperaturePortn_Object = MibTableColumn
pm1004mMesrotx1LaserTemperaturePortn = _Pm1004mMesrotx1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 225, 1, 2),
    _Pm1004mMesrotx1LaserTemperaturePortn_Type()
)
pm1004mMesrotx1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrotx1LaserTemperaturePortn.setStatus("deprecated")
_Pm1004mMesrotx1FreqDeviationTable_Object = MibTable
pm1004mMesrotx1FreqDeviationTable = _Pm1004mMesrotx1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pm1004mMesrotx1FreqDeviationTable.setStatus("current")
_Pm1004mMesrotx1FreqDeviationEntry_Object = MibTableRow
pm1004mMesrotx1FreqDeviationEntry = _Pm1004mMesrotx1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 226, 1)
)
pm1004mMesrotx1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrotx1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrotx1FreqDeviationEntry.setStatus("current")


class _Pm1004mMesrotx1FreqDeviationIndex_Type(Integer32):
    """Custom type pm1004mMesrotx1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrotx1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pm1004mMesrotx1FreqDeviationIndex_Object = MibTableColumn
pm1004mMesrotx1FreqDeviationIndex = _Pm1004mMesrotx1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 226, 1, 1),
    _Pm1004mMesrotx1FreqDeviationIndex_Type()
)
pm1004mMesrotx1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrotx1FreqDeviationIndex.setStatus("current")


class _Pm1004mMesrotx1FreqDeviationPortn_Type(Integer32):
    """Custom type pm1004mMesrotx1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrotx1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pm1004mMesrotx1FreqDeviationPortn_Object = MibTableColumn
pm1004mMesrotx1FreqDeviationPortn = _Pm1004mMesrotx1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 226, 1, 2),
    _Pm1004mMesrotx1FreqDeviationPortn_Type()
)
pm1004mMesrotx1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrotx1FreqDeviationPortn.setStatus("current")
_Pm1004mMesrotx1LaserWvlengthTable_Object = MibTable
pm1004mMesrotx1LaserWvlengthTable = _Pm1004mMesrotx1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pm1004mMesrotx1LaserWvlengthTable.setStatus("current")
_Pm1004mMesrotx1LaserWvlengthEntry_Object = MibTableRow
pm1004mMesrotx1LaserWvlengthEntry = _Pm1004mMesrotx1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 227, 1)
)
pm1004mMesrotx1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mMesrotx1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pm1004mMesrotx1LaserWvlengthEntry.setStatus("current")


class _Pm1004mMesrotx1LaserWvlengthIndex_Type(Integer32):
    """Custom type pm1004mMesrotx1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mMesrotx1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pm1004mMesrotx1LaserWvlengthIndex_Object = MibTableColumn
pm1004mMesrotx1LaserWvlengthIndex = _Pm1004mMesrotx1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 227, 1, 1),
    _Pm1004mMesrotx1LaserWvlengthIndex_Type()
)
pm1004mMesrotx1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrotx1LaserWvlengthIndex.setStatus("current")


class _Pm1004mMesrotx1LaserWvlengthPortn_Type(Integer32):
    """Custom type pm1004mMesrotx1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004mMesrotx1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pm1004mMesrotx1LaserWvlengthPortn_Object = MibTableColumn
pm1004mMesrotx1LaserWvlengthPortn = _Pm1004mMesrotx1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 3, 3, 227, 1, 2),
    _Pm1004mMesrotx1LaserWvlengthPortn_Type()
)
pm1004mMesrotx1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mMesrotx1LaserWvlengthPortn.setStatus("current")
_Pm1004mcounters_ObjectIdentity = ObjectIdentity
pm1004mcounters = _Pm1004mcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4)
)
_Pm1004mCntOther_ObjectIdentity = ObjectIdentity
pm1004mCntOther = _Pm1004mCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 1)
)
_Pm1004mCntClient_ObjectIdentity = ObjectIdentity
pm1004mCntClient = _Pm1004mCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2)
)
_Pm1004mCntupRaRemCntTable_Object = MibTable
pm1004mCntupRaRemCntTable = _Pm1004mCntupRaRemCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004mCntupRaRemCntTable.setStatus("current")
_Pm1004mCntupRaRemCntEntry_Object = MibTableRow
pm1004mCntupRaRemCntEntry = _Pm1004mCntupRaRemCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 16, 1)
)
pm1004mCntupRaRemCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCntupRaRemCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCntupRaRemCntEntry.setStatus("current")


class _Pm1004mCntupRaRemCntIndex_Type(Integer32):
    """Custom type pm1004mCntupRaRemCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCntupRaRemCntIndex_Type.__name__ = "Integer32"
_Pm1004mCntupRaRemCntIndex_Object = MibTableColumn
pm1004mCntupRaRemCntIndex = _Pm1004mCntupRaRemCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 16, 1, 1),
    _Pm1004mCntupRaRemCntIndex_Type()
)
pm1004mCntupRaRemCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRaRemCntIndex.setStatus("current")
_Pm1004mCntupRaRemCntValuePortn_Type = Counter32
_Pm1004mCntupRaRemCntValuePortn_Object = MibTableColumn
pm1004mCntupRaRemCntValuePortn = _Pm1004mCntupRaRemCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 16, 1, 2),
    _Pm1004mCntupRaRemCntValuePortn_Type()
)
pm1004mCntupRaRemCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRaRemCntValuePortn.setStatus("current")
_Pm1004mCntupRaRemCntErrorPortn_Type = EkiOnOff
_Pm1004mCntupRaRemCntErrorPortn_Object = MibTableColumn
pm1004mCntupRaRemCntErrorPortn = _Pm1004mCntupRaRemCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 16, 1, 3),
    _Pm1004mCntupRaRemCntErrorPortn_Type()
)
pm1004mCntupRaRemCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRaRemCntErrorPortn.setStatus("current")
_Pm1004mCntupRaRemCntOverloadPortn_Type = EkiOnOff
_Pm1004mCntupRaRemCntOverloadPortn_Object = MibTableColumn
pm1004mCntupRaRemCntOverloadPortn = _Pm1004mCntupRaRemCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 16, 1, 4),
    _Pm1004mCntupRaRemCntOverloadPortn_Type()
)
pm1004mCntupRaRemCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRaRemCntOverloadPortn.setStatus("current")
_Pm1004mCntupRaInsCntTable_Object = MibTable
pm1004mCntupRaInsCntTable = _Pm1004mCntupRaInsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 24)
)
if mibBuilder.loadTexts:
    pm1004mCntupRaInsCntTable.setStatus("current")
_Pm1004mCntupRaInsCntEntry_Object = MibTableRow
pm1004mCntupRaInsCntEntry = _Pm1004mCntupRaInsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 24, 1)
)
pm1004mCntupRaInsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCntupRaInsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCntupRaInsCntEntry.setStatus("current")


class _Pm1004mCntupRaInsCntIndex_Type(Integer32):
    """Custom type pm1004mCntupRaInsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCntupRaInsCntIndex_Type.__name__ = "Integer32"
_Pm1004mCntupRaInsCntIndex_Object = MibTableColumn
pm1004mCntupRaInsCntIndex = _Pm1004mCntupRaInsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 24, 1, 1),
    _Pm1004mCntupRaInsCntIndex_Type()
)
pm1004mCntupRaInsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRaInsCntIndex.setStatus("current")
_Pm1004mCntupRaInsCntValuePortn_Type = Counter32
_Pm1004mCntupRaInsCntValuePortn_Object = MibTableColumn
pm1004mCntupRaInsCntValuePortn = _Pm1004mCntupRaInsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 24, 1, 2),
    _Pm1004mCntupRaInsCntValuePortn_Type()
)
pm1004mCntupRaInsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRaInsCntValuePortn.setStatus("current")
_Pm1004mCntupRaInsCntErrorPortn_Type = EkiOnOff
_Pm1004mCntupRaInsCntErrorPortn_Object = MibTableColumn
pm1004mCntupRaInsCntErrorPortn = _Pm1004mCntupRaInsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 24, 1, 3),
    _Pm1004mCntupRaInsCntErrorPortn_Type()
)
pm1004mCntupRaInsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRaInsCntErrorPortn.setStatus("current")
_Pm1004mCntupRaInsCntOverloadPortn_Type = EkiOnOff
_Pm1004mCntupRaInsCntOverloadPortn_Object = MibTableColumn
pm1004mCntupRaInsCntOverloadPortn = _Pm1004mCntupRaInsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 24, 1, 4),
    _Pm1004mCntupRaInsCntOverloadPortn_Type()
)
pm1004mCntupRaInsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRaInsCntOverloadPortn.setStatus("current")
_Pm1004mCntupRdErrCntTable_Object = MibTable
pm1004mCntupRdErrCntTable = _Pm1004mCntupRdErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004mCntupRdErrCntTable.setStatus("current")
_Pm1004mCntupRdErrCntEntry_Object = MibTableRow
pm1004mCntupRdErrCntEntry = _Pm1004mCntupRdErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 32, 1)
)
pm1004mCntupRdErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCntupRdErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCntupRdErrCntEntry.setStatus("current")


class _Pm1004mCntupRdErrCntIndex_Type(Integer32):
    """Custom type pm1004mCntupRdErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCntupRdErrCntIndex_Type.__name__ = "Integer32"
_Pm1004mCntupRdErrCntIndex_Object = MibTableColumn
pm1004mCntupRdErrCntIndex = _Pm1004mCntupRdErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 32, 1, 1),
    _Pm1004mCntupRdErrCntIndex_Type()
)
pm1004mCntupRdErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRdErrCntIndex.setStatus("current")
_Pm1004mCntupRdErrCntValuePortn_Type = Counter32
_Pm1004mCntupRdErrCntValuePortn_Object = MibTableColumn
pm1004mCntupRdErrCntValuePortn = _Pm1004mCntupRdErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 32, 1, 2),
    _Pm1004mCntupRdErrCntValuePortn_Type()
)
pm1004mCntupRdErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRdErrCntValuePortn.setStatus("current")
_Pm1004mCntupRdErrCntErrorPortn_Type = EkiOnOff
_Pm1004mCntupRdErrCntErrorPortn_Object = MibTableColumn
pm1004mCntupRdErrCntErrorPortn = _Pm1004mCntupRdErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 32, 1, 3),
    _Pm1004mCntupRdErrCntErrorPortn_Type()
)
pm1004mCntupRdErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRdErrCntErrorPortn.setStatus("current")
_Pm1004mCntupRdErrCntOverloadPortn_Type = EkiOnOff
_Pm1004mCntupRdErrCntOverloadPortn_Object = MibTableColumn
pm1004mCntupRdErrCntOverloadPortn = _Pm1004mCntupRdErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 32, 1, 4),
    _Pm1004mCntupRdErrCntOverloadPortn_Type()
)
pm1004mCntupRdErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupRdErrCntOverloadPortn.setStatus("current")
_Pm1004mCntupTimCntTable_Object = MibTable
pm1004mCntupTimCntTable = _Pm1004mCntupTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 40)
)
if mibBuilder.loadTexts:
    pm1004mCntupTimCntTable.setStatus("current")
_Pm1004mCntupTimCntEntry_Object = MibTableRow
pm1004mCntupTimCntEntry = _Pm1004mCntupTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 40, 1)
)
pm1004mCntupTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCntupTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCntupTimCntEntry.setStatus("current")


class _Pm1004mCntupTimCntIndex_Type(Integer32):
    """Custom type pm1004mCntupTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCntupTimCntIndex_Type.__name__ = "Integer32"
_Pm1004mCntupTimCntIndex_Object = MibTableColumn
pm1004mCntupTimCntIndex = _Pm1004mCntupTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 40, 1, 1),
    _Pm1004mCntupTimCntIndex_Type()
)
pm1004mCntupTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupTimCntIndex.setStatus("current")
_Pm1004mCntupTimCntValuePortn_Type = Counter32
_Pm1004mCntupTimCntValuePortn_Object = MibTableColumn
pm1004mCntupTimCntValuePortn = _Pm1004mCntupTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 40, 1, 2),
    _Pm1004mCntupTimCntValuePortn_Type()
)
pm1004mCntupTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupTimCntValuePortn.setStatus("current")
_Pm1004mCntupTimCntErrorPortn_Type = EkiOnOff
_Pm1004mCntupTimCntErrorPortn_Object = MibTableColumn
pm1004mCntupTimCntErrorPortn = _Pm1004mCntupTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 40, 1, 3),
    _Pm1004mCntupTimCntErrorPortn_Type()
)
pm1004mCntupTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupTimCntErrorPortn.setStatus("current")
_Pm1004mCntupTimCntOverloadPortn_Type = EkiOnOff
_Pm1004mCntupTimCntOverloadPortn_Object = MibTableColumn
pm1004mCntupTimCntOverloadPortn = _Pm1004mCntupTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 40, 1, 4),
    _Pm1004mCntupTimCntOverloadPortn_Type()
)
pm1004mCntupTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupTimCntOverloadPortn.setStatus("current")
_Pm1004mCntupCvErrCntTable_Object = MibTable
pm1004mCntupCvErrCntTable = _Pm1004mCntupCvErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 48)
)
if mibBuilder.loadTexts:
    pm1004mCntupCvErrCntTable.setStatus("current")
_Pm1004mCntupCvErrCntEntry_Object = MibTableRow
pm1004mCntupCvErrCntEntry = _Pm1004mCntupCvErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 48, 1)
)
pm1004mCntupCvErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCntupCvErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCntupCvErrCntEntry.setStatus("current")


class _Pm1004mCntupCvErrCntIndex_Type(Integer32):
    """Custom type pm1004mCntupCvErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCntupCvErrCntIndex_Type.__name__ = "Integer32"
_Pm1004mCntupCvErrCntIndex_Object = MibTableColumn
pm1004mCntupCvErrCntIndex = _Pm1004mCntupCvErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 48, 1, 1),
    _Pm1004mCntupCvErrCntIndex_Type()
)
pm1004mCntupCvErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupCvErrCntIndex.setStatus("current")
_Pm1004mCntupCvErrCntValuePortn_Type = Counter32
_Pm1004mCntupCvErrCntValuePortn_Object = MibTableColumn
pm1004mCntupCvErrCntValuePortn = _Pm1004mCntupCvErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 48, 1, 2),
    _Pm1004mCntupCvErrCntValuePortn_Type()
)
pm1004mCntupCvErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupCvErrCntValuePortn.setStatus("current")
_Pm1004mCntupCvErrCntErrorPortn_Type = EkiOnOff
_Pm1004mCntupCvErrCntErrorPortn_Object = MibTableColumn
pm1004mCntupCvErrCntErrorPortn = _Pm1004mCntupCvErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 48, 1, 3),
    _Pm1004mCntupCvErrCntErrorPortn_Type()
)
pm1004mCntupCvErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupCvErrCntErrorPortn.setStatus("current")
_Pm1004mCntupCvErrCntOverloadPortn_Type = EkiOnOff
_Pm1004mCntupCvErrCntOverloadPortn_Object = MibTableColumn
pm1004mCntupCvErrCntOverloadPortn = _Pm1004mCntupCvErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 48, 1, 4),
    _Pm1004mCntupCvErrCntOverloadPortn_Type()
)
pm1004mCntupCvErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntupCvErrCntOverloadPortn.setStatus("current")
_Pm1004mCntdwTimCntTable_Object = MibTable
pm1004mCntdwTimCntTable = _Pm1004mCntdwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 72)
)
if mibBuilder.loadTexts:
    pm1004mCntdwTimCntTable.setStatus("current")
_Pm1004mCntdwTimCntEntry_Object = MibTableRow
pm1004mCntdwTimCntEntry = _Pm1004mCntdwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 72, 1)
)
pm1004mCntdwTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCntdwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCntdwTimCntEntry.setStatus("current")


class _Pm1004mCntdwTimCntIndex_Type(Integer32):
    """Custom type pm1004mCntdwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCntdwTimCntIndex_Type.__name__ = "Integer32"
_Pm1004mCntdwTimCntIndex_Object = MibTableColumn
pm1004mCntdwTimCntIndex = _Pm1004mCntdwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 72, 1, 1),
    _Pm1004mCntdwTimCntIndex_Type()
)
pm1004mCntdwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdwTimCntIndex.setStatus("current")
_Pm1004mCntdwTimCntValuePortn_Type = Counter32
_Pm1004mCntdwTimCntValuePortn_Object = MibTableColumn
pm1004mCntdwTimCntValuePortn = _Pm1004mCntdwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 72, 1, 2),
    _Pm1004mCntdwTimCntValuePortn_Type()
)
pm1004mCntdwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdwTimCntValuePortn.setStatus("current")
_Pm1004mCntdwTimCntErrorPortn_Type = EkiOnOff
_Pm1004mCntdwTimCntErrorPortn_Object = MibTableColumn
pm1004mCntdwTimCntErrorPortn = _Pm1004mCntdwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 72, 1, 3),
    _Pm1004mCntdwTimCntErrorPortn_Type()
)
pm1004mCntdwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdwTimCntErrorPortn.setStatus("current")
_Pm1004mCntdwTimCntOverloadPortn_Type = EkiOnOff
_Pm1004mCntdwTimCntOverloadPortn_Object = MibTableColumn
pm1004mCntdwTimCntOverloadPortn = _Pm1004mCntdwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 2, 72, 1, 4),
    _Pm1004mCntdwTimCntOverloadPortn_Type()
)
pm1004mCntdwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdwTimCntOverloadPortn.setStatus("current")
_Pm1004mCntLine_ObjectIdentity = ObjectIdentity
pm1004mCntLine = _Pm1004mCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3)
)
_Pm1004mCntdfrmB1ErrCntTable_Object = MibTable
pm1004mCntdfrmB1ErrCntTable = _Pm1004mCntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm1004mCntdfrmB1ErrCntTable.setStatus("current")
_Pm1004mCntdfrmB1ErrCntEntry_Object = MibTableRow
pm1004mCntdfrmB1ErrCntEntry = _Pm1004mCntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 152, 1)
)
pm1004mCntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCntdfrmB1ErrCntEntry.setStatus("current")


class _Pm1004mCntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm1004mCntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm1004mCntdfrmB1ErrCntIndex_Object = MibTableColumn
pm1004mCntdfrmB1ErrCntIndex = _Pm1004mCntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 152, 1, 1),
    _Pm1004mCntdfrmB1ErrCntIndex_Type()
)
pm1004mCntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdfrmB1ErrCntIndex.setStatus("current")
_Pm1004mCntdfrmB1ErrCntValuePortn_Type = Counter32
_Pm1004mCntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pm1004mCntdfrmB1ErrCntValuePortn = _Pm1004mCntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 152, 1, 2),
    _Pm1004mCntdfrmB1ErrCntValuePortn_Type()
)
pm1004mCntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdfrmB1ErrCntValuePortn.setStatus("current")
_Pm1004mCntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm1004mCntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm1004mCntdfrmB1ErrCntErrorPortn = _Pm1004mCntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 152, 1, 3),
    _Pm1004mCntdfrmB1ErrCntErrorPortn_Type()
)
pm1004mCntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pm1004mCntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm1004mCntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm1004mCntdfrmB1ErrCntOverloadPortn = _Pm1004mCntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 152, 1, 4),
    _Pm1004mCntdfrmB1ErrCntOverloadPortn_Type()
)
pm1004mCntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm1004mCntdfrmTimCntTable_Object = MibTable
pm1004mCntdfrmTimCntTable = _Pm1004mCntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm1004mCntdfrmTimCntTable.setStatus("current")
_Pm1004mCntdfrmTimCntEntry_Object = MibTableRow
pm1004mCntdfrmTimCntEntry = _Pm1004mCntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 153, 1)
)
pm1004mCntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCntdfrmTimCntEntry.setStatus("current")


class _Pm1004mCntdfrmTimCntIndex_Type(Integer32):
    """Custom type pm1004mCntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm1004mCntdfrmTimCntIndex_Object = MibTableColumn
pm1004mCntdfrmTimCntIndex = _Pm1004mCntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 153, 1, 1),
    _Pm1004mCntdfrmTimCntIndex_Type()
)
pm1004mCntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdfrmTimCntIndex.setStatus("current")
_Pm1004mCntdfrmTimCntValuePortn_Type = Counter32
_Pm1004mCntdfrmTimCntValuePortn_Object = MibTableColumn
pm1004mCntdfrmTimCntValuePortn = _Pm1004mCntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 153, 1, 2),
    _Pm1004mCntdfrmTimCntValuePortn_Type()
)
pm1004mCntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdfrmTimCntValuePortn.setStatus("current")
_Pm1004mCntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pm1004mCntdfrmTimCntErrorPortn_Object = MibTableColumn
pm1004mCntdfrmTimCntErrorPortn = _Pm1004mCntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 153, 1, 3),
    _Pm1004mCntdfrmTimCntErrorPortn_Type()
)
pm1004mCntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdfrmTimCntErrorPortn.setStatus("current")
_Pm1004mCntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm1004mCntdfrmTimCntOverloadPortn_Object = MibTableColumn
pm1004mCntdfrmTimCntOverloadPortn = _Pm1004mCntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 3, 153, 1, 4),
    _Pm1004mCntdfrmTimCntOverloadPortn_Type()
)
pm1004mCntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCntdfrmTimCntOverloadPortn.setStatus("current")
_Pm1004mCntCountersReset_Type = EkiOnOff
_Pm1004mCntCountersReset_Object = MibScalar
pm1004mCntCountersReset = _Pm1004mCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 259),
    _Pm1004mCntCountersReset_Type()
)
pm1004mCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCntCountersReset.setStatus("current")
_Pm1004mCntCountersStop_Type = EkiOnOff
_Pm1004mCntCountersStop_Object = MibScalar
pm1004mCntCountersStop = _Pm1004mCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 4, 260),
    _Pm1004mCntCountersStop_Type()
)
pm1004mCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCntCountersStop.setStatus("current")
_Pm1004mcontrolsWrite_ObjectIdentity = ObjectIdentity
pm1004mcontrolsWrite = _Pm1004mcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6)
)
_Pm1004mCtrlOther_ObjectIdentity = ObjectIdentity
pm1004mCtrlOther = _Pm1004mCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1)
)
_Pm1004mCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm1004mCtrlconfMgnt1 = _Pm1004mCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 1)
)
_Pm1004mCtrlConf1Load1_Type = EkiOnOff
_Pm1004mCtrlConf1Load1_Object = MibScalar
pm1004mCtrlConf1Load1 = _Pm1004mCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 1, 1),
    _Pm1004mCtrlConf1Load1_Type()
)
pm1004mCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlConf1Load1.setStatus("current")
_Pm1004mCtrlConf2Load1_Type = EkiOnOff
_Pm1004mCtrlConf2Load1_Object = MibScalar
pm1004mCtrlConf2Load1 = _Pm1004mCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 1, 2),
    _Pm1004mCtrlConf2Load1_Type()
)
pm1004mCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlConf2Load1.setStatus("current")
_Pm1004mCtrlConf2Flash1_Type = EkiOnOff
_Pm1004mCtrlConf2Flash1_Object = MibScalar
pm1004mCtrlConf2Flash1 = _Pm1004mCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 1, 10),
    _Pm1004mCtrlConf2Flash1_Type()
)
pm1004mCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlConf2Flash1.setStatus("current")
_Pm1004mCtrlConf2Clear1_Type = EkiOnOff
_Pm1004mCtrlConf2Clear1_Object = MibScalar
pm1004mCtrlConf2Clear1 = _Pm1004mCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 1, 14),
    _Pm1004mCtrlConf2Clear1_Type()
)
pm1004mCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlConf2Clear1.setStatus("current")
_Pm1004mCtrlsynth4_ObjectIdentity = ObjectIdentity
pm1004mCtrlsynth4 = _Pm1004mCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 4)
)
_Pm1004mCtrlCorrelatOn_Type = EkiOnOff
_Pm1004mCtrlCorrelatOn_Object = MibScalar
pm1004mCtrlCorrelatOn = _Pm1004mCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 4, 1),
    _Pm1004mCtrlCorrelatOn_Type()
)
pm1004mCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlCorrelatOn.setStatus("current")
_Pm1004mCtrlCorrelatOff_Type = EkiOnOff
_Pm1004mCtrlCorrelatOff_Object = MibScalar
pm1004mCtrlCorrelatOff = _Pm1004mCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 4, 2),
    _Pm1004mCtrlCorrelatOff_Type()
)
pm1004mCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlCorrelatOff.setStatus("current")
_Pm1004mCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1004mCtrlswMgnt = _Pm1004mCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 5)
)
_Pm1004mCtrlColdReset_Type = EkiOnOff
_Pm1004mCtrlColdReset_Object = MibScalar
pm1004mCtrlColdReset = _Pm1004mCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 5, 2),
    _Pm1004mCtrlColdReset_Type()
)
pm1004mCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlColdReset.setStatus("current")
_Pm1004mCtrlWarmReset_Type = EkiOnOff
_Pm1004mCtrlWarmReset_Object = MibScalar
pm1004mCtrlWarmReset = _Pm1004mCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 5, 3),
    _Pm1004mCtrlWarmReset_Type()
)
pm1004mCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlWarmReset.setStatus("current")
_Pm1004mCtrlLoadSwBank1_Type = EkiOnOff
_Pm1004mCtrlLoadSwBank1_Object = MibScalar
pm1004mCtrlLoadSwBank1 = _Pm1004mCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 5, 5),
    _Pm1004mCtrlLoadSwBank1_Type()
)
pm1004mCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlLoadSwBank1.setStatus("current")
_Pm1004mCtrlLoadSwBank2_Type = EkiOnOff
_Pm1004mCtrlLoadSwBank2_Object = MibScalar
pm1004mCtrlLoadSwBank2 = _Pm1004mCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 5, 6),
    _Pm1004mCtrlLoadSwBank2_Type()
)
pm1004mCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlLoadSwBank2.setStatus("current")
_Pm1004mCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm1004mCtrlgwMgnt = _Pm1004mCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 6)
)
_Pm1004mCtrlCurrentGwReset_Type = EkiOnOff
_Pm1004mCtrlCurrentGwReset_Object = MibScalar
pm1004mCtrlCurrentGwReset = _Pm1004mCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 6, 1),
    _Pm1004mCtrlCurrentGwReset_Type()
)
pm1004mCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlCurrentGwReset.setStatus("current")
_Pm1004mCtrlLoadGwBank1_Type = EkiOnOff
_Pm1004mCtrlLoadGwBank1_Object = MibScalar
pm1004mCtrlLoadGwBank1 = _Pm1004mCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 6, 5),
    _Pm1004mCtrlLoadGwBank1_Type()
)
pm1004mCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlLoadGwBank1.setStatus("current")
_Pm1004mCtrlLoadGwBank2_Type = EkiOnOff
_Pm1004mCtrlLoadGwBank2_Object = MibScalar
pm1004mCtrlLoadGwBank2 = _Pm1004mCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 6, 6),
    _Pm1004mCtrlLoadGwBank2_Type()
)
pm1004mCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlLoadGwBank2.setStatus("current")
_Pm1004mCtrlLoadGwBank3_Type = EkiOnOff
_Pm1004mCtrlLoadGwBank3_Object = MibScalar
pm1004mCtrlLoadGwBank3 = _Pm1004mCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 6, 7),
    _Pm1004mCtrlLoadGwBank3_Type()
)
pm1004mCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlLoadGwBank3.setStatus("current")
_Pm1004mCtrlLoadGwBank4_Type = EkiOnOff
_Pm1004mCtrlLoadGwBank4_Object = MibScalar
pm1004mCtrlLoadGwBank4 = _Pm1004mCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 6, 8),
    _Pm1004mCtrlLoadGwBank4_Type()
)
pm1004mCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlLoadGwBank4.setStatus("current")
_Pm1004mCtrlledTest_ObjectIdentity = ObjectIdentity
pm1004mCtrlledTest = _Pm1004mCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 192)
)
_Pm1004mCtrlGreenLed_Type = EkiOnOff
_Pm1004mCtrlGreenLed_Object = MibScalar
pm1004mCtrlGreenLed = _Pm1004mCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 192, 1),
    _Pm1004mCtrlGreenLed_Type()
)
pm1004mCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlGreenLed.setStatus("current")
_Pm1004mCtrlRedLed_Type = EkiOnOff
_Pm1004mCtrlRedLed_Object = MibScalar
pm1004mCtrlRedLed = _Pm1004mCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 192, 2),
    _Pm1004mCtrlRedLed_Type()
)
pm1004mCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlRedLed.setStatus("current")
_Pm1004mCtrlLedOff_Type = EkiOnOff
_Pm1004mCtrlLedOff_Object = MibScalar
pm1004mCtrlLedOff = _Pm1004mCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 192, 3),
    _Pm1004mCtrlLedOff_Type()
)
pm1004mCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlLedOff.setStatus("current")
_Pm1004mCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm1004mCtrlmoduleOosMode = _Pm1004mCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 193)
)
_Pm1004mCtrlModuleOosMode_Type = EkiOnOff
_Pm1004mCtrlModuleOosMode_Object = MibScalar
pm1004mCtrlModuleOosMode = _Pm1004mCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 193, 1),
    _Pm1004mCtrlModuleOosMode_Type()
)
pm1004mCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlModuleOosMode.setStatus("current")
_Pm1004mCtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm1004mCtrlmaintenanceMode = _Pm1004mCtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 197)
)
_Pm1004mCtrlMaintenanceMode_Type = EkiOnOff
_Pm1004mCtrlMaintenanceMode_Object = MibScalar
pm1004mCtrlMaintenanceMode = _Pm1004mCtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 197, 1),
    _Pm1004mCtrlMaintenanceMode_Type()
)
pm1004mCtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlMaintenanceMode.setStatus("current")
_Pm1004mCtrldccEnable_ObjectIdentity = ObjectIdentity
pm1004mCtrldccEnable = _Pm1004mCtrldccEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 198)
)
_Pm1004mCtrlDccEnable_Type = EkiOnOff
_Pm1004mCtrlDccEnable_Object = MibScalar
pm1004mCtrlDccEnable = _Pm1004mCtrlDccEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 1, 198, 1),
    _Pm1004mCtrlDccEnable_Type()
)
pm1004mCtrlDccEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlDccEnable.setStatus("current")
_Pm1004mCtrlClient_ObjectIdentity = ObjectIdentity
pm1004mCtrlClient = _Pm1004mCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2)
)
_Pm1004mCtrlaccessLoopTable_Object = MibTable
pm1004mCtrlaccessLoopTable = _Pm1004mCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004mCtrlaccessLoopTable.setStatus("current")
_Pm1004mCtrlaccessLoopEntry_Object = MibTableRow
pm1004mCtrlaccessLoopEntry = _Pm1004mCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 16, 1)
)
pm1004mCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlaccessLoopEntry.setStatus("current")


class _Pm1004mCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm1004mCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlaccessLoopIndex_Object = MibTableColumn
pm1004mCtrlaccessLoopIndex = _Pm1004mCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 16, 1, 1),
    _Pm1004mCtrlaccessLoopIndex_Type()
)
pm1004mCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlaccessLoopIndex.setStatus("current")
_Pm1004mCtrlaccessLoopPortn_Type = EkiState
_Pm1004mCtrlaccessLoopPortn_Object = MibTableColumn
pm1004mCtrlaccessLoopPortn = _Pm1004mCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 16, 1, 2),
    _Pm1004mCtrlaccessLoopPortn_Type()
)
pm1004mCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlaccessLoopPortn.setStatus("current")
_Pm1004mCtrlportOosModeTable_Object = MibTable
pm1004mCtrlportOosModeTable = _Pm1004mCtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm1004mCtrlportOosModeTable.setStatus("current")
_Pm1004mCtrlportOosModeEntry_Object = MibTableRow
pm1004mCtrlportOosModeEntry = _Pm1004mCtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 18, 1)
)
pm1004mCtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlportOosModeEntry.setStatus("current")


class _Pm1004mCtrlportOosModeIndex_Type(Integer32):
    """Custom type pm1004mCtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlportOosModeIndex_Object = MibTableColumn
pm1004mCtrlportOosModeIndex = _Pm1004mCtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 18, 1, 1),
    _Pm1004mCtrlportOosModeIndex_Type()
)
pm1004mCtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlportOosModeIndex.setStatus("current")
_Pm1004mCtrlportOosModePortn_Type = EkiState
_Pm1004mCtrlportOosModePortn_Object = MibTableColumn
pm1004mCtrlportOosModePortn = _Pm1004mCtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 18, 1, 2),
    _Pm1004mCtrlportOosModePortn_Type()
)
pm1004mCtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlportOosModePortn.setStatus("current")
_Pm1004mCtrlsfpOnCtrlTable_Object = MibTable
pm1004mCtrlsfpOnCtrlTable = _Pm1004mCtrlsfpOnCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 19)
)
if mibBuilder.loadTexts:
    pm1004mCtrlsfpOnCtrlTable.setStatus("current")
_Pm1004mCtrlsfpOnCtrlEntry_Object = MibTableRow
pm1004mCtrlsfpOnCtrlEntry = _Pm1004mCtrlsfpOnCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 19, 1)
)
pm1004mCtrlsfpOnCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlsfpOnCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlsfpOnCtrlEntry.setStatus("current")


class _Pm1004mCtrlsfpOnCtrlIndex_Type(Integer32):
    """Custom type pm1004mCtrlsfpOnCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlsfpOnCtrlIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlsfpOnCtrlIndex_Object = MibTableColumn
pm1004mCtrlsfpOnCtrlIndex = _Pm1004mCtrlsfpOnCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 19, 1, 1),
    _Pm1004mCtrlsfpOnCtrlIndex_Type()
)
pm1004mCtrlsfpOnCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlsfpOnCtrlIndex.setStatus("current")
_Pm1004mCtrlsfpOnCtrlPortn_Type = EkiState
_Pm1004mCtrlsfpOnCtrlPortn_Object = MibTableColumn
pm1004mCtrlsfpOnCtrlPortn = _Pm1004mCtrlsfpOnCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 19, 1, 2),
    _Pm1004mCtrlsfpOnCtrlPortn_Type()
)
pm1004mCtrlsfpOnCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlsfpOnCtrlPortn.setStatus("current")
_Pm1004mCtrlsfpOffCtrlTable_Object = MibTable
pm1004mCtrlsfpOffCtrlTable = _Pm1004mCtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm1004mCtrlsfpOffCtrlTable.setStatus("current")
_Pm1004mCtrlsfpOffCtrlEntry_Object = MibTableRow
pm1004mCtrlsfpOffCtrlEntry = _Pm1004mCtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 20, 1)
)
pm1004mCtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlsfpOffCtrlEntry.setStatus("current")


class _Pm1004mCtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pm1004mCtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlsfpOffCtrlIndex_Object = MibTableColumn
pm1004mCtrlsfpOffCtrlIndex = _Pm1004mCtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 20, 1, 1),
    _Pm1004mCtrlsfpOffCtrlIndex_Type()
)
pm1004mCtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlsfpOffCtrlIndex.setStatus("current")
_Pm1004mCtrlsfpOffCtrlPortn_Type = EkiState
_Pm1004mCtrlsfpOffCtrlPortn_Object = MibTableColumn
pm1004mCtrlsfpOffCtrlPortn = _Pm1004mCtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 20, 1, 2),
    _Pm1004mCtrlsfpOffCtrlPortn_Type()
)
pm1004mCtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlsfpOffCtrlPortn.setStatus("current")
_Pm1004mCtrlcsfUpInsTable_Object = MibTable
pm1004mCtrlcsfUpInsTable = _Pm1004mCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm1004mCtrlcsfUpInsTable.setStatus("current")
_Pm1004mCtrlcsfUpInsEntry_Object = MibTableRow
pm1004mCtrlcsfUpInsEntry = _Pm1004mCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 21, 1)
)
pm1004mCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlcsfUpInsEntry.setStatus("current")


class _Pm1004mCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm1004mCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlcsfUpInsIndex_Object = MibTableColumn
pm1004mCtrlcsfUpInsIndex = _Pm1004mCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 21, 1, 1),
    _Pm1004mCtrlcsfUpInsIndex_Type()
)
pm1004mCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlcsfUpInsIndex.setStatus("current")
_Pm1004mCtrlcsfUpInsPortn_Type = EkiState
_Pm1004mCtrlcsfUpInsPortn_Object = MibTableColumn
pm1004mCtrlcsfUpInsPortn = _Pm1004mCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 21, 1, 2),
    _Pm1004mCtrlcsfUpInsPortn_Type()
)
pm1004mCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlcsfUpInsPortn.setStatus("current")
_Pm1004mCtrlcaisDwInsTable_Object = MibTable
pm1004mCtrlcaisDwInsTable = _Pm1004mCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm1004mCtrlcaisDwInsTable.setStatus("current")
_Pm1004mCtrlcaisDwInsEntry_Object = MibTableRow
pm1004mCtrlcaisDwInsEntry = _Pm1004mCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 22, 1)
)
pm1004mCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlcaisDwInsEntry.setStatus("current")


class _Pm1004mCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm1004mCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlcaisDwInsIndex_Object = MibTableColumn
pm1004mCtrlcaisDwInsIndex = _Pm1004mCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 22, 1, 1),
    _Pm1004mCtrlcaisDwInsIndex_Type()
)
pm1004mCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlcaisDwInsIndex.setStatus("current")
_Pm1004mCtrlcaisDwInsPortn_Type = EkiState
_Pm1004mCtrlcaisDwInsPortn_Object = MibTableColumn
pm1004mCtrlcaisDwInsPortn = _Pm1004mCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 22, 1, 2),
    _Pm1004mCtrlcaisDwInsPortn_Type()
)
pm1004mCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlcaisDwInsPortn.setStatus("current")
_Pm1004mCtrlclientAccessTermLoopTable_Object = MibTable
pm1004mCtrlclientAccessTermLoopTable = _Pm1004mCtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pm1004mCtrlclientAccessTermLoopTable.setStatus("current")
_Pm1004mCtrlclientAccessTermLoopEntry_Object = MibTableRow
pm1004mCtrlclientAccessTermLoopEntry = _Pm1004mCtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 26, 1)
)
pm1004mCtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm1004mCtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm1004mCtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm1004mCtrlclientAccessTermLoopIndex = _Pm1004mCtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 26, 1, 1),
    _Pm1004mCtrlclientAccessTermLoopIndex_Type()
)
pm1004mCtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlclientAccessTermLoopIndex.setStatus("current")
_Pm1004mCtrlclientAccessTermLoopPortn_Type = EkiState
_Pm1004mCtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm1004mCtrlclientAccessTermLoopPortn = _Pm1004mCtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 26, 1, 2),
    _Pm1004mCtrlclientAccessTermLoopPortn_Type()
)
pm1004mCtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlclientAccessTermLoopPortn.setStatus("current")
_Pm1004mCtrlresetCount15PortTable_Object = MibTable
pm1004mCtrlresetCount15PortTable = _Pm1004mCtrlresetCount15PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 35)
)
if mibBuilder.loadTexts:
    pm1004mCtrlresetCount15PortTable.setStatus("current")
_Pm1004mCtrlresetCount15PortEntry_Object = MibTableRow
pm1004mCtrlresetCount15PortEntry = _Pm1004mCtrlresetCount15PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 35, 1)
)
pm1004mCtrlresetCount15PortEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlresetCount15PortIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlresetCount15PortEntry.setStatus("current")


class _Pm1004mCtrlresetCount15PortIndex_Type(Integer32):
    """Custom type pm1004mCtrlresetCount15PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlresetCount15PortIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlresetCount15PortIndex_Object = MibTableColumn
pm1004mCtrlresetCount15PortIndex = _Pm1004mCtrlresetCount15PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 35, 1, 1),
    _Pm1004mCtrlresetCount15PortIndex_Type()
)
pm1004mCtrlresetCount15PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlresetCount15PortIndex.setStatus("current")
_Pm1004mCtrlclientResetAllPerfCount15Portn_Type = EkiState
_Pm1004mCtrlclientResetAllPerfCount15Portn_Object = MibTableColumn
pm1004mCtrlclientResetAllPerfCount15Portn = _Pm1004mCtrlclientResetAllPerfCount15Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 35, 1, 2),
    _Pm1004mCtrlclientResetAllPerfCount15Portn_Type()
)
pm1004mCtrlclientResetAllPerfCount15Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlclientResetAllPerfCount15Portn.setStatus("current")
_Pm1004mCtrlresetCount24PortTable_Object = MibTable
pm1004mCtrlresetCount24PortTable = _Pm1004mCtrlresetCount24PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 36)
)
if mibBuilder.loadTexts:
    pm1004mCtrlresetCount24PortTable.setStatus("current")
_Pm1004mCtrlresetCount24PortEntry_Object = MibTableRow
pm1004mCtrlresetCount24PortEntry = _Pm1004mCtrlresetCount24PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 36, 1)
)
pm1004mCtrlresetCount24PortEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlresetCount24PortIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlresetCount24PortEntry.setStatus("current")


class _Pm1004mCtrlresetCount24PortIndex_Type(Integer32):
    """Custom type pm1004mCtrlresetCount24PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlresetCount24PortIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlresetCount24PortIndex_Object = MibTableColumn
pm1004mCtrlresetCount24PortIndex = _Pm1004mCtrlresetCount24PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 36, 1, 1),
    _Pm1004mCtrlresetCount24PortIndex_Type()
)
pm1004mCtrlresetCount24PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlresetCount24PortIndex.setStatus("current")
_Pm1004mCtrlclientResetAllPerfCount24Portn_Type = EkiState
_Pm1004mCtrlclientResetAllPerfCount24Portn_Object = MibTableColumn
pm1004mCtrlclientResetAllPerfCount24Portn = _Pm1004mCtrlclientResetAllPerfCount24Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 2, 36, 1, 2),
    _Pm1004mCtrlclientResetAllPerfCount24Portn_Type()
)
pm1004mCtrlclientResetAllPerfCount24Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlclientResetAllPerfCount24Portn.setStatus("current")
_Pm1004mCtrlLine_ObjectIdentity = ObjectIdentity
pm1004mCtrlLine = _Pm1004mCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3)
)
_Pm1004mCtrlcommAccessLoop_ObjectIdentity = ObjectIdentity
pm1004mCtrlcommAccessLoop = _Pm1004mCtrlcommAccessLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 64)
)
_Pm1004mCtrlCommAccessloop_Type = EkiOnOff
_Pm1004mCtrlCommAccessloop_Object = MibScalar
pm1004mCtrlCommAccessloop = _Pm1004mCtrlCommAccessloop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 64, 1),
    _Pm1004mCtrlCommAccessloop_Type()
)
pm1004mCtrlCommAccessloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlCommAccessloop.setStatus("deprecated")
_Pm1004mCtrllineLoop_ObjectIdentity = ObjectIdentity
pm1004mCtrllineLoop = _Pm1004mCtrllineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 66)
)
_Pm1004mCtrlLineLoop_Type = EkiOnOff
_Pm1004mCtrlLineLoop_Object = MibScalar
pm1004mCtrlLineLoop = _Pm1004mCtrlLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 66, 1),
    _Pm1004mCtrlLineLoop_Type()
)
pm1004mCtrlLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlLineLoop.setStatus("deprecated")
_Pm1004mCtrlmsAis_ObjectIdentity = ObjectIdentity
pm1004mCtrlmsAis = _Pm1004mCtrlmsAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 67)
)
_Pm1004mCtrlMsAis_Type = EkiOnOff
_Pm1004mCtrlMsAis_Object = MibScalar
pm1004mCtrlMsAis = _Pm1004mCtrlMsAis_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 67, 1),
    _Pm1004mCtrlMsAis_Type()
)
pm1004mCtrlMsAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlMsAis.setStatus("current")
_Pm1004mCtrlProtMgnt_ObjectIdentity = ObjectIdentity
pm1004mCtrlProtMgnt = _Pm1004mCtrlProtMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 73)
)


class _Pm1004mCtrlLineNumber_Type(Unsigned32):
    """Custom type pm1004mCtrlLineNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Pm1004mCtrlLineNumber_Type.__name__ = "Unsigned32"
_Pm1004mCtrlLineNumber_Object = MibScalar
pm1004mCtrlLineNumber = _Pm1004mCtrlLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 73, 1),
    _Pm1004mCtrlLineNumber_Type()
)
pm1004mCtrlLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlLineNumber.setStatus("current")
_Pm1004mCtrlProtMode_Type = EkiMode
_Pm1004mCtrlProtMode_Object = MibScalar
pm1004mCtrlProtMode = _Pm1004mCtrlProtMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 73, 2),
    _Pm1004mCtrlProtMode_Type()
)
pm1004mCtrlProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlProtMode.setStatus("current")
_Pm1004mCtrllineOosModeTable_Object = MibTable
pm1004mCtrllineOosModeTable = _Pm1004mCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm1004mCtrllineOosModeTable.setStatus("current")
_Pm1004mCtrllineOosModeEntry_Object = MibTableRow
pm1004mCtrllineOosModeEntry = _Pm1004mCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 74, 1)
)
pm1004mCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrllineOosModeEntry.setStatus("current")


class _Pm1004mCtrllineOosModeIndex_Type(Integer32):
    """Custom type pm1004mCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm1004mCtrllineOosModeIndex_Object = MibTableColumn
pm1004mCtrllineOosModeIndex = _Pm1004mCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 74, 1, 1),
    _Pm1004mCtrllineOosModeIndex_Type()
)
pm1004mCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrllineOosModeIndex.setStatus("current")
_Pm1004mCtrllineOosModePortn_Type = EkiState
_Pm1004mCtrllineOosModePortn_Object = MibTableColumn
pm1004mCtrllineOosModePortn = _Pm1004mCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 74, 1, 2),
    _Pm1004mCtrllineOosModePortn_Type()
)
pm1004mCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrllineOosModePortn.setStatus("current")
_Pm1004mCtrllineResetCount15LineTable_Object = MibTable
pm1004mCtrllineResetCount15LineTable = _Pm1004mCtrllineResetCount15LineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 86)
)
if mibBuilder.loadTexts:
    pm1004mCtrllineResetCount15LineTable.setStatus("current")
_Pm1004mCtrllineResetCount15LineEntry_Object = MibTableRow
pm1004mCtrllineResetCount15LineEntry = _Pm1004mCtrllineResetCount15LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 86, 1)
)
pm1004mCtrllineResetCount15LineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrllineResetCount15LineIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrllineResetCount15LineEntry.setStatus("current")


class _Pm1004mCtrllineResetCount15LineIndex_Type(Integer32):
    """Custom type pm1004mCtrllineResetCount15LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrllineResetCount15LineIndex_Type.__name__ = "Integer32"
_Pm1004mCtrllineResetCount15LineIndex_Object = MibTableColumn
pm1004mCtrllineResetCount15LineIndex = _Pm1004mCtrllineResetCount15LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 86, 1, 1),
    _Pm1004mCtrllineResetCount15LineIndex_Type()
)
pm1004mCtrllineResetCount15LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrllineResetCount15LineIndex.setStatus("current")
_Pm1004mCtrlresetAllPerfCount15Portn_Type = EkiState
_Pm1004mCtrlresetAllPerfCount15Portn_Object = MibTableColumn
pm1004mCtrlresetAllPerfCount15Portn = _Pm1004mCtrlresetAllPerfCount15Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 86, 1, 2),
    _Pm1004mCtrlresetAllPerfCount15Portn_Type()
)
pm1004mCtrlresetAllPerfCount15Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlresetAllPerfCount15Portn.setStatus("current")
_Pm1004mCtrllineResetCount24LineTable_Object = MibTable
pm1004mCtrllineResetCount24LineTable = _Pm1004mCtrllineResetCount24LineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 87)
)
if mibBuilder.loadTexts:
    pm1004mCtrllineResetCount24LineTable.setStatus("current")
_Pm1004mCtrllineResetCount24LineEntry_Object = MibTableRow
pm1004mCtrllineResetCount24LineEntry = _Pm1004mCtrllineResetCount24LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 87, 1)
)
pm1004mCtrllineResetCount24LineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrllineResetCount24LineIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrllineResetCount24LineEntry.setStatus("current")


class _Pm1004mCtrllineResetCount24LineIndex_Type(Integer32):
    """Custom type pm1004mCtrllineResetCount24LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrllineResetCount24LineIndex_Type.__name__ = "Integer32"
_Pm1004mCtrllineResetCount24LineIndex_Object = MibTableColumn
pm1004mCtrllineResetCount24LineIndex = _Pm1004mCtrllineResetCount24LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 87, 1, 1),
    _Pm1004mCtrllineResetCount24LineIndex_Type()
)
pm1004mCtrllineResetCount24LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrllineResetCount24LineIndex.setStatus("current")
_Pm1004mCtrlresetAllPerfCount24Portn_Type = EkiState
_Pm1004mCtrlresetAllPerfCount24Portn_Object = MibTableColumn
pm1004mCtrlresetAllPerfCount24Portn = _Pm1004mCtrlresetAllPerfCount24Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 87, 1, 2),
    _Pm1004mCtrlresetAllPerfCount24Portn_Type()
)
pm1004mCtrlresetAllPerfCount24Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlresetAllPerfCount24Portn.setStatus("current")
_Pm1004mCtrlxfpOnoffTable_Object = MibTable
pm1004mCtrlxfpOnoffTable = _Pm1004mCtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004mCtrlxfpOnoffTable.setStatus("current")
_Pm1004mCtrlxfpOnoffEntry_Object = MibTableRow
pm1004mCtrlxfpOnoffEntry = _Pm1004mCtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 208, 1)
)
pm1004mCtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlxfpOnoffEntry.setStatus("current")


class _Pm1004mCtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pm1004mCtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlxfpOnoffIndex_Object = MibTableColumn
pm1004mCtrlxfpOnoffIndex = _Pm1004mCtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 208, 1, 1),
    _Pm1004mCtrlxfpOnoffIndex_Type()
)
pm1004mCtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlxfpOnoffIndex.setStatus("current")
_Pm1004mCtrlxfpOnoffPortn_Type = EkiState
_Pm1004mCtrlxfpOnoffPortn_Object = MibTableColumn
pm1004mCtrlxfpOnoffPortn = _Pm1004mCtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 208, 1, 2),
    _Pm1004mCtrlxfpOnoffPortn_Type()
)
pm1004mCtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlxfpOnoffPortn.setStatus("current")
_Pm1004mCtrlxfpLineLoopTable_Object = MibTable
pm1004mCtrlxfpLineLoopTable = _Pm1004mCtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004mCtrlxfpLineLoopTable.setStatus("current")
_Pm1004mCtrlxfpLineLoopEntry_Object = MibTableRow
pm1004mCtrlxfpLineLoopEntry = _Pm1004mCtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 209, 1)
)
pm1004mCtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlxfpLineLoopEntry.setStatus("current")


class _Pm1004mCtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pm1004mCtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlxfpLineLoopIndex_Object = MibTableColumn
pm1004mCtrlxfpLineLoopIndex = _Pm1004mCtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 209, 1, 1),
    _Pm1004mCtrlxfpLineLoopIndex_Type()
)
pm1004mCtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlxfpLineLoopIndex.setStatus("current")
_Pm1004mCtrlxfpLineLoopPortn_Type = EkiState
_Pm1004mCtrlxfpLineLoopPortn_Object = MibTableColumn
pm1004mCtrlxfpLineLoopPortn = _Pm1004mCtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 209, 1, 2),
    _Pm1004mCtrlxfpLineLoopPortn_Type()
)
pm1004mCtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlxfpLineLoopPortn.setStatus("current")
_Pm1004mCtrlxfpXfiLoopTable_Object = MibTable
pm1004mCtrlxfpXfiLoopTable = _Pm1004mCtrlxfpXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004mCtrlxfpXfiLoopTable.setStatus("current")
_Pm1004mCtrlxfpXfiLoopEntry_Object = MibTableRow
pm1004mCtrlxfpXfiLoopEntry = _Pm1004mCtrlxfpXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 210, 1)
)
pm1004mCtrlxfpXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrlxfpXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrlxfpXfiLoopEntry.setStatus("current")


class _Pm1004mCtrlxfpXfiLoopIndex_Type(Integer32):
    """Custom type pm1004mCtrlxfpXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrlxfpXfiLoopIndex_Type.__name__ = "Integer32"
_Pm1004mCtrlxfpXfiLoopIndex_Object = MibTableColumn
pm1004mCtrlxfpXfiLoopIndex = _Pm1004mCtrlxfpXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 210, 1, 1),
    _Pm1004mCtrlxfpXfiLoopIndex_Type()
)
pm1004mCtrlxfpXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrlxfpXfiLoopIndex.setStatus("current")
_Pm1004mCtrlxfpXfiLoopPortn_Type = EkiState
_Pm1004mCtrlxfpXfiLoopPortn_Object = MibTableColumn
pm1004mCtrlxfpXfiLoopPortn = _Pm1004mCtrlxfpXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 210, 1, 2),
    _Pm1004mCtrlxfpXfiLoopPortn_Type()
)
pm1004mCtrlxfpXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrlxfpXfiLoopPortn.setStatus("current")
_Pm1004mCtrllineTunableChannelTable_Object = MibTable
pm1004mCtrllineTunableChannelTable = _Pm1004mCtrllineTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm1004mCtrllineTunableChannelTable.setStatus("current")
_Pm1004mCtrllineTunableChannelEntry_Object = MibTableRow
pm1004mCtrllineTunableChannelEntry = _Pm1004mCtrllineTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 212, 1)
)
pm1004mCtrllineTunableChannelEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrllineTunableChannelIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrllineTunableChannelEntry.setStatus("current")


class _Pm1004mCtrllineTunableChannelIndex_Type(Integer32):
    """Custom type pm1004mCtrllineTunableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrllineTunableChannelIndex_Type.__name__ = "Integer32"
_Pm1004mCtrllineTunableChannelIndex_Object = MibTableColumn
pm1004mCtrllineTunableChannelIndex = _Pm1004mCtrllineTunableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 212, 1, 1),
    _Pm1004mCtrllineTunableChannelIndex_Type()
)
pm1004mCtrllineTunableChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrllineTunableChannelIndex.setStatus("current")
_Pm1004mCtrllineTunableChannelPortn_Type = Pm1004mOtxChannel
_Pm1004mCtrllineTunableChannelPortn_Object = MibTableColumn
pm1004mCtrllineTunableChannelPortn = _Pm1004mCtrllineTunableChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 212, 1, 2),
    _Pm1004mCtrllineTunableChannelPortn_Type()
)
pm1004mCtrllineTunableChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrllineTunableChannelPortn.setStatus("current")
_Pm1004mCtrllinePhotodiodeModeTable_Object = MibTable
pm1004mCtrllinePhotodiodeModeTable = _Pm1004mCtrllinePhotodiodeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 213)
)
if mibBuilder.loadTexts:
    pm1004mCtrllinePhotodiodeModeTable.setStatus("current")
_Pm1004mCtrllinePhotodiodeModeEntry_Object = MibTableRow
pm1004mCtrllinePhotodiodeModeEntry = _Pm1004mCtrllinePhotodiodeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 213, 1)
)
pm1004mCtrllinePhotodiodeModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrllinePhotodiodeModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrllinePhotodiodeModeEntry.setStatus("current")


class _Pm1004mCtrllinePhotodiodeModeIndex_Type(Integer32):
    """Custom type pm1004mCtrllinePhotodiodeModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrllinePhotodiodeModeIndex_Type.__name__ = "Integer32"
_Pm1004mCtrllinePhotodiodeModeIndex_Object = MibTableColumn
pm1004mCtrllinePhotodiodeModeIndex = _Pm1004mCtrllinePhotodiodeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 213, 1, 1),
    _Pm1004mCtrllinePhotodiodeModeIndex_Type()
)
pm1004mCtrllinePhotodiodeModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrllinePhotodiodeModeIndex.setStatus("current")
_Pm1004mCtrllinePhotodiodeModePortn_Type = Pm1004mOtxMode
_Pm1004mCtrllinePhotodiodeModePortn_Object = MibTableColumn
pm1004mCtrllinePhotodiodeModePortn = _Pm1004mCtrllinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 213, 1, 2),
    _Pm1004mCtrllinePhotodiodeModePortn_Type()
)
pm1004mCtrllinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrllinePhotodiodeModePortn.setStatus("current")
_Pm1004mCtrllinePhotodiodeValueTable_Object = MibTable
pm1004mCtrllinePhotodiodeValueTable = _Pm1004mCtrllinePhotodiodeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 214)
)
if mibBuilder.loadTexts:
    pm1004mCtrllinePhotodiodeValueTable.setStatus("current")
_Pm1004mCtrllinePhotodiodeValueEntry_Object = MibTableRow
pm1004mCtrllinePhotodiodeValueEntry = _Pm1004mCtrllinePhotodiodeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 214, 1)
)
pm1004mCtrllinePhotodiodeValueEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrllinePhotodiodeValueIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrllinePhotodiodeValueEntry.setStatus("current")


class _Pm1004mCtrllinePhotodiodeValueIndex_Type(Integer32):
    """Custom type pm1004mCtrllinePhotodiodeValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrllinePhotodiodeValueIndex_Type.__name__ = "Integer32"
_Pm1004mCtrllinePhotodiodeValueIndex_Object = MibTableColumn
pm1004mCtrllinePhotodiodeValueIndex = _Pm1004mCtrllinePhotodiodeValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 214, 1, 1),
    _Pm1004mCtrllinePhotodiodeValueIndex_Type()
)
pm1004mCtrllinePhotodiodeValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrllinePhotodiodeValueIndex.setStatus("current")
_Pm1004mCtrllinePhotodiodeValuePortn_Type = Pm1004mAdjustValue
_Pm1004mCtrllinePhotodiodeValuePortn_Object = MibTableColumn
pm1004mCtrllinePhotodiodeValuePortn = _Pm1004mCtrllinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 214, 1, 2),
    _Pm1004mCtrllinePhotodiodeValuePortn_Type()
)
pm1004mCtrllinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrllinePhotodiodeValuePortn.setStatus("current")
_Pm1004mCtrllinePowerLaserTable_Object = MibTable
pm1004mCtrllinePowerLaserTable = _Pm1004mCtrllinePowerLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 215)
)
if mibBuilder.loadTexts:
    pm1004mCtrllinePowerLaserTable.setStatus("current")
_Pm1004mCtrllinePowerLaserEntry_Object = MibTableRow
pm1004mCtrllinePowerLaserEntry = _Pm1004mCtrllinePowerLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 215, 1)
)
pm1004mCtrllinePowerLaserEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCtrllinePowerLaserIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCtrllinePowerLaserEntry.setStatus("current")


class _Pm1004mCtrllinePowerLaserIndex_Type(Integer32):
    """Custom type pm1004mCtrllinePowerLaserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCtrllinePowerLaserIndex_Type.__name__ = "Integer32"
_Pm1004mCtrllinePowerLaserIndex_Object = MibTableColumn
pm1004mCtrllinePowerLaserIndex = _Pm1004mCtrllinePowerLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 215, 1, 1),
    _Pm1004mCtrllinePowerLaserIndex_Type()
)
pm1004mCtrllinePowerLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCtrllinePowerLaserIndex.setStatus("current")


class _Pm1004mCtrllinePowerLaserPortn_Type(Integer32):
    """Custom type pm1004mCtrllinePowerLaserPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1004mCtrllinePowerLaserPortn_Type.__name__ = "Integer32"
_Pm1004mCtrllinePowerLaserPortn_Object = MibTableColumn
pm1004mCtrllinePowerLaserPortn = _Pm1004mCtrllinePowerLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 6, 3, 215, 1, 2),
    _Pm1004mCtrllinePowerLaserPortn_Type()
)
pm1004mCtrllinePowerLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCtrllinePowerLaserPortn.setStatus("current")
_Pm1004mri_ObjectIdentity = ObjectIdentity
pm1004mri = _Pm1004mri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7)
)
_Pm1004mriTable_ObjectIdentity = ObjectIdentity
pm1004mriTable = _Pm1004mriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 1)
)
_Pm1004mRinvSfpTable_Object = MibTable
pm1004mRinvSfpTable = _Pm1004mRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004mRinvSfpTable.setStatus("current")
_Pm1004mRinvSfpEntry_Object = MibTableRow
pm1004mRinvSfpEntry = _Pm1004mRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 1, 1, 1)
)
pm1004mRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm1004mRinvSfpEntry.setStatus("current")


class _Pm1004mRinvSfpIndex_Type(Integer32):
    """Custom type pm1004mRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004mRinvSfpIndex_Type.__name__ = "Integer32"
_Pm1004mRinvSfpIndex_Object = MibTableColumn
pm1004mRinvSfpIndex = _Pm1004mRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 1, 1, 1, 1),
    _Pm1004mRinvSfpIndex_Type()
)
pm1004mRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mRinvSfpIndex.setStatus("current")
_Pm1004mRinvsfp_Type = DisplayString
_Pm1004mRinvsfp_Object = MibTableColumn
pm1004mRinvsfp = _Pm1004mRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 1, 1, 1, 2),
    _Pm1004mRinvsfp_Type()
)
pm1004mRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mRinvsfp.setStatus("current")
_Pm1004mRinvLineTable_Object = MibTable
pm1004mRinvLineTable = _Pm1004mRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm1004mRinvLineTable.setStatus("current")
_Pm1004mRinvLineEntry_Object = MibTableRow
pm1004mRinvLineEntry = _Pm1004mRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 1, 2, 1)
)
pm1004mRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004mRinvLineEntry.setStatus("current")


class _Pm1004mRinvLineIndex_Type(Integer32):
    """Custom type pm1004mRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004mRinvLineIndex_Type.__name__ = "Integer32"
_Pm1004mRinvLineIndex_Object = MibTableColumn
pm1004mRinvLineIndex = _Pm1004mRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 1, 2, 1, 1),
    _Pm1004mRinvLineIndex_Type()
)
pm1004mRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mRinvLineIndex.setStatus("current")
_Pm1004mRinvxfpLine_Type = DisplayString
_Pm1004mRinvxfpLine_Object = MibTableColumn
pm1004mRinvxfpLine = _Pm1004mRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 1, 2, 1, 2),
    _Pm1004mRinvxfpLine_Type()
)
pm1004mRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mRinvxfpLine.setStatus("current")
_Pm1004mRinvReloadInventory_Type = EkiOnOff
_Pm1004mRinvReloadInventory_Object = MibScalar
pm1004mRinvReloadInventory = _Pm1004mRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 2),
    _Pm1004mRinvReloadInventory_Type()
)
pm1004mRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mRinvReloadInventory.setStatus("current")
_Pm1004mRinvHwPlatform_Type = DisplayString
_Pm1004mRinvHwPlatform_Object = MibScalar
pm1004mRinvHwPlatform = _Pm1004mRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 3),
    _Pm1004mRinvHwPlatform_Type()
)
pm1004mRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mRinvHwPlatform.setStatus("current")
_Pm1004mRinvModulePlatform_Type = DisplayString
_Pm1004mRinvModulePlatform_Object = MibScalar
pm1004mRinvModulePlatform = _Pm1004mRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 4),
    _Pm1004mRinvModulePlatform_Type()
)
pm1004mRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mRinvModulePlatform.setStatus("current")
_Pm1004mRinvSwPlatform_Type = DisplayString
_Pm1004mRinvSwPlatform_Object = MibScalar
pm1004mRinvSwPlatform = _Pm1004mRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 5),
    _Pm1004mRinvSwPlatform_Type()
)
pm1004mRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mRinvSwPlatform.setStatus("current")
_Pm1004mRinvGwPlatform_Type = DisplayString
_Pm1004mRinvGwPlatform_Object = MibScalar
pm1004mRinvGwPlatform = _Pm1004mRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 7, 6),
    _Pm1004mRinvGwPlatform_Type()
)
pm1004mRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mRinvGwPlatform.setStatus("current")
_Pm1004mdownload_ObjectIdentity = ObjectIdentity
pm1004mdownload = _Pm1004mdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8)
)
_Pm1004mDwlOther_ObjectIdentity = ObjectIdentity
pm1004mDwlOther = _Pm1004mDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1)
)
_Pm1004mDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm1004mDwlrestartProcess = _Pm1004mDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 0)
)
_Pm1004mDwlWarmRestartProcessed_Type = EkiOnOff
_Pm1004mDwlWarmRestartProcessed_Object = MibScalar
pm1004mDwlWarmRestartProcessed = _Pm1004mDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 0, 1),
    _Pm1004mDwlWarmRestartProcessed_Type()
)
pm1004mDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlWarmRestartProcessed.setStatus("current")
_Pm1004mDwlColdRestartProcessed_Type = EkiOnOff
_Pm1004mDwlColdRestartProcessed_Object = MibScalar
pm1004mDwlColdRestartProcessed = _Pm1004mDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 0, 2),
    _Pm1004mDwlColdRestartProcessed_Type()
)
pm1004mDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlColdRestartProcessed.setStatus("current")
_Pm1004mDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm1004mDwlswBanksUsed = _Pm1004mDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 1)
)
_Pm1004mDwlSwBank1Used_Type = EkiOnOff
_Pm1004mDwlSwBank1Used_Object = MibScalar
pm1004mDwlSwBank1Used = _Pm1004mDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 1, 1),
    _Pm1004mDwlSwBank1Used_Type()
)
pm1004mDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlSwBank1Used.setStatus("current")
_Pm1004mDwlSwBank2Used_Type = EkiOnOff
_Pm1004mDwlSwBank2Used_Object = MibScalar
pm1004mDwlSwBank2Used = _Pm1004mDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 1, 2),
    _Pm1004mDwlSwBank2Used_Type()
)
pm1004mDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlSwBank2Used.setStatus("current")
_Pm1004mDwlSwBank1Notempty_Type = EkiOnOff
_Pm1004mDwlSwBank1Notempty_Object = MibScalar
pm1004mDwlSwBank1Notempty = _Pm1004mDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 1, 5),
    _Pm1004mDwlSwBank1Notempty_Type()
)
pm1004mDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlSwBank1Notempty.setStatus("current")
_Pm1004mDwlSwBank2Notempty_Type = EkiOnOff
_Pm1004mDwlSwBank2Notempty_Object = MibScalar
pm1004mDwlSwBank2Notempty = _Pm1004mDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 1, 6),
    _Pm1004mDwlSwBank2Notempty_Type()
)
pm1004mDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlSwBank2Notempty.setStatus("current")
_Pm1004mDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm1004mDwlgwBanksUsed = _Pm1004mDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 2)
)
_Pm1004mDwlGwBank1Used_Type = EkiOnOff
_Pm1004mDwlGwBank1Used_Object = MibScalar
pm1004mDwlGwBank1Used = _Pm1004mDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 2, 1),
    _Pm1004mDwlGwBank1Used_Type()
)
pm1004mDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlGwBank1Used.setStatus("current")
_Pm1004mDwlGwBank2Used_Type = EkiOnOff
_Pm1004mDwlGwBank2Used_Object = MibScalar
pm1004mDwlGwBank2Used = _Pm1004mDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 2, 2),
    _Pm1004mDwlGwBank2Used_Type()
)
pm1004mDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlGwBank2Used.setStatus("current")
_Pm1004mDwlGwBank3Used_Type = EkiOnOff
_Pm1004mDwlGwBank3Used_Object = MibScalar
pm1004mDwlGwBank3Used = _Pm1004mDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 2, 3),
    _Pm1004mDwlGwBank3Used_Type()
)
pm1004mDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlGwBank3Used.setStatus("current")
_Pm1004mDwlGwBank4Used_Type = EkiOnOff
_Pm1004mDwlGwBank4Used_Object = MibScalar
pm1004mDwlGwBank4Used = _Pm1004mDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 2, 4),
    _Pm1004mDwlGwBank4Used_Type()
)
pm1004mDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlGwBank4Used.setStatus("current")
_Pm1004mDwlGwBank1Notempty_Type = EkiOnOff
_Pm1004mDwlGwBank1Notempty_Object = MibScalar
pm1004mDwlGwBank1Notempty = _Pm1004mDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 2, 5),
    _Pm1004mDwlGwBank1Notempty_Type()
)
pm1004mDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlGwBank1Notempty.setStatus("current")
_Pm1004mDwlGwBank2Notempty_Type = EkiOnOff
_Pm1004mDwlGwBank2Notempty_Object = MibScalar
pm1004mDwlGwBank2Notempty = _Pm1004mDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 2, 6),
    _Pm1004mDwlGwBank2Notempty_Type()
)
pm1004mDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlGwBank2Notempty.setStatus("current")
_Pm1004mDwlGwBank3Notempty_Type = EkiOnOff
_Pm1004mDwlGwBank3Notempty_Object = MibScalar
pm1004mDwlGwBank3Notempty = _Pm1004mDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 2, 7),
    _Pm1004mDwlGwBank3Notempty_Type()
)
pm1004mDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlGwBank3Notempty.setStatus("current")
_Pm1004mDwlGwBank4Notempty_Type = EkiOnOff
_Pm1004mDwlGwBank4Notempty_Object = MibScalar
pm1004mDwlGwBank4Notempty = _Pm1004mDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 1, 2, 8),
    _Pm1004mDwlGwBank4Notempty_Type()
)
pm1004mDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mDwlGwBank4Notempty.setStatus("current")
_Pm1004mDwlClient_ObjectIdentity = ObjectIdentity
pm1004mDwlClient = _Pm1004mDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 2)
)
_Pm1004mDwlLine_ObjectIdentity = ObjectIdentity
pm1004mDwlLine = _Pm1004mDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 8, 3)
)
_Pm1004mConfig_ObjectIdentity = ObjectIdentity
pm1004mConfig = _Pm1004mConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9)
)
_Pm1004mCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm1004mCfgAccessCAisCsf = _Pm1004mCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1)
)
_Pm1004mCfgClientcaiscsfTable_Object = MibTable
pm1004mCfgClientcaiscsfTable = _Pm1004mCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004mCfgClientcaiscsfTable.setStatus("current")
_Pm1004mCfgClientcaiscsfEntry_Object = MibTableRow
pm1004mCfgClientcaiscsfEntry = _Pm1004mCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1)
)
pm1004mCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCfgClientcaiscsfEntry.setStatus("current")


class _Pm1004mCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm1004mCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm1004mCfgClientcaiscsfIndex_Object = MibTableColumn
pm1004mCfgClientcaiscsfIndex = _Pm1004mCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 1),
    _Pm1004mCfgClientcaiscsfIndex_Type()
)
pm1004mCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgClientcaiscsfIndex.setStatus("current")


class _Pm1004mCfgCAisModePortn_Type(Unsigned32):
    """Custom type pm1004mCfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgCAisModePortn_Object = MibTableColumn
pm1004mCfgCAisModePortn = _Pm1004mCfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 3),
    _Pm1004mCfgCAisModePortn_Type()
)
pm1004mCfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgCAisModePortn.setStatus("current")


class _Pm1004mCfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004mCfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgUpAccessioAlmPortn_Object = MibTableColumn
pm1004mCfgUpAccessioAlmPortn = _Pm1004mCfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 9),
    _Pm1004mCfgUpAccessioAlmPortn_Type()
)
pm1004mCfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgUpAccessioAlmPortn.setStatus("current")


class _Pm1004mCfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004mCfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgUpMapperDeAlmPortn_Object = MibTableColumn
pm1004mCfgUpMapperDeAlmPortn = _Pm1004mCfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 10),
    _Pm1004mCfgUpMapperDeAlmPortn_Type()
)
pm1004mCfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgUpMapperDeAlmPortn.setStatus("current")


class _Pm1004mCfgUpAccessioSdhAlmPortn_Type(Unsigned32):
    """Custom type pm1004mCfgUpAccessioSdhAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgUpAccessioSdhAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgUpAccessioSdhAlmPortn_Object = MibTableColumn
pm1004mCfgUpAccessioSdhAlmPortn = _Pm1004mCfgUpAccessioSdhAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 11),
    _Pm1004mCfgUpAccessioSdhAlmPortn_Type()
)
pm1004mCfgUpAccessioSdhAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgUpAccessioSdhAlmPortn.setStatus("current")


class _Pm1004mCfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004mCfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgDownAccessioAlmPortn_Object = MibTableColumn
pm1004mCfgDownAccessioAlmPortn = _Pm1004mCfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 17),
    _Pm1004mCfgDownAccessioAlmPortn_Type()
)
pm1004mCfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgDownAccessioAlmPortn.setStatus("current")


class _Pm1004mCfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004mCfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgDownMapperDeAlmPortn_Object = MibTableColumn
pm1004mCfgDownMapperDeAlmPortn = _Pm1004mCfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 18),
    _Pm1004mCfgDownMapperDeAlmPortn_Type()
)
pm1004mCfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgDownMapperDeAlmPortn.setStatus("current")


class _Pm1004mCfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm1004mCfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgDownDfrmAlmPortn_Object = MibTableColumn
pm1004mCfgDownDfrmAlmPortn = _Pm1004mCfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 19),
    _Pm1004mCfgDownDfrmAlmPortn_Type()
)
pm1004mCfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgDownDfrmAlmPortn.setStatus("current")


class _Pm1004mCfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pm1004mCfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pm1004mCfgDownLineSyncAlarmsPortn = _Pm1004mCfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 20),
    _Pm1004mCfgDownLineSyncAlarmsPortn_Type()
)
pm1004mCfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgDownLineSyncAlarmsPortn.setStatus("deprecated")


class _Pm1004mCfgDownAccessioSdhAlmPortn_Type(Unsigned32):
    """Custom type pm1004mCfgDownAccessioSdhAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgDownAccessioSdhAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgDownAccessioSdhAlmPortn_Object = MibTableColumn
pm1004mCfgDownAccessioSdhAlmPortn = _Pm1004mCfgDownAccessioSdhAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 1, 1, 1, 21),
    _Pm1004mCfgDownAccessioSdhAlmPortn_Type()
)
pm1004mCfgDownAccessioSdhAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgDownAccessioSdhAlmPortn.setStatus("current")
_Pm1004mCfgStartup_ObjectIdentity = ObjectIdentity
pm1004mCfgStartup = _Pm1004mCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2)
)
_Pm1004mCfgClientStartupTable_Object = MibTable
pm1004mCfgClientStartupTable = _Pm1004mCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm1004mCfgClientStartupTable.setStatus("current")
_Pm1004mCfgClientStartupEntry_Object = MibTableRow
pm1004mCfgClientStartupEntry = _Pm1004mCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 1, 1)
)
pm1004mCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCfgClientStartupEntry.setStatus("current")


class _Pm1004mCfgClientStartupIndex_Type(Integer32):
    """Custom type pm1004mCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm1004mCfgClientStartupIndex_Object = MibTableColumn
pm1004mCfgClientStartupIndex = _Pm1004mCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 1, 1, 1),
    _Pm1004mCfgClientStartupIndex_Type()
)
pm1004mCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgClientStartupIndex.setStatus("current")


class _Pm1004mCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm1004mCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgSystConfPortPortn_Object = MibTableColumn
pm1004mCfgSystConfPortPortn = _Pm1004mCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 1, 1, 3),
    _Pm1004mCfgSystConfPortPortn_Type()
)
pm1004mCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgSystConfPortPortn.setStatus("current")


class _Pm1004mCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm1004mCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgNetConfPortPortn_Object = MibTableColumn
pm1004mCfgNetConfPortPortn = _Pm1004mCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 1, 1, 4),
    _Pm1004mCfgNetConfPortPortn_Type()
)
pm1004mCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgNetConfPortPortn.setStatus("current")
_Pm1004mtablelineStartup_ObjectIdentity = ObjectIdentity
pm1004mtablelineStartup = _Pm1004mtablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 2)
)


class _Pm1004mCfgsystConfLine1_Type(Unsigned32):
    """Custom type pm1004mCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm1004mCfgsystConfLine1_Object = MibScalar
pm1004mCfgsystConfLine1 = _Pm1004mCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 2, 2),
    _Pm1004mCfgsystConfLine1_Type()
)
pm1004mCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgsystConfLine1.setStatus("current")


class _Pm1004mCfglineOptions1_Type(Unsigned32):
    """Custom type pm1004mCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfglineOptions1_Type.__name__ = "Unsigned32"
_Pm1004mCfglineOptions1_Object = MibScalar
pm1004mCfglineOptions1 = _Pm1004mCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 2, 5),
    _Pm1004mCfglineOptions1_Type()
)
pm1004mCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfglineOptions1.setStatus("current")


class _Pm1004mCfgsystConfLine2_Type(Unsigned32):
    """Custom type pm1004mCfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm1004mCfgsystConfLine2_Object = MibScalar
pm1004mCfgsystConfLine2 = _Pm1004mCfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 2, 6),
    _Pm1004mCfgsystConfLine2_Type()
)
pm1004mCfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgsystConfLine2.setStatus("current")


class _Pm1004mCfglineSelection_Type(Unsigned32):
    """Custom type pm1004mCfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfglineSelection_Type.__name__ = "Unsigned32"
_Pm1004mCfglineSelection_Object = MibScalar
pm1004mCfglineSelection = _Pm1004mCfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 2, 7),
    _Pm1004mCfglineSelection_Type()
)
pm1004mCfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfglineSelection.setStatus("current")
_Pm1004mCfgXfpTable_Object = MibTable
pm1004mCfgXfpTable = _Pm1004mCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm1004mCfgXfpTable.setStatus("current")
_Pm1004mCfgXfpEntry_Object = MibTableRow
pm1004mCfgXfpEntry = _Pm1004mCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 3, 1)
)
pm1004mCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCfgXfpEntry.setStatus("current")


class _Pm1004mCfgXfpIndex_Type(Integer32):
    """Custom type pm1004mCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCfgXfpIndex_Type.__name__ = "Integer32"
_Pm1004mCfgXfpIndex_Object = MibTableColumn
pm1004mCfgXfpIndex = _Pm1004mCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 3, 1, 1),
    _Pm1004mCfgXfpIndex_Type()
)
pm1004mCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgXfpIndex.setStatus("current")


class _Pm1004mCfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004mCfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgSystConfXfpPortn_Object = MibTableColumn
pm1004mCfgSystConfXfpPortn = _Pm1004mCfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 3, 1, 3),
    _Pm1004mCfgSystConfXfpPortn_Type()
)
pm1004mCfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgSystConfXfpPortn.setStatus("current")


class _Pm1004mCfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004mCfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgDataRateConfXfpPortn_Object = MibTableColumn
pm1004mCfgDataRateConfXfpPortn = _Pm1004mCfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 2, 3, 1, 4),
    _Pm1004mCfgDataRateConfXfpPortn_Type()
)
pm1004mCfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgDataRateConfXfpPortn.setStatus("deprecated")
_Pm1004mCfgLabels_ObjectIdentity = ObjectIdentity
pm1004mCfgLabels = _Pm1004mCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 3)
)
_Pm1004mCfgLabelclientTable_Object = MibTable
pm1004mCfgLabelclientTable = _Pm1004mCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm1004mCfgLabelclientTable.setStatus("current")
_Pm1004mCfgLabelclientEntry_Object = MibTableRow
pm1004mCfgLabelclientEntry = _Pm1004mCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 3, 1, 1)
)
pm1004mCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCfgLabelclientEntry.setStatus("current")


class _Pm1004mCfgLabelclientIndex_Type(Integer32):
    """Custom type pm1004mCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1004mCfgLabelclientIndex_Object = MibTableColumn
pm1004mCfgLabelclientIndex = _Pm1004mCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 3, 1, 1, 1),
    _Pm1004mCfgLabelclientIndex_Type()
)
pm1004mCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgLabelclientIndex.setStatus("current")


class _Pm1004mCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1004mCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004mCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1004mCfgLabelclientPortn_Object = MibTableColumn
pm1004mCfgLabelclientPortn = _Pm1004mCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 3, 1, 1, 3),
    _Pm1004mCfgLabelclientPortn_Type()
)
pm1004mCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgLabelclientPortn.setStatus("current")
_Pm1004mCfgLabellineTable_Object = MibTable
pm1004mCfgLabellineTable = _Pm1004mCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm1004mCfgLabellineTable.setStatus("current")
_Pm1004mCfgLabellineEntry_Object = MibTableRow
pm1004mCfgLabellineEntry = _Pm1004mCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 3, 2, 1)
)
pm1004mCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCfgLabellineEntry.setStatus("current")


class _Pm1004mCfgLabellineIndex_Type(Integer32):
    """Custom type pm1004mCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1004mCfgLabellineIndex_Object = MibTableColumn
pm1004mCfgLabellineIndex = _Pm1004mCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 3, 2, 1, 1),
    _Pm1004mCfgLabellineIndex_Type()
)
pm1004mCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgLabellineIndex.setStatus("current")


class _Pm1004mCfgLabellinePortn_Type(DisplayString):
    """Custom type pm1004mCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004mCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1004mCfgLabellinePortn_Object = MibTableColumn
pm1004mCfgLabellinePortn = _Pm1004mCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 3, 2, 1, 3),
    _Pm1004mCfgLabellinePortn_Type()
)
pm1004mCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgLabellinePortn.setStatus("current")
_Pm1004mCfgModPerfConfig_ObjectIdentity = ObjectIdentity
pm1004mCfgModPerfConfig = _Pm1004mCfgModPerfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 4)
)
_Pm1004mtablemodPerfConfig_ObjectIdentity = ObjectIdentity
pm1004mtablemodPerfConfig = _Pm1004mtablemodPerfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 4, 1)
)


class _Pm1004mCfgperfMode_Type(Unsigned32):
    """Custom type pm1004mCfgperfMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgperfMode_Type.__name__ = "Unsigned32"
_Pm1004mCfgperfMode_Object = MibScalar
pm1004mCfgperfMode = _Pm1004mCfgperfMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 4, 1, 2),
    _Pm1004mCfgperfMode_Type()
)
pm1004mCfgperfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgperfMode.setStatus("current")
_Pm1004mCfgJ0Client_ObjectIdentity = ObjectIdentity
pm1004mCfgJ0Client = _Pm1004mCfgJ0Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 5)
)
_Pm1004mCfgEmptyTable_Object = MibTable
pm1004mCfgEmptyTable = _Pm1004mCfgEmptyTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pm1004mCfgEmptyTable.setStatus("current")
_Pm1004mCfgEmptyEntry_Object = MibTableRow
pm1004mCfgEmptyEntry = _Pm1004mCfgEmptyEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 5, 1, 1)
)
pm1004mCfgEmptyEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCfgEmptyIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCfgEmptyEntry.setStatus("current")


class _Pm1004mCfgEmptyIndex_Type(Integer32):
    """Custom type pm1004mCfgEmptyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCfgEmptyIndex_Type.__name__ = "Integer32"
_Pm1004mCfgEmptyIndex_Object = MibTableColumn
pm1004mCfgEmptyIndex = _Pm1004mCfgEmptyIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 5, 1, 1, 1),
    _Pm1004mCfgEmptyIndex_Type()
)
pm1004mCfgEmptyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgEmptyIndex.setStatus("current")


class _Pm1004mCfgClientExpectJ0SetupPortn_Type(Unsigned32):
    """Custom type pm1004mCfgClientExpectJ0SetupPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgClientExpectJ0SetupPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgClientExpectJ0SetupPortn_Object = MibTableColumn
pm1004mCfgClientExpectJ0SetupPortn = _Pm1004mCfgClientExpectJ0SetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 5, 1, 1, 3),
    _Pm1004mCfgClientExpectJ0SetupPortn_Type()
)
pm1004mCfgClientExpectJ0SetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgClientExpectJ0SetupPortn.setStatus("current")
_Pm1004mCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm1004mCfgStartuptlh = _Pm1004mCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6)
)
_Pm1004mCfgOtxtlhTable_Object = MibTable
pm1004mCfgOtxtlhTable = _Pm1004mCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm1004mCfgOtxtlhTable.setStatus("current")
_Pm1004mCfgOtxtlhEntry_Object = MibTableRow
pm1004mCfgOtxtlhEntry = _Pm1004mCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1)
)
pm1004mCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCfgOtxtlhEntry.setStatus("current")


class _Pm1004mCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm1004mCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm1004mCfgOtxtlhIndex_Object = MibTableColumn
pm1004mCfgOtxtlhIndex = _Pm1004mCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 1),
    _Pm1004mCfgOtxtlhIndex_Type()
)
pm1004mCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgOtxtlhIndex.setStatus("current")


class _Pm1004mCfgNuPortn_Type(Unsigned32):
    """Custom type pm1004mCfgNuPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgNuPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgNuPortn_Object = MibTableColumn
pm1004mCfgNuPortn = _Pm1004mCfgNuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 3),
    _Pm1004mCfgNuPortn_Type()
)
pm1004mCfgNuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgNuPortn.setStatus("deprecated")


class _Pm1004mCfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pm1004mCfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgLineDitherRatePortn_Object = MibTableColumn
pm1004mCfgLineDitherRatePortn = _Pm1004mCfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 4),
    _Pm1004mCfgLineDitherRatePortn_Type()
)
pm1004mCfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgLineDitherRatePortn.setStatus("current")


class _Pm1004mCfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pm1004mCfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgLineDitherFhzPortn_Object = MibTableColumn
pm1004mCfgLineDitherFhzPortn = _Pm1004mCfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 5),
    _Pm1004mCfgLineDitherFhzPortn_Type()
)
pm1004mCfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgLineDitherFhzPortn.setStatus("current")


class _Pm1004mCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm1004mCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgLinePwrLaserPortn_Object = MibTableColumn
pm1004mCfgLinePwrLaserPortn = _Pm1004mCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 6),
    _Pm1004mCfgLinePwrLaserPortn_Type()
)
pm1004mCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgLinePwrLaserPortn.setStatus("current")


class _Pm1004mCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm1004mCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgLineFCurrentPortn_Object = MibTableColumn
pm1004mCfgLineFCurrentPortn = _Pm1004mCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 7),
    _Pm1004mCfgLineFCurrentPortn_Type()
)
pm1004mCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgLineFCurrentPortn.setStatus("current")


class _Pm1004mCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm1004mCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgLineGridCurrentPortn_Object = MibTableColumn
pm1004mCfgLineGridCurrentPortn = _Pm1004mCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 8),
    _Pm1004mCfgLineGridCurrentPortn_Type()
)
pm1004mCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgLineGridCurrentPortn.setStatus("current")


class _Pm1004mCfgFPortn_Type(Unsigned32):
    """Custom type pm1004mCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgFPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgFPortn_Object = MibTableColumn
pm1004mCfgFPortn = _Pm1004mCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 9),
    _Pm1004mCfgFPortn_Type()
)
pm1004mCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgFPortn.setStatus("current")


class _Pm1004mCfgReservedPortn_Type(Unsigned32):
    """Custom type pm1004mCfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgReservedPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgReservedPortn_Object = MibTableColumn
pm1004mCfgReservedPortn = _Pm1004mCfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 10),
    _Pm1004mCfgReservedPortn_Type()
)
pm1004mCfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgReservedPortn.setStatus("deprecated")


class _Pm1004mCfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pm1004mCfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgLinePhotodiodeModePortn_Object = MibTableColumn
pm1004mCfgLinePhotodiodeModePortn = _Pm1004mCfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 11),
    _Pm1004mCfgLinePhotodiodeModePortn_Type()
)
pm1004mCfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgLinePhotodiodeModePortn.setStatus("current")


class _Pm1004mCfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pm1004mCfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgLinePhotodiodeValuePortn_Object = MibTableColumn
pm1004mCfgLinePhotodiodeValuePortn = _Pm1004mCfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 6, 1, 1, 12),
    _Pm1004mCfgLinePhotodiodeValuePortn_Type()
)
pm1004mCfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgLinePhotodiodeValuePortn.setStatus("current")
_Pm1004mCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm1004mCfgStartuptablefive = _Pm1004mCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 7)
)
_Pm1004mCfgOtxtlhcapabilitiesTable_Object = MibTable
pm1004mCfgOtxtlhcapabilitiesTable = _Pm1004mCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 7, 1)
)
if mibBuilder.loadTexts:
    pm1004mCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm1004mCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm1004mCfgOtxtlhcapabilitiesEntry = _Pm1004mCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 7, 1, 1)
)
pm1004mCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm1004mCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm1004mCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm1004mCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm1004mCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm1004mCfgOtxtlhcapabilitiesIndex = _Pm1004mCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 7, 1, 1, 1),
    _Pm1004mCfgOtxtlhcapabilitiesIndex_Type()
)
pm1004mCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm1004mCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm1004mCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgComponentTypePortn_Object = MibTableColumn
pm1004mCfgComponentTypePortn = _Pm1004mCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 7, 1, 1, 3),
    _Pm1004mCfgComponentTypePortn_Type()
)
pm1004mCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgComponentTypePortn.setStatus("current")


class _Pm1004mCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm1004mCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgMiscellaneousPortn_Object = MibTableColumn
pm1004mCfgMiscellaneousPortn = _Pm1004mCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 7, 1, 1, 4),
    _Pm1004mCfgMiscellaneousPortn_Type()
)
pm1004mCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgMiscellaneousPortn.setStatus("current")


class _Pm1004mCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm1004mCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgFirstChannelPortn_Object = MibTableColumn
pm1004mCfgFirstChannelPortn = _Pm1004mCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 7, 1, 1, 5),
    _Pm1004mCfgFirstChannelPortn_Type()
)
pm1004mCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgFirstChannelPortn.setStatus("current")


class _Pm1004mCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm1004mCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgLastChannelPortn_Object = MibTableColumn
pm1004mCfgLastChannelPortn = _Pm1004mCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 7, 1, 1, 6),
    _Pm1004mCfgLastChannelPortn_Type()
)
pm1004mCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgLastChannelPortn.setStatus("current")


class _Pm1004mCfgGridPortn_Type(Unsigned32):
    """Custom type pm1004mCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004mCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm1004mCfgGridPortn_Object = MibTableColumn
pm1004mCfgGridPortn = _Pm1004mCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 7, 1, 1, 7),
    _Pm1004mCfgGridPortn_Type()
)
pm1004mCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mCfgGridPortn.setStatus("current")
_Pm1004mCfgWriteConfiguration_Type = EkiOnOff
_Pm1004mCfgWriteConfiguration_Object = MibScalar
pm1004mCfgWriteConfiguration = _Pm1004mCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 9, 257),
    _Pm1004mCfgWriteConfiguration_Type()
)
pm1004mCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mCfgWriteConfiguration.setStatus("current")
_Pm1004mtraps_ObjectIdentity = ObjectIdentity
pm1004mtraps = _Pm1004mtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10)
)


class _Pm1004mtrapPortNumber_Type(Integer32):
    """Custom type pm1004mtrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004mtrapPortNumber_Type.__name__ = "Integer32"
_Pm1004mtrapPortNumber_Object = MibScalar
pm1004mtrapPortNumber = _Pm1004mtrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 2),
    _Pm1004mtrapPortNumber_Type()
)
pm1004mtrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mtrapPortNumber.setStatus("current")


class _Pm1004mtrapLineNumber_Type(Integer32):
    """Custom type pm1004mtrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004mtrapLineNumber_Type.__name__ = "Integer32"
_Pm1004mtrapLineNumber_Object = MibScalar
pm1004mtrapLineNumber = _Pm1004mtrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 3),
    _Pm1004mtrapLineNumber_Type()
)
pm1004mtrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mtrapLineNumber.setStatus("current")


class _Pm1004mtrapBoardNumber_Type(Integer32):
    """Custom type pm1004mtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004mtrapBoardNumber_Type.__name__ = "Integer32"
_Pm1004mtrapBoardNumber_Object = MibScalar
pm1004mtrapBoardNumber = _Pm1004mtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 4),
    _Pm1004mtrapBoardNumber_Type()
)
pm1004mtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mtrapBoardNumber.setStatus("current")
_Pm1004mMonitoring_ObjectIdentity = ObjectIdentity
pm1004mMonitoring = _Pm1004mMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11)
)
_Pm1004mMonOther_ObjectIdentity = ObjectIdentity
pm1004mMonOther = _Pm1004mMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1)
)
_Pm1004mMonSync_ObjectIdentity = ObjectIdentity
pm1004mMonSync = _Pm1004mMonSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 1)
)
_Pm1004mPerfEnable_Type = EkiOnOff
_Pm1004mPerfEnable_Object = MibScalar
pm1004mPerfEnable = _Pm1004mPerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 1, 257),
    _Pm1004mPerfEnable_Type()
)
pm1004mPerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mPerfEnable.setStatus("current")
_Pm1004mPerfSyncSource_Type = EkiSynchroMode
_Pm1004mPerfSyncSource_Object = MibScalar
pm1004mPerfSyncSource = _Pm1004mPerfSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 1, 258),
    _Pm1004mPerfSyncSource_Type()
)
pm1004mPerfSyncSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mPerfSyncSource.setStatus("current")
_Pm1004mPerf15minSync_Type = EkiOnOff
_Pm1004mPerf15minSync_Object = MibScalar
pm1004mPerf15minSync = _Pm1004mPerf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 1, 259),
    _Pm1004mPerf15minSync_Type()
)
pm1004mPerf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mPerf15minSync.setStatus("current")
_Pm1004mPerf24hSync_Type = EkiOnOff
_Pm1004mPerf24hSync_Object = MibScalar
pm1004mPerf24hSync = _Pm1004mPerf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 1, 260),
    _Pm1004mPerf24hSync_Type()
)
pm1004mPerf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mPerf24hSync.setStatus("current")
_Pm1004mMonTimeStamp_ObjectIdentity = ObjectIdentity
pm1004mMonTimeStamp = _Pm1004mMonTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 2)
)
_Pm1004mPerfCurrent15MinElapsedTime_Type = Counter32
_Pm1004mPerfCurrent15MinElapsedTime_Object = MibScalar
pm1004mPerfCurrent15MinElapsedTime = _Pm1004mPerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 2, 5),
    _Pm1004mPerfCurrent15MinElapsedTime_Type()
)
pm1004mPerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mPerfCurrent15MinElapsedTime.setStatus("current")
_Pm1004mPerfCurrent24HoursElapsedTime_Type = Counter32
_Pm1004mPerfCurrent24HoursElapsedTime_Object = MibScalar
pm1004mPerfCurrent24HoursElapsedTime = _Pm1004mPerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 2, 6),
    _Pm1004mPerfCurrent24HoursElapsedTime_Type()
)
pm1004mPerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mPerfCurrent24HoursElapsedTime.setStatus("current")
_Pm1004mPerfPast15MinElapsedTime_Type = Counter32
_Pm1004mPerfPast15MinElapsedTime_Object = MibScalar
pm1004mPerfPast15MinElapsedTime = _Pm1004mPerfPast15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 2, 7),
    _Pm1004mPerfPast15MinElapsedTime_Type()
)
pm1004mPerfPast15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mPerfPast15MinElapsedTime.setStatus("current")
_Pm1004mPerfPast24HoursElapsedTime_Type = Counter32
_Pm1004mPerfPast24HoursElapsedTime_Object = MibScalar
pm1004mPerfPast24HoursElapsedTime = _Pm1004mPerfPast24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 1, 2, 8),
    _Pm1004mPerfPast24HoursElapsedTime_Type()
)
pm1004mPerfPast24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004mPerfPast24HoursElapsedTime.setStatus("current")
_Pm1004mMonClient_ObjectIdentity = ObjectIdentity
pm1004mMonClient = _Pm1004mMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2)
)
_Pm1004mMonClientPerformance_ObjectIdentity = ObjectIdentity
pm1004mMonClientPerformance = _Pm1004mMonClientPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1)
)
_Pm1004mPerfUpCurrent15CntTable_Object = MibTable
pm1004mPerfUpCurrent15CntTable = _Pm1004mPerfUpCurrent15CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16)
)
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntTable.setStatus("current")
_Pm1004mPerfUpCurrent15CntEntry_Object = MibTableRow
pm1004mPerfUpCurrent15CntEntry = _Pm1004mPerfUpCurrent15CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1)
)
pm1004mPerfUpCurrent15CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mPerfUpCurrent15CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntEntry.setStatus("current")


class _Pm1004mPerfUpCurrent15CntIndex_Type(Integer32):
    """Custom type pm1004mPerfUpCurrent15CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mPerfUpCurrent15CntIndex_Type.__name__ = "Integer32"
_Pm1004mPerfUpCurrent15CntIndex_Object = MibTableColumn
pm1004mPerfUpCurrent15CntIndex = _Pm1004mPerfUpCurrent15CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 1),
    _Pm1004mPerfUpCurrent15CntIndex_Type()
)
pm1004mPerfUpCurrent15CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntIndex.setStatus("current")
_Pm1004mPerfUpCurrent15CntInvCvPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent15CntInvCvPortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntInvCvPortn = _Pm1004mPerfUpCurrent15CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 2),
    _Pm1004mPerfUpCurrent15CntInvCvPortn_Type()
)
pm1004mPerfUpCurrent15CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntInvCvPortn.setStatus("current")
_Pm1004mPerfUpCurrent15CntCvValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent15CntCvValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntCvValuePortn = _Pm1004mPerfUpCurrent15CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 3),
    _Pm1004mPerfUpCurrent15CntCvValuePortn_Type()
)
pm1004mPerfUpCurrent15CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntCvValuePortn.setStatus("current")
_Pm1004mPerfUpCurrent15CntInvEsPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent15CntInvEsPortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntInvEsPortn = _Pm1004mPerfUpCurrent15CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 4),
    _Pm1004mPerfUpCurrent15CntInvEsPortn_Type()
)
pm1004mPerfUpCurrent15CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntInvEsPortn.setStatus("current")
_Pm1004mPerfUpCurrent15CntEsValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent15CntEsValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntEsValuePortn = _Pm1004mPerfUpCurrent15CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 5),
    _Pm1004mPerfUpCurrent15CntEsValuePortn_Type()
)
pm1004mPerfUpCurrent15CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntEsValuePortn.setStatus("current")
_Pm1004mPerfUpCurrent15CntInvSesPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent15CntInvSesPortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntInvSesPortn = _Pm1004mPerfUpCurrent15CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 6),
    _Pm1004mPerfUpCurrent15CntInvSesPortn_Type()
)
pm1004mPerfUpCurrent15CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntInvSesPortn.setStatus("current")
_Pm1004mPerfUpCurrent15CntSesValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent15CntSesValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntSesValuePortn = _Pm1004mPerfUpCurrent15CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 7),
    _Pm1004mPerfUpCurrent15CntSesValuePortn_Type()
)
pm1004mPerfUpCurrent15CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntSesValuePortn.setStatus("current")
_Pm1004mPerfUpCurrent15CntInvSefsPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent15CntInvSefsPortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntInvSefsPortn = _Pm1004mPerfUpCurrent15CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 8),
    _Pm1004mPerfUpCurrent15CntInvSefsPortn_Type()
)
pm1004mPerfUpCurrent15CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntInvSefsPortn.setStatus("current")
_Pm1004mPerfUpCurrent15CntSefsValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent15CntSefsValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntSefsValuePortn = _Pm1004mPerfUpCurrent15CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 9),
    _Pm1004mPerfUpCurrent15CntSefsValuePortn_Type()
)
pm1004mPerfUpCurrent15CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntSefsValuePortn.setStatus("current")
_Pm1004mPerfUpCurrent15CntInvUasPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent15CntInvUasPortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntInvUasPortn = _Pm1004mPerfUpCurrent15CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 10),
    _Pm1004mPerfUpCurrent15CntInvUasPortn_Type()
)
pm1004mPerfUpCurrent15CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntInvUasPortn.setStatus("current")
_Pm1004mPerfUpCurrent15CntUasValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent15CntUasValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent15CntUasValuePortn = _Pm1004mPerfUpCurrent15CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 16, 1, 11),
    _Pm1004mPerfUpCurrent15CntUasValuePortn_Type()
)
pm1004mPerfUpCurrent15CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent15CntUasValuePortn.setStatus("current")
_Pm1004mPerfUpPast15CntTable_Object = MibTable
pm1004mPerfUpPast15CntTable = _Pm1004mPerfUpPast15CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24)
)
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntTable.setStatus("current")
_Pm1004mPerfUpPast15CntEntry_Object = MibTableRow
pm1004mPerfUpPast15CntEntry = _Pm1004mPerfUpPast15CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1)
)
pm1004mPerfUpPast15CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mPerfUpPast15CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntEntry.setStatus("current")


class _Pm1004mPerfUpPast15CntIndex_Type(Integer32):
    """Custom type pm1004mPerfUpPast15CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mPerfUpPast15CntIndex_Type.__name__ = "Integer32"
_Pm1004mPerfUpPast15CntIndex_Object = MibTableColumn
pm1004mPerfUpPast15CntIndex = _Pm1004mPerfUpPast15CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 1),
    _Pm1004mPerfUpPast15CntIndex_Type()
)
pm1004mPerfUpPast15CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntIndex.setStatus("current")
_Pm1004mPerfUpPast15CntInvCvPortn_Type = EkiOnOff
_Pm1004mPerfUpPast15CntInvCvPortn_Object = MibTableColumn
pm1004mPerfUpPast15CntInvCvPortn = _Pm1004mPerfUpPast15CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 2),
    _Pm1004mPerfUpPast15CntInvCvPortn_Type()
)
pm1004mPerfUpPast15CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntInvCvPortn.setStatus("current")
_Pm1004mPerfUpPast15CntCvValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast15CntCvValuePortn_Object = MibTableColumn
pm1004mPerfUpPast15CntCvValuePortn = _Pm1004mPerfUpPast15CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 3),
    _Pm1004mPerfUpPast15CntCvValuePortn_Type()
)
pm1004mPerfUpPast15CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntCvValuePortn.setStatus("current")
_Pm1004mPerfUpPast15CntInvEsPortn_Type = EkiOnOff
_Pm1004mPerfUpPast15CntInvEsPortn_Object = MibTableColumn
pm1004mPerfUpPast15CntInvEsPortn = _Pm1004mPerfUpPast15CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 4),
    _Pm1004mPerfUpPast15CntInvEsPortn_Type()
)
pm1004mPerfUpPast15CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntInvEsPortn.setStatus("current")
_Pm1004mPerfUpPast15CntEsValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast15CntEsValuePortn_Object = MibTableColumn
pm1004mPerfUpPast15CntEsValuePortn = _Pm1004mPerfUpPast15CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 5),
    _Pm1004mPerfUpPast15CntEsValuePortn_Type()
)
pm1004mPerfUpPast15CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntEsValuePortn.setStatus("current")
_Pm1004mPerfUpPast15CntInvSesPortn_Type = EkiOnOff
_Pm1004mPerfUpPast15CntInvSesPortn_Object = MibTableColumn
pm1004mPerfUpPast15CntInvSesPortn = _Pm1004mPerfUpPast15CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 6),
    _Pm1004mPerfUpPast15CntInvSesPortn_Type()
)
pm1004mPerfUpPast15CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntInvSesPortn.setStatus("current")
_Pm1004mPerfUpPast15CntSesValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast15CntSesValuePortn_Object = MibTableColumn
pm1004mPerfUpPast15CntSesValuePortn = _Pm1004mPerfUpPast15CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 7),
    _Pm1004mPerfUpPast15CntSesValuePortn_Type()
)
pm1004mPerfUpPast15CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntSesValuePortn.setStatus("current")
_Pm1004mPerfUpPast15CntInvSefsPortn_Type = EkiOnOff
_Pm1004mPerfUpPast15CntInvSefsPortn_Object = MibTableColumn
pm1004mPerfUpPast15CntInvSefsPortn = _Pm1004mPerfUpPast15CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 8),
    _Pm1004mPerfUpPast15CntInvSefsPortn_Type()
)
pm1004mPerfUpPast15CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntInvSefsPortn.setStatus("current")
_Pm1004mPerfUpPast15CntSefsValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast15CntSefsValuePortn_Object = MibTableColumn
pm1004mPerfUpPast15CntSefsValuePortn = _Pm1004mPerfUpPast15CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 9),
    _Pm1004mPerfUpPast15CntSefsValuePortn_Type()
)
pm1004mPerfUpPast15CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntSefsValuePortn.setStatus("current")
_Pm1004mPerfUpPast15CntInvUasPortn_Type = EkiOnOff
_Pm1004mPerfUpPast15CntInvUasPortn_Object = MibTableColumn
pm1004mPerfUpPast15CntInvUasPortn = _Pm1004mPerfUpPast15CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 10),
    _Pm1004mPerfUpPast15CntInvUasPortn_Type()
)
pm1004mPerfUpPast15CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntInvUasPortn.setStatus("current")
_Pm1004mPerfUpPast15CntUasValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast15CntUasValuePortn_Object = MibTableColumn
pm1004mPerfUpPast15CntUasValuePortn = _Pm1004mPerfUpPast15CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 24, 1, 11),
    _Pm1004mPerfUpPast15CntUasValuePortn_Type()
)
pm1004mPerfUpPast15CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast15CntUasValuePortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntTable_Object = MibTable
pm1004mPerfUpCurrent24CntTable = _Pm1004mPerfUpCurrent24CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32)
)
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntTable.setStatus("current")
_Pm1004mPerfUpCurrent24CntEntry_Object = MibTableRow
pm1004mPerfUpCurrent24CntEntry = _Pm1004mPerfUpCurrent24CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1)
)
pm1004mPerfUpCurrent24CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mPerfUpCurrent24CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntEntry.setStatus("current")


class _Pm1004mPerfUpCurrent24CntIndex_Type(Integer32):
    """Custom type pm1004mPerfUpCurrent24CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mPerfUpCurrent24CntIndex_Type.__name__ = "Integer32"
_Pm1004mPerfUpCurrent24CntIndex_Object = MibTableColumn
pm1004mPerfUpCurrent24CntIndex = _Pm1004mPerfUpCurrent24CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 1),
    _Pm1004mPerfUpCurrent24CntIndex_Type()
)
pm1004mPerfUpCurrent24CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntIndex.setStatus("current")
_Pm1004mPerfUpCurrent24CntInvCvPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent24CntInvCvPortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntInvCvPortn = _Pm1004mPerfUpCurrent24CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 2),
    _Pm1004mPerfUpCurrent24CntInvCvPortn_Type()
)
pm1004mPerfUpCurrent24CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntInvCvPortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntCvValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent24CntCvValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntCvValuePortn = _Pm1004mPerfUpCurrent24CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 3),
    _Pm1004mPerfUpCurrent24CntCvValuePortn_Type()
)
pm1004mPerfUpCurrent24CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntCvValuePortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntInvEsPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent24CntInvEsPortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntInvEsPortn = _Pm1004mPerfUpCurrent24CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 4),
    _Pm1004mPerfUpCurrent24CntInvEsPortn_Type()
)
pm1004mPerfUpCurrent24CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntInvEsPortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntEsValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent24CntEsValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntEsValuePortn = _Pm1004mPerfUpCurrent24CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 5),
    _Pm1004mPerfUpCurrent24CntEsValuePortn_Type()
)
pm1004mPerfUpCurrent24CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntEsValuePortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntInvSesPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent24CntInvSesPortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntInvSesPortn = _Pm1004mPerfUpCurrent24CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 6),
    _Pm1004mPerfUpCurrent24CntInvSesPortn_Type()
)
pm1004mPerfUpCurrent24CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntInvSesPortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntSesValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent24CntSesValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntSesValuePortn = _Pm1004mPerfUpCurrent24CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 7),
    _Pm1004mPerfUpCurrent24CntSesValuePortn_Type()
)
pm1004mPerfUpCurrent24CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntSesValuePortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntInvSefsPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent24CntInvSefsPortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntInvSefsPortn = _Pm1004mPerfUpCurrent24CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 8),
    _Pm1004mPerfUpCurrent24CntInvSefsPortn_Type()
)
pm1004mPerfUpCurrent24CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntInvSefsPortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntSefsValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent24CntSefsValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntSefsValuePortn = _Pm1004mPerfUpCurrent24CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 9),
    _Pm1004mPerfUpCurrent24CntSefsValuePortn_Type()
)
pm1004mPerfUpCurrent24CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntSefsValuePortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntInvUasPortn_Type = EkiOnOff
_Pm1004mPerfUpCurrent24CntInvUasPortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntInvUasPortn = _Pm1004mPerfUpCurrent24CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 10),
    _Pm1004mPerfUpCurrent24CntInvUasPortn_Type()
)
pm1004mPerfUpCurrent24CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntInvUasPortn.setStatus("current")
_Pm1004mPerfUpCurrent24CntUasValuePortn_Type = Unsigned32
_Pm1004mPerfUpCurrent24CntUasValuePortn_Object = MibTableColumn
pm1004mPerfUpCurrent24CntUasValuePortn = _Pm1004mPerfUpCurrent24CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 32, 1, 11),
    _Pm1004mPerfUpCurrent24CntUasValuePortn_Type()
)
pm1004mPerfUpCurrent24CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpCurrent24CntUasValuePortn.setStatus("current")
_Pm1004mPerfUpPast24CntTable_Object = MibTable
pm1004mPerfUpPast24CntTable = _Pm1004mPerfUpPast24CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40)
)
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntTable.setStatus("current")
_Pm1004mPerfUpPast24CntEntry_Object = MibTableRow
pm1004mPerfUpPast24CntEntry = _Pm1004mPerfUpPast24CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1)
)
pm1004mPerfUpPast24CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mPerfUpPast24CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntEntry.setStatus("current")


class _Pm1004mPerfUpPast24CntIndex_Type(Integer32):
    """Custom type pm1004mPerfUpPast24CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mPerfUpPast24CntIndex_Type.__name__ = "Integer32"
_Pm1004mPerfUpPast24CntIndex_Object = MibTableColumn
pm1004mPerfUpPast24CntIndex = _Pm1004mPerfUpPast24CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 1),
    _Pm1004mPerfUpPast24CntIndex_Type()
)
pm1004mPerfUpPast24CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntIndex.setStatus("current")
_Pm1004mPerfUpPast24CntInvCvPortn_Type = EkiOnOff
_Pm1004mPerfUpPast24CntInvCvPortn_Object = MibTableColumn
pm1004mPerfUpPast24CntInvCvPortn = _Pm1004mPerfUpPast24CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 2),
    _Pm1004mPerfUpPast24CntInvCvPortn_Type()
)
pm1004mPerfUpPast24CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntInvCvPortn.setStatus("current")
_Pm1004mPerfUpPast24CntCvValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast24CntCvValuePortn_Object = MibTableColumn
pm1004mPerfUpPast24CntCvValuePortn = _Pm1004mPerfUpPast24CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 3),
    _Pm1004mPerfUpPast24CntCvValuePortn_Type()
)
pm1004mPerfUpPast24CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntCvValuePortn.setStatus("current")
_Pm1004mPerfUpPast24CntInvEsPortn_Type = EkiOnOff
_Pm1004mPerfUpPast24CntInvEsPortn_Object = MibTableColumn
pm1004mPerfUpPast24CntInvEsPortn = _Pm1004mPerfUpPast24CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 4),
    _Pm1004mPerfUpPast24CntInvEsPortn_Type()
)
pm1004mPerfUpPast24CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntInvEsPortn.setStatus("current")
_Pm1004mPerfUpPast24CntEsValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast24CntEsValuePortn_Object = MibTableColumn
pm1004mPerfUpPast24CntEsValuePortn = _Pm1004mPerfUpPast24CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 5),
    _Pm1004mPerfUpPast24CntEsValuePortn_Type()
)
pm1004mPerfUpPast24CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntEsValuePortn.setStatus("current")
_Pm1004mPerfUpPast24CntInvSesPortn_Type = EkiOnOff
_Pm1004mPerfUpPast24CntInvSesPortn_Object = MibTableColumn
pm1004mPerfUpPast24CntInvSesPortn = _Pm1004mPerfUpPast24CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 6),
    _Pm1004mPerfUpPast24CntInvSesPortn_Type()
)
pm1004mPerfUpPast24CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntInvSesPortn.setStatus("current")
_Pm1004mPerfUpPast24CntSesValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast24CntSesValuePortn_Object = MibTableColumn
pm1004mPerfUpPast24CntSesValuePortn = _Pm1004mPerfUpPast24CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 7),
    _Pm1004mPerfUpPast24CntSesValuePortn_Type()
)
pm1004mPerfUpPast24CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntSesValuePortn.setStatus("current")
_Pm1004mPerfUpPast24CntInvSefsPortn_Type = EkiOnOff
_Pm1004mPerfUpPast24CntInvSefsPortn_Object = MibTableColumn
pm1004mPerfUpPast24CntInvSefsPortn = _Pm1004mPerfUpPast24CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 8),
    _Pm1004mPerfUpPast24CntInvSefsPortn_Type()
)
pm1004mPerfUpPast24CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntInvSefsPortn.setStatus("current")
_Pm1004mPerfUpPast24CntSefsValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast24CntSefsValuePortn_Object = MibTableColumn
pm1004mPerfUpPast24CntSefsValuePortn = _Pm1004mPerfUpPast24CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 9),
    _Pm1004mPerfUpPast24CntSefsValuePortn_Type()
)
pm1004mPerfUpPast24CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntSefsValuePortn.setStatus("current")
_Pm1004mPerfUpPast24CntInvUasPortn_Type = EkiOnOff
_Pm1004mPerfUpPast24CntInvUasPortn_Object = MibTableColumn
pm1004mPerfUpPast24CntInvUasPortn = _Pm1004mPerfUpPast24CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 10),
    _Pm1004mPerfUpPast24CntInvUasPortn_Type()
)
pm1004mPerfUpPast24CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntInvUasPortn.setStatus("current")
_Pm1004mPerfUpPast24CntUasValuePortn_Type = Unsigned32
_Pm1004mPerfUpPast24CntUasValuePortn_Object = MibTableColumn
pm1004mPerfUpPast24CntUasValuePortn = _Pm1004mPerfUpPast24CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 1, 40, 1, 11),
    _Pm1004mPerfUpPast24CntUasValuePortn_Type()
)
pm1004mPerfUpPast24CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfUpPast24CntUasValuePortn.setStatus("current")
_Pm1004mMonClientTraceIdentifier_ObjectIdentity = ObjectIdentity
pm1004mMonClientTraceIdentifier = _Pm1004mMonClientTraceIdentifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 2)
)
_Pm1004mAlmj0AlarmTable_Object = MibTable
pm1004mAlmj0AlarmTable = _Pm1004mAlmj0AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 2, 2112)
)
if mibBuilder.loadTexts:
    pm1004mAlmj0AlarmTable.setStatus("current")
_Pm1004mAlmj0AlarmEntry_Object = MibTableRow
pm1004mAlmj0AlarmEntry = _Pm1004mAlmj0AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 2, 2112, 1)
)
pm1004mAlmj0AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mAlmj0AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004mAlmj0AlarmEntry.setStatus("current")


class _Pm1004mAlmj0AlarmIndex_Type(Integer32):
    """Custom type pm1004mAlmj0AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mAlmj0AlarmIndex_Type.__name__ = "Integer32"
_Pm1004mAlmj0AlarmIndex_Object = MibTableColumn
pm1004mAlmj0AlarmIndex = _Pm1004mAlmj0AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 2, 2112, 1, 1),
    _Pm1004mAlmj0AlarmIndex_Type()
)
pm1004mAlmj0AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmj0AlarmIndex.setStatus("current")
_Pm1004mAlmJ0TimAlarmPortn_Type = EkiOnOff
_Pm1004mAlmJ0TimAlarmPortn_Object = MibTableColumn
pm1004mAlmJ0TimAlarmPortn = _Pm1004mAlmJ0TimAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 2, 2112, 1, 2),
    _Pm1004mAlmJ0TimAlarmPortn_Type()
)
pm1004mAlmJ0TimAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmJ0TimAlarmPortn.setStatus("current")
_Pm1004mAlmJ0TiiAlarmPortn_Type = EkiOnOff
_Pm1004mAlmJ0TiiAlarmPortn_Object = MibTableColumn
pm1004mAlmJ0TiiAlarmPortn = _Pm1004mAlmJ0TiiAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 2, 2112, 1, 3),
    _Pm1004mAlmJ0TiiAlarmPortn_Type()
)
pm1004mAlmJ0TiiAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmJ0TiiAlarmPortn.setStatus("current")
_Pm1004mAlmCrc7ErrorPortn_Type = EkiOnOff
_Pm1004mAlmCrc7ErrorPortn_Object = MibTableColumn
pm1004mAlmCrc7ErrorPortn = _Pm1004mAlmCrc7ErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 2, 2, 2112, 1, 4),
    _Pm1004mAlmCrc7ErrorPortn_Type()
)
pm1004mAlmCrc7ErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mAlmCrc7ErrorPortn.setStatus("current")
_Pm1004mMonLine_ObjectIdentity = ObjectIdentity
pm1004mMonLine = _Pm1004mMonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3)
)
_Pm1004mMonLinePerformance_ObjectIdentity = ObjectIdentity
pm1004mMonLinePerformance = _Pm1004mMonLinePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1)
)
_Pm1004mPerfLineCurrent15CntTable_Object = MibTable
pm1004mPerfLineCurrent15CntTable = _Pm1004mPerfLineCurrent15CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128)
)
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntTable.setStatus("current")
_Pm1004mPerfLineCurrent15CntEntry_Object = MibTableRow
pm1004mPerfLineCurrent15CntEntry = _Pm1004mPerfLineCurrent15CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1)
)
pm1004mPerfLineCurrent15CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mPerfLineCurrent15CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntEntry.setStatus("current")


class _Pm1004mPerfLineCurrent15CntIndex_Type(Integer32):
    """Custom type pm1004mPerfLineCurrent15CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mPerfLineCurrent15CntIndex_Type.__name__ = "Integer32"
_Pm1004mPerfLineCurrent15CntIndex_Object = MibTableColumn
pm1004mPerfLineCurrent15CntIndex = _Pm1004mPerfLineCurrent15CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 1),
    _Pm1004mPerfLineCurrent15CntIndex_Type()
)
pm1004mPerfLineCurrent15CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntIndex.setStatus("current")
_Pm1004mPerfLineCurrent15CntInvCvPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent15CntInvCvPortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntInvCvPortn = _Pm1004mPerfLineCurrent15CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 2),
    _Pm1004mPerfLineCurrent15CntInvCvPortn_Type()
)
pm1004mPerfLineCurrent15CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntInvCvPortn.setStatus("current")
_Pm1004mPerfLineCurrent15CntCvValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent15CntCvValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntCvValuePortn = _Pm1004mPerfLineCurrent15CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 3),
    _Pm1004mPerfLineCurrent15CntCvValuePortn_Type()
)
pm1004mPerfLineCurrent15CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntCvValuePortn.setStatus("current")
_Pm1004mPerfLineCurrent15CntInvEsPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent15CntInvEsPortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntInvEsPortn = _Pm1004mPerfLineCurrent15CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 4),
    _Pm1004mPerfLineCurrent15CntInvEsPortn_Type()
)
pm1004mPerfLineCurrent15CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntInvEsPortn.setStatus("current")
_Pm1004mPerfLineCurrent15CntEsValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent15CntEsValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntEsValuePortn = _Pm1004mPerfLineCurrent15CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 5),
    _Pm1004mPerfLineCurrent15CntEsValuePortn_Type()
)
pm1004mPerfLineCurrent15CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntEsValuePortn.setStatus("current")
_Pm1004mPerfLineCurrent15CntInvSesPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent15CntInvSesPortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntInvSesPortn = _Pm1004mPerfLineCurrent15CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 6),
    _Pm1004mPerfLineCurrent15CntInvSesPortn_Type()
)
pm1004mPerfLineCurrent15CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntInvSesPortn.setStatus("current")
_Pm1004mPerfLineCurrent15CntSesValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent15CntSesValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntSesValuePortn = _Pm1004mPerfLineCurrent15CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 7),
    _Pm1004mPerfLineCurrent15CntSesValuePortn_Type()
)
pm1004mPerfLineCurrent15CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntSesValuePortn.setStatus("current")
_Pm1004mPerfLineCurrent15CntInvSefsPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent15CntInvSefsPortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntInvSefsPortn = _Pm1004mPerfLineCurrent15CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 8),
    _Pm1004mPerfLineCurrent15CntInvSefsPortn_Type()
)
pm1004mPerfLineCurrent15CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntInvSefsPortn.setStatus("current")
_Pm1004mPerfLineCurrent15CntSefsValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent15CntSefsValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntSefsValuePortn = _Pm1004mPerfLineCurrent15CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 9),
    _Pm1004mPerfLineCurrent15CntSefsValuePortn_Type()
)
pm1004mPerfLineCurrent15CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntSefsValuePortn.setStatus("current")
_Pm1004mPerfLineCurrent15CntInvUasPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent15CntInvUasPortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntInvUasPortn = _Pm1004mPerfLineCurrent15CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 10),
    _Pm1004mPerfLineCurrent15CntInvUasPortn_Type()
)
pm1004mPerfLineCurrent15CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntInvUasPortn.setStatus("current")
_Pm1004mPerfLineCurrent15CntUasValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent15CntUasValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent15CntUasValuePortn = _Pm1004mPerfLineCurrent15CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 128, 1, 11),
    _Pm1004mPerfLineCurrent15CntUasValuePortn_Type()
)
pm1004mPerfLineCurrent15CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent15CntUasValuePortn.setStatus("current")
_Pm1004mPerfLinePast15CntTable_Object = MibTable
pm1004mPerfLinePast15CntTable = _Pm1004mPerfLinePast15CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129)
)
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntTable.setStatus("current")
_Pm1004mPerfLinePast15CntEntry_Object = MibTableRow
pm1004mPerfLinePast15CntEntry = _Pm1004mPerfLinePast15CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1)
)
pm1004mPerfLinePast15CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mPerfLinePast15CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntEntry.setStatus("current")


class _Pm1004mPerfLinePast15CntIndex_Type(Integer32):
    """Custom type pm1004mPerfLinePast15CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mPerfLinePast15CntIndex_Type.__name__ = "Integer32"
_Pm1004mPerfLinePast15CntIndex_Object = MibTableColumn
pm1004mPerfLinePast15CntIndex = _Pm1004mPerfLinePast15CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 1),
    _Pm1004mPerfLinePast15CntIndex_Type()
)
pm1004mPerfLinePast15CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntIndex.setStatus("current")
_Pm1004mPerfLinePast15CntInvCvPortn_Type = EkiOnOff
_Pm1004mPerfLinePast15CntInvCvPortn_Object = MibTableColumn
pm1004mPerfLinePast15CntInvCvPortn = _Pm1004mPerfLinePast15CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 2),
    _Pm1004mPerfLinePast15CntInvCvPortn_Type()
)
pm1004mPerfLinePast15CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntInvCvPortn.setStatus("current")
_Pm1004mPerfLinePast15CntCvValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast15CntCvValuePortn_Object = MibTableColumn
pm1004mPerfLinePast15CntCvValuePortn = _Pm1004mPerfLinePast15CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 3),
    _Pm1004mPerfLinePast15CntCvValuePortn_Type()
)
pm1004mPerfLinePast15CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntCvValuePortn.setStatus("current")
_Pm1004mPerfLinePast15CntInvEsPortn_Type = EkiOnOff
_Pm1004mPerfLinePast15CntInvEsPortn_Object = MibTableColumn
pm1004mPerfLinePast15CntInvEsPortn = _Pm1004mPerfLinePast15CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 4),
    _Pm1004mPerfLinePast15CntInvEsPortn_Type()
)
pm1004mPerfLinePast15CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntInvEsPortn.setStatus("current")
_Pm1004mPerfLinePast15CntEsValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast15CntEsValuePortn_Object = MibTableColumn
pm1004mPerfLinePast15CntEsValuePortn = _Pm1004mPerfLinePast15CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 5),
    _Pm1004mPerfLinePast15CntEsValuePortn_Type()
)
pm1004mPerfLinePast15CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntEsValuePortn.setStatus("current")
_Pm1004mPerfLinePast15CntInvSesPortn_Type = EkiOnOff
_Pm1004mPerfLinePast15CntInvSesPortn_Object = MibTableColumn
pm1004mPerfLinePast15CntInvSesPortn = _Pm1004mPerfLinePast15CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 6),
    _Pm1004mPerfLinePast15CntInvSesPortn_Type()
)
pm1004mPerfLinePast15CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntInvSesPortn.setStatus("current")
_Pm1004mPerfLinePast15CntSesValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast15CntSesValuePortn_Object = MibTableColumn
pm1004mPerfLinePast15CntSesValuePortn = _Pm1004mPerfLinePast15CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 7),
    _Pm1004mPerfLinePast15CntSesValuePortn_Type()
)
pm1004mPerfLinePast15CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntSesValuePortn.setStatus("current")
_Pm1004mPerfLinePast15CntInvSefsPortn_Type = EkiOnOff
_Pm1004mPerfLinePast15CntInvSefsPortn_Object = MibTableColumn
pm1004mPerfLinePast15CntInvSefsPortn = _Pm1004mPerfLinePast15CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 8),
    _Pm1004mPerfLinePast15CntInvSefsPortn_Type()
)
pm1004mPerfLinePast15CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntInvSefsPortn.setStatus("current")
_Pm1004mPerfLinePast15CntSefsValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast15CntSefsValuePortn_Object = MibTableColumn
pm1004mPerfLinePast15CntSefsValuePortn = _Pm1004mPerfLinePast15CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 9),
    _Pm1004mPerfLinePast15CntSefsValuePortn_Type()
)
pm1004mPerfLinePast15CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntSefsValuePortn.setStatus("current")
_Pm1004mPerfLinePast15CntInvUasPortn_Type = EkiOnOff
_Pm1004mPerfLinePast15CntInvUasPortn_Object = MibTableColumn
pm1004mPerfLinePast15CntInvUasPortn = _Pm1004mPerfLinePast15CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 10),
    _Pm1004mPerfLinePast15CntInvUasPortn_Type()
)
pm1004mPerfLinePast15CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntInvUasPortn.setStatus("current")
_Pm1004mPerfLinePast15CntUasValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast15CntUasValuePortn_Object = MibTableColumn
pm1004mPerfLinePast15CntUasValuePortn = _Pm1004mPerfLinePast15CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 129, 1, 11),
    _Pm1004mPerfLinePast15CntUasValuePortn_Type()
)
pm1004mPerfLinePast15CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast15CntUasValuePortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntTable_Object = MibTable
pm1004mPerfLineCurrent24CntTable = _Pm1004mPerfLineCurrent24CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130)
)
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntTable.setStatus("current")
_Pm1004mPerfLineCurrent24CntEntry_Object = MibTableRow
pm1004mPerfLineCurrent24CntEntry = _Pm1004mPerfLineCurrent24CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1)
)
pm1004mPerfLineCurrent24CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mPerfLineCurrent24CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntEntry.setStatus("current")


class _Pm1004mPerfLineCurrent24CntIndex_Type(Integer32):
    """Custom type pm1004mPerfLineCurrent24CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mPerfLineCurrent24CntIndex_Type.__name__ = "Integer32"
_Pm1004mPerfLineCurrent24CntIndex_Object = MibTableColumn
pm1004mPerfLineCurrent24CntIndex = _Pm1004mPerfLineCurrent24CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 1),
    _Pm1004mPerfLineCurrent24CntIndex_Type()
)
pm1004mPerfLineCurrent24CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntIndex.setStatus("current")
_Pm1004mPerfLineCurrent24CntInvCvPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent24CntInvCvPortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntInvCvPortn = _Pm1004mPerfLineCurrent24CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 2),
    _Pm1004mPerfLineCurrent24CntInvCvPortn_Type()
)
pm1004mPerfLineCurrent24CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntInvCvPortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntCvValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent24CntCvValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntCvValuePortn = _Pm1004mPerfLineCurrent24CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 3),
    _Pm1004mPerfLineCurrent24CntCvValuePortn_Type()
)
pm1004mPerfLineCurrent24CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntCvValuePortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntInvEsPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent24CntInvEsPortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntInvEsPortn = _Pm1004mPerfLineCurrent24CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 4),
    _Pm1004mPerfLineCurrent24CntInvEsPortn_Type()
)
pm1004mPerfLineCurrent24CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntInvEsPortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntEsValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent24CntEsValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntEsValuePortn = _Pm1004mPerfLineCurrent24CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 5),
    _Pm1004mPerfLineCurrent24CntEsValuePortn_Type()
)
pm1004mPerfLineCurrent24CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntEsValuePortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntInvSesPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent24CntInvSesPortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntInvSesPortn = _Pm1004mPerfLineCurrent24CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 6),
    _Pm1004mPerfLineCurrent24CntInvSesPortn_Type()
)
pm1004mPerfLineCurrent24CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntInvSesPortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntSesValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent24CntSesValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntSesValuePortn = _Pm1004mPerfLineCurrent24CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 7),
    _Pm1004mPerfLineCurrent24CntSesValuePortn_Type()
)
pm1004mPerfLineCurrent24CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntSesValuePortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntInvSefsPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent24CntInvSefsPortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntInvSefsPortn = _Pm1004mPerfLineCurrent24CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 8),
    _Pm1004mPerfLineCurrent24CntInvSefsPortn_Type()
)
pm1004mPerfLineCurrent24CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntInvSefsPortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntSefsValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent24CntSefsValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntSefsValuePortn = _Pm1004mPerfLineCurrent24CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 9),
    _Pm1004mPerfLineCurrent24CntSefsValuePortn_Type()
)
pm1004mPerfLineCurrent24CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntSefsValuePortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntInvUasPortn_Type = EkiOnOff
_Pm1004mPerfLineCurrent24CntInvUasPortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntInvUasPortn = _Pm1004mPerfLineCurrent24CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 10),
    _Pm1004mPerfLineCurrent24CntInvUasPortn_Type()
)
pm1004mPerfLineCurrent24CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntInvUasPortn.setStatus("current")
_Pm1004mPerfLineCurrent24CntUasValuePortn_Type = Unsigned32
_Pm1004mPerfLineCurrent24CntUasValuePortn_Object = MibTableColumn
pm1004mPerfLineCurrent24CntUasValuePortn = _Pm1004mPerfLineCurrent24CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 130, 1, 11),
    _Pm1004mPerfLineCurrent24CntUasValuePortn_Type()
)
pm1004mPerfLineCurrent24CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLineCurrent24CntUasValuePortn.setStatus("current")
_Pm1004mPerfLinePast24CntTable_Object = MibTable
pm1004mPerfLinePast24CntTable = _Pm1004mPerfLinePast24CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131)
)
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntTable.setStatus("current")
_Pm1004mPerfLinePast24CntEntry_Object = MibTableRow
pm1004mPerfLinePast24CntEntry = _Pm1004mPerfLinePast24CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1)
)
pm1004mPerfLinePast24CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004m-MIB", "pm1004mPerfLinePast24CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntEntry.setStatus("current")


class _Pm1004mPerfLinePast24CntIndex_Type(Integer32):
    """Custom type pm1004mPerfLinePast24CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004mPerfLinePast24CntIndex_Type.__name__ = "Integer32"
_Pm1004mPerfLinePast24CntIndex_Object = MibTableColumn
pm1004mPerfLinePast24CntIndex = _Pm1004mPerfLinePast24CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 1),
    _Pm1004mPerfLinePast24CntIndex_Type()
)
pm1004mPerfLinePast24CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntIndex.setStatus("current")
_Pm1004mPerfLinePast24CntInvCvPortn_Type = EkiOnOff
_Pm1004mPerfLinePast24CntInvCvPortn_Object = MibTableColumn
pm1004mPerfLinePast24CntInvCvPortn = _Pm1004mPerfLinePast24CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 2),
    _Pm1004mPerfLinePast24CntInvCvPortn_Type()
)
pm1004mPerfLinePast24CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntInvCvPortn.setStatus("current")
_Pm1004mPerfLinePast24CntCvValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast24CntCvValuePortn_Object = MibTableColumn
pm1004mPerfLinePast24CntCvValuePortn = _Pm1004mPerfLinePast24CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 3),
    _Pm1004mPerfLinePast24CntCvValuePortn_Type()
)
pm1004mPerfLinePast24CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntCvValuePortn.setStatus("current")
_Pm1004mPerfLinePast24CntInvEsPortn_Type = EkiOnOff
_Pm1004mPerfLinePast24CntInvEsPortn_Object = MibTableColumn
pm1004mPerfLinePast24CntInvEsPortn = _Pm1004mPerfLinePast24CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 4),
    _Pm1004mPerfLinePast24CntInvEsPortn_Type()
)
pm1004mPerfLinePast24CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntInvEsPortn.setStatus("current")
_Pm1004mPerfLinePast24CntEsValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast24CntEsValuePortn_Object = MibTableColumn
pm1004mPerfLinePast24CntEsValuePortn = _Pm1004mPerfLinePast24CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 5),
    _Pm1004mPerfLinePast24CntEsValuePortn_Type()
)
pm1004mPerfLinePast24CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntEsValuePortn.setStatus("current")
_Pm1004mPerfLinePast24CntInvSesPortn_Type = EkiOnOff
_Pm1004mPerfLinePast24CntInvSesPortn_Object = MibTableColumn
pm1004mPerfLinePast24CntInvSesPortn = _Pm1004mPerfLinePast24CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 6),
    _Pm1004mPerfLinePast24CntInvSesPortn_Type()
)
pm1004mPerfLinePast24CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntInvSesPortn.setStatus("current")
_Pm1004mPerfLinePast24CntSesValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast24CntSesValuePortn_Object = MibTableColumn
pm1004mPerfLinePast24CntSesValuePortn = _Pm1004mPerfLinePast24CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 7),
    _Pm1004mPerfLinePast24CntSesValuePortn_Type()
)
pm1004mPerfLinePast24CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntSesValuePortn.setStatus("current")
_Pm1004mPerfLinePast24CntInvSefsPortn_Type = EkiOnOff
_Pm1004mPerfLinePast24CntInvSefsPortn_Object = MibTableColumn
pm1004mPerfLinePast24CntInvSefsPortn = _Pm1004mPerfLinePast24CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 8),
    _Pm1004mPerfLinePast24CntInvSefsPortn_Type()
)
pm1004mPerfLinePast24CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntInvSefsPortn.setStatus("current")
_Pm1004mPerfLinePast24CntSefsValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast24CntSefsValuePortn_Object = MibTableColumn
pm1004mPerfLinePast24CntSefsValuePortn = _Pm1004mPerfLinePast24CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 9),
    _Pm1004mPerfLinePast24CntSefsValuePortn_Type()
)
pm1004mPerfLinePast24CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntSefsValuePortn.setStatus("current")
_Pm1004mPerfLinePast24CntInvUasPortn_Type = EkiOnOff
_Pm1004mPerfLinePast24CntInvUasPortn_Object = MibTableColumn
pm1004mPerfLinePast24CntInvUasPortn = _Pm1004mPerfLinePast24CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 10),
    _Pm1004mPerfLinePast24CntInvUasPortn_Type()
)
pm1004mPerfLinePast24CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntInvUasPortn.setStatus("current")
_Pm1004mPerfLinePast24CntUasValuePortn_Type = Unsigned32
_Pm1004mPerfLinePast24CntUasValuePortn_Object = MibTableColumn
pm1004mPerfLinePast24CntUasValuePortn = _Pm1004mPerfLinePast24CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 1, 131, 1, 11),
    _Pm1004mPerfLinePast24CntUasValuePortn_Type()
)
pm1004mPerfLinePast24CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004mPerfLinePast24CntUasValuePortn.setStatus("current")
_Pm1004mMonLineTraceIdentifier_ObjectIdentity = ObjectIdentity
pm1004mMonLineTraceIdentifier = _Pm1004mMonLineTraceIdentifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 29, 11, 3, 2)
)

# Managed Objects groups


# Notification objects

pm1004mLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 30)
)
pm1004mLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapLineNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1004mLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 31)
)
pm1004mLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapLineNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1004mLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 32)
)
pm1004mLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapLineNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004mLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 33)
)
pm1004mLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapLineNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1004mLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 34)
)
pm1004mLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmLineFailPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapLineNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mLineTrapCritGoesOn.setStatus(
        "current"
    )

pm1004mLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 35)
)
pm1004mLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmLineFailPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapLineNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mLineTrapCritGoesOff.setStatus(
        "current"
    )

pm1004mClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 40)
)
pm1004mClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapPortNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1004mClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 41)
)
pm1004mClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapPortNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1004mClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 42)
)
pm1004mClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapPortNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004mClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 43)
)
pm1004mClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapPortNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1004mClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 44)
)
pm1004mClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmFailAccPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapPortNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mClientTrapCritGoesOn.setStatus(
        "current"
    )

pm1004mClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 45)
)
pm1004mClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmFailAccPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapPortNumber"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mClientTrapCritGoesOff.setStatus(
        "current"
    )

pm1004mPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 50)
)
pm1004mPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmDefFuseB"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mAlmDefFuseA"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004mPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 29, 10, 51)
)
pm1004mPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004m-MIB", "pm1004mAlmDefFuseB"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mAlmDefFuseA"),
        ("EKINOPS-Pm1004m-MIB", "pm1004mtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004mPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1004m-MIB",
    **{"Pm1004mOtxMode": Pm1004mOtxMode,
       "Pm1004mOtxGrid": Pm1004mOtxGrid,
       "Pm1004mAdjustValue": Pm1004mAdjustValue,
       "Pm1004mOtxChannel": Pm1004mOtxChannel,
       "modulePm1004m": modulePm1004m,
       "pm1004malarms": pm1004malarms,
       "pm1004mAlmOther": pm1004mAlmOther,
       "pm1004mAlmOtherNurg": pm1004mAlmOtherNurg,
       "pm1004mAlmsynthAlm2": pm1004mAlmsynthAlm2,
       "pm1004mAlmConfTableSave": pm1004mAlmConfTableSave,
       "pm1004mAlmInvUpload": pm1004mAlmInvUpload,
       "pm1004mAlmConfTableLoad": pm1004mAlmConfTableLoad,
       "pm1004mAlmCorrelatOff": pm1004mAlmCorrelatOff,
       "pm1004mAlmMaintenanceOn": pm1004mAlmMaintenanceOn,
       "pm1004mAlmOtherUrg": pm1004mAlmOtherUrg,
       "pm1004mAlmmodInitFailLevel2": pm1004mAlmmodInitFailLevel2,
       "pm1004mAlmLedFail": pm1004mAlmLedFail,
       "pm1004mAlmNextColdBootForced": pm1004mAlmNextColdBootForced,
       "pm1004mAlmBootUndone": pm1004mAlmBootUndone,
       "pm1004mAlmResetHwInitFail": pm1004mAlmResetHwInitFail,
       "pm1004mAlmSwInitFail": pm1004mAlmSwInitFail,
       "pm1004mAlmmodInitFailLevel3": pm1004mAlmmodInitFailLevel3,
       "pm1004mAlmGwIdentFail": pm1004mAlmGwIdentFail,
       "pm1004mAlmObmTypeReadFail": pm1004mAlmObmTypeReadFail,
       "pm1004mAlmInitModuleFail": pm1004mAlmInitModuleFail,
       "pm1004mAlmXfp1InitFail": pm1004mAlmXfp1InitFail,
       "pm1004mAlmXfp2InitFail": pm1004mAlmXfp2InitFail,
       "pm1004mAlmLine1InitFail": pm1004mAlmLine1InitFail,
       "pm1004mAlmLine2InitFail": pm1004mAlmLine2InitFail,
       "pm1004mAlmClient1InitFail": pm1004mAlmClient1InitFail,
       "pm1004mAlmClient2InitFail": pm1004mAlmClient2InitFail,
       "pm1004mAlmClient3InitFail": pm1004mAlmClient3InitFail,
       "pm1004mAlmClient4InitFail": pm1004mAlmClient4InitFail,
       "pm1004mAlmOtherCrit": pm1004mAlmOtherCrit,
       "pm1004mAlmsynthAlm0": pm1004mAlmsynthAlm0,
       "pm1004mAlmModGlobFail": pm1004mAlmModGlobFail,
       "pm1004mAlmDefFuseA": pm1004mAlmDefFuseA,
       "pm1004mAlmDefFuseB": pm1004mAlmDefFuseB,
       "pm1004mAlmClient": pm1004mAlmClient,
       "pm1004mAlmClientNurg": pm1004mAlmClientNurg,
       "pm1004mAlmsfpWarnDdmTable": pm1004mAlmsfpWarnDdmTable,
       "pm1004mAlmsfpWarnDdmEntry": pm1004mAlmsfpWarnDdmEntry,
       "pm1004mAlmsfpWarnDdmIndex": pm1004mAlmsfpWarnDdmIndex,
       "pm1004mAlmTxPwLowWngPortn": pm1004mAlmTxPwLowWngPortn,
       "pm1004mAlmTxPwrHighWngPortn": pm1004mAlmTxPwrHighWngPortn,
       "pm1004mAlmTxBiasLowWngPortn": pm1004mAlmTxBiasLowWngPortn,
       "pm1004mAlmTxBiasHighWngPortn": pm1004mAlmTxBiasHighWngPortn,
       "pm1004mAlmVccLowWngPortn": pm1004mAlmVccLowWngPortn,
       "pm1004mAlmVccHighWngPortn": pm1004mAlmVccHighWngPortn,
       "pm1004mAlmTempLowWngPortn": pm1004mAlmTempLowWngPortn,
       "pm1004mAlmTempHighWngPortn": pm1004mAlmTempHighWngPortn,
       "pm1004mAlmRxPwrLowWngPortn": pm1004mAlmRxPwrLowWngPortn,
       "pm1004mAlmRxPwrHighWngPortn": pm1004mAlmRxPwrHighWngPortn,
       "pm1004mAlmk1K2ClientTable": pm1004mAlmk1K2ClientTable,
       "pm1004mAlmk1K2ClientEntry": pm1004mAlmk1K2ClientEntry,
       "pm1004mAlmk1K2ClientIndex": pm1004mAlmk1K2ClientIndex,
       "pm1004mAlmk1K2ClientPortn": pm1004mAlmk1K2ClientPortn,
       "pm1004mAlmClientUrg": pm1004mAlmClientUrg,
       "pm1004mAlmsfpAlmDdmTable": pm1004mAlmsfpAlmDdmTable,
       "pm1004mAlmsfpAlmDdmEntry": pm1004mAlmsfpAlmDdmEntry,
       "pm1004mAlmsfpAlmDdmIndex": pm1004mAlmsfpAlmDdmIndex,
       "pm1004mAlmTxPwrLowAlaPortn": pm1004mAlmTxPwrLowAlaPortn,
       "pm1004mAlmTxPwrHighAlaPortn": pm1004mAlmTxPwrHighAlaPortn,
       "pm1004mAlmTxBiasLowAlaPortn": pm1004mAlmTxBiasLowAlaPortn,
       "pm1004mAlmTxBiasHighAlaPortn": pm1004mAlmTxBiasHighAlaPortn,
       "pm1004mAlmVccLowAlaPortn": pm1004mAlmVccLowAlaPortn,
       "pm1004mAlmVccHighAlaPortn": pm1004mAlmVccHighAlaPortn,
       "pm1004mAlmTempLowAlaPortn": pm1004mAlmTempLowAlaPortn,
       "pm1004mAlmTempHighAlaPortn": pm1004mAlmTempHighAlaPortn,
       "pm1004mAlmRxPwrLowAlaPortn": pm1004mAlmRxPwrLowAlaPortn,
       "pm1004mAlmRxPwrHighAlaPortn": pm1004mAlmRxPwrHighAlaPortn,
       "pm1004mAlmClientCrit": pm1004mAlmClientCrit,
       "pm1004mAlmsynthAlmPortTable": pm1004mAlmsynthAlmPortTable,
       "pm1004mAlmsynthAlmPortEntry": pm1004mAlmsynthAlmPortEntry,
       "pm1004mAlmsynthAlmPortIndex": pm1004mAlmsynthAlmPortIndex,
       "pm1004mAlmSfpAbsentPortn": pm1004mAlmSfpAbsentPortn,
       "pm1004mAlmDdmAbsentPortn": pm1004mAlmDdmAbsentPortn,
       "pm1004mAlmHwFailAccPortn": pm1004mAlmHwFailAccPortn,
       "pm1004mAlmDwLsdPortn": pm1004mAlmDwLsdPortn,
       "pm1004mAlmClientLocalOosPortn": pm1004mAlmClientLocalOosPortn,
       "pm1004mAlmClientRemoteOosPortn": pm1004mAlmClientRemoteOosPortn,
       "pm1004mAlmDwCaisPortn": pm1004mAlmDwCaisPortn,
       "pm1004mAlmSfpDdmWarningPortn": pm1004mAlmSfpDdmWarningPortn,
       "pm1004mAlmSfpDdmAlmPortn": pm1004mAlmSfpDdmAlmPortn,
       "pm1004mAlmFailAccPortn": pm1004mAlmFailAccPortn,
       "pm1004mAlmUpCsfPortn": pm1004mAlmUpCsfPortn,
       "pm1004mAlmaccessioAlmTable": pm1004mAlmaccessioAlmTable,
       "pm1004mAlmaccessioAlmEntry": pm1004mAlmaccessioAlmEntry,
       "pm1004mAlmaccessioAlmIndex": pm1004mAlmaccessioAlmIndex,
       "pm1004mAlmDwLasFailPortn": pm1004mAlmDwLasFailPortn,
       "pm1004mAlmUpLosPortn": pm1004mAlmUpLosPortn,
       "pm1004mAlmmapperDeAlmTable": pm1004mAlmmapperDeAlmTable,
       "pm1004mAlmmapperDeAlmEntry": pm1004mAlmmapperDeAlmEntry,
       "pm1004mAlmmapperDeAlmIndex": pm1004mAlmmapperDeAlmIndex,
       "pm1004mAlmUpAccOosPortn": pm1004mAlmUpAccOosPortn,
       "pm1004mAlmUpBufferOvlPortn": pm1004mAlmUpBufferOvlPortn,
       "pm1004mAlmDwCsfDetPortn": pm1004mAlmDwCsfDetPortn,
       "pm1004mAlmDwBufferOvlPortn": pm1004mAlmDwBufferOvlPortn,
       "pm1004mAlmaccessioSdhAlarmTable": pm1004mAlmaccessioSdhAlarmTable,
       "pm1004mAlmaccessioSdhAlarmEntry": pm1004mAlmaccessioSdhAlarmEntry,
       "pm1004mAlmaccessioSdhAlarmIndex": pm1004mAlmaccessioSdhAlarmIndex,
       "pm1004mAlmFifoErrPortn": pm1004mAlmFifoErrPortn,
       "pm1004mAlmRxLossOfLockPortn": pm1004mAlmRxLossOfLockPortn,
       "pm1004mAlmTxLossOfLockPortn": pm1004mAlmTxLossOfLockPortn,
       "pm1004mAlmClientAisDetPortn": pm1004mAlmClientAisDetPortn,
       "pm1004mAlmClientRdiDetPortn": pm1004mAlmClientRdiDetPortn,
       "pm1004mAlmClientOofPortn": pm1004mAlmClientOofPortn,
       "pm1004mAlmLine": pm1004mAlmLine,
       "pm1004mAlmLineNurg": pm1004mAlmLineNurg,
       "pm1004mAlmlineXfp1WarningsTable": pm1004mAlmlineXfp1WarningsTable,
       "pm1004mAlmlineXfp1WarningsEntry": pm1004mAlmlineXfp1WarningsEntry,
       "pm1004mAlmlineXfp1WarningsIndex": pm1004mAlmlineXfp1WarningsIndex,
       "pm1004mAlmTxPowerLowWarningPortn": pm1004mAlmTxPowerLowWarningPortn,
       "pm1004mAlmTxPowerHighWarningPortn": pm1004mAlmTxPowerHighWarningPortn,
       "pm1004mAlmTxBiasLowWarningPortn": pm1004mAlmTxBiasLowWarningPortn,
       "pm1004mAlmTxBiasHighWarningPortn": pm1004mAlmTxBiasHighWarningPortn,
       "pm1004mAlmTempLowWarningPortn": pm1004mAlmTempLowWarningPortn,
       "pm1004mAlmTempHighWarningPortn": pm1004mAlmTempHighWarningPortn,
       "pm1004mAlmRxPowerLowWarningPortn": pm1004mAlmRxPowerLowWarningPortn,
       "pm1004mAlmRxPowerHighWarningPortn": pm1004mAlmRxPowerHighWarningPortn,
       "pm1004mAlmlineOtx1TlhWarningsTable": pm1004mAlmlineOtx1TlhWarningsTable,
       "pm1004mAlmlineOtx1TlhWarningsEntry": pm1004mAlmlineOtx1TlhWarningsEntry,
       "pm1004mAlmlineOtx1TlhWarningsIndex": pm1004mAlmlineOtx1TlhWarningsIndex,
       "pm1004mAlmLineModulatorAgingHighWarningPortn": pm1004mAlmLineModulatorAgingHighWarningPortn,
       "pm1004mAlmLineAgingHighWarningPortn": pm1004mAlmLineAgingHighWarningPortn,
       "pm1004mAlmLineFreqDevHighWarningPortn": pm1004mAlmLineFreqDevHighWarningPortn,
       "pm1004mAlmLineLaserTempHighWarningPortn": pm1004mAlmLineLaserTempHighWarningPortn,
       "pm1004mAlmLineUrg": pm1004mAlmLineUrg,
       "pm1004mAlmdfrmBerTable": pm1004mAlmdfrmBerTable,
       "pm1004mAlmdfrmBerEntry": pm1004mAlmdfrmBerEntry,
       "pm1004mAlmdfrmBerIndex": pm1004mAlmdfrmBerIndex,
       "pm1004mAlmLineSignalDegradePortn": pm1004mAlmLineSignalDegradePortn,
       "pm1004mAlmLineSignalFailPortn": pm1004mAlmLineSignalFailPortn,
       "pm1004mAlmLineDegradePortn": pm1004mAlmLineDegradePortn,
       "pm1004mAlmlineXfp1AlarmTable": pm1004mAlmlineXfp1AlarmTable,
       "pm1004mAlmlineXfp1AlarmEntry": pm1004mAlmlineXfp1AlarmEntry,
       "pm1004mAlmlineXfp1AlarmIndex": pm1004mAlmlineXfp1AlarmIndex,
       "pm1004mAlmTxPowerLowAlarmPortn": pm1004mAlmTxPowerLowAlarmPortn,
       "pm1004mAlmTxPowerHighAlarmPortn": pm1004mAlmTxPowerHighAlarmPortn,
       "pm1004mAlmTxBiasLowAlarmPortn": pm1004mAlmTxBiasLowAlarmPortn,
       "pm1004mAlmTxBiasHighAlarmPortn": pm1004mAlmTxBiasHighAlarmPortn,
       "pm1004mAlmTempLowAlarmPortn": pm1004mAlmTempLowAlarmPortn,
       "pm1004mAlmTempHighAlarmPortn": pm1004mAlmTempHighAlarmPortn,
       "pm1004mAlmRxPowerLowAlarmPortn": pm1004mAlmRxPowerLowAlarmPortn,
       "pm1004mAlmRxPowerHighAlarmPortn": pm1004mAlmRxPowerHighAlarmPortn,
       "pm1004mAlmlineXfp1SupplyAlarmTable": pm1004mAlmlineXfp1SupplyAlarmTable,
       "pm1004mAlmlineXfp1SupplyAlarmEntry": pm1004mAlmlineXfp1SupplyAlarmEntry,
       "pm1004mAlmlineXfp1SupplyAlarmIndex": pm1004mAlmlineXfp1SupplyAlarmIndex,
       "pm1004mAlmVee5LowAlarmPortn": pm1004mAlmVee5LowAlarmPortn,
       "pm1004mAlmVee5HighAlarmPortn": pm1004mAlmVee5HighAlarmPortn,
       "pm1004mAlmVcc2LowAlarmPortn": pm1004mAlmVcc2LowAlarmPortn,
       "pm1004mAlmVcc2HighAlarmPortn": pm1004mAlmVcc2HighAlarmPortn,
       "pm1004mAlmVcc3LowAlarmPortn": pm1004mAlmVcc3LowAlarmPortn,
       "pm1004mAlmVcc3HighAlarmPortn": pm1004mAlmVcc3HighAlarmPortn,
       "pm1004mAlmVcc5LowAlarmPortn": pm1004mAlmVcc5LowAlarmPortn,
       "pm1004mAlmVcc5HighAlarmPortn": pm1004mAlmVcc5HighAlarmPortn,
       "pm1004mAlmVee5LowWarningPortn": pm1004mAlmVee5LowWarningPortn,
       "pm1004mAlmVee5HighWarningPortn": pm1004mAlmVee5HighWarningPortn,
       "pm1004mAlmVcc2LowWarningPortn": pm1004mAlmVcc2LowWarningPortn,
       "pm1004mAlmVcc2HighWarningPortn": pm1004mAlmVcc2HighWarningPortn,
       "pm1004mAlmVcc3LowWarningPortn": pm1004mAlmVcc3LowWarningPortn,
       "pm1004mAlmVcc3HighWarningPortn": pm1004mAlmVcc3HighWarningPortn,
       "pm1004mAlmVcc5LowWarningPortn": pm1004mAlmVcc5LowWarningPortn,
       "pm1004mAlmVcc5HighWarningPortn": pm1004mAlmVcc5HighWarningPortn,
       "pm1004mAlmlineOtx1TlhAlarmsTable": pm1004mAlmlineOtx1TlhAlarmsTable,
       "pm1004mAlmlineOtx1TlhAlarmsEntry": pm1004mAlmlineOtx1TlhAlarmsEntry,
       "pm1004mAlmlineOtx1TlhAlarmsIndex": pm1004mAlmlineOtx1TlhAlarmsIndex,
       "pm1004mAlmLineModulatorAgingHighAlaPortn": pm1004mAlmLineModulatorAgingHighAlaPortn,
       "pm1004mAlmLineAgingHighAlaPortn": pm1004mAlmLineAgingHighAlaPortn,
       "pm1004mAlmLineFreqDevHighAlaPortn": pm1004mAlmLineFreqDevHighAlaPortn,
       "pm1004mAlmLineLaserTempHighAlaPortn": pm1004mAlmLineLaserTempHighAlaPortn,
       "pm1004mAlmLineCrit": pm1004mAlmLineCrit,
       "pm1004mAlmsynthAlmLineTable": pm1004mAlmsynthAlmLineTable,
       "pm1004mAlmsynthAlmLineEntry": pm1004mAlmsynthAlmLineEntry,
       "pm1004mAlmsynthAlmLineIndex": pm1004mAlmsynthAlmLineIndex,
       "pm1004mAlmXfpAbsentPortn": pm1004mAlmXfpAbsentPortn,
       "pm1004mAlmXfpInitNotComplPortn": pm1004mAlmXfpInitNotComplPortn,
       "pm1004mAlmLineHwFailPortn": pm1004mAlmLineHwFailPortn,
       "pm1004mAlmXfpTxOffPortn": pm1004mAlmXfpTxOffPortn,
       "pm1004mAlmLineLocalOosPortn": pm1004mAlmLineLocalOosPortn,
       "pm1004mAlmUpRdiInsPortn": pm1004mAlmUpRdiInsPortn,
       "pm1004mAlmLineDdmWarningPortn": pm1004mAlmLineDdmWarningPortn,
       "pm1004mAlmLineDdmAlmPortn": pm1004mAlmLineDdmAlmPortn,
       "pm1004mAlmLineFailPortn": pm1004mAlmLineFailPortn,
       "pm1004mAlmLineActivePortn": pm1004mAlmLineActivePortn,
       "pm1004mAlmdfrmAlmTable": pm1004mAlmdfrmAlmTable,
       "pm1004mAlmdfrmAlmEntry": pm1004mAlmdfrmAlmEntry,
       "pm1004mAlmdfrmAlmIndex": pm1004mAlmdfrmAlmIndex,
       "pm1004mAlmDwAisDetPortn": pm1004mAlmDwAisDetPortn,
       "pm1004mAlmDwRdiDetPortn": pm1004mAlmDwRdiDetPortn,
       "pm1004mAlmDwOofPortn": pm1004mAlmDwOofPortn,
       "pm1004mAlmDwLofPortn": pm1004mAlmDwLofPortn,
       "pm1004mAlmlineSyncAlarmsTable": pm1004mAlmlineSyncAlarmsTable,
       "pm1004mAlmlineSyncAlarmsEntry": pm1004mAlmlineSyncAlarmsEntry,
       "pm1004mAlmlineSyncAlarmsIndex": pm1004mAlmlineSyncAlarmsIndex,
       "pm1004mAlmDwLockerrPortn": pm1004mAlmDwLockerrPortn,
       "pm1004mAlmUpLockerrPortn": pm1004mAlmUpLockerrPortn,
       "pm1004mAlmDwLosPortn": pm1004mAlmDwLosPortn,
       "pm1004mAlmlineXfp1AlarmsTable": pm1004mAlmlineXfp1AlarmsTable,
       "pm1004mAlmlineXfp1AlarmsEntry": pm1004mAlmlineXfp1AlarmsEntry,
       "pm1004mAlmlineXfp1AlarmsIndex": pm1004mAlmlineXfp1AlarmsIndex,
       "pm1004mAlmModNrPortn": pm1004mAlmModNrPortn,
       "pm1004mAlmRxCdrNotLockedPortn": pm1004mAlmRxCdrNotLockedPortn,
       "pm1004mAlmRxNrPortn": pm1004mAlmRxNrPortn,
       "pm1004mAlmTxCdrNotLockedPortn": pm1004mAlmTxCdrNotLockedPortn,
       "pm1004mAlmTxFaultPortn": pm1004mAlmTxFaultPortn,
       "pm1004mAlmTxNrPortn": pm1004mAlmTxNrPortn,
       "pm1004mAlmWavelengthUnlockedPortn": pm1004mAlmWavelengthUnlockedPortn,
       "pm1004mAlmTecFaultPortn": pm1004mAlmTecFaultPortn,
       "pm1004mAlmApdSupplyFaultPortn": pm1004mAlmApdSupplyFaultPortn,
       "pm1004mmeasures": pm1004mmeasures,
       "pm1004mMesrOther": pm1004mMesrOther,
       "pm1004mMesrsynth0": pm1004mMesrsynth0,
       "pm1004mMesrsynth1": pm1004mMesrsynth1,
       "pm1004mMesrClient": pm1004mMesrClient,
       "pm1004mMesrtempMeasTable": pm1004mMesrtempMeasTable,
       "pm1004mMesrtempMeasEntry": pm1004mMesrtempMeasEntry,
       "pm1004mMesrtempMeasIndex": pm1004mMesrtempMeasIndex,
       "pm1004mMesrtempMeasPortn": pm1004mMesrtempMeasPortn,
       "pm1004mMesrvoltMeasTable": pm1004mMesrvoltMeasTable,
       "pm1004mMesrvoltMeasEntry": pm1004mMesrvoltMeasEntry,
       "pm1004mMesrvoltMeasIndex": pm1004mMesrvoltMeasIndex,
       "pm1004mMesrvoltMeasPortn": pm1004mMesrvoltMeasPortn,
       "pm1004mMesrbiasMeasTable": pm1004mMesrbiasMeasTable,
       "pm1004mMesrbiasMeasEntry": pm1004mMesrbiasMeasEntry,
       "pm1004mMesrbiasMeasIndex": pm1004mMesrbiasMeasIndex,
       "pm1004mMesrbiasMeasPortn": pm1004mMesrbiasMeasPortn,
       "pm1004mMesrtxpwrMeasTable": pm1004mMesrtxpwrMeasTable,
       "pm1004mMesrtxpwrMeasEntry": pm1004mMesrtxpwrMeasEntry,
       "pm1004mMesrtxpwrMeasIndex": pm1004mMesrtxpwrMeasIndex,
       "pm1004mMesrtxpwrMeasPortn": pm1004mMesrtxpwrMeasPortn,
       "pm1004mMesrrxpwrMeasTable": pm1004mMesrrxpwrMeasTable,
       "pm1004mMesrrxpwrMeasEntry": pm1004mMesrrxpwrMeasEntry,
       "pm1004mMesrrxpwrMeasIndex": pm1004mMesrrxpwrMeasIndex,
       "pm1004mMesrrxpwrMeasPortn": pm1004mMesrrxpwrMeasPortn,
       "pm1004mMesrLine": pm1004mMesrLine,
       "pm1004mMesrxfp1LxModTempMeasTable": pm1004mMesrxfp1LxModTempMeasTable,
       "pm1004mMesrxfp1LxModTempMeasEntry": pm1004mMesrxfp1LxModTempMeasEntry,
       "pm1004mMesrxfp1LxModTempMeasIndex": pm1004mMesrxfp1LxModTempMeasIndex,
       "pm1004mMesrxfp1LxModTempMeasPortn": pm1004mMesrxfp1LxModTempMeasPortn,
       "pm1004mMesrxfp1ReservedTable": pm1004mMesrxfp1ReservedTable,
       "pm1004mMesrxfp1ReservedEntry": pm1004mMesrxfp1ReservedEntry,
       "pm1004mMesrxfp1ReservedIndex": pm1004mMesrxfp1ReservedIndex,
       "pm1004mMesrxfp1ReservedPortn": pm1004mMesrxfp1ReservedPortn,
       "pm1004mMesrxfp1LoBiasCurrentMeasTable": pm1004mMesrxfp1LoBiasCurrentMeasTable,
       "pm1004mMesrxfp1LoBiasCurrentMeasEntry": pm1004mMesrxfp1LoBiasCurrentMeasEntry,
       "pm1004mMesrxfp1LoBiasCurrentMeasIndex": pm1004mMesrxfp1LoBiasCurrentMeasIndex,
       "pm1004mMesrxfp1LoBiasCurrentMeasPortn": pm1004mMesrxfp1LoBiasCurrentMeasPortn,
       "pm1004mMesrxfp1LoTxPowerMeasTable": pm1004mMesrxfp1LoTxPowerMeasTable,
       "pm1004mMesrxfp1LoTxPowerMeasEntry": pm1004mMesrxfp1LoTxPowerMeasEntry,
       "pm1004mMesrxfp1LoTxPowerMeasIndex": pm1004mMesrxfp1LoTxPowerMeasIndex,
       "pm1004mMesrxfp1LoTxPowerMeasPortn": pm1004mMesrxfp1LoTxPowerMeasPortn,
       "pm1004mMesrxfp1LiRxPowerMeasTable": pm1004mMesrxfp1LiRxPowerMeasTable,
       "pm1004mMesrxfp1LiRxPowerMeasEntry": pm1004mMesrxfp1LiRxPowerMeasEntry,
       "pm1004mMesrxfp1LiRxPowerMeasIndex": pm1004mMesrxfp1LiRxPowerMeasIndex,
       "pm1004mMesrxfp1LiRxPowerMeasPortn": pm1004mMesrxfp1LiRxPowerMeasPortn,
       "pm1004mMesrxfp1LxAux1MeasTable": pm1004mMesrxfp1LxAux1MeasTable,
       "pm1004mMesrxfp1LxAux1MeasEntry": pm1004mMesrxfp1LxAux1MeasEntry,
       "pm1004mMesrxfp1LxAux1MeasIndex": pm1004mMesrxfp1LxAux1MeasIndex,
       "pm1004mMesrxfp1LxAux1MeasPortn": pm1004mMesrxfp1LxAux1MeasPortn,
       "pm1004mMesrxfp1LxAux2MeasTable": pm1004mMesrxfp1LxAux2MeasTable,
       "pm1004mMesrxfp1LxAux2MeasEntry": pm1004mMesrxfp1LxAux2MeasEntry,
       "pm1004mMesrxfp1LxAux2MeasIndex": pm1004mMesrxfp1LxAux2MeasIndex,
       "pm1004mMesrxfp1LxAux2MeasPortn": pm1004mMesrxfp1LxAux2MeasPortn,
       "pm1004mMesrotx1AgingTable": pm1004mMesrotx1AgingTable,
       "pm1004mMesrotx1AgingEntry": pm1004mMesrotx1AgingEntry,
       "pm1004mMesrotx1AgingIndex": pm1004mMesrotx1AgingIndex,
       "pm1004mMesrotx1AgingPortn": pm1004mMesrotx1AgingPortn,
       "pm1004mMesrotx1LaserTemperatureTable": pm1004mMesrotx1LaserTemperatureTable,
       "pm1004mMesrotx1LaserTemperatureEntry": pm1004mMesrotx1LaserTemperatureEntry,
       "pm1004mMesrotx1LaserTemperatureIndex": pm1004mMesrotx1LaserTemperatureIndex,
       "pm1004mMesrotx1LaserTemperaturePortn": pm1004mMesrotx1LaserTemperaturePortn,
       "pm1004mMesrotx1FreqDeviationTable": pm1004mMesrotx1FreqDeviationTable,
       "pm1004mMesrotx1FreqDeviationEntry": pm1004mMesrotx1FreqDeviationEntry,
       "pm1004mMesrotx1FreqDeviationIndex": pm1004mMesrotx1FreqDeviationIndex,
       "pm1004mMesrotx1FreqDeviationPortn": pm1004mMesrotx1FreqDeviationPortn,
       "pm1004mMesrotx1LaserWvlengthTable": pm1004mMesrotx1LaserWvlengthTable,
       "pm1004mMesrotx1LaserWvlengthEntry": pm1004mMesrotx1LaserWvlengthEntry,
       "pm1004mMesrotx1LaserWvlengthIndex": pm1004mMesrotx1LaserWvlengthIndex,
       "pm1004mMesrotx1LaserWvlengthPortn": pm1004mMesrotx1LaserWvlengthPortn,
       "pm1004mcounters": pm1004mcounters,
       "pm1004mCntOther": pm1004mCntOther,
       "pm1004mCntClient": pm1004mCntClient,
       "pm1004mCntupRaRemCntTable": pm1004mCntupRaRemCntTable,
       "pm1004mCntupRaRemCntEntry": pm1004mCntupRaRemCntEntry,
       "pm1004mCntupRaRemCntIndex": pm1004mCntupRaRemCntIndex,
       "pm1004mCntupRaRemCntValuePortn": pm1004mCntupRaRemCntValuePortn,
       "pm1004mCntupRaRemCntErrorPortn": pm1004mCntupRaRemCntErrorPortn,
       "pm1004mCntupRaRemCntOverloadPortn": pm1004mCntupRaRemCntOverloadPortn,
       "pm1004mCntupRaInsCntTable": pm1004mCntupRaInsCntTable,
       "pm1004mCntupRaInsCntEntry": pm1004mCntupRaInsCntEntry,
       "pm1004mCntupRaInsCntIndex": pm1004mCntupRaInsCntIndex,
       "pm1004mCntupRaInsCntValuePortn": pm1004mCntupRaInsCntValuePortn,
       "pm1004mCntupRaInsCntErrorPortn": pm1004mCntupRaInsCntErrorPortn,
       "pm1004mCntupRaInsCntOverloadPortn": pm1004mCntupRaInsCntOverloadPortn,
       "pm1004mCntupRdErrCntTable": pm1004mCntupRdErrCntTable,
       "pm1004mCntupRdErrCntEntry": pm1004mCntupRdErrCntEntry,
       "pm1004mCntupRdErrCntIndex": pm1004mCntupRdErrCntIndex,
       "pm1004mCntupRdErrCntValuePortn": pm1004mCntupRdErrCntValuePortn,
       "pm1004mCntupRdErrCntErrorPortn": pm1004mCntupRdErrCntErrorPortn,
       "pm1004mCntupRdErrCntOverloadPortn": pm1004mCntupRdErrCntOverloadPortn,
       "pm1004mCntupTimCntTable": pm1004mCntupTimCntTable,
       "pm1004mCntupTimCntEntry": pm1004mCntupTimCntEntry,
       "pm1004mCntupTimCntIndex": pm1004mCntupTimCntIndex,
       "pm1004mCntupTimCntValuePortn": pm1004mCntupTimCntValuePortn,
       "pm1004mCntupTimCntErrorPortn": pm1004mCntupTimCntErrorPortn,
       "pm1004mCntupTimCntOverloadPortn": pm1004mCntupTimCntOverloadPortn,
       "pm1004mCntupCvErrCntTable": pm1004mCntupCvErrCntTable,
       "pm1004mCntupCvErrCntEntry": pm1004mCntupCvErrCntEntry,
       "pm1004mCntupCvErrCntIndex": pm1004mCntupCvErrCntIndex,
       "pm1004mCntupCvErrCntValuePortn": pm1004mCntupCvErrCntValuePortn,
       "pm1004mCntupCvErrCntErrorPortn": pm1004mCntupCvErrCntErrorPortn,
       "pm1004mCntupCvErrCntOverloadPortn": pm1004mCntupCvErrCntOverloadPortn,
       "pm1004mCntdwTimCntTable": pm1004mCntdwTimCntTable,
       "pm1004mCntdwTimCntEntry": pm1004mCntdwTimCntEntry,
       "pm1004mCntdwTimCntIndex": pm1004mCntdwTimCntIndex,
       "pm1004mCntdwTimCntValuePortn": pm1004mCntdwTimCntValuePortn,
       "pm1004mCntdwTimCntErrorPortn": pm1004mCntdwTimCntErrorPortn,
       "pm1004mCntdwTimCntOverloadPortn": pm1004mCntdwTimCntOverloadPortn,
       "pm1004mCntLine": pm1004mCntLine,
       "pm1004mCntdfrmB1ErrCntTable": pm1004mCntdfrmB1ErrCntTable,
       "pm1004mCntdfrmB1ErrCntEntry": pm1004mCntdfrmB1ErrCntEntry,
       "pm1004mCntdfrmB1ErrCntIndex": pm1004mCntdfrmB1ErrCntIndex,
       "pm1004mCntdfrmB1ErrCntValuePortn": pm1004mCntdfrmB1ErrCntValuePortn,
       "pm1004mCntdfrmB1ErrCntErrorPortn": pm1004mCntdfrmB1ErrCntErrorPortn,
       "pm1004mCntdfrmB1ErrCntOverloadPortn": pm1004mCntdfrmB1ErrCntOverloadPortn,
       "pm1004mCntdfrmTimCntTable": pm1004mCntdfrmTimCntTable,
       "pm1004mCntdfrmTimCntEntry": pm1004mCntdfrmTimCntEntry,
       "pm1004mCntdfrmTimCntIndex": pm1004mCntdfrmTimCntIndex,
       "pm1004mCntdfrmTimCntValuePortn": pm1004mCntdfrmTimCntValuePortn,
       "pm1004mCntdfrmTimCntErrorPortn": pm1004mCntdfrmTimCntErrorPortn,
       "pm1004mCntdfrmTimCntOverloadPortn": pm1004mCntdfrmTimCntOverloadPortn,
       "pm1004mCntCountersReset": pm1004mCntCountersReset,
       "pm1004mCntCountersStop": pm1004mCntCountersStop,
       "pm1004mcontrolsWrite": pm1004mcontrolsWrite,
       "pm1004mCtrlOther": pm1004mCtrlOther,
       "pm1004mCtrlconfMgnt1": pm1004mCtrlconfMgnt1,
       "pm1004mCtrlConf1Load1": pm1004mCtrlConf1Load1,
       "pm1004mCtrlConf2Load1": pm1004mCtrlConf2Load1,
       "pm1004mCtrlConf2Flash1": pm1004mCtrlConf2Flash1,
       "pm1004mCtrlConf2Clear1": pm1004mCtrlConf2Clear1,
       "pm1004mCtrlsynth4": pm1004mCtrlsynth4,
       "pm1004mCtrlCorrelatOn": pm1004mCtrlCorrelatOn,
       "pm1004mCtrlCorrelatOff": pm1004mCtrlCorrelatOff,
       "pm1004mCtrlswMgnt": pm1004mCtrlswMgnt,
       "pm1004mCtrlColdReset": pm1004mCtrlColdReset,
       "pm1004mCtrlWarmReset": pm1004mCtrlWarmReset,
       "pm1004mCtrlLoadSwBank1": pm1004mCtrlLoadSwBank1,
       "pm1004mCtrlLoadSwBank2": pm1004mCtrlLoadSwBank2,
       "pm1004mCtrlgwMgnt": pm1004mCtrlgwMgnt,
       "pm1004mCtrlCurrentGwReset": pm1004mCtrlCurrentGwReset,
       "pm1004mCtrlLoadGwBank1": pm1004mCtrlLoadGwBank1,
       "pm1004mCtrlLoadGwBank2": pm1004mCtrlLoadGwBank2,
       "pm1004mCtrlLoadGwBank3": pm1004mCtrlLoadGwBank3,
       "pm1004mCtrlLoadGwBank4": pm1004mCtrlLoadGwBank4,
       "pm1004mCtrlledTest": pm1004mCtrlledTest,
       "pm1004mCtrlGreenLed": pm1004mCtrlGreenLed,
       "pm1004mCtrlRedLed": pm1004mCtrlRedLed,
       "pm1004mCtrlLedOff": pm1004mCtrlLedOff,
       "pm1004mCtrlmoduleOosMode": pm1004mCtrlmoduleOosMode,
       "pm1004mCtrlModuleOosMode": pm1004mCtrlModuleOosMode,
       "pm1004mCtrlmaintenanceMode": pm1004mCtrlmaintenanceMode,
       "pm1004mCtrlMaintenanceMode": pm1004mCtrlMaintenanceMode,
       "pm1004mCtrldccEnable": pm1004mCtrldccEnable,
       "pm1004mCtrlDccEnable": pm1004mCtrlDccEnable,
       "pm1004mCtrlClient": pm1004mCtrlClient,
       "pm1004mCtrlaccessLoopTable": pm1004mCtrlaccessLoopTable,
       "pm1004mCtrlaccessLoopEntry": pm1004mCtrlaccessLoopEntry,
       "pm1004mCtrlaccessLoopIndex": pm1004mCtrlaccessLoopIndex,
       "pm1004mCtrlaccessLoopPortn": pm1004mCtrlaccessLoopPortn,
       "pm1004mCtrlportOosModeTable": pm1004mCtrlportOosModeTable,
       "pm1004mCtrlportOosModeEntry": pm1004mCtrlportOosModeEntry,
       "pm1004mCtrlportOosModeIndex": pm1004mCtrlportOosModeIndex,
       "pm1004mCtrlportOosModePortn": pm1004mCtrlportOosModePortn,
       "pm1004mCtrlsfpOnCtrlTable": pm1004mCtrlsfpOnCtrlTable,
       "pm1004mCtrlsfpOnCtrlEntry": pm1004mCtrlsfpOnCtrlEntry,
       "pm1004mCtrlsfpOnCtrlIndex": pm1004mCtrlsfpOnCtrlIndex,
       "pm1004mCtrlsfpOnCtrlPortn": pm1004mCtrlsfpOnCtrlPortn,
       "pm1004mCtrlsfpOffCtrlTable": pm1004mCtrlsfpOffCtrlTable,
       "pm1004mCtrlsfpOffCtrlEntry": pm1004mCtrlsfpOffCtrlEntry,
       "pm1004mCtrlsfpOffCtrlIndex": pm1004mCtrlsfpOffCtrlIndex,
       "pm1004mCtrlsfpOffCtrlPortn": pm1004mCtrlsfpOffCtrlPortn,
       "pm1004mCtrlcsfUpInsTable": pm1004mCtrlcsfUpInsTable,
       "pm1004mCtrlcsfUpInsEntry": pm1004mCtrlcsfUpInsEntry,
       "pm1004mCtrlcsfUpInsIndex": pm1004mCtrlcsfUpInsIndex,
       "pm1004mCtrlcsfUpInsPortn": pm1004mCtrlcsfUpInsPortn,
       "pm1004mCtrlcaisDwInsTable": pm1004mCtrlcaisDwInsTable,
       "pm1004mCtrlcaisDwInsEntry": pm1004mCtrlcaisDwInsEntry,
       "pm1004mCtrlcaisDwInsIndex": pm1004mCtrlcaisDwInsIndex,
       "pm1004mCtrlcaisDwInsPortn": pm1004mCtrlcaisDwInsPortn,
       "pm1004mCtrlclientAccessTermLoopTable": pm1004mCtrlclientAccessTermLoopTable,
       "pm1004mCtrlclientAccessTermLoopEntry": pm1004mCtrlclientAccessTermLoopEntry,
       "pm1004mCtrlclientAccessTermLoopIndex": pm1004mCtrlclientAccessTermLoopIndex,
       "pm1004mCtrlclientAccessTermLoopPortn": pm1004mCtrlclientAccessTermLoopPortn,
       "pm1004mCtrlresetCount15PortTable": pm1004mCtrlresetCount15PortTable,
       "pm1004mCtrlresetCount15PortEntry": pm1004mCtrlresetCount15PortEntry,
       "pm1004mCtrlresetCount15PortIndex": pm1004mCtrlresetCount15PortIndex,
       "pm1004mCtrlclientResetAllPerfCount15Portn": pm1004mCtrlclientResetAllPerfCount15Portn,
       "pm1004mCtrlresetCount24PortTable": pm1004mCtrlresetCount24PortTable,
       "pm1004mCtrlresetCount24PortEntry": pm1004mCtrlresetCount24PortEntry,
       "pm1004mCtrlresetCount24PortIndex": pm1004mCtrlresetCount24PortIndex,
       "pm1004mCtrlclientResetAllPerfCount24Portn": pm1004mCtrlclientResetAllPerfCount24Portn,
       "pm1004mCtrlLine": pm1004mCtrlLine,
       "pm1004mCtrlcommAccessLoop": pm1004mCtrlcommAccessLoop,
       "pm1004mCtrlCommAccessloop": pm1004mCtrlCommAccessloop,
       "pm1004mCtrllineLoop": pm1004mCtrllineLoop,
       "pm1004mCtrlLineLoop": pm1004mCtrlLineLoop,
       "pm1004mCtrlmsAis": pm1004mCtrlmsAis,
       "pm1004mCtrlMsAis": pm1004mCtrlMsAis,
       "pm1004mCtrlProtMgnt": pm1004mCtrlProtMgnt,
       "pm1004mCtrlLineNumber": pm1004mCtrlLineNumber,
       "pm1004mCtrlProtMode": pm1004mCtrlProtMode,
       "pm1004mCtrllineOosModeTable": pm1004mCtrllineOosModeTable,
       "pm1004mCtrllineOosModeEntry": pm1004mCtrllineOosModeEntry,
       "pm1004mCtrllineOosModeIndex": pm1004mCtrllineOosModeIndex,
       "pm1004mCtrllineOosModePortn": pm1004mCtrllineOosModePortn,
       "pm1004mCtrllineResetCount15LineTable": pm1004mCtrllineResetCount15LineTable,
       "pm1004mCtrllineResetCount15LineEntry": pm1004mCtrllineResetCount15LineEntry,
       "pm1004mCtrllineResetCount15LineIndex": pm1004mCtrllineResetCount15LineIndex,
       "pm1004mCtrlresetAllPerfCount15Portn": pm1004mCtrlresetAllPerfCount15Portn,
       "pm1004mCtrllineResetCount24LineTable": pm1004mCtrllineResetCount24LineTable,
       "pm1004mCtrllineResetCount24LineEntry": pm1004mCtrllineResetCount24LineEntry,
       "pm1004mCtrllineResetCount24LineIndex": pm1004mCtrllineResetCount24LineIndex,
       "pm1004mCtrlresetAllPerfCount24Portn": pm1004mCtrlresetAllPerfCount24Portn,
       "pm1004mCtrlxfpOnoffTable": pm1004mCtrlxfpOnoffTable,
       "pm1004mCtrlxfpOnoffEntry": pm1004mCtrlxfpOnoffEntry,
       "pm1004mCtrlxfpOnoffIndex": pm1004mCtrlxfpOnoffIndex,
       "pm1004mCtrlxfpOnoffPortn": pm1004mCtrlxfpOnoffPortn,
       "pm1004mCtrlxfpLineLoopTable": pm1004mCtrlxfpLineLoopTable,
       "pm1004mCtrlxfpLineLoopEntry": pm1004mCtrlxfpLineLoopEntry,
       "pm1004mCtrlxfpLineLoopIndex": pm1004mCtrlxfpLineLoopIndex,
       "pm1004mCtrlxfpLineLoopPortn": pm1004mCtrlxfpLineLoopPortn,
       "pm1004mCtrlxfpXfiLoopTable": pm1004mCtrlxfpXfiLoopTable,
       "pm1004mCtrlxfpXfiLoopEntry": pm1004mCtrlxfpXfiLoopEntry,
       "pm1004mCtrlxfpXfiLoopIndex": pm1004mCtrlxfpXfiLoopIndex,
       "pm1004mCtrlxfpXfiLoopPortn": pm1004mCtrlxfpXfiLoopPortn,
       "pm1004mCtrllineTunableChannelTable": pm1004mCtrllineTunableChannelTable,
       "pm1004mCtrllineTunableChannelEntry": pm1004mCtrllineTunableChannelEntry,
       "pm1004mCtrllineTunableChannelIndex": pm1004mCtrllineTunableChannelIndex,
       "pm1004mCtrllineTunableChannelPortn": pm1004mCtrllineTunableChannelPortn,
       "pm1004mCtrllinePhotodiodeModeTable": pm1004mCtrllinePhotodiodeModeTable,
       "pm1004mCtrllinePhotodiodeModeEntry": pm1004mCtrllinePhotodiodeModeEntry,
       "pm1004mCtrllinePhotodiodeModeIndex": pm1004mCtrllinePhotodiodeModeIndex,
       "pm1004mCtrllinePhotodiodeModePortn": pm1004mCtrllinePhotodiodeModePortn,
       "pm1004mCtrllinePhotodiodeValueTable": pm1004mCtrllinePhotodiodeValueTable,
       "pm1004mCtrllinePhotodiodeValueEntry": pm1004mCtrllinePhotodiodeValueEntry,
       "pm1004mCtrllinePhotodiodeValueIndex": pm1004mCtrllinePhotodiodeValueIndex,
       "pm1004mCtrllinePhotodiodeValuePortn": pm1004mCtrllinePhotodiodeValuePortn,
       "pm1004mCtrllinePowerLaserTable": pm1004mCtrllinePowerLaserTable,
       "pm1004mCtrllinePowerLaserEntry": pm1004mCtrllinePowerLaserEntry,
       "pm1004mCtrllinePowerLaserIndex": pm1004mCtrllinePowerLaserIndex,
       "pm1004mCtrllinePowerLaserPortn": pm1004mCtrllinePowerLaserPortn,
       "pm1004mri": pm1004mri,
       "pm1004mriTable": pm1004mriTable,
       "pm1004mRinvSfpTable": pm1004mRinvSfpTable,
       "pm1004mRinvSfpEntry": pm1004mRinvSfpEntry,
       "pm1004mRinvSfpIndex": pm1004mRinvSfpIndex,
       "pm1004mRinvsfp": pm1004mRinvsfp,
       "pm1004mRinvLineTable": pm1004mRinvLineTable,
       "pm1004mRinvLineEntry": pm1004mRinvLineEntry,
       "pm1004mRinvLineIndex": pm1004mRinvLineIndex,
       "pm1004mRinvxfpLine": pm1004mRinvxfpLine,
       "pm1004mRinvReloadInventory": pm1004mRinvReloadInventory,
       "pm1004mRinvHwPlatform": pm1004mRinvHwPlatform,
       "pm1004mRinvModulePlatform": pm1004mRinvModulePlatform,
       "pm1004mRinvSwPlatform": pm1004mRinvSwPlatform,
       "pm1004mRinvGwPlatform": pm1004mRinvGwPlatform,
       "pm1004mdownload": pm1004mdownload,
       "pm1004mDwlOther": pm1004mDwlOther,
       "pm1004mDwlrestartProcess": pm1004mDwlrestartProcess,
       "pm1004mDwlWarmRestartProcessed": pm1004mDwlWarmRestartProcessed,
       "pm1004mDwlColdRestartProcessed": pm1004mDwlColdRestartProcessed,
       "pm1004mDwlswBanksUsed": pm1004mDwlswBanksUsed,
       "pm1004mDwlSwBank1Used": pm1004mDwlSwBank1Used,
       "pm1004mDwlSwBank2Used": pm1004mDwlSwBank2Used,
       "pm1004mDwlSwBank1Notempty": pm1004mDwlSwBank1Notempty,
       "pm1004mDwlSwBank2Notempty": pm1004mDwlSwBank2Notempty,
       "pm1004mDwlgwBanksUsed": pm1004mDwlgwBanksUsed,
       "pm1004mDwlGwBank1Used": pm1004mDwlGwBank1Used,
       "pm1004mDwlGwBank2Used": pm1004mDwlGwBank2Used,
       "pm1004mDwlGwBank3Used": pm1004mDwlGwBank3Used,
       "pm1004mDwlGwBank4Used": pm1004mDwlGwBank4Used,
       "pm1004mDwlGwBank1Notempty": pm1004mDwlGwBank1Notempty,
       "pm1004mDwlGwBank2Notempty": pm1004mDwlGwBank2Notempty,
       "pm1004mDwlGwBank3Notempty": pm1004mDwlGwBank3Notempty,
       "pm1004mDwlGwBank4Notempty": pm1004mDwlGwBank4Notempty,
       "pm1004mDwlClient": pm1004mDwlClient,
       "pm1004mDwlLine": pm1004mDwlLine,
       "pm1004mConfig": pm1004mConfig,
       "pm1004mCfgAccessCAisCsf": pm1004mCfgAccessCAisCsf,
       "pm1004mCfgClientcaiscsfTable": pm1004mCfgClientcaiscsfTable,
       "pm1004mCfgClientcaiscsfEntry": pm1004mCfgClientcaiscsfEntry,
       "pm1004mCfgClientcaiscsfIndex": pm1004mCfgClientcaiscsfIndex,
       "pm1004mCfgCAisModePortn": pm1004mCfgCAisModePortn,
       "pm1004mCfgUpAccessioAlmPortn": pm1004mCfgUpAccessioAlmPortn,
       "pm1004mCfgUpMapperDeAlmPortn": pm1004mCfgUpMapperDeAlmPortn,
       "pm1004mCfgUpAccessioSdhAlmPortn": pm1004mCfgUpAccessioSdhAlmPortn,
       "pm1004mCfgDownAccessioAlmPortn": pm1004mCfgDownAccessioAlmPortn,
       "pm1004mCfgDownMapperDeAlmPortn": pm1004mCfgDownMapperDeAlmPortn,
       "pm1004mCfgDownDfrmAlmPortn": pm1004mCfgDownDfrmAlmPortn,
       "pm1004mCfgDownLineSyncAlarmsPortn": pm1004mCfgDownLineSyncAlarmsPortn,
       "pm1004mCfgDownAccessioSdhAlmPortn": pm1004mCfgDownAccessioSdhAlmPortn,
       "pm1004mCfgStartup": pm1004mCfgStartup,
       "pm1004mCfgClientStartupTable": pm1004mCfgClientStartupTable,
       "pm1004mCfgClientStartupEntry": pm1004mCfgClientStartupEntry,
       "pm1004mCfgClientStartupIndex": pm1004mCfgClientStartupIndex,
       "pm1004mCfgSystConfPortPortn": pm1004mCfgSystConfPortPortn,
       "pm1004mCfgNetConfPortPortn": pm1004mCfgNetConfPortPortn,
       "pm1004mtablelineStartup": pm1004mtablelineStartup,
       "pm1004mCfgsystConfLine1": pm1004mCfgsystConfLine1,
       "pm1004mCfglineOptions1": pm1004mCfglineOptions1,
       "pm1004mCfgsystConfLine2": pm1004mCfgsystConfLine2,
       "pm1004mCfglineSelection": pm1004mCfglineSelection,
       "pm1004mCfgXfpTable": pm1004mCfgXfpTable,
       "pm1004mCfgXfpEntry": pm1004mCfgXfpEntry,
       "pm1004mCfgXfpIndex": pm1004mCfgXfpIndex,
       "pm1004mCfgSystConfXfpPortn": pm1004mCfgSystConfXfpPortn,
       "pm1004mCfgDataRateConfXfpPortn": pm1004mCfgDataRateConfXfpPortn,
       "pm1004mCfgLabels": pm1004mCfgLabels,
       "pm1004mCfgLabelclientTable": pm1004mCfgLabelclientTable,
       "pm1004mCfgLabelclientEntry": pm1004mCfgLabelclientEntry,
       "pm1004mCfgLabelclientIndex": pm1004mCfgLabelclientIndex,
       "pm1004mCfgLabelclientPortn": pm1004mCfgLabelclientPortn,
       "pm1004mCfgLabellineTable": pm1004mCfgLabellineTable,
       "pm1004mCfgLabellineEntry": pm1004mCfgLabellineEntry,
       "pm1004mCfgLabellineIndex": pm1004mCfgLabellineIndex,
       "pm1004mCfgLabellinePortn": pm1004mCfgLabellinePortn,
       "pm1004mCfgModPerfConfig": pm1004mCfgModPerfConfig,
       "pm1004mtablemodPerfConfig": pm1004mtablemodPerfConfig,
       "pm1004mCfgperfMode": pm1004mCfgperfMode,
       "pm1004mCfgJ0Client": pm1004mCfgJ0Client,
       "pm1004mCfgEmptyTable": pm1004mCfgEmptyTable,
       "pm1004mCfgEmptyEntry": pm1004mCfgEmptyEntry,
       "pm1004mCfgEmptyIndex": pm1004mCfgEmptyIndex,
       "pm1004mCfgClientExpectJ0SetupPortn": pm1004mCfgClientExpectJ0SetupPortn,
       "pm1004mCfgStartuptlh": pm1004mCfgStartuptlh,
       "pm1004mCfgOtxtlhTable": pm1004mCfgOtxtlhTable,
       "pm1004mCfgOtxtlhEntry": pm1004mCfgOtxtlhEntry,
       "pm1004mCfgOtxtlhIndex": pm1004mCfgOtxtlhIndex,
       "pm1004mCfgNuPortn": pm1004mCfgNuPortn,
       "pm1004mCfgLineDitherRatePortn": pm1004mCfgLineDitherRatePortn,
       "pm1004mCfgLineDitherFhzPortn": pm1004mCfgLineDitherFhzPortn,
       "pm1004mCfgLinePwrLaserPortn": pm1004mCfgLinePwrLaserPortn,
       "pm1004mCfgLineFCurrentPortn": pm1004mCfgLineFCurrentPortn,
       "pm1004mCfgLineGridCurrentPortn": pm1004mCfgLineGridCurrentPortn,
       "pm1004mCfgFPortn": pm1004mCfgFPortn,
       "pm1004mCfgReservedPortn": pm1004mCfgReservedPortn,
       "pm1004mCfgLinePhotodiodeModePortn": pm1004mCfgLinePhotodiodeModePortn,
       "pm1004mCfgLinePhotodiodeValuePortn": pm1004mCfgLinePhotodiodeValuePortn,
       "pm1004mCfgStartuptablefive": pm1004mCfgStartuptablefive,
       "pm1004mCfgOtxtlhcapabilitiesTable": pm1004mCfgOtxtlhcapabilitiesTable,
       "pm1004mCfgOtxtlhcapabilitiesEntry": pm1004mCfgOtxtlhcapabilitiesEntry,
       "pm1004mCfgOtxtlhcapabilitiesIndex": pm1004mCfgOtxtlhcapabilitiesIndex,
       "pm1004mCfgComponentTypePortn": pm1004mCfgComponentTypePortn,
       "pm1004mCfgMiscellaneousPortn": pm1004mCfgMiscellaneousPortn,
       "pm1004mCfgFirstChannelPortn": pm1004mCfgFirstChannelPortn,
       "pm1004mCfgLastChannelPortn": pm1004mCfgLastChannelPortn,
       "pm1004mCfgGridPortn": pm1004mCfgGridPortn,
       "pm1004mCfgWriteConfiguration": pm1004mCfgWriteConfiguration,
       "pm1004mtraps": pm1004mtraps,
       "pm1004mtrapPortNumber": pm1004mtrapPortNumber,
       "pm1004mtrapLineNumber": pm1004mtrapLineNumber,
       "pm1004mtrapBoardNumber": pm1004mtrapBoardNumber,
       "pm1004mLineTrapNotUrgentGoesOn": pm1004mLineTrapNotUrgentGoesOn,
       "pm1004mLineTrapNotUrgentGoesOff": pm1004mLineTrapNotUrgentGoesOff,
       "pm1004mLineTrapUrgentGoesOn": pm1004mLineTrapUrgentGoesOn,
       "pm1004mLineTrapUrgentGoesOff": pm1004mLineTrapUrgentGoesOff,
       "pm1004mLineTrapCritGoesOn": pm1004mLineTrapCritGoesOn,
       "pm1004mLineTrapCritGoesOff": pm1004mLineTrapCritGoesOff,
       "pm1004mClientTrapNotUrgentGoesOn": pm1004mClientTrapNotUrgentGoesOn,
       "pm1004mClientTrapNotUrgentGoesOff": pm1004mClientTrapNotUrgentGoesOff,
       "pm1004mClientTrapUrgentGoesOn": pm1004mClientTrapUrgentGoesOn,
       "pm1004mClientTrapUrgentGoesOff": pm1004mClientTrapUrgentGoesOff,
       "pm1004mClientTrapCritGoesOn": pm1004mClientTrapCritGoesOn,
       "pm1004mClientTrapCritGoesOff": pm1004mClientTrapCritGoesOff,
       "pm1004mPowerTrapUrgentGoesOn": pm1004mPowerTrapUrgentGoesOn,
       "pm1004mPowerTrapUrgentGoesOff": pm1004mPowerTrapUrgentGoesOff,
       "pm1004mMonitoring": pm1004mMonitoring,
       "pm1004mMonOther": pm1004mMonOther,
       "pm1004mMonSync": pm1004mMonSync,
       "pm1004mPerfEnable": pm1004mPerfEnable,
       "pm1004mPerfSyncSource": pm1004mPerfSyncSource,
       "pm1004mPerf15minSync": pm1004mPerf15minSync,
       "pm1004mPerf24hSync": pm1004mPerf24hSync,
       "pm1004mMonTimeStamp": pm1004mMonTimeStamp,
       "pm1004mPerfCurrent15MinElapsedTime": pm1004mPerfCurrent15MinElapsedTime,
       "pm1004mPerfCurrent24HoursElapsedTime": pm1004mPerfCurrent24HoursElapsedTime,
       "pm1004mPerfPast15MinElapsedTime": pm1004mPerfPast15MinElapsedTime,
       "pm1004mPerfPast24HoursElapsedTime": pm1004mPerfPast24HoursElapsedTime,
       "pm1004mMonClient": pm1004mMonClient,
       "pm1004mMonClientPerformance": pm1004mMonClientPerformance,
       "pm1004mPerfUpCurrent15CntTable": pm1004mPerfUpCurrent15CntTable,
       "pm1004mPerfUpCurrent15CntEntry": pm1004mPerfUpCurrent15CntEntry,
       "pm1004mPerfUpCurrent15CntIndex": pm1004mPerfUpCurrent15CntIndex,
       "pm1004mPerfUpCurrent15CntInvCvPortn": pm1004mPerfUpCurrent15CntInvCvPortn,
       "pm1004mPerfUpCurrent15CntCvValuePortn": pm1004mPerfUpCurrent15CntCvValuePortn,
       "pm1004mPerfUpCurrent15CntInvEsPortn": pm1004mPerfUpCurrent15CntInvEsPortn,
       "pm1004mPerfUpCurrent15CntEsValuePortn": pm1004mPerfUpCurrent15CntEsValuePortn,
       "pm1004mPerfUpCurrent15CntInvSesPortn": pm1004mPerfUpCurrent15CntInvSesPortn,
       "pm1004mPerfUpCurrent15CntSesValuePortn": pm1004mPerfUpCurrent15CntSesValuePortn,
       "pm1004mPerfUpCurrent15CntInvSefsPortn": pm1004mPerfUpCurrent15CntInvSefsPortn,
       "pm1004mPerfUpCurrent15CntSefsValuePortn": pm1004mPerfUpCurrent15CntSefsValuePortn,
       "pm1004mPerfUpCurrent15CntInvUasPortn": pm1004mPerfUpCurrent15CntInvUasPortn,
       "pm1004mPerfUpCurrent15CntUasValuePortn": pm1004mPerfUpCurrent15CntUasValuePortn,
       "pm1004mPerfUpPast15CntTable": pm1004mPerfUpPast15CntTable,
       "pm1004mPerfUpPast15CntEntry": pm1004mPerfUpPast15CntEntry,
       "pm1004mPerfUpPast15CntIndex": pm1004mPerfUpPast15CntIndex,
       "pm1004mPerfUpPast15CntInvCvPortn": pm1004mPerfUpPast15CntInvCvPortn,
       "pm1004mPerfUpPast15CntCvValuePortn": pm1004mPerfUpPast15CntCvValuePortn,
       "pm1004mPerfUpPast15CntInvEsPortn": pm1004mPerfUpPast15CntInvEsPortn,
       "pm1004mPerfUpPast15CntEsValuePortn": pm1004mPerfUpPast15CntEsValuePortn,
       "pm1004mPerfUpPast15CntInvSesPortn": pm1004mPerfUpPast15CntInvSesPortn,
       "pm1004mPerfUpPast15CntSesValuePortn": pm1004mPerfUpPast15CntSesValuePortn,
       "pm1004mPerfUpPast15CntInvSefsPortn": pm1004mPerfUpPast15CntInvSefsPortn,
       "pm1004mPerfUpPast15CntSefsValuePortn": pm1004mPerfUpPast15CntSefsValuePortn,
       "pm1004mPerfUpPast15CntInvUasPortn": pm1004mPerfUpPast15CntInvUasPortn,
       "pm1004mPerfUpPast15CntUasValuePortn": pm1004mPerfUpPast15CntUasValuePortn,
       "pm1004mPerfUpCurrent24CntTable": pm1004mPerfUpCurrent24CntTable,
       "pm1004mPerfUpCurrent24CntEntry": pm1004mPerfUpCurrent24CntEntry,
       "pm1004mPerfUpCurrent24CntIndex": pm1004mPerfUpCurrent24CntIndex,
       "pm1004mPerfUpCurrent24CntInvCvPortn": pm1004mPerfUpCurrent24CntInvCvPortn,
       "pm1004mPerfUpCurrent24CntCvValuePortn": pm1004mPerfUpCurrent24CntCvValuePortn,
       "pm1004mPerfUpCurrent24CntInvEsPortn": pm1004mPerfUpCurrent24CntInvEsPortn,
       "pm1004mPerfUpCurrent24CntEsValuePortn": pm1004mPerfUpCurrent24CntEsValuePortn,
       "pm1004mPerfUpCurrent24CntInvSesPortn": pm1004mPerfUpCurrent24CntInvSesPortn,
       "pm1004mPerfUpCurrent24CntSesValuePortn": pm1004mPerfUpCurrent24CntSesValuePortn,
       "pm1004mPerfUpCurrent24CntInvSefsPortn": pm1004mPerfUpCurrent24CntInvSefsPortn,
       "pm1004mPerfUpCurrent24CntSefsValuePortn": pm1004mPerfUpCurrent24CntSefsValuePortn,
       "pm1004mPerfUpCurrent24CntInvUasPortn": pm1004mPerfUpCurrent24CntInvUasPortn,
       "pm1004mPerfUpCurrent24CntUasValuePortn": pm1004mPerfUpCurrent24CntUasValuePortn,
       "pm1004mPerfUpPast24CntTable": pm1004mPerfUpPast24CntTable,
       "pm1004mPerfUpPast24CntEntry": pm1004mPerfUpPast24CntEntry,
       "pm1004mPerfUpPast24CntIndex": pm1004mPerfUpPast24CntIndex,
       "pm1004mPerfUpPast24CntInvCvPortn": pm1004mPerfUpPast24CntInvCvPortn,
       "pm1004mPerfUpPast24CntCvValuePortn": pm1004mPerfUpPast24CntCvValuePortn,
       "pm1004mPerfUpPast24CntInvEsPortn": pm1004mPerfUpPast24CntInvEsPortn,
       "pm1004mPerfUpPast24CntEsValuePortn": pm1004mPerfUpPast24CntEsValuePortn,
       "pm1004mPerfUpPast24CntInvSesPortn": pm1004mPerfUpPast24CntInvSesPortn,
       "pm1004mPerfUpPast24CntSesValuePortn": pm1004mPerfUpPast24CntSesValuePortn,
       "pm1004mPerfUpPast24CntInvSefsPortn": pm1004mPerfUpPast24CntInvSefsPortn,
       "pm1004mPerfUpPast24CntSefsValuePortn": pm1004mPerfUpPast24CntSefsValuePortn,
       "pm1004mPerfUpPast24CntInvUasPortn": pm1004mPerfUpPast24CntInvUasPortn,
       "pm1004mPerfUpPast24CntUasValuePortn": pm1004mPerfUpPast24CntUasValuePortn,
       "pm1004mMonClientTraceIdentifier": pm1004mMonClientTraceIdentifier,
       "pm1004mAlmj0AlarmTable": pm1004mAlmj0AlarmTable,
       "pm1004mAlmj0AlarmEntry": pm1004mAlmj0AlarmEntry,
       "pm1004mAlmj0AlarmIndex": pm1004mAlmj0AlarmIndex,
       "pm1004mAlmJ0TimAlarmPortn": pm1004mAlmJ0TimAlarmPortn,
       "pm1004mAlmJ0TiiAlarmPortn": pm1004mAlmJ0TiiAlarmPortn,
       "pm1004mAlmCrc7ErrorPortn": pm1004mAlmCrc7ErrorPortn,
       "pm1004mMonLine": pm1004mMonLine,
       "pm1004mMonLinePerformance": pm1004mMonLinePerformance,
       "pm1004mPerfLineCurrent15CntTable": pm1004mPerfLineCurrent15CntTable,
       "pm1004mPerfLineCurrent15CntEntry": pm1004mPerfLineCurrent15CntEntry,
       "pm1004mPerfLineCurrent15CntIndex": pm1004mPerfLineCurrent15CntIndex,
       "pm1004mPerfLineCurrent15CntInvCvPortn": pm1004mPerfLineCurrent15CntInvCvPortn,
       "pm1004mPerfLineCurrent15CntCvValuePortn": pm1004mPerfLineCurrent15CntCvValuePortn,
       "pm1004mPerfLineCurrent15CntInvEsPortn": pm1004mPerfLineCurrent15CntInvEsPortn,
       "pm1004mPerfLineCurrent15CntEsValuePortn": pm1004mPerfLineCurrent15CntEsValuePortn,
       "pm1004mPerfLineCurrent15CntInvSesPortn": pm1004mPerfLineCurrent15CntInvSesPortn,
       "pm1004mPerfLineCurrent15CntSesValuePortn": pm1004mPerfLineCurrent15CntSesValuePortn,
       "pm1004mPerfLineCurrent15CntInvSefsPortn": pm1004mPerfLineCurrent15CntInvSefsPortn,
       "pm1004mPerfLineCurrent15CntSefsValuePortn": pm1004mPerfLineCurrent15CntSefsValuePortn,
       "pm1004mPerfLineCurrent15CntInvUasPortn": pm1004mPerfLineCurrent15CntInvUasPortn,
       "pm1004mPerfLineCurrent15CntUasValuePortn": pm1004mPerfLineCurrent15CntUasValuePortn,
       "pm1004mPerfLinePast15CntTable": pm1004mPerfLinePast15CntTable,
       "pm1004mPerfLinePast15CntEntry": pm1004mPerfLinePast15CntEntry,
       "pm1004mPerfLinePast15CntIndex": pm1004mPerfLinePast15CntIndex,
       "pm1004mPerfLinePast15CntInvCvPortn": pm1004mPerfLinePast15CntInvCvPortn,
       "pm1004mPerfLinePast15CntCvValuePortn": pm1004mPerfLinePast15CntCvValuePortn,
       "pm1004mPerfLinePast15CntInvEsPortn": pm1004mPerfLinePast15CntInvEsPortn,
       "pm1004mPerfLinePast15CntEsValuePortn": pm1004mPerfLinePast15CntEsValuePortn,
       "pm1004mPerfLinePast15CntInvSesPortn": pm1004mPerfLinePast15CntInvSesPortn,
       "pm1004mPerfLinePast15CntSesValuePortn": pm1004mPerfLinePast15CntSesValuePortn,
       "pm1004mPerfLinePast15CntInvSefsPortn": pm1004mPerfLinePast15CntInvSefsPortn,
       "pm1004mPerfLinePast15CntSefsValuePortn": pm1004mPerfLinePast15CntSefsValuePortn,
       "pm1004mPerfLinePast15CntInvUasPortn": pm1004mPerfLinePast15CntInvUasPortn,
       "pm1004mPerfLinePast15CntUasValuePortn": pm1004mPerfLinePast15CntUasValuePortn,
       "pm1004mPerfLineCurrent24CntTable": pm1004mPerfLineCurrent24CntTable,
       "pm1004mPerfLineCurrent24CntEntry": pm1004mPerfLineCurrent24CntEntry,
       "pm1004mPerfLineCurrent24CntIndex": pm1004mPerfLineCurrent24CntIndex,
       "pm1004mPerfLineCurrent24CntInvCvPortn": pm1004mPerfLineCurrent24CntInvCvPortn,
       "pm1004mPerfLineCurrent24CntCvValuePortn": pm1004mPerfLineCurrent24CntCvValuePortn,
       "pm1004mPerfLineCurrent24CntInvEsPortn": pm1004mPerfLineCurrent24CntInvEsPortn,
       "pm1004mPerfLineCurrent24CntEsValuePortn": pm1004mPerfLineCurrent24CntEsValuePortn,
       "pm1004mPerfLineCurrent24CntInvSesPortn": pm1004mPerfLineCurrent24CntInvSesPortn,
       "pm1004mPerfLineCurrent24CntSesValuePortn": pm1004mPerfLineCurrent24CntSesValuePortn,
       "pm1004mPerfLineCurrent24CntInvSefsPortn": pm1004mPerfLineCurrent24CntInvSefsPortn,
       "pm1004mPerfLineCurrent24CntSefsValuePortn": pm1004mPerfLineCurrent24CntSefsValuePortn,
       "pm1004mPerfLineCurrent24CntInvUasPortn": pm1004mPerfLineCurrent24CntInvUasPortn,
       "pm1004mPerfLineCurrent24CntUasValuePortn": pm1004mPerfLineCurrent24CntUasValuePortn,
       "pm1004mPerfLinePast24CntTable": pm1004mPerfLinePast24CntTable,
       "pm1004mPerfLinePast24CntEntry": pm1004mPerfLinePast24CntEntry,
       "pm1004mPerfLinePast24CntIndex": pm1004mPerfLinePast24CntIndex,
       "pm1004mPerfLinePast24CntInvCvPortn": pm1004mPerfLinePast24CntInvCvPortn,
       "pm1004mPerfLinePast24CntCvValuePortn": pm1004mPerfLinePast24CntCvValuePortn,
       "pm1004mPerfLinePast24CntInvEsPortn": pm1004mPerfLinePast24CntInvEsPortn,
       "pm1004mPerfLinePast24CntEsValuePortn": pm1004mPerfLinePast24CntEsValuePortn,
       "pm1004mPerfLinePast24CntInvSesPortn": pm1004mPerfLinePast24CntInvSesPortn,
       "pm1004mPerfLinePast24CntSesValuePortn": pm1004mPerfLinePast24CntSesValuePortn,
       "pm1004mPerfLinePast24CntInvSefsPortn": pm1004mPerfLinePast24CntInvSefsPortn,
       "pm1004mPerfLinePast24CntSefsValuePortn": pm1004mPerfLinePast24CntSefsValuePortn,
       "pm1004mPerfLinePast24CntInvUasPortn": pm1004mPerfLinePast24CntInvUasPortn,
       "pm1004mPerfLinePast24CntUasValuePortn": pm1004mPerfLinePast24CntUasValuePortn,
       "pm1004mMonLineTraceIdentifier": pm1004mMonLineTraceIdentifier}
)
