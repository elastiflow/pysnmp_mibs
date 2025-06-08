# SNMP MIB module (EKINOPS-Pm1001lhr-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1001lhr-MIB.mib
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

modulePm1001lhr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22)
)
if mibBuilder.loadTexts:
    modulePm1001lhr.setRevisions(
        ("2007-02-01 00:00",
         "2007-05-31 00:00",
         "2007-06-29 00:00",
         "2007-12-05 00:00",
         "2008-11-27 00:00",
         "2009-02-06 00:00",
         "2009-10-07 00:00",
         "2010-02-15 00:00",
         "2011-02-03 00:00",
         "2012-07-03 00:00",
         "2014-03-28 00:00",
         "2015-01-20 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1001lhrOtxMode(TextualConvention, Integer32):
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



class Pm1001lhrOtxGrid(TextualConvention, Integer32):
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



class Pm1001lhrAdjustValue(TextualConvention, Integer32):
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



class Pm1001lhrOtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm1001lhralarms_ObjectIdentity = ObjectIdentity
pm1001lhralarms = _Pm1001lhralarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2)
)
_Pm1001lhrAlmOther_ObjectIdentity = ObjectIdentity
pm1001lhrAlmOther = _Pm1001lhrAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1)
)
_Pm1001lhrAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1001lhrAlmOtherNurg = _Pm1001lhrAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 1)
)
_Pm1001lhrAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm1001lhrAlmsynthAlm2 = _Pm1001lhrAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 1, 2)
)
_Pm1001lhrAlmConfTableSave_Type = EkiOnOff
_Pm1001lhrAlmConfTableSave_Object = MibScalar
pm1001lhrAlmConfTableSave = _Pm1001lhrAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 1, 2, 1),
    _Pm1001lhrAlmConfTableSave_Type()
)
pm1001lhrAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmConfTableSave.setStatus("current")
_Pm1001lhrAlmInvUpload_Type = EkiOnOff
_Pm1001lhrAlmInvUpload_Object = MibScalar
pm1001lhrAlmInvUpload = _Pm1001lhrAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 1, 2, 2),
    _Pm1001lhrAlmInvUpload_Type()
)
pm1001lhrAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmInvUpload.setStatus("current")
_Pm1001lhrAlmConfTableLoad_Type = EkiOnOff
_Pm1001lhrAlmConfTableLoad_Object = MibScalar
pm1001lhrAlmConfTableLoad = _Pm1001lhrAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 1, 2, 3),
    _Pm1001lhrAlmConfTableLoad_Type()
)
pm1001lhrAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmConfTableLoad.setStatus("current")
_Pm1001lhrAlmCorrelatOff_Type = EkiOnOff
_Pm1001lhrAlmCorrelatOff_Object = MibScalar
pm1001lhrAlmCorrelatOff = _Pm1001lhrAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 1, 2, 4),
    _Pm1001lhrAlmCorrelatOff_Type()
)
pm1001lhrAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmCorrelatOff.setStatus("current")
_Pm1001lhrAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1001lhrAlmOtherUrg = _Pm1001lhrAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2)
)
_Pm1001lhrAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm1001lhrAlmmodInitFailLevel2 = _Pm1001lhrAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 194)
)
_Pm1001lhrAlmLedFail_Type = EkiOnOff
_Pm1001lhrAlmLedFail_Object = MibScalar
pm1001lhrAlmLedFail = _Pm1001lhrAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 194, 1),
    _Pm1001lhrAlmLedFail_Type()
)
pm1001lhrAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLedFail.setStatus("current")
_Pm1001lhrAlmNextColdBootForced_Type = EkiOnOff
_Pm1001lhrAlmNextColdBootForced_Object = MibScalar
pm1001lhrAlmNextColdBootForced = _Pm1001lhrAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 194, 2),
    _Pm1001lhrAlmNextColdBootForced_Type()
)
pm1001lhrAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmNextColdBootForced.setStatus("current")
_Pm1001lhrAlmBootUndone_Type = EkiOnOff
_Pm1001lhrAlmBootUndone_Object = MibScalar
pm1001lhrAlmBootUndone = _Pm1001lhrAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 194, 3),
    _Pm1001lhrAlmBootUndone_Type()
)
pm1001lhrAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmBootUndone.setStatus("current")
_Pm1001lhrAlmResetHwInitFail_Type = EkiOnOff
_Pm1001lhrAlmResetHwInitFail_Object = MibScalar
pm1001lhrAlmResetHwInitFail = _Pm1001lhrAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 194, 4),
    _Pm1001lhrAlmResetHwInitFail_Type()
)
pm1001lhrAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmResetHwInitFail.setStatus("current")
_Pm1001lhrAlmSwInitFail_Type = EkiOnOff
_Pm1001lhrAlmSwInitFail_Object = MibScalar
pm1001lhrAlmSwInitFail = _Pm1001lhrAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 194, 5),
    _Pm1001lhrAlmSwInitFail_Type()
)
pm1001lhrAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmSwInitFail.setStatus("current")
_Pm1001lhrAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm1001lhrAlmmodInitFailLevel3 = _Pm1001lhrAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 195)
)
_Pm1001lhrAlmGwIdentFail_Type = EkiOnOff
_Pm1001lhrAlmGwIdentFail_Object = MibScalar
pm1001lhrAlmGwIdentFail = _Pm1001lhrAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 195, 1),
    _Pm1001lhrAlmGwIdentFail_Type()
)
pm1001lhrAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmGwIdentFail.setStatus("current")
_Pm1001lhrAlmObmTypeReadFail_Type = EkiOnOff
_Pm1001lhrAlmObmTypeReadFail_Object = MibScalar
pm1001lhrAlmObmTypeReadFail = _Pm1001lhrAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 195, 2),
    _Pm1001lhrAlmObmTypeReadFail_Type()
)
pm1001lhrAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmObmTypeReadFail.setStatus("current")
_Pm1001lhrAlmInitModuleFail_Type = EkiOnOff
_Pm1001lhrAlmInitModuleFail_Object = MibScalar
pm1001lhrAlmInitModuleFail = _Pm1001lhrAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 195, 3),
    _Pm1001lhrAlmInitModuleFail_Type()
)
pm1001lhrAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmInitModuleFail.setStatus("current")
_Pm1001lhrAlmXfp1InitFail_Type = EkiOnOff
_Pm1001lhrAlmXfp1InitFail_Object = MibScalar
pm1001lhrAlmXfp1InitFail = _Pm1001lhrAlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 195, 5),
    _Pm1001lhrAlmXfp1InitFail_Type()
)
pm1001lhrAlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmXfp1InitFail.setStatus("current")
_Pm1001lhrAlmXfp2InitFail_Type = EkiOnOff
_Pm1001lhrAlmXfp2InitFail_Object = MibScalar
pm1001lhrAlmXfp2InitFail = _Pm1001lhrAlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 195, 6),
    _Pm1001lhrAlmXfp2InitFail_Type()
)
pm1001lhrAlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmXfp2InitFail.setStatus("current")
_Pm1001lhrAlmLine1InitFail_Type = EkiOnOff
_Pm1001lhrAlmLine1InitFail_Object = MibScalar
pm1001lhrAlmLine1InitFail = _Pm1001lhrAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 195, 7),
    _Pm1001lhrAlmLine1InitFail_Type()
)
pm1001lhrAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLine1InitFail.setStatus("current")
_Pm1001lhrAlmLine2InitFail_Type = EkiOnOff
_Pm1001lhrAlmLine2InitFail_Object = MibScalar
pm1001lhrAlmLine2InitFail = _Pm1001lhrAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 2, 195, 8),
    _Pm1001lhrAlmLine2InitFail_Type()
)
pm1001lhrAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLine2InitFail.setStatus("current")
_Pm1001lhrAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1001lhrAlmOtherCrit = _Pm1001lhrAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 3)
)
_Pm1001lhrAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1001lhrAlmsynthAlm0 = _Pm1001lhrAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 3, 0)
)
_Pm1001lhrAlmModGlobFail_Type = EkiOnOff
_Pm1001lhrAlmModGlobFail_Object = MibScalar
pm1001lhrAlmModGlobFail = _Pm1001lhrAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 3, 0, 9),
    _Pm1001lhrAlmModGlobFail_Type()
)
pm1001lhrAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmModGlobFail.setStatus("current")
_Pm1001lhrAlmDefFuseA_Type = EkiOnOff
_Pm1001lhrAlmDefFuseA_Object = MibScalar
pm1001lhrAlmDefFuseA = _Pm1001lhrAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 3, 0, 15),
    _Pm1001lhrAlmDefFuseA_Type()
)
pm1001lhrAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmDefFuseA.setStatus("current")
_Pm1001lhrAlmDefFuseB_Type = EkiOnOff
_Pm1001lhrAlmDefFuseB_Object = MibScalar
pm1001lhrAlmDefFuseB = _Pm1001lhrAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 1, 3, 0, 16),
    _Pm1001lhrAlmDefFuseB_Type()
)
pm1001lhrAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmDefFuseB.setStatus("current")
_Pm1001lhrAlmClient_ObjectIdentity = ObjectIdentity
pm1001lhrAlmClient = _Pm1001lhrAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 2)
)
_Pm1001lhrAlmClientNurg_ObjectIdentity = ObjectIdentity
pm1001lhrAlmClientNurg = _Pm1001lhrAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 2, 1)
)
_Pm1001lhrAlmClientUrg_ObjectIdentity = ObjectIdentity
pm1001lhrAlmClientUrg = _Pm1001lhrAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 2, 2)
)
_Pm1001lhrAlmClientCrit_ObjectIdentity = ObjectIdentity
pm1001lhrAlmClientCrit = _Pm1001lhrAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 2, 3)
)
_Pm1001lhrAlmLine_ObjectIdentity = ObjectIdentity
pm1001lhrAlmLine = _Pm1001lhrAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3)
)
_Pm1001lhrAlmLineNurg_ObjectIdentity = ObjectIdentity
pm1001lhrAlmLineNurg = _Pm1001lhrAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1)
)
_Pm1001lhrAlmlineXfp1WarningsTable_Object = MibTable
pm1001lhrAlmlineXfp1WarningsTable = _Pm1001lhrAlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1WarningsTable.setStatus("current")
_Pm1001lhrAlmlineXfp1WarningsEntry_Object = MibTableRow
pm1001lhrAlmlineXfp1WarningsEntry = _Pm1001lhrAlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1)
)
pm1001lhrAlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1WarningsEntry.setStatus("current")


class _Pm1001lhrAlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pm1001lhrAlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmlineXfp1WarningsIndex_Object = MibTableColumn
pm1001lhrAlmlineXfp1WarningsIndex = _Pm1001lhrAlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1, 1),
    _Pm1001lhrAlmlineXfp1WarningsIndex_Type()
)
pm1001lhrAlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1WarningsIndex.setStatus("current")
_Pm1001lhrAlmTxPowerLowWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmTxPowerLowWarningPortn_Object = MibTableColumn
pm1001lhrAlmTxPowerLowWarningPortn = _Pm1001lhrAlmTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1, 2),
    _Pm1001lhrAlmTxPowerLowWarningPortn_Type()
)
pm1001lhrAlmTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxPowerLowWarningPortn.setStatus("current")
_Pm1001lhrAlmTxPowerHighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmTxPowerHighWarningPortn_Object = MibTableColumn
pm1001lhrAlmTxPowerHighWarningPortn = _Pm1001lhrAlmTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1, 3),
    _Pm1001lhrAlmTxPowerHighWarningPortn_Type()
)
pm1001lhrAlmTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxPowerHighWarningPortn.setStatus("current")
_Pm1001lhrAlmTxBiasLowWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmTxBiasLowWarningPortn_Object = MibTableColumn
pm1001lhrAlmTxBiasLowWarningPortn = _Pm1001lhrAlmTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1, 4),
    _Pm1001lhrAlmTxBiasLowWarningPortn_Type()
)
pm1001lhrAlmTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxBiasLowWarningPortn.setStatus("current")
_Pm1001lhrAlmTxBiasHighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmTxBiasHighWarningPortn_Object = MibTableColumn
pm1001lhrAlmTxBiasHighWarningPortn = _Pm1001lhrAlmTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1, 5),
    _Pm1001lhrAlmTxBiasHighWarningPortn_Type()
)
pm1001lhrAlmTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxBiasHighWarningPortn.setStatus("current")
_Pm1001lhrAlmTempLowWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmTempLowWarningPortn_Object = MibTableColumn
pm1001lhrAlmTempLowWarningPortn = _Pm1001lhrAlmTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1, 8),
    _Pm1001lhrAlmTempLowWarningPortn_Type()
)
pm1001lhrAlmTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTempLowWarningPortn.setStatus("current")
_Pm1001lhrAlmTempHighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmTempHighWarningPortn_Object = MibTableColumn
pm1001lhrAlmTempHighWarningPortn = _Pm1001lhrAlmTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1, 9),
    _Pm1001lhrAlmTempHighWarningPortn_Type()
)
pm1001lhrAlmTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTempHighWarningPortn.setStatus("current")
_Pm1001lhrAlmRxPowerLowWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmRxPowerLowWarningPortn_Object = MibTableColumn
pm1001lhrAlmRxPowerLowWarningPortn = _Pm1001lhrAlmRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1, 16),
    _Pm1001lhrAlmRxPowerLowWarningPortn_Type()
)
pm1001lhrAlmRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmRxPowerLowWarningPortn.setStatus("current")
_Pm1001lhrAlmRxPowerHighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmRxPowerHighWarningPortn_Object = MibTableColumn
pm1001lhrAlmRxPowerHighWarningPortn = _Pm1001lhrAlmRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 209, 1, 17),
    _Pm1001lhrAlmRxPowerHighWarningPortn_Type()
)
pm1001lhrAlmRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmRxPowerHighWarningPortn.setStatus("current")
_Pm1001lhrAlmlineOtx1TlhWarningsTable_Object = MibTable
pm1001lhrAlmlineOtx1TlhWarningsTable = _Pm1001lhrAlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineOtx1TlhWarningsTable.setStatus("current")
_Pm1001lhrAlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pm1001lhrAlmlineOtx1TlhWarningsEntry = _Pm1001lhrAlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 225, 1)
)
pm1001lhrAlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pm1001lhrAlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pm1001lhrAlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pm1001lhrAlmlineOtx1TlhWarningsIndex = _Pm1001lhrAlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 225, 1, 1),
    _Pm1001lhrAlmlineOtx1TlhWarningsIndex_Type()
)
pm1001lhrAlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pm1001lhrAlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pm1001lhrAlmLineModulatorAgingHighWarningPortn = _Pm1001lhrAlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 225, 1, 6),
    _Pm1001lhrAlmLineModulatorAgingHighWarningPortn_Type()
)
pm1001lhrAlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pm1001lhrAlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmLineAgingHighWarningPortn_Object = MibTableColumn
pm1001lhrAlmLineAgingHighWarningPortn = _Pm1001lhrAlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 225, 1, 7),
    _Pm1001lhrAlmLineAgingHighWarningPortn_Type()
)
pm1001lhrAlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineAgingHighWarningPortn.setStatus("current")
_Pm1001lhrAlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pm1001lhrAlmLineFreqDevHighWarningPortn = _Pm1001lhrAlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 225, 1, 13),
    _Pm1001lhrAlmLineFreqDevHighWarningPortn_Type()
)
pm1001lhrAlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineFreqDevHighWarningPortn.setStatus("current")
_Pm1001lhrAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm1001lhrAlmLineLaserTempHighWarningPortn = _Pm1001lhrAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 1, 225, 1, 15),
    _Pm1001lhrAlmLineLaserTempHighWarningPortn_Type()
)
pm1001lhrAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm1001lhrAlmLineUrg_ObjectIdentity = ObjectIdentity
pm1001lhrAlmLineUrg = _Pm1001lhrAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2)
)
_Pm1001lhrAlmdfrmBerTable_Object = MibTable
pm1001lhrAlmdfrmBerTable = _Pm1001lhrAlmdfrmBerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 129)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmdfrmBerTable.setStatus("current")
_Pm1001lhrAlmdfrmBerEntry_Object = MibTableRow
pm1001lhrAlmdfrmBerEntry = _Pm1001lhrAlmdfrmBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 129, 1)
)
pm1001lhrAlmdfrmBerEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmdfrmBerIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmdfrmBerEntry.setStatus("current")


class _Pm1001lhrAlmdfrmBerIndex_Type(Integer32):
    """Custom type pm1001lhrAlmdfrmBerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmdfrmBerIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmdfrmBerIndex_Object = MibTableColumn
pm1001lhrAlmdfrmBerIndex = _Pm1001lhrAlmdfrmBerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 129, 1, 1),
    _Pm1001lhrAlmdfrmBerIndex_Type()
)
pm1001lhrAlmdfrmBerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmdfrmBerIndex.setStatus("current")
_Pm1001lhrAlmLineSignalDegradePortn_Type = EkiOnOff
_Pm1001lhrAlmLineSignalDegradePortn_Object = MibTableColumn
pm1001lhrAlmLineSignalDegradePortn = _Pm1001lhrAlmLineSignalDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 129, 1, 2),
    _Pm1001lhrAlmLineSignalDegradePortn_Type()
)
pm1001lhrAlmLineSignalDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineSignalDegradePortn.setStatus("current")
_Pm1001lhrAlmLineSignalFailPortn_Type = EkiOnOff
_Pm1001lhrAlmLineSignalFailPortn_Object = MibTableColumn
pm1001lhrAlmLineSignalFailPortn = _Pm1001lhrAlmLineSignalFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 129, 1, 3),
    _Pm1001lhrAlmLineSignalFailPortn_Type()
)
pm1001lhrAlmLineSignalFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineSignalFailPortn.setStatus("current")
_Pm1001lhrAlmLineDegradePortn_Type = EkiOnOff
_Pm1001lhrAlmLineDegradePortn_Object = MibTableColumn
pm1001lhrAlmLineDegradePortn = _Pm1001lhrAlmLineDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 129, 1, 6),
    _Pm1001lhrAlmLineDegradePortn_Type()
)
pm1001lhrAlmLineDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineDegradePortn.setStatus("current")
_Pm1001lhrAlmlineXfp1AlarmTable_Object = MibTable
pm1001lhrAlmlineXfp1AlarmTable = _Pm1001lhrAlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1AlarmTable.setStatus("current")
_Pm1001lhrAlmlineXfp1AlarmEntry_Object = MibTableRow
pm1001lhrAlmlineXfp1AlarmEntry = _Pm1001lhrAlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1)
)
pm1001lhrAlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1AlarmEntry.setStatus("current")


class _Pm1001lhrAlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pm1001lhrAlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmlineXfp1AlarmIndex_Object = MibTableColumn
pm1001lhrAlmlineXfp1AlarmIndex = _Pm1001lhrAlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1, 1),
    _Pm1001lhrAlmlineXfp1AlarmIndex_Type()
)
pm1001lhrAlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1AlarmIndex.setStatus("current")
_Pm1001lhrAlmTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmTxPowerLowAlarmPortn_Object = MibTableColumn
pm1001lhrAlmTxPowerLowAlarmPortn = _Pm1001lhrAlmTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1, 2),
    _Pm1001lhrAlmTxPowerLowAlarmPortn_Type()
)
pm1001lhrAlmTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxPowerLowAlarmPortn.setStatus("current")
_Pm1001lhrAlmTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmTxPowerHighAlarmPortn_Object = MibTableColumn
pm1001lhrAlmTxPowerHighAlarmPortn = _Pm1001lhrAlmTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1, 3),
    _Pm1001lhrAlmTxPowerHighAlarmPortn_Type()
)
pm1001lhrAlmTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxPowerHighAlarmPortn.setStatus("current")
_Pm1001lhrAlmTxBiasLowAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmTxBiasLowAlarmPortn_Object = MibTableColumn
pm1001lhrAlmTxBiasLowAlarmPortn = _Pm1001lhrAlmTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1, 4),
    _Pm1001lhrAlmTxBiasLowAlarmPortn_Type()
)
pm1001lhrAlmTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxBiasLowAlarmPortn.setStatus("current")
_Pm1001lhrAlmTxBiasHighAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmTxBiasHighAlarmPortn_Object = MibTableColumn
pm1001lhrAlmTxBiasHighAlarmPortn = _Pm1001lhrAlmTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1, 5),
    _Pm1001lhrAlmTxBiasHighAlarmPortn_Type()
)
pm1001lhrAlmTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxBiasHighAlarmPortn.setStatus("current")
_Pm1001lhrAlmTempLowAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmTempLowAlarmPortn_Object = MibTableColumn
pm1001lhrAlmTempLowAlarmPortn = _Pm1001lhrAlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1, 8),
    _Pm1001lhrAlmTempLowAlarmPortn_Type()
)
pm1001lhrAlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTempLowAlarmPortn.setStatus("current")
_Pm1001lhrAlmTempHighAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmTempHighAlarmPortn_Object = MibTableColumn
pm1001lhrAlmTempHighAlarmPortn = _Pm1001lhrAlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1, 9),
    _Pm1001lhrAlmTempHighAlarmPortn_Type()
)
pm1001lhrAlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTempHighAlarmPortn.setStatus("current")
_Pm1001lhrAlmRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmRxPowerLowAlarmPortn_Object = MibTableColumn
pm1001lhrAlmRxPowerLowAlarmPortn = _Pm1001lhrAlmRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1, 16),
    _Pm1001lhrAlmRxPowerLowAlarmPortn_Type()
)
pm1001lhrAlmRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmRxPowerLowAlarmPortn.setStatus("current")
_Pm1001lhrAlmRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmRxPowerHighAlarmPortn_Object = MibTableColumn
pm1001lhrAlmRxPowerHighAlarmPortn = _Pm1001lhrAlmRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 208, 1, 17),
    _Pm1001lhrAlmRxPowerHighAlarmPortn_Type()
)
pm1001lhrAlmRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmRxPowerHighAlarmPortn.setStatus("current")
_Pm1001lhrAlmlineXfp1SupplyAlarmTable_Object = MibTable
pm1001lhrAlmlineXfp1SupplyAlarmTable = _Pm1001lhrAlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pm1001lhrAlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pm1001lhrAlmlineXfp1SupplyAlarmEntry = _Pm1001lhrAlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1)
)
pm1001lhrAlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pm1001lhrAlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pm1001lhrAlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pm1001lhrAlmlineXfp1SupplyAlarmIndex = _Pm1001lhrAlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 1),
    _Pm1001lhrAlmlineXfp1SupplyAlarmIndex_Type()
)
pm1001lhrAlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pm1001lhrAlmVee5LowAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmVee5LowAlarmPortn_Object = MibTableColumn
pm1001lhrAlmVee5LowAlarmPortn = _Pm1001lhrAlmVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 2),
    _Pm1001lhrAlmVee5LowAlarmPortn_Type()
)
pm1001lhrAlmVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVee5LowAlarmPortn.setStatus("current")
_Pm1001lhrAlmVee5HighAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmVee5HighAlarmPortn_Object = MibTableColumn
pm1001lhrAlmVee5HighAlarmPortn = _Pm1001lhrAlmVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 3),
    _Pm1001lhrAlmVee5HighAlarmPortn_Type()
)
pm1001lhrAlmVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVee5HighAlarmPortn.setStatus("current")
_Pm1001lhrAlmVcc2LowAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc2LowAlarmPortn_Object = MibTableColumn
pm1001lhrAlmVcc2LowAlarmPortn = _Pm1001lhrAlmVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 4),
    _Pm1001lhrAlmVcc2LowAlarmPortn_Type()
)
pm1001lhrAlmVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc2LowAlarmPortn.setStatus("current")
_Pm1001lhrAlmVcc2HighAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc2HighAlarmPortn_Object = MibTableColumn
pm1001lhrAlmVcc2HighAlarmPortn = _Pm1001lhrAlmVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 5),
    _Pm1001lhrAlmVcc2HighAlarmPortn_Type()
)
pm1001lhrAlmVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc2HighAlarmPortn.setStatus("current")
_Pm1001lhrAlmVcc3LowAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc3LowAlarmPortn_Object = MibTableColumn
pm1001lhrAlmVcc3LowAlarmPortn = _Pm1001lhrAlmVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 6),
    _Pm1001lhrAlmVcc3LowAlarmPortn_Type()
)
pm1001lhrAlmVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc3LowAlarmPortn.setStatus("current")
_Pm1001lhrAlmVcc3HighAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc3HighAlarmPortn_Object = MibTableColumn
pm1001lhrAlmVcc3HighAlarmPortn = _Pm1001lhrAlmVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 7),
    _Pm1001lhrAlmVcc3HighAlarmPortn_Type()
)
pm1001lhrAlmVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc3HighAlarmPortn.setStatus("current")
_Pm1001lhrAlmVcc5LowAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc5LowAlarmPortn_Object = MibTableColumn
pm1001lhrAlmVcc5LowAlarmPortn = _Pm1001lhrAlmVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 8),
    _Pm1001lhrAlmVcc5LowAlarmPortn_Type()
)
pm1001lhrAlmVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc5LowAlarmPortn.setStatus("current")
_Pm1001lhrAlmVcc5HighAlarmPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc5HighAlarmPortn_Object = MibTableColumn
pm1001lhrAlmVcc5HighAlarmPortn = _Pm1001lhrAlmVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 9),
    _Pm1001lhrAlmVcc5HighAlarmPortn_Type()
)
pm1001lhrAlmVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc5HighAlarmPortn.setStatus("current")
_Pm1001lhrAlmVee5LowWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmVee5LowWarningPortn_Object = MibTableColumn
pm1001lhrAlmVee5LowWarningPortn = _Pm1001lhrAlmVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 10),
    _Pm1001lhrAlmVee5LowWarningPortn_Type()
)
pm1001lhrAlmVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVee5LowWarningPortn.setStatus("current")
_Pm1001lhrAlmVee5HighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmVee5HighWarningPortn_Object = MibTableColumn
pm1001lhrAlmVee5HighWarningPortn = _Pm1001lhrAlmVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 11),
    _Pm1001lhrAlmVee5HighWarningPortn_Type()
)
pm1001lhrAlmVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVee5HighWarningPortn.setStatus("current")
_Pm1001lhrAlmVcc2LowWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc2LowWarningPortn_Object = MibTableColumn
pm1001lhrAlmVcc2LowWarningPortn = _Pm1001lhrAlmVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 12),
    _Pm1001lhrAlmVcc2LowWarningPortn_Type()
)
pm1001lhrAlmVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc2LowWarningPortn.setStatus("current")
_Pm1001lhrAlmVcc2HighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc2HighWarningPortn_Object = MibTableColumn
pm1001lhrAlmVcc2HighWarningPortn = _Pm1001lhrAlmVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 13),
    _Pm1001lhrAlmVcc2HighWarningPortn_Type()
)
pm1001lhrAlmVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc2HighWarningPortn.setStatus("current")
_Pm1001lhrAlmVcc3LowWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc3LowWarningPortn_Object = MibTableColumn
pm1001lhrAlmVcc3LowWarningPortn = _Pm1001lhrAlmVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 14),
    _Pm1001lhrAlmVcc3LowWarningPortn_Type()
)
pm1001lhrAlmVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc3LowWarningPortn.setStatus("current")
_Pm1001lhrAlmVcc3HighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc3HighWarningPortn_Object = MibTableColumn
pm1001lhrAlmVcc3HighWarningPortn = _Pm1001lhrAlmVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 15),
    _Pm1001lhrAlmVcc3HighWarningPortn_Type()
)
pm1001lhrAlmVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc3HighWarningPortn.setStatus("current")
_Pm1001lhrAlmVcc5LowWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc5LowWarningPortn_Object = MibTableColumn
pm1001lhrAlmVcc5LowWarningPortn = _Pm1001lhrAlmVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 16),
    _Pm1001lhrAlmVcc5LowWarningPortn_Type()
)
pm1001lhrAlmVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc5LowWarningPortn.setStatus("current")
_Pm1001lhrAlmVcc5HighWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmVcc5HighWarningPortn_Object = MibTableColumn
pm1001lhrAlmVcc5HighWarningPortn = _Pm1001lhrAlmVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 212, 1, 17),
    _Pm1001lhrAlmVcc5HighWarningPortn_Type()
)
pm1001lhrAlmVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmVcc5HighWarningPortn.setStatus("current")
_Pm1001lhrAlmlineOtx1TlhAlarmsTable_Object = MibTable
pm1001lhrAlmlineOtx1TlhAlarmsTable = _Pm1001lhrAlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pm1001lhrAlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pm1001lhrAlmlineOtx1TlhAlarmsEntry = _Pm1001lhrAlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 224, 1)
)
pm1001lhrAlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pm1001lhrAlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pm1001lhrAlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pm1001lhrAlmlineOtx1TlhAlarmsIndex = _Pm1001lhrAlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 224, 1, 1),
    _Pm1001lhrAlmlineOtx1TlhAlarmsIndex_Type()
)
pm1001lhrAlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pm1001lhrAlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pm1001lhrAlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pm1001lhrAlmLineModulatorAgingHighAlaPortn = _Pm1001lhrAlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 224, 1, 6),
    _Pm1001lhrAlmLineModulatorAgingHighAlaPortn_Type()
)
pm1001lhrAlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pm1001lhrAlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pm1001lhrAlmLineAgingHighAlaPortn_Object = MibTableColumn
pm1001lhrAlmLineAgingHighAlaPortn = _Pm1001lhrAlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 224, 1, 7),
    _Pm1001lhrAlmLineAgingHighAlaPortn_Type()
)
pm1001lhrAlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineAgingHighAlaPortn.setStatus("current")
_Pm1001lhrAlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pm1001lhrAlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pm1001lhrAlmLineFreqDevHighAlaPortn = _Pm1001lhrAlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 224, 1, 13),
    _Pm1001lhrAlmLineFreqDevHighAlaPortn_Type()
)
pm1001lhrAlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineFreqDevHighAlaPortn.setStatus("current")
_Pm1001lhrAlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pm1001lhrAlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pm1001lhrAlmLineLaserTempHighAlaPortn = _Pm1001lhrAlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 2, 224, 1, 15),
    _Pm1001lhrAlmLineLaserTempHighAlaPortn_Type()
)
pm1001lhrAlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineLaserTempHighAlaPortn.setStatus("current")
_Pm1001lhrAlmLineCrit_ObjectIdentity = ObjectIdentity
pm1001lhrAlmLineCrit = _Pm1001lhrAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3)
)
_Pm1001lhrAlmsynthAlmLineTable_Object = MibTable
pm1001lhrAlmsynthAlmLineTable = _Pm1001lhrAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmsynthAlmLineTable.setStatus("current")
_Pm1001lhrAlmsynthAlmLineEntry_Object = MibTableRow
pm1001lhrAlmsynthAlmLineEntry = _Pm1001lhrAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1)
)
pm1001lhrAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmsynthAlmLineEntry.setStatus("current")


class _Pm1001lhrAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm1001lhrAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmsynthAlmLineIndex_Object = MibTableColumn
pm1001lhrAlmsynthAlmLineIndex = _Pm1001lhrAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1, 1),
    _Pm1001lhrAlmsynthAlmLineIndex_Type()
)
pm1001lhrAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmsynthAlmLineIndex.setStatus("current")
_Pm1001lhrAlmXfpAbsentPortn_Type = EkiOnOff
_Pm1001lhrAlmXfpAbsentPortn_Object = MibTableColumn
pm1001lhrAlmXfpAbsentPortn = _Pm1001lhrAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1, 2),
    _Pm1001lhrAlmXfpAbsentPortn_Type()
)
pm1001lhrAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmXfpAbsentPortn.setStatus("current")
_Pm1001lhrAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm1001lhrAlmXfpInitNotComplPortn_Object = MibTableColumn
pm1001lhrAlmXfpInitNotComplPortn = _Pm1001lhrAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1, 3),
    _Pm1001lhrAlmXfpInitNotComplPortn_Type()
)
pm1001lhrAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmXfpInitNotComplPortn.setStatus("current")
_Pm1001lhrAlmLineHwFailPortn_Type = EkiOnOff
_Pm1001lhrAlmLineHwFailPortn_Object = MibTableColumn
pm1001lhrAlmLineHwFailPortn = _Pm1001lhrAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1, 5),
    _Pm1001lhrAlmLineHwFailPortn_Type()
)
pm1001lhrAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineHwFailPortn.setStatus("current")
_Pm1001lhrAlmXfpTxOffPortn_Type = EkiOnOff
_Pm1001lhrAlmXfpTxOffPortn_Object = MibTableColumn
pm1001lhrAlmXfpTxOffPortn = _Pm1001lhrAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1, 6),
    _Pm1001lhrAlmXfpTxOffPortn_Type()
)
pm1001lhrAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmXfpTxOffPortn.setStatus("current")
_Pm1001lhrAlmLineLocalOosPortn_Type = EkiOnOff
_Pm1001lhrAlmLineLocalOosPortn_Object = MibTableColumn
pm1001lhrAlmLineLocalOosPortn = _Pm1001lhrAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1, 7),
    _Pm1001lhrAlmLineLocalOosPortn_Type()
)
pm1001lhrAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineLocalOosPortn.setStatus("current")
_Pm1001lhrAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm1001lhrAlmLineDdmWarningPortn_Object = MibTableColumn
pm1001lhrAlmLineDdmWarningPortn = _Pm1001lhrAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1, 10),
    _Pm1001lhrAlmLineDdmWarningPortn_Type()
)
pm1001lhrAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineDdmWarningPortn.setStatus("current")
_Pm1001lhrAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm1001lhrAlmLineDdmAlmPortn_Object = MibTableColumn
pm1001lhrAlmLineDdmAlmPortn = _Pm1001lhrAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1, 11),
    _Pm1001lhrAlmLineDdmAlmPortn_Type()
)
pm1001lhrAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineDdmAlmPortn.setStatus("current")
_Pm1001lhrAlmLineFailPortn_Type = EkiOnOff
_Pm1001lhrAlmLineFailPortn_Object = MibTableColumn
pm1001lhrAlmLineFailPortn = _Pm1001lhrAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 7, 1, 13),
    _Pm1001lhrAlmLineFailPortn_Type()
)
pm1001lhrAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmLineFailPortn.setStatus("current")
_Pm1001lhrAlmdfrmAlmTable_Object = MibTable
pm1001lhrAlmdfrmAlmTable = _Pm1001lhrAlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmdfrmAlmTable.setStatus("current")
_Pm1001lhrAlmdfrmAlmEntry_Object = MibTableRow
pm1001lhrAlmdfrmAlmEntry = _Pm1001lhrAlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 128, 1)
)
pm1001lhrAlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmdfrmAlmEntry.setStatus("current")


class _Pm1001lhrAlmdfrmAlmIndex_Type(Integer32):
    """Custom type pm1001lhrAlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmdfrmAlmIndex_Object = MibTableColumn
pm1001lhrAlmdfrmAlmIndex = _Pm1001lhrAlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 128, 1, 1),
    _Pm1001lhrAlmdfrmAlmIndex_Type()
)
pm1001lhrAlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmdfrmAlmIndex.setStatus("current")
_Pm1001lhrAlmDwAisDetPortn_Type = EkiOnOff
_Pm1001lhrAlmDwAisDetPortn_Object = MibTableColumn
pm1001lhrAlmDwAisDetPortn = _Pm1001lhrAlmDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 128, 1, 2),
    _Pm1001lhrAlmDwAisDetPortn_Type()
)
pm1001lhrAlmDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmDwAisDetPortn.setStatus("current")
_Pm1001lhrAlmDwRdiDetPortn_Type = EkiOnOff
_Pm1001lhrAlmDwRdiDetPortn_Object = MibTableColumn
pm1001lhrAlmDwRdiDetPortn = _Pm1001lhrAlmDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 128, 1, 3),
    _Pm1001lhrAlmDwRdiDetPortn_Type()
)
pm1001lhrAlmDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmDwRdiDetPortn.setStatus("current")
_Pm1001lhrAlmDwOofPortn_Type = EkiOnOff
_Pm1001lhrAlmDwOofPortn_Object = MibTableColumn
pm1001lhrAlmDwOofPortn = _Pm1001lhrAlmDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 128, 1, 4),
    _Pm1001lhrAlmDwOofPortn_Type()
)
pm1001lhrAlmDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmDwOofPortn.setStatus("current")
_Pm1001lhrAlmDwLofPortn_Type = EkiOnOff
_Pm1001lhrAlmDwLofPortn_Object = MibTableColumn
pm1001lhrAlmDwLofPortn = _Pm1001lhrAlmDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 128, 1, 5),
    _Pm1001lhrAlmDwLofPortn_Type()
)
pm1001lhrAlmDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmDwLofPortn.setStatus("current")
_Pm1001lhrAlmlineSyncAlarmsTable_Object = MibTable
pm1001lhrAlmlineSyncAlarmsTable = _Pm1001lhrAlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineSyncAlarmsTable.setStatus("current")
_Pm1001lhrAlmlineSyncAlarmsEntry_Object = MibTableRow
pm1001lhrAlmlineSyncAlarmsEntry = _Pm1001lhrAlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 133, 1)
)
pm1001lhrAlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineSyncAlarmsEntry.setStatus("current")


class _Pm1001lhrAlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pm1001lhrAlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmlineSyncAlarmsIndex_Object = MibTableColumn
pm1001lhrAlmlineSyncAlarmsIndex = _Pm1001lhrAlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 133, 1, 1),
    _Pm1001lhrAlmlineSyncAlarmsIndex_Type()
)
pm1001lhrAlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmlineSyncAlarmsIndex.setStatus("current")
_Pm1001lhrAlmDwLockerrPortn_Type = EkiOnOff
_Pm1001lhrAlmDwLockerrPortn_Object = MibTableColumn
pm1001lhrAlmDwLockerrPortn = _Pm1001lhrAlmDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 133, 1, 13),
    _Pm1001lhrAlmDwLockerrPortn_Type()
)
pm1001lhrAlmDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmDwLockerrPortn.setStatus("current")
_Pm1001lhrAlmUpLockerrPortn_Type = EkiOnOff
_Pm1001lhrAlmUpLockerrPortn_Object = MibTableColumn
pm1001lhrAlmUpLockerrPortn = _Pm1001lhrAlmUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 133, 1, 14),
    _Pm1001lhrAlmUpLockerrPortn_Type()
)
pm1001lhrAlmUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmUpLockerrPortn.setStatus("current")
_Pm1001lhrAlmDwLosPortn_Type = EkiOnOff
_Pm1001lhrAlmDwLosPortn_Object = MibTableColumn
pm1001lhrAlmDwLosPortn = _Pm1001lhrAlmDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 133, 1, 17),
    _Pm1001lhrAlmDwLosPortn_Type()
)
pm1001lhrAlmDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmDwLosPortn.setStatus("current")
_Pm1001lhrAlmlineXfp1AlarmsTable_Object = MibTable
pm1001lhrAlmlineXfp1AlarmsTable = _Pm1001lhrAlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1AlarmsTable.setStatus("current")
_Pm1001lhrAlmlineXfp1AlarmsEntry_Object = MibTableRow
pm1001lhrAlmlineXfp1AlarmsEntry = _Pm1001lhrAlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1)
)
pm1001lhrAlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1AlarmsEntry.setStatus("current")


class _Pm1001lhrAlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pm1001lhrAlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrAlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pm1001lhrAlmlineXfp1AlarmsIndex_Object = MibTableColumn
pm1001lhrAlmlineXfp1AlarmsIndex = _Pm1001lhrAlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 1),
    _Pm1001lhrAlmlineXfp1AlarmsIndex_Type()
)
pm1001lhrAlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmlineXfp1AlarmsIndex.setStatus("current")
_Pm1001lhrAlmModNrPortn_Type = EkiOnOff
_Pm1001lhrAlmModNrPortn_Object = MibTableColumn
pm1001lhrAlmModNrPortn = _Pm1001lhrAlmModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 3),
    _Pm1001lhrAlmModNrPortn_Type()
)
pm1001lhrAlmModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmModNrPortn.setStatus("current")
_Pm1001lhrAlmRxCdrNotLockedPortn_Type = EkiOnOff
_Pm1001lhrAlmRxCdrNotLockedPortn_Object = MibTableColumn
pm1001lhrAlmRxCdrNotLockedPortn = _Pm1001lhrAlmRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 4),
    _Pm1001lhrAlmRxCdrNotLockedPortn_Type()
)
pm1001lhrAlmRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmRxCdrNotLockedPortn.setStatus("current")
_Pm1001lhrAlmRxNrPortn_Type = EkiOnOff
_Pm1001lhrAlmRxNrPortn_Object = MibTableColumn
pm1001lhrAlmRxNrPortn = _Pm1001lhrAlmRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 6),
    _Pm1001lhrAlmRxNrPortn_Type()
)
pm1001lhrAlmRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmRxNrPortn.setStatus("current")
_Pm1001lhrAlmTxCdrNotLockedPortn_Type = EkiOnOff
_Pm1001lhrAlmTxCdrNotLockedPortn_Object = MibTableColumn
pm1001lhrAlmTxCdrNotLockedPortn = _Pm1001lhrAlmTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 7),
    _Pm1001lhrAlmTxCdrNotLockedPortn_Type()
)
pm1001lhrAlmTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxCdrNotLockedPortn.setStatus("current")
_Pm1001lhrAlmTxFaultPortn_Type = EkiOnOff
_Pm1001lhrAlmTxFaultPortn_Object = MibTableColumn
pm1001lhrAlmTxFaultPortn = _Pm1001lhrAlmTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 8),
    _Pm1001lhrAlmTxFaultPortn_Type()
)
pm1001lhrAlmTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxFaultPortn.setStatus("current")
_Pm1001lhrAlmTxNrPortn_Type = EkiOnOff
_Pm1001lhrAlmTxNrPortn_Object = MibTableColumn
pm1001lhrAlmTxNrPortn = _Pm1001lhrAlmTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 9),
    _Pm1001lhrAlmTxNrPortn_Type()
)
pm1001lhrAlmTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTxNrPortn.setStatus("current")
_Pm1001lhrAlmWavelengthUnlockedPortn_Type = EkiOnOff
_Pm1001lhrAlmWavelengthUnlockedPortn_Object = MibTableColumn
pm1001lhrAlmWavelengthUnlockedPortn = _Pm1001lhrAlmWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 15),
    _Pm1001lhrAlmWavelengthUnlockedPortn_Type()
)
pm1001lhrAlmWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmWavelengthUnlockedPortn.setStatus("current")
_Pm1001lhrAlmTecFaultPortn_Type = EkiOnOff
_Pm1001lhrAlmTecFaultPortn_Object = MibTableColumn
pm1001lhrAlmTecFaultPortn = _Pm1001lhrAlmTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 16),
    _Pm1001lhrAlmTecFaultPortn_Type()
)
pm1001lhrAlmTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmTecFaultPortn.setStatus("current")
_Pm1001lhrAlmApdSupplyFaultPortn_Type = EkiOnOff
_Pm1001lhrAlmApdSupplyFaultPortn_Object = MibTableColumn
pm1001lhrAlmApdSupplyFaultPortn = _Pm1001lhrAlmApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 2, 3, 3, 211, 1, 17),
    _Pm1001lhrAlmApdSupplyFaultPortn_Type()
)
pm1001lhrAlmApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrAlmApdSupplyFaultPortn.setStatus("current")
_Pm1001lhrmeasures_ObjectIdentity = ObjectIdentity
pm1001lhrmeasures = _Pm1001lhrmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3)
)
_Pm1001lhrMesrOther_ObjectIdentity = ObjectIdentity
pm1001lhrMesrOther = _Pm1001lhrMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 1)
)
_Pm1001lhrMesrsynth0_Type = EkiMeasureType
_Pm1001lhrMesrsynth0_Object = MibScalar
pm1001lhrMesrsynth0 = _Pm1001lhrMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 1, 0),
    _Pm1001lhrMesrsynth0_Type()
)
pm1001lhrMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrsynth0.setStatus("deprecated")
_Pm1001lhrMesrsynth1_Type = EkiMeasureType
_Pm1001lhrMesrsynth1_Object = MibScalar
pm1001lhrMesrsynth1 = _Pm1001lhrMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 1, 1),
    _Pm1001lhrMesrsynth1_Type()
)
pm1001lhrMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrsynth1.setStatus("deprecated")
_Pm1001lhrMesrClient_ObjectIdentity = ObjectIdentity
pm1001lhrMesrClient = _Pm1001lhrMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 2)
)
_Pm1001lhrMesrLine_ObjectIdentity = ObjectIdentity
pm1001lhrMesrLine = _Pm1001lhrMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3)
)
_Pm1001lhrMesrxfp1LxModTempMeasTable_Object = MibTable
pm1001lhrMesrxfp1LxModTempMeasTable = _Pm1001lhrMesrxfp1LxModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxModTempMeasTable.setStatus("current")
_Pm1001lhrMesrxfp1LxModTempMeasEntry_Object = MibTableRow
pm1001lhrMesrxfp1LxModTempMeasEntry = _Pm1001lhrMesrxfp1LxModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 208, 1)
)
pm1001lhrMesrxfp1LxModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrxfp1LxModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxModTempMeasEntry.setStatus("current")


class _Pm1001lhrMesrxfp1LxModTempMeasIndex_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LxModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrxfp1LxModTempMeasIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LxModTempMeasIndex_Object = MibTableColumn
pm1001lhrMesrxfp1LxModTempMeasIndex = _Pm1001lhrMesrxfp1LxModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 208, 1, 1),
    _Pm1001lhrMesrxfp1LxModTempMeasIndex_Type()
)
pm1001lhrMesrxfp1LxModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxModTempMeasIndex.setStatus("current")


class _Pm1001lhrMesrxfp1LxModTempMeasPortn_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LxModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrxfp1LxModTempMeasPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LxModTempMeasPortn_Object = MibTableColumn
pm1001lhrMesrxfp1LxModTempMeasPortn = _Pm1001lhrMesrxfp1LxModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 208, 1, 2),
    _Pm1001lhrMesrxfp1LxModTempMeasPortn_Type()
)
pm1001lhrMesrxfp1LxModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxModTempMeasPortn.setStatus("current")
_Pm1001lhrMesrxfp1ReservedTable_Object = MibTable
pm1001lhrMesrxfp1ReservedTable = _Pm1001lhrMesrxfp1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1ReservedTable.setStatus("deprecated")
_Pm1001lhrMesrxfp1ReservedEntry_Object = MibTableRow
pm1001lhrMesrxfp1ReservedEntry = _Pm1001lhrMesrxfp1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 209, 1)
)
pm1001lhrMesrxfp1ReservedEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrxfp1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1ReservedEntry.setStatus("deprecated")


class _Pm1001lhrMesrxfp1ReservedIndex_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrxfp1ReservedIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1ReservedIndex_Object = MibTableColumn
pm1001lhrMesrxfp1ReservedIndex = _Pm1001lhrMesrxfp1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 209, 1, 1),
    _Pm1001lhrMesrxfp1ReservedIndex_Type()
)
pm1001lhrMesrxfp1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1ReservedIndex.setStatus("deprecated")


class _Pm1001lhrMesrxfp1ReservedPortn_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrxfp1ReservedPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1ReservedPortn_Object = MibTableColumn
pm1001lhrMesrxfp1ReservedPortn = _Pm1001lhrMesrxfp1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 209, 1, 2),
    _Pm1001lhrMesrxfp1ReservedPortn_Type()
)
pm1001lhrMesrxfp1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1ReservedPortn.setStatus("deprecated")
_Pm1001lhrMesrxfp1LoBiasCurrentMeasTable_Object = MibTable
pm1001lhrMesrxfp1LoBiasCurrentMeasTable = _Pm1001lhrMesrxfp1LoBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LoBiasCurrentMeasTable.setStatus("current")
_Pm1001lhrMesrxfp1LoBiasCurrentMeasEntry_Object = MibTableRow
pm1001lhrMesrxfp1LoBiasCurrentMeasEntry = _Pm1001lhrMesrxfp1LoBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 210, 1)
)
pm1001lhrMesrxfp1LoBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrxfp1LoBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LoBiasCurrentMeasEntry.setStatus("current")


class _Pm1001lhrMesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LoBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrxfp1LoBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LoBiasCurrentMeasIndex_Object = MibTableColumn
pm1001lhrMesrxfp1LoBiasCurrentMeasIndex = _Pm1001lhrMesrxfp1LoBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 210, 1, 1),
    _Pm1001lhrMesrxfp1LoBiasCurrentMeasIndex_Type()
)
pm1001lhrMesrxfp1LoBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LoBiasCurrentMeasIndex.setStatus("current")


class _Pm1001lhrMesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LoBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrxfp1LoBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LoBiasCurrentMeasPortn_Object = MibTableColumn
pm1001lhrMesrxfp1LoBiasCurrentMeasPortn = _Pm1001lhrMesrxfp1LoBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 210, 1, 2),
    _Pm1001lhrMesrxfp1LoBiasCurrentMeasPortn_Type()
)
pm1001lhrMesrxfp1LoBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LoBiasCurrentMeasPortn.setStatus("current")
_Pm1001lhrMesrxfp1LoTxPowerMeasTable_Object = MibTable
pm1001lhrMesrxfp1LoTxPowerMeasTable = _Pm1001lhrMesrxfp1LoTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LoTxPowerMeasTable.setStatus("current")
_Pm1001lhrMesrxfp1LoTxPowerMeasEntry_Object = MibTableRow
pm1001lhrMesrxfp1LoTxPowerMeasEntry = _Pm1001lhrMesrxfp1LoTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 211, 1)
)
pm1001lhrMesrxfp1LoTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrxfp1LoTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LoTxPowerMeasEntry.setStatus("current")


class _Pm1001lhrMesrxfp1LoTxPowerMeasIndex_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LoTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrxfp1LoTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LoTxPowerMeasIndex_Object = MibTableColumn
pm1001lhrMesrxfp1LoTxPowerMeasIndex = _Pm1001lhrMesrxfp1LoTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 211, 1, 1),
    _Pm1001lhrMesrxfp1LoTxPowerMeasIndex_Type()
)
pm1001lhrMesrxfp1LoTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LoTxPowerMeasIndex.setStatus("current")


class _Pm1001lhrMesrxfp1LoTxPowerMeasPortn_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LoTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrxfp1LoTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LoTxPowerMeasPortn_Object = MibTableColumn
pm1001lhrMesrxfp1LoTxPowerMeasPortn = _Pm1001lhrMesrxfp1LoTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 211, 1, 2),
    _Pm1001lhrMesrxfp1LoTxPowerMeasPortn_Type()
)
pm1001lhrMesrxfp1LoTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LoTxPowerMeasPortn.setStatus("current")
_Pm1001lhrMesrxfp1LiRxPowerMeasTable_Object = MibTable
pm1001lhrMesrxfp1LiRxPowerMeasTable = _Pm1001lhrMesrxfp1LiRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LiRxPowerMeasTable.setStatus("current")
_Pm1001lhrMesrxfp1LiRxPowerMeasEntry_Object = MibTableRow
pm1001lhrMesrxfp1LiRxPowerMeasEntry = _Pm1001lhrMesrxfp1LiRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 212, 1)
)
pm1001lhrMesrxfp1LiRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrxfp1LiRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LiRxPowerMeasEntry.setStatus("current")


class _Pm1001lhrMesrxfp1LiRxPowerMeasIndex_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LiRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrxfp1LiRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LiRxPowerMeasIndex_Object = MibTableColumn
pm1001lhrMesrxfp1LiRxPowerMeasIndex = _Pm1001lhrMesrxfp1LiRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 212, 1, 1),
    _Pm1001lhrMesrxfp1LiRxPowerMeasIndex_Type()
)
pm1001lhrMesrxfp1LiRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LiRxPowerMeasIndex.setStatus("current")


class _Pm1001lhrMesrxfp1LiRxPowerMeasPortn_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LiRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrxfp1LiRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LiRxPowerMeasPortn_Object = MibTableColumn
pm1001lhrMesrxfp1LiRxPowerMeasPortn = _Pm1001lhrMesrxfp1LiRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 212, 1, 2),
    _Pm1001lhrMesrxfp1LiRxPowerMeasPortn_Type()
)
pm1001lhrMesrxfp1LiRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LiRxPowerMeasPortn.setStatus("current")
_Pm1001lhrMesrxfp1LxAux1MeasTable_Object = MibTable
pm1001lhrMesrxfp1LxAux1MeasTable = _Pm1001lhrMesrxfp1LxAux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxAux1MeasTable.setStatus("deprecated")
_Pm1001lhrMesrxfp1LxAux1MeasEntry_Object = MibTableRow
pm1001lhrMesrxfp1LxAux1MeasEntry = _Pm1001lhrMesrxfp1LxAux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 213, 1)
)
pm1001lhrMesrxfp1LxAux1MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrxfp1LxAux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxAux1MeasEntry.setStatus("deprecated")


class _Pm1001lhrMesrxfp1LxAux1MeasIndex_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LxAux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrxfp1LxAux1MeasIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LxAux1MeasIndex_Object = MibTableColumn
pm1001lhrMesrxfp1LxAux1MeasIndex = _Pm1001lhrMesrxfp1LxAux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 213, 1, 1),
    _Pm1001lhrMesrxfp1LxAux1MeasIndex_Type()
)
pm1001lhrMesrxfp1LxAux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxAux1MeasIndex.setStatus("deprecated")


class _Pm1001lhrMesrxfp1LxAux1MeasPortn_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LxAux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrxfp1LxAux1MeasPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LxAux1MeasPortn_Object = MibTableColumn
pm1001lhrMesrxfp1LxAux1MeasPortn = _Pm1001lhrMesrxfp1LxAux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 213, 1, 2),
    _Pm1001lhrMesrxfp1LxAux1MeasPortn_Type()
)
pm1001lhrMesrxfp1LxAux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxAux1MeasPortn.setStatus("deprecated")
_Pm1001lhrMesrxfp1LxAux2MeasTable_Object = MibTable
pm1001lhrMesrxfp1LxAux2MeasTable = _Pm1001lhrMesrxfp1LxAux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxAux2MeasTable.setStatus("deprecated")
_Pm1001lhrMesrxfp1LxAux2MeasEntry_Object = MibTableRow
pm1001lhrMesrxfp1LxAux2MeasEntry = _Pm1001lhrMesrxfp1LxAux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 214, 1)
)
pm1001lhrMesrxfp1LxAux2MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrxfp1LxAux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxAux2MeasEntry.setStatus("deprecated")


class _Pm1001lhrMesrxfp1LxAux2MeasIndex_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LxAux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrxfp1LxAux2MeasIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LxAux2MeasIndex_Object = MibTableColumn
pm1001lhrMesrxfp1LxAux2MeasIndex = _Pm1001lhrMesrxfp1LxAux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 214, 1, 1),
    _Pm1001lhrMesrxfp1LxAux2MeasIndex_Type()
)
pm1001lhrMesrxfp1LxAux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxAux2MeasIndex.setStatus("deprecated")


class _Pm1001lhrMesrxfp1LxAux2MeasPortn_Type(Integer32):
    """Custom type pm1001lhrMesrxfp1LxAux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrxfp1LxAux2MeasPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrxfp1LxAux2MeasPortn_Object = MibTableColumn
pm1001lhrMesrxfp1LxAux2MeasPortn = _Pm1001lhrMesrxfp1LxAux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 214, 1, 2),
    _Pm1001lhrMesrxfp1LxAux2MeasPortn_Type()
)
pm1001lhrMesrxfp1LxAux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrxfp1LxAux2MeasPortn.setStatus("deprecated")
_Pm1001lhrMesrotx1AgingTable_Object = MibTable
pm1001lhrMesrotx1AgingTable = _Pm1001lhrMesrotx1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1AgingTable.setStatus("current")
_Pm1001lhrMesrotx1AgingEntry_Object = MibTableRow
pm1001lhrMesrotx1AgingEntry = _Pm1001lhrMesrotx1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 224, 1)
)
pm1001lhrMesrotx1AgingEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrotx1AgingIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1AgingEntry.setStatus("current")


class _Pm1001lhrMesrotx1AgingIndex_Type(Integer32):
    """Custom type pm1001lhrMesrotx1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrotx1AgingIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrotx1AgingIndex_Object = MibTableColumn
pm1001lhrMesrotx1AgingIndex = _Pm1001lhrMesrotx1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 224, 1, 1),
    _Pm1001lhrMesrotx1AgingIndex_Type()
)
pm1001lhrMesrotx1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1AgingIndex.setStatus("current")


class _Pm1001lhrMesrotx1AgingPortn_Type(Integer32):
    """Custom type pm1001lhrMesrotx1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrotx1AgingPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrotx1AgingPortn_Object = MibTableColumn
pm1001lhrMesrotx1AgingPortn = _Pm1001lhrMesrotx1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 224, 1, 2),
    _Pm1001lhrMesrotx1AgingPortn_Type()
)
pm1001lhrMesrotx1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1AgingPortn.setStatus("current")
_Pm1001lhrMesrotx1LaserTemperatureTable_Object = MibTable
pm1001lhrMesrotx1LaserTemperatureTable = _Pm1001lhrMesrotx1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1LaserTemperatureTable.setStatus("deprecated")
_Pm1001lhrMesrotx1LaserTemperatureEntry_Object = MibTableRow
pm1001lhrMesrotx1LaserTemperatureEntry = _Pm1001lhrMesrotx1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 225, 1)
)
pm1001lhrMesrotx1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrotx1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1LaserTemperatureEntry.setStatus("deprecated")


class _Pm1001lhrMesrotx1LaserTemperatureIndex_Type(Integer32):
    """Custom type pm1001lhrMesrotx1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrotx1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrotx1LaserTemperatureIndex_Object = MibTableColumn
pm1001lhrMesrotx1LaserTemperatureIndex = _Pm1001lhrMesrotx1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 225, 1, 1),
    _Pm1001lhrMesrotx1LaserTemperatureIndex_Type()
)
pm1001lhrMesrotx1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1LaserTemperatureIndex.setStatus("deprecated")


class _Pm1001lhrMesrotx1LaserTemperaturePortn_Type(Integer32):
    """Custom type pm1001lhrMesrotx1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrotx1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrotx1LaserTemperaturePortn_Object = MibTableColumn
pm1001lhrMesrotx1LaserTemperaturePortn = _Pm1001lhrMesrotx1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 225, 1, 2),
    _Pm1001lhrMesrotx1LaserTemperaturePortn_Type()
)
pm1001lhrMesrotx1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1LaserTemperaturePortn.setStatus("deprecated")
_Pm1001lhrMesrotx1FreqDeviationTable_Object = MibTable
pm1001lhrMesrotx1FreqDeviationTable = _Pm1001lhrMesrotx1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1FreqDeviationTable.setStatus("current")
_Pm1001lhrMesrotx1FreqDeviationEntry_Object = MibTableRow
pm1001lhrMesrotx1FreqDeviationEntry = _Pm1001lhrMesrotx1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 226, 1)
)
pm1001lhrMesrotx1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrotx1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1FreqDeviationEntry.setStatus("current")


class _Pm1001lhrMesrotx1FreqDeviationIndex_Type(Integer32):
    """Custom type pm1001lhrMesrotx1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrotx1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrotx1FreqDeviationIndex_Object = MibTableColumn
pm1001lhrMesrotx1FreqDeviationIndex = _Pm1001lhrMesrotx1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 226, 1, 1),
    _Pm1001lhrMesrotx1FreqDeviationIndex_Type()
)
pm1001lhrMesrotx1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1FreqDeviationIndex.setStatus("current")


class _Pm1001lhrMesrotx1FreqDeviationPortn_Type(Integer32):
    """Custom type pm1001lhrMesrotx1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrotx1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrotx1FreqDeviationPortn_Object = MibTableColumn
pm1001lhrMesrotx1FreqDeviationPortn = _Pm1001lhrMesrotx1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 226, 1, 2),
    _Pm1001lhrMesrotx1FreqDeviationPortn_Type()
)
pm1001lhrMesrotx1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1FreqDeviationPortn.setStatus("current")
_Pm1001lhrMesrotx1LaserWvlengthTable_Object = MibTable
pm1001lhrMesrotx1LaserWvlengthTable = _Pm1001lhrMesrotx1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1LaserWvlengthTable.setStatus("current")
_Pm1001lhrMesrotx1LaserWvlengthEntry_Object = MibTableRow
pm1001lhrMesrotx1LaserWvlengthEntry = _Pm1001lhrMesrotx1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 227, 1)
)
pm1001lhrMesrotx1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrMesrotx1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1LaserWvlengthEntry.setStatus("current")


class _Pm1001lhrMesrotx1LaserWvlengthIndex_Type(Integer32):
    """Custom type pm1001lhrMesrotx1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrMesrotx1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pm1001lhrMesrotx1LaserWvlengthIndex_Object = MibTableColumn
pm1001lhrMesrotx1LaserWvlengthIndex = _Pm1001lhrMesrotx1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 227, 1, 1),
    _Pm1001lhrMesrotx1LaserWvlengthIndex_Type()
)
pm1001lhrMesrotx1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1LaserWvlengthIndex.setStatus("current")


class _Pm1001lhrMesrotx1LaserWvlengthPortn_Type(Integer32):
    """Custom type pm1001lhrMesrotx1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001lhrMesrotx1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pm1001lhrMesrotx1LaserWvlengthPortn_Object = MibTableColumn
pm1001lhrMesrotx1LaserWvlengthPortn = _Pm1001lhrMesrotx1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 3, 3, 227, 1, 2),
    _Pm1001lhrMesrotx1LaserWvlengthPortn_Type()
)
pm1001lhrMesrotx1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrMesrotx1LaserWvlengthPortn.setStatus("current")
_Pm1001lhrcounters_ObjectIdentity = ObjectIdentity
pm1001lhrcounters = _Pm1001lhrcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4)
)
_Pm1001lhrCntOther_ObjectIdentity = ObjectIdentity
pm1001lhrCntOther = _Pm1001lhrCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 1)
)
_Pm1001lhrCntClient_ObjectIdentity = ObjectIdentity
pm1001lhrCntClient = _Pm1001lhrCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 2)
)
_Pm1001lhrCntLine_ObjectIdentity = ObjectIdentity
pm1001lhrCntLine = _Pm1001lhrCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3)
)
_Pm1001lhrCntdfrmB1ErrCntTable_Object = MibTable
pm1001lhrCntdfrmB1ErrCntTable = _Pm1001lhrCntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmB1ErrCntTable.setStatus("current")
_Pm1001lhrCntdfrmB1ErrCntEntry_Object = MibTableRow
pm1001lhrCntdfrmB1ErrCntEntry = _Pm1001lhrCntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 152, 1)
)
pm1001lhrCntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmB1ErrCntEntry.setStatus("current")


class _Pm1001lhrCntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm1001lhrCntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm1001lhrCntdfrmB1ErrCntIndex_Object = MibTableColumn
pm1001lhrCntdfrmB1ErrCntIndex = _Pm1001lhrCntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 152, 1, 1),
    _Pm1001lhrCntdfrmB1ErrCntIndex_Type()
)
pm1001lhrCntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmB1ErrCntIndex.setStatus("current")
_Pm1001lhrCntdfrmB1ErrCntValuePortn_Type = Counter32
_Pm1001lhrCntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pm1001lhrCntdfrmB1ErrCntValuePortn = _Pm1001lhrCntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 152, 1, 2),
    _Pm1001lhrCntdfrmB1ErrCntValuePortn_Type()
)
pm1001lhrCntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmB1ErrCntValuePortn.setStatus("current")
_Pm1001lhrCntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm1001lhrCntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm1001lhrCntdfrmB1ErrCntErrorPortn = _Pm1001lhrCntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 152, 1, 3),
    _Pm1001lhrCntdfrmB1ErrCntErrorPortn_Type()
)
pm1001lhrCntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pm1001lhrCntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm1001lhrCntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm1001lhrCntdfrmB1ErrCntOverloadPortn = _Pm1001lhrCntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 152, 1, 4),
    _Pm1001lhrCntdfrmB1ErrCntOverloadPortn_Type()
)
pm1001lhrCntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm1001lhrCntdfrmTimCntTable_Object = MibTable
pm1001lhrCntdfrmTimCntTable = _Pm1001lhrCntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmTimCntTable.setStatus("current")
_Pm1001lhrCntdfrmTimCntEntry_Object = MibTableRow
pm1001lhrCntdfrmTimCntEntry = _Pm1001lhrCntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 153, 1)
)
pm1001lhrCntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmTimCntEntry.setStatus("current")


class _Pm1001lhrCntdfrmTimCntIndex_Type(Integer32):
    """Custom type pm1001lhrCntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm1001lhrCntdfrmTimCntIndex_Object = MibTableColumn
pm1001lhrCntdfrmTimCntIndex = _Pm1001lhrCntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 153, 1, 1),
    _Pm1001lhrCntdfrmTimCntIndex_Type()
)
pm1001lhrCntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmTimCntIndex.setStatus("current")
_Pm1001lhrCntdfrmTimCntValuePortn_Type = Counter32
_Pm1001lhrCntdfrmTimCntValuePortn_Object = MibTableColumn
pm1001lhrCntdfrmTimCntValuePortn = _Pm1001lhrCntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 153, 1, 2),
    _Pm1001lhrCntdfrmTimCntValuePortn_Type()
)
pm1001lhrCntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmTimCntValuePortn.setStatus("current")
_Pm1001lhrCntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pm1001lhrCntdfrmTimCntErrorPortn_Object = MibTableColumn
pm1001lhrCntdfrmTimCntErrorPortn = _Pm1001lhrCntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 153, 1, 3),
    _Pm1001lhrCntdfrmTimCntErrorPortn_Type()
)
pm1001lhrCntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmTimCntErrorPortn.setStatus("current")
_Pm1001lhrCntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm1001lhrCntdfrmTimCntOverloadPortn_Object = MibTableColumn
pm1001lhrCntdfrmTimCntOverloadPortn = _Pm1001lhrCntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 153, 1, 4),
    _Pm1001lhrCntdfrmTimCntOverloadPortn_Type()
)
pm1001lhrCntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmTimCntOverloadPortn.setStatus("current")
_Pm1001lhrCntdfrmPrimLineErrCntTable_Object = MibTable
pm1001lhrCntdfrmPrimLineErrCntTable = _Pm1001lhrCntdfrmPrimLineErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 154)
)
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmPrimLineErrCntTable.setStatus("current")
_Pm1001lhrCntdfrmPrimLineErrCntEntry_Object = MibTableRow
pm1001lhrCntdfrmPrimLineErrCntEntry = _Pm1001lhrCntdfrmPrimLineErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 154, 1)
)
pm1001lhrCntdfrmPrimLineErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCntdfrmPrimLineErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmPrimLineErrCntEntry.setStatus("current")


class _Pm1001lhrCntdfrmPrimLineErrCntIndex_Type(Integer32):
    """Custom type pm1001lhrCntdfrmPrimLineErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCntdfrmPrimLineErrCntIndex_Type.__name__ = "Integer32"
_Pm1001lhrCntdfrmPrimLineErrCntIndex_Object = MibTableColumn
pm1001lhrCntdfrmPrimLineErrCntIndex = _Pm1001lhrCntdfrmPrimLineErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 154, 1, 1),
    _Pm1001lhrCntdfrmPrimLineErrCntIndex_Type()
)
pm1001lhrCntdfrmPrimLineErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmPrimLineErrCntIndex.setStatus("current")
_Pm1001lhrCntdfrmPrimLineErrCntValuePortn_Type = Counter32
_Pm1001lhrCntdfrmPrimLineErrCntValuePortn_Object = MibTableColumn
pm1001lhrCntdfrmPrimLineErrCntValuePortn = _Pm1001lhrCntdfrmPrimLineErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 154, 1, 2),
    _Pm1001lhrCntdfrmPrimLineErrCntValuePortn_Type()
)
pm1001lhrCntdfrmPrimLineErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmPrimLineErrCntValuePortn.setStatus("current")
_Pm1001lhrCntdfrmPrimLineErrCntErrorPortn_Type = EkiOnOff
_Pm1001lhrCntdfrmPrimLineErrCntErrorPortn_Object = MibTableColumn
pm1001lhrCntdfrmPrimLineErrCntErrorPortn = _Pm1001lhrCntdfrmPrimLineErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 154, 1, 3),
    _Pm1001lhrCntdfrmPrimLineErrCntErrorPortn_Type()
)
pm1001lhrCntdfrmPrimLineErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmPrimLineErrCntErrorPortn.setStatus("current")
_Pm1001lhrCntdfrmPrimLineErrCntOverloadPortn_Type = EkiOnOff
_Pm1001lhrCntdfrmPrimLineErrCntOverloadPortn_Object = MibTableColumn
pm1001lhrCntdfrmPrimLineErrCntOverloadPortn = _Pm1001lhrCntdfrmPrimLineErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 3, 154, 1, 4),
    _Pm1001lhrCntdfrmPrimLineErrCntOverloadPortn_Type()
)
pm1001lhrCntdfrmPrimLineErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCntdfrmPrimLineErrCntOverloadPortn.setStatus("current")
_Pm1001lhrCntCountersReset_Type = EkiOnOff
_Pm1001lhrCntCountersReset_Object = MibScalar
pm1001lhrCntCountersReset = _Pm1001lhrCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 259),
    _Pm1001lhrCntCountersReset_Type()
)
pm1001lhrCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCntCountersReset.setStatus("current")
_Pm1001lhrCntCountersStop_Type = EkiOnOff
_Pm1001lhrCntCountersStop_Object = MibScalar
pm1001lhrCntCountersStop = _Pm1001lhrCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 4, 260),
    _Pm1001lhrCntCountersStop_Type()
)
pm1001lhrCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCntCountersStop.setStatus("current")
_Pm1001lhrcontrolsWrite_ObjectIdentity = ObjectIdentity
pm1001lhrcontrolsWrite = _Pm1001lhrcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6)
)
_Pm1001lhrCtrlOther_ObjectIdentity = ObjectIdentity
pm1001lhrCtrlOther = _Pm1001lhrCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1)
)
_Pm1001lhrCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm1001lhrCtrlconfMgnt1 = _Pm1001lhrCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 1)
)
_Pm1001lhrCtrlConf1Load1_Type = EkiOnOff
_Pm1001lhrCtrlConf1Load1_Object = MibScalar
pm1001lhrCtrlConf1Load1 = _Pm1001lhrCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 1, 1),
    _Pm1001lhrCtrlConf1Load1_Type()
)
pm1001lhrCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlConf1Load1.setStatus("current")
_Pm1001lhrCtrlConf2Load1_Type = EkiOnOff
_Pm1001lhrCtrlConf2Load1_Object = MibScalar
pm1001lhrCtrlConf2Load1 = _Pm1001lhrCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 1, 2),
    _Pm1001lhrCtrlConf2Load1_Type()
)
pm1001lhrCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlConf2Load1.setStatus("current")
_Pm1001lhrCtrlConf2Flash1_Type = EkiOnOff
_Pm1001lhrCtrlConf2Flash1_Object = MibScalar
pm1001lhrCtrlConf2Flash1 = _Pm1001lhrCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 1, 10),
    _Pm1001lhrCtrlConf2Flash1_Type()
)
pm1001lhrCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlConf2Flash1.setStatus("current")
_Pm1001lhrCtrlConf2Clear1_Type = EkiOnOff
_Pm1001lhrCtrlConf2Clear1_Object = MibScalar
pm1001lhrCtrlConf2Clear1 = _Pm1001lhrCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 1, 14),
    _Pm1001lhrCtrlConf2Clear1_Type()
)
pm1001lhrCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlConf2Clear1.setStatus("current")
_Pm1001lhrCtrlsynth4_ObjectIdentity = ObjectIdentity
pm1001lhrCtrlsynth4 = _Pm1001lhrCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 4)
)
_Pm1001lhrCtrlCorrelatOn_Type = EkiOnOff
_Pm1001lhrCtrlCorrelatOn_Object = MibScalar
pm1001lhrCtrlCorrelatOn = _Pm1001lhrCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 4, 1),
    _Pm1001lhrCtrlCorrelatOn_Type()
)
pm1001lhrCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlCorrelatOn.setStatus("current")
_Pm1001lhrCtrlCorrelatOff_Type = EkiOnOff
_Pm1001lhrCtrlCorrelatOff_Object = MibScalar
pm1001lhrCtrlCorrelatOff = _Pm1001lhrCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 4, 2),
    _Pm1001lhrCtrlCorrelatOff_Type()
)
pm1001lhrCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlCorrelatOff.setStatus("current")
_Pm1001lhrCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1001lhrCtrlswMgnt = _Pm1001lhrCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 5)
)
_Pm1001lhrCtrlColdReset_Type = EkiOnOff
_Pm1001lhrCtrlColdReset_Object = MibScalar
pm1001lhrCtrlColdReset = _Pm1001lhrCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 5, 2),
    _Pm1001lhrCtrlColdReset_Type()
)
pm1001lhrCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlColdReset.setStatus("current")
_Pm1001lhrCtrlWarmReset_Type = EkiOnOff
_Pm1001lhrCtrlWarmReset_Object = MibScalar
pm1001lhrCtrlWarmReset = _Pm1001lhrCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 5, 3),
    _Pm1001lhrCtrlWarmReset_Type()
)
pm1001lhrCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlWarmReset.setStatus("current")
_Pm1001lhrCtrlLoadSwBank1_Type = EkiOnOff
_Pm1001lhrCtrlLoadSwBank1_Object = MibScalar
pm1001lhrCtrlLoadSwBank1 = _Pm1001lhrCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 5, 5),
    _Pm1001lhrCtrlLoadSwBank1_Type()
)
pm1001lhrCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlLoadSwBank1.setStatus("current")
_Pm1001lhrCtrlLoadSwBank2_Type = EkiOnOff
_Pm1001lhrCtrlLoadSwBank2_Object = MibScalar
pm1001lhrCtrlLoadSwBank2 = _Pm1001lhrCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 5, 6),
    _Pm1001lhrCtrlLoadSwBank2_Type()
)
pm1001lhrCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlLoadSwBank2.setStatus("current")
_Pm1001lhrCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm1001lhrCtrlgwMgnt = _Pm1001lhrCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 6)
)
_Pm1001lhrCtrlCurrentGwReset_Type = EkiOnOff
_Pm1001lhrCtrlCurrentGwReset_Object = MibScalar
pm1001lhrCtrlCurrentGwReset = _Pm1001lhrCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 6, 1),
    _Pm1001lhrCtrlCurrentGwReset_Type()
)
pm1001lhrCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlCurrentGwReset.setStatus("current")
_Pm1001lhrCtrlLoadGwBank1_Type = EkiOnOff
_Pm1001lhrCtrlLoadGwBank1_Object = MibScalar
pm1001lhrCtrlLoadGwBank1 = _Pm1001lhrCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 6, 5),
    _Pm1001lhrCtrlLoadGwBank1_Type()
)
pm1001lhrCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlLoadGwBank1.setStatus("current")
_Pm1001lhrCtrlLoadGwBank2_Type = EkiOnOff
_Pm1001lhrCtrlLoadGwBank2_Object = MibScalar
pm1001lhrCtrlLoadGwBank2 = _Pm1001lhrCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 6, 6),
    _Pm1001lhrCtrlLoadGwBank2_Type()
)
pm1001lhrCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlLoadGwBank2.setStatus("current")
_Pm1001lhrCtrlLoadGwBank3_Type = EkiOnOff
_Pm1001lhrCtrlLoadGwBank3_Object = MibScalar
pm1001lhrCtrlLoadGwBank3 = _Pm1001lhrCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 6, 7),
    _Pm1001lhrCtrlLoadGwBank3_Type()
)
pm1001lhrCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlLoadGwBank3.setStatus("current")
_Pm1001lhrCtrlLoadGwBank4_Type = EkiOnOff
_Pm1001lhrCtrlLoadGwBank4_Object = MibScalar
pm1001lhrCtrlLoadGwBank4 = _Pm1001lhrCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 6, 8),
    _Pm1001lhrCtrlLoadGwBank4_Type()
)
pm1001lhrCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlLoadGwBank4.setStatus("current")
_Pm1001lhrCtrlledTest_ObjectIdentity = ObjectIdentity
pm1001lhrCtrlledTest = _Pm1001lhrCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 192)
)
_Pm1001lhrCtrlGreenLed_Type = EkiOnOff
_Pm1001lhrCtrlGreenLed_Object = MibScalar
pm1001lhrCtrlGreenLed = _Pm1001lhrCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 192, 1),
    _Pm1001lhrCtrlGreenLed_Type()
)
pm1001lhrCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlGreenLed.setStatus("current")
_Pm1001lhrCtrlRedLed_Type = EkiOnOff
_Pm1001lhrCtrlRedLed_Object = MibScalar
pm1001lhrCtrlRedLed = _Pm1001lhrCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 192, 2),
    _Pm1001lhrCtrlRedLed_Type()
)
pm1001lhrCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlRedLed.setStatus("current")
_Pm1001lhrCtrlLedOff_Type = EkiOnOff
_Pm1001lhrCtrlLedOff_Object = MibScalar
pm1001lhrCtrlLedOff = _Pm1001lhrCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 192, 3),
    _Pm1001lhrCtrlLedOff_Type()
)
pm1001lhrCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlLedOff.setStatus("current")
_Pm1001lhrCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm1001lhrCtrlmoduleOosMode = _Pm1001lhrCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 193)
)
_Pm1001lhrCtrlModuleOosMode_Type = EkiOnOff
_Pm1001lhrCtrlModuleOosMode_Object = MibScalar
pm1001lhrCtrlModuleOosMode = _Pm1001lhrCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 1, 193, 1),
    _Pm1001lhrCtrlModuleOosMode_Type()
)
pm1001lhrCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlModuleOosMode.setStatus("current")
_Pm1001lhrCtrlClient_ObjectIdentity = ObjectIdentity
pm1001lhrCtrlClient = _Pm1001lhrCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 2)
)
_Pm1001lhrCtrlaccessLoopTable_Object = MibTable
pm1001lhrCtrlaccessLoopTable = _Pm1001lhrCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlaccessLoopTable.setStatus("current")
_Pm1001lhrCtrlaccessLoopEntry_Object = MibTableRow
pm1001lhrCtrlaccessLoopEntry = _Pm1001lhrCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 2, 16, 1)
)
pm1001lhrCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlaccessLoopEntry.setStatus("current")


class _Pm1001lhrCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm1001lhrCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrlaccessLoopIndex_Object = MibTableColumn
pm1001lhrCtrlaccessLoopIndex = _Pm1001lhrCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 2, 16, 1, 1),
    _Pm1001lhrCtrlaccessLoopIndex_Type()
)
pm1001lhrCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrlaccessLoopIndex.setStatus("current")
_Pm1001lhrCtrlaccessLoopPortn_Type = EkiState
_Pm1001lhrCtrlaccessLoopPortn_Object = MibTableColumn
pm1001lhrCtrlaccessLoopPortn = _Pm1001lhrCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 2, 16, 1, 2),
    _Pm1001lhrCtrlaccessLoopPortn_Type()
)
pm1001lhrCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlaccessLoopPortn.setStatus("current")
_Pm1001lhrCtrlclientAccessTermLoopTable_Object = MibTable
pm1001lhrCtrlclientAccessTermLoopTable = _Pm1001lhrCtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlclientAccessTermLoopTable.setStatus("current")
_Pm1001lhrCtrlclientAccessTermLoopEntry_Object = MibTableRow
pm1001lhrCtrlclientAccessTermLoopEntry = _Pm1001lhrCtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 2, 26, 1)
)
pm1001lhrCtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm1001lhrCtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm1001lhrCtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm1001lhrCtrlclientAccessTermLoopIndex = _Pm1001lhrCtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 2, 26, 1, 1),
    _Pm1001lhrCtrlclientAccessTermLoopIndex_Type()
)
pm1001lhrCtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrlclientAccessTermLoopIndex.setStatus("current")
_Pm1001lhrCtrlclientAccessTermLoopPortn_Type = EkiState
_Pm1001lhrCtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm1001lhrCtrlclientAccessTermLoopPortn = _Pm1001lhrCtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 2, 26, 1, 2),
    _Pm1001lhrCtrlclientAccessTermLoopPortn_Type()
)
pm1001lhrCtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlclientAccessTermLoopPortn.setStatus("current")
_Pm1001lhrCtrlLine_ObjectIdentity = ObjectIdentity
pm1001lhrCtrlLine = _Pm1001lhrCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3)
)
_Pm1001lhrCtrlprotocol_Type = EkiProtocol
_Pm1001lhrCtrlprotocol_Object = MibScalar
pm1001lhrCtrlprotocol = _Pm1001lhrCtrlprotocol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 52),
    _Pm1001lhrCtrlprotocol_Type()
)
pm1001lhrCtrlprotocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlprotocol.setStatus("current")
_Pm1001lhrCtrlfecDisableTable_Object = MibTable
pm1001lhrCtrlfecDisableTable = _Pm1001lhrCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlfecDisableTable.setStatus("current")
_Pm1001lhrCtrlfecDisableEntry_Object = MibTableRow
pm1001lhrCtrlfecDisableEntry = _Pm1001lhrCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 69, 1)
)
pm1001lhrCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlfecDisableEntry.setStatus("current")


class _Pm1001lhrCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm1001lhrCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrlfecDisableIndex_Object = MibTableColumn
pm1001lhrCtrlfecDisableIndex = _Pm1001lhrCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 69, 1, 1),
    _Pm1001lhrCtrlfecDisableIndex_Type()
)
pm1001lhrCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrlfecDisableIndex.setStatus("current")
_Pm1001lhrCtrlfecDisablePortn_Type = EkiState
_Pm1001lhrCtrlfecDisablePortn_Object = MibTableColumn
pm1001lhrCtrlfecDisablePortn = _Pm1001lhrCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 69, 1, 2),
    _Pm1001lhrCtrlfecDisablePortn_Type()
)
pm1001lhrCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlfecDisablePortn.setStatus("current")
_Pm1001lhrCtrllineOosModeTable_Object = MibTable
pm1001lhrCtrllineOosModeTable = _Pm1001lhrCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllineOosModeTable.setStatus("current")
_Pm1001lhrCtrllineOosModeEntry_Object = MibTableRow
pm1001lhrCtrllineOosModeEntry = _Pm1001lhrCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 74, 1)
)
pm1001lhrCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllineOosModeEntry.setStatus("current")


class _Pm1001lhrCtrllineOosModeIndex_Type(Integer32):
    """Custom type pm1001lhrCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrllineOosModeIndex_Object = MibTableColumn
pm1001lhrCtrllineOosModeIndex = _Pm1001lhrCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 74, 1, 1),
    _Pm1001lhrCtrllineOosModeIndex_Type()
)
pm1001lhrCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrllineOosModeIndex.setStatus("current")
_Pm1001lhrCtrllineOosModePortn_Type = EkiState
_Pm1001lhrCtrllineOosModePortn_Object = MibTableColumn
pm1001lhrCtrllineOosModePortn = _Pm1001lhrCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 74, 1, 2),
    _Pm1001lhrCtrllineOosModePortn_Type()
)
pm1001lhrCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrllineOosModePortn.setStatus("current")
_Pm1001lhrCtrlxfpOnoffTable_Object = MibTable
pm1001lhrCtrlxfpOnoffTable = _Pm1001lhrCtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpOnoffTable.setStatus("current")
_Pm1001lhrCtrlxfpOnoffEntry_Object = MibTableRow
pm1001lhrCtrlxfpOnoffEntry = _Pm1001lhrCtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 208, 1)
)
pm1001lhrCtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpOnoffEntry.setStatus("current")


class _Pm1001lhrCtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pm1001lhrCtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrlxfpOnoffIndex_Object = MibTableColumn
pm1001lhrCtrlxfpOnoffIndex = _Pm1001lhrCtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 208, 1, 1),
    _Pm1001lhrCtrlxfpOnoffIndex_Type()
)
pm1001lhrCtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpOnoffIndex.setStatus("current")
_Pm1001lhrCtrlxfpOnoffPortn_Type = EkiState
_Pm1001lhrCtrlxfpOnoffPortn_Object = MibTableColumn
pm1001lhrCtrlxfpOnoffPortn = _Pm1001lhrCtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 208, 1, 2),
    _Pm1001lhrCtrlxfpOnoffPortn_Type()
)
pm1001lhrCtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpOnoffPortn.setStatus("current")
_Pm1001lhrCtrlxfpLineLoopTable_Object = MibTable
pm1001lhrCtrlxfpLineLoopTable = _Pm1001lhrCtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpLineLoopTable.setStatus("current")
_Pm1001lhrCtrlxfpLineLoopEntry_Object = MibTableRow
pm1001lhrCtrlxfpLineLoopEntry = _Pm1001lhrCtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 209, 1)
)
pm1001lhrCtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpLineLoopEntry.setStatus("current")


class _Pm1001lhrCtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pm1001lhrCtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrlxfpLineLoopIndex_Object = MibTableColumn
pm1001lhrCtrlxfpLineLoopIndex = _Pm1001lhrCtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 209, 1, 1),
    _Pm1001lhrCtrlxfpLineLoopIndex_Type()
)
pm1001lhrCtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpLineLoopIndex.setStatus("current")
_Pm1001lhrCtrlxfpLineLoopPortn_Type = EkiState
_Pm1001lhrCtrlxfpLineLoopPortn_Object = MibTableColumn
pm1001lhrCtrlxfpLineLoopPortn = _Pm1001lhrCtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 209, 1, 2),
    _Pm1001lhrCtrlxfpLineLoopPortn_Type()
)
pm1001lhrCtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpLineLoopPortn.setStatus("current")
_Pm1001lhrCtrlxfpXfiLoopTable_Object = MibTable
pm1001lhrCtrlxfpXfiLoopTable = _Pm1001lhrCtrlxfpXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpXfiLoopTable.setStatus("current")
_Pm1001lhrCtrlxfpXfiLoopEntry_Object = MibTableRow
pm1001lhrCtrlxfpXfiLoopEntry = _Pm1001lhrCtrlxfpXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 210, 1)
)
pm1001lhrCtrlxfpXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrlxfpXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpXfiLoopEntry.setStatus("current")


class _Pm1001lhrCtrlxfpXfiLoopIndex_Type(Integer32):
    """Custom type pm1001lhrCtrlxfpXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrlxfpXfiLoopIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrlxfpXfiLoopIndex_Object = MibTableColumn
pm1001lhrCtrlxfpXfiLoopIndex = _Pm1001lhrCtrlxfpXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 210, 1, 1),
    _Pm1001lhrCtrlxfpXfiLoopIndex_Type()
)
pm1001lhrCtrlxfpXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpXfiLoopIndex.setStatus("current")
_Pm1001lhrCtrlxfpXfiLoopPortn_Type = EkiState
_Pm1001lhrCtrlxfpXfiLoopPortn_Object = MibTableColumn
pm1001lhrCtrlxfpXfiLoopPortn = _Pm1001lhrCtrlxfpXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 210, 1, 2),
    _Pm1001lhrCtrlxfpXfiLoopPortn_Type()
)
pm1001lhrCtrlxfpXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrlxfpXfiLoopPortn.setStatus("current")
_Pm1001lhrCtrllineTunableChannelTable_Object = MibTable
pm1001lhrCtrllineTunableChannelTable = _Pm1001lhrCtrllineTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllineTunableChannelTable.setStatus("current")
_Pm1001lhrCtrllineTunableChannelEntry_Object = MibTableRow
pm1001lhrCtrllineTunableChannelEntry = _Pm1001lhrCtrllineTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 212, 1)
)
pm1001lhrCtrllineTunableChannelEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrllineTunableChannelIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllineTunableChannelEntry.setStatus("current")


class _Pm1001lhrCtrllineTunableChannelIndex_Type(Integer32):
    """Custom type pm1001lhrCtrllineTunableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrllineTunableChannelIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrllineTunableChannelIndex_Object = MibTableColumn
pm1001lhrCtrllineTunableChannelIndex = _Pm1001lhrCtrllineTunableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 212, 1, 1),
    _Pm1001lhrCtrllineTunableChannelIndex_Type()
)
pm1001lhrCtrllineTunableChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrllineTunableChannelIndex.setStatus("current")
_Pm1001lhrCtrllineTunableChannelPortn_Type = Pm1001lhrOtxChannel
_Pm1001lhrCtrllineTunableChannelPortn_Object = MibTableColumn
pm1001lhrCtrllineTunableChannelPortn = _Pm1001lhrCtrllineTunableChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 212, 1, 2),
    _Pm1001lhrCtrllineTunableChannelPortn_Type()
)
pm1001lhrCtrllineTunableChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrllineTunableChannelPortn.setStatus("current")
_Pm1001lhrCtrllinePhotodiodeModeTable_Object = MibTable
pm1001lhrCtrllinePhotodiodeModeTable = _Pm1001lhrCtrllinePhotodiodeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 213)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePhotodiodeModeTable.setStatus("current")
_Pm1001lhrCtrllinePhotodiodeModeEntry_Object = MibTableRow
pm1001lhrCtrllinePhotodiodeModeEntry = _Pm1001lhrCtrllinePhotodiodeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 213, 1)
)
pm1001lhrCtrllinePhotodiodeModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrllinePhotodiodeModeIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePhotodiodeModeEntry.setStatus("current")


class _Pm1001lhrCtrllinePhotodiodeModeIndex_Type(Integer32):
    """Custom type pm1001lhrCtrllinePhotodiodeModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrllinePhotodiodeModeIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrllinePhotodiodeModeIndex_Object = MibTableColumn
pm1001lhrCtrllinePhotodiodeModeIndex = _Pm1001lhrCtrllinePhotodiodeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 213, 1, 1),
    _Pm1001lhrCtrllinePhotodiodeModeIndex_Type()
)
pm1001lhrCtrllinePhotodiodeModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePhotodiodeModeIndex.setStatus("current")
_Pm1001lhrCtrllinePhotodiodeModePortn_Type = Pm1001lhrOtxMode
_Pm1001lhrCtrllinePhotodiodeModePortn_Object = MibTableColumn
pm1001lhrCtrllinePhotodiodeModePortn = _Pm1001lhrCtrllinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 213, 1, 2),
    _Pm1001lhrCtrllinePhotodiodeModePortn_Type()
)
pm1001lhrCtrllinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePhotodiodeModePortn.setStatus("current")
_Pm1001lhrCtrllinePhotodiodeValueTable_Object = MibTable
pm1001lhrCtrllinePhotodiodeValueTable = _Pm1001lhrCtrllinePhotodiodeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 214)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePhotodiodeValueTable.setStatus("current")
_Pm1001lhrCtrllinePhotodiodeValueEntry_Object = MibTableRow
pm1001lhrCtrllinePhotodiodeValueEntry = _Pm1001lhrCtrllinePhotodiodeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 214, 1)
)
pm1001lhrCtrllinePhotodiodeValueEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrllinePhotodiodeValueIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePhotodiodeValueEntry.setStatus("current")


class _Pm1001lhrCtrllinePhotodiodeValueIndex_Type(Integer32):
    """Custom type pm1001lhrCtrllinePhotodiodeValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrllinePhotodiodeValueIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrllinePhotodiodeValueIndex_Object = MibTableColumn
pm1001lhrCtrllinePhotodiodeValueIndex = _Pm1001lhrCtrllinePhotodiodeValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 214, 1, 1),
    _Pm1001lhrCtrllinePhotodiodeValueIndex_Type()
)
pm1001lhrCtrllinePhotodiodeValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePhotodiodeValueIndex.setStatus("current")
_Pm1001lhrCtrllinePhotodiodeValuePortn_Type = Pm1001lhrAdjustValue
_Pm1001lhrCtrllinePhotodiodeValuePortn_Object = MibTableColumn
pm1001lhrCtrllinePhotodiodeValuePortn = _Pm1001lhrCtrllinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 214, 1, 2),
    _Pm1001lhrCtrllinePhotodiodeValuePortn_Type()
)
pm1001lhrCtrllinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePhotodiodeValuePortn.setStatus("current")
_Pm1001lhrCtrllinePowerLaserTable_Object = MibTable
pm1001lhrCtrllinePowerLaserTable = _Pm1001lhrCtrllinePowerLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 215)
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePowerLaserTable.setStatus("current")
_Pm1001lhrCtrllinePowerLaserEntry_Object = MibTableRow
pm1001lhrCtrllinePowerLaserEntry = _Pm1001lhrCtrllinePowerLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 215, 1)
)
pm1001lhrCtrllinePowerLaserEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCtrllinePowerLaserIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePowerLaserEntry.setStatus("current")


class _Pm1001lhrCtrllinePowerLaserIndex_Type(Integer32):
    """Custom type pm1001lhrCtrllinePowerLaserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCtrllinePowerLaserIndex_Type.__name__ = "Integer32"
_Pm1001lhrCtrllinePowerLaserIndex_Object = MibTableColumn
pm1001lhrCtrllinePowerLaserIndex = _Pm1001lhrCtrllinePowerLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 215, 1, 1),
    _Pm1001lhrCtrllinePowerLaserIndex_Type()
)
pm1001lhrCtrllinePowerLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePowerLaserIndex.setStatus("current")


class _Pm1001lhrCtrllinePowerLaserPortn_Type(Integer32):
    """Custom type pm1001lhrCtrllinePowerLaserPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1001lhrCtrllinePowerLaserPortn_Type.__name__ = "Integer32"
_Pm1001lhrCtrllinePowerLaserPortn_Object = MibTableColumn
pm1001lhrCtrllinePowerLaserPortn = _Pm1001lhrCtrllinePowerLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 6, 3, 215, 1, 2),
    _Pm1001lhrCtrllinePowerLaserPortn_Type()
)
pm1001lhrCtrllinePowerLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCtrllinePowerLaserPortn.setStatus("current")
_Pm1001lhrri_ObjectIdentity = ObjectIdentity
pm1001lhrri = _Pm1001lhrri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7)
)
_Pm1001lhrriTable_ObjectIdentity = ObjectIdentity
pm1001lhrriTable = _Pm1001lhrriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 1)
)
_Pm1001lhrRinvLineTable_Object = MibTable
pm1001lhrRinvLineTable = _Pm1001lhrRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm1001lhrRinvLineTable.setStatus("current")
_Pm1001lhrRinvLineEntry_Object = MibTableRow
pm1001lhrRinvLineEntry = _Pm1001lhrRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 1, 1, 1)
)
pm1001lhrRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrRinvLineEntry.setStatus("current")


class _Pm1001lhrRinvLineIndex_Type(Integer32):
    """Custom type pm1001lhrRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1001lhrRinvLineIndex_Type.__name__ = "Integer32"
_Pm1001lhrRinvLineIndex_Object = MibTableColumn
pm1001lhrRinvLineIndex = _Pm1001lhrRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 1, 1, 1, 1),
    _Pm1001lhrRinvLineIndex_Type()
)
pm1001lhrRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrRinvLineIndex.setStatus("current")
_Pm1001lhrRinvxfpLine_Type = DisplayString
_Pm1001lhrRinvxfpLine_Object = MibTableColumn
pm1001lhrRinvxfpLine = _Pm1001lhrRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 1, 1, 1, 2),
    _Pm1001lhrRinvxfpLine_Type()
)
pm1001lhrRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrRinvxfpLine.setStatus("current")
_Pm1001lhrRinvReloadInventory_Type = EkiOnOff
_Pm1001lhrRinvReloadInventory_Object = MibScalar
pm1001lhrRinvReloadInventory = _Pm1001lhrRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 2),
    _Pm1001lhrRinvReloadInventory_Type()
)
pm1001lhrRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrRinvReloadInventory.setStatus("current")
_Pm1001lhrRinvHwPlatform_Type = DisplayString
_Pm1001lhrRinvHwPlatform_Object = MibScalar
pm1001lhrRinvHwPlatform = _Pm1001lhrRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 3),
    _Pm1001lhrRinvHwPlatform_Type()
)
pm1001lhrRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrRinvHwPlatform.setStatus("current")
_Pm1001lhrRinvModulePlatform_Type = DisplayString
_Pm1001lhrRinvModulePlatform_Object = MibScalar
pm1001lhrRinvModulePlatform = _Pm1001lhrRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 4),
    _Pm1001lhrRinvModulePlatform_Type()
)
pm1001lhrRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrRinvModulePlatform.setStatus("current")
_Pm1001lhrRinvSwPlatform_Type = DisplayString
_Pm1001lhrRinvSwPlatform_Object = MibScalar
pm1001lhrRinvSwPlatform = _Pm1001lhrRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 5),
    _Pm1001lhrRinvSwPlatform_Type()
)
pm1001lhrRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrRinvSwPlatform.setStatus("current")
_Pm1001lhrRinvGwPlatform_Type = DisplayString
_Pm1001lhrRinvGwPlatform_Object = MibScalar
pm1001lhrRinvGwPlatform = _Pm1001lhrRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 7, 6),
    _Pm1001lhrRinvGwPlatform_Type()
)
pm1001lhrRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrRinvGwPlatform.setStatus("current")
_Pm1001lhrdownload_ObjectIdentity = ObjectIdentity
pm1001lhrdownload = _Pm1001lhrdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8)
)
_Pm1001lhrDwlOther_ObjectIdentity = ObjectIdentity
pm1001lhrDwlOther = _Pm1001lhrDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1)
)
_Pm1001lhrDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm1001lhrDwlrestartProcess = _Pm1001lhrDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 0)
)
_Pm1001lhrDwlWarmRestartProcessed_Type = EkiOnOff
_Pm1001lhrDwlWarmRestartProcessed_Object = MibScalar
pm1001lhrDwlWarmRestartProcessed = _Pm1001lhrDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 0, 1),
    _Pm1001lhrDwlWarmRestartProcessed_Type()
)
pm1001lhrDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlWarmRestartProcessed.setStatus("current")
_Pm1001lhrDwlColdRestartProcessed_Type = EkiOnOff
_Pm1001lhrDwlColdRestartProcessed_Object = MibScalar
pm1001lhrDwlColdRestartProcessed = _Pm1001lhrDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 0, 2),
    _Pm1001lhrDwlColdRestartProcessed_Type()
)
pm1001lhrDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlColdRestartProcessed.setStatus("current")
_Pm1001lhrDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm1001lhrDwlswBanksUsed = _Pm1001lhrDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 1)
)
_Pm1001lhrDwlSwBank1Used_Type = EkiOnOff
_Pm1001lhrDwlSwBank1Used_Object = MibScalar
pm1001lhrDwlSwBank1Used = _Pm1001lhrDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 1, 1),
    _Pm1001lhrDwlSwBank1Used_Type()
)
pm1001lhrDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlSwBank1Used.setStatus("current")
_Pm1001lhrDwlSwBank2Used_Type = EkiOnOff
_Pm1001lhrDwlSwBank2Used_Object = MibScalar
pm1001lhrDwlSwBank2Used = _Pm1001lhrDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 1, 2),
    _Pm1001lhrDwlSwBank2Used_Type()
)
pm1001lhrDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlSwBank2Used.setStatus("current")
_Pm1001lhrDwlSwBank1Notempty_Type = EkiOnOff
_Pm1001lhrDwlSwBank1Notempty_Object = MibScalar
pm1001lhrDwlSwBank1Notempty = _Pm1001lhrDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 1, 5),
    _Pm1001lhrDwlSwBank1Notempty_Type()
)
pm1001lhrDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlSwBank1Notempty.setStatus("current")
_Pm1001lhrDwlSwBank2Notempty_Type = EkiOnOff
_Pm1001lhrDwlSwBank2Notempty_Object = MibScalar
pm1001lhrDwlSwBank2Notempty = _Pm1001lhrDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 1, 6),
    _Pm1001lhrDwlSwBank2Notempty_Type()
)
pm1001lhrDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlSwBank2Notempty.setStatus("current")
_Pm1001lhrDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm1001lhrDwlgwBanksUsed = _Pm1001lhrDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 2)
)
_Pm1001lhrDwlGwBank1Used_Type = EkiOnOff
_Pm1001lhrDwlGwBank1Used_Object = MibScalar
pm1001lhrDwlGwBank1Used = _Pm1001lhrDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 2, 1),
    _Pm1001lhrDwlGwBank1Used_Type()
)
pm1001lhrDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlGwBank1Used.setStatus("current")
_Pm1001lhrDwlGwBank2Used_Type = EkiOnOff
_Pm1001lhrDwlGwBank2Used_Object = MibScalar
pm1001lhrDwlGwBank2Used = _Pm1001lhrDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 2, 2),
    _Pm1001lhrDwlGwBank2Used_Type()
)
pm1001lhrDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlGwBank2Used.setStatus("current")
_Pm1001lhrDwlGwBank3Used_Type = EkiOnOff
_Pm1001lhrDwlGwBank3Used_Object = MibScalar
pm1001lhrDwlGwBank3Used = _Pm1001lhrDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 2, 3),
    _Pm1001lhrDwlGwBank3Used_Type()
)
pm1001lhrDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlGwBank3Used.setStatus("current")
_Pm1001lhrDwlGwBank4Used_Type = EkiOnOff
_Pm1001lhrDwlGwBank4Used_Object = MibScalar
pm1001lhrDwlGwBank4Used = _Pm1001lhrDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 2, 4),
    _Pm1001lhrDwlGwBank4Used_Type()
)
pm1001lhrDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlGwBank4Used.setStatus("current")
_Pm1001lhrDwlGwBank1Notempty_Type = EkiOnOff
_Pm1001lhrDwlGwBank1Notempty_Object = MibScalar
pm1001lhrDwlGwBank1Notempty = _Pm1001lhrDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 2, 5),
    _Pm1001lhrDwlGwBank1Notempty_Type()
)
pm1001lhrDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlGwBank1Notempty.setStatus("current")
_Pm1001lhrDwlGwBank2Notempty_Type = EkiOnOff
_Pm1001lhrDwlGwBank2Notempty_Object = MibScalar
pm1001lhrDwlGwBank2Notempty = _Pm1001lhrDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 2, 6),
    _Pm1001lhrDwlGwBank2Notempty_Type()
)
pm1001lhrDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlGwBank2Notempty.setStatus("current")
_Pm1001lhrDwlGwBank3Notempty_Type = EkiOnOff
_Pm1001lhrDwlGwBank3Notempty_Object = MibScalar
pm1001lhrDwlGwBank3Notempty = _Pm1001lhrDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 2, 7),
    _Pm1001lhrDwlGwBank3Notempty_Type()
)
pm1001lhrDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlGwBank3Notempty.setStatus("current")
_Pm1001lhrDwlGwBank4Notempty_Type = EkiOnOff
_Pm1001lhrDwlGwBank4Notempty_Object = MibScalar
pm1001lhrDwlGwBank4Notempty = _Pm1001lhrDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 1, 2, 8),
    _Pm1001lhrDwlGwBank4Notempty_Type()
)
pm1001lhrDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrDwlGwBank4Notempty.setStatus("current")
_Pm1001lhrDwlClient_ObjectIdentity = ObjectIdentity
pm1001lhrDwlClient = _Pm1001lhrDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 2)
)
_Pm1001lhrDwlLine_ObjectIdentity = ObjectIdentity
pm1001lhrDwlLine = _Pm1001lhrDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 8, 3)
)
_Pm1001lhrConfig_ObjectIdentity = ObjectIdentity
pm1001lhrConfig = _Pm1001lhrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9)
)
_Pm1001lhrCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm1001lhrCfgAccessCAisCsf = _Pm1001lhrCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 1)
)
_Pm1001lhrCfgStartup_ObjectIdentity = ObjectIdentity
pm1001lhrCfgStartup = _Pm1001lhrCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2)
)
_Pm1001lhrtablelineStartup_ObjectIdentity = ObjectIdentity
pm1001lhrtablelineStartup = _Pm1001lhrtablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 1)
)


class _Pm1001lhrCfgsystConfLine1_Type(Unsigned32):
    """Custom type pm1001lhrCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgsystConfLine1_Object = MibScalar
pm1001lhrCfgsystConfLine1 = _Pm1001lhrCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 1, 2),
    _Pm1001lhrCfgsystConfLine1_Type()
)
pm1001lhrCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgsystConfLine1.setStatus("current")


class _Pm1001lhrCfgnetConfMod_Type(Unsigned32):
    """Custom type pm1001lhrCfgnetConfMod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgnetConfMod_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgnetConfMod_Object = MibScalar
pm1001lhrCfgnetConfMod = _Pm1001lhrCfgnetConfMod_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 1, 3),
    _Pm1001lhrCfgnetConfMod_Type()
)
pm1001lhrCfgnetConfMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgnetConfMod.setStatus("current")


class _Pm1001lhrCfglineOptions1_Type(Unsigned32):
    """Custom type pm1001lhrCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfglineOptions1_Type.__name__ = "Unsigned32"
_Pm1001lhrCfglineOptions1_Object = MibScalar
pm1001lhrCfglineOptions1 = _Pm1001lhrCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 1, 5),
    _Pm1001lhrCfglineOptions1_Type()
)
pm1001lhrCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfglineOptions1.setStatus("current")


class _Pm1001lhrCfgsystConfLine2_Type(Unsigned32):
    """Custom type pm1001lhrCfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgsystConfLine2_Object = MibScalar
pm1001lhrCfgsystConfLine2 = _Pm1001lhrCfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 1, 6),
    _Pm1001lhrCfgsystConfLine2_Type()
)
pm1001lhrCfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgsystConfLine2.setStatus("current")


class _Pm1001lhrCfglineOptions2_Type(Unsigned32):
    """Custom type pm1001lhrCfglineOptions2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfglineOptions2_Type.__name__ = "Unsigned32"
_Pm1001lhrCfglineOptions2_Object = MibScalar
pm1001lhrCfglineOptions2 = _Pm1001lhrCfglineOptions2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 1, 9),
    _Pm1001lhrCfglineOptions2_Type()
)
pm1001lhrCfglineOptions2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfglineOptions2.setStatus("current")
_Pm1001lhrCfgXfpTable_Object = MibTable
pm1001lhrCfgXfpTable = _Pm1001lhrCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm1001lhrCfgXfpTable.setStatus("current")
_Pm1001lhrCfgXfpEntry_Object = MibTableRow
pm1001lhrCfgXfpEntry = _Pm1001lhrCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 2, 1)
)
pm1001lhrCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCfgXfpEntry.setStatus("current")


class _Pm1001lhrCfgXfpIndex_Type(Integer32):
    """Custom type pm1001lhrCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCfgXfpIndex_Type.__name__ = "Integer32"
_Pm1001lhrCfgXfpIndex_Object = MibTableColumn
pm1001lhrCfgXfpIndex = _Pm1001lhrCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 2, 1, 1),
    _Pm1001lhrCfgXfpIndex_Type()
)
pm1001lhrCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgXfpIndex.setStatus("current")


class _Pm1001lhrCfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgSystConfXfpPortn_Object = MibTableColumn
pm1001lhrCfgSystConfXfpPortn = _Pm1001lhrCfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 2, 1, 3),
    _Pm1001lhrCfgSystConfXfpPortn_Type()
)
pm1001lhrCfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgSystConfXfpPortn.setStatus("current")


class _Pm1001lhrCfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgDataRateConfXfpPortn_Object = MibTableColumn
pm1001lhrCfgDataRateConfXfpPortn = _Pm1001lhrCfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 2, 2, 1, 4),
    _Pm1001lhrCfgDataRateConfXfpPortn_Type()
)
pm1001lhrCfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgDataRateConfXfpPortn.setStatus("deprecated")
_Pm1001lhrCfgLabels_ObjectIdentity = ObjectIdentity
pm1001lhrCfgLabels = _Pm1001lhrCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 3)
)
_Pm1001lhrCfgLabelclientTable_Object = MibTable
pm1001lhrCfgLabelclientTable = _Pm1001lhrCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm1001lhrCfgLabelclientTable.setStatus("current")
_Pm1001lhrCfgLabelclientEntry_Object = MibTableRow
pm1001lhrCfgLabelclientEntry = _Pm1001lhrCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 3, 1, 1)
)
pm1001lhrCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCfgLabelclientEntry.setStatus("current")


class _Pm1001lhrCfgLabelclientIndex_Type(Integer32):
    """Custom type pm1001lhrCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1001lhrCfgLabelclientIndex_Object = MibTableColumn
pm1001lhrCfgLabelclientIndex = _Pm1001lhrCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 3, 1, 1, 1),
    _Pm1001lhrCfgLabelclientIndex_Type()
)
pm1001lhrCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgLabelclientIndex.setStatus("current")


class _Pm1001lhrCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1001lhrCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1001lhrCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1001lhrCfgLabelclientPortn_Object = MibTableColumn
pm1001lhrCfgLabelclientPortn = _Pm1001lhrCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 3, 1, 1, 3),
    _Pm1001lhrCfgLabelclientPortn_Type()
)
pm1001lhrCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgLabelclientPortn.setStatus("current")
_Pm1001lhrCfgLabellineTable_Object = MibTable
pm1001lhrCfgLabellineTable = _Pm1001lhrCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm1001lhrCfgLabellineTable.setStatus("current")
_Pm1001lhrCfgLabellineEntry_Object = MibTableRow
pm1001lhrCfgLabellineEntry = _Pm1001lhrCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 3, 2, 1)
)
pm1001lhrCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCfgLabellineEntry.setStatus("current")


class _Pm1001lhrCfgLabellineIndex_Type(Integer32):
    """Custom type pm1001lhrCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1001lhrCfgLabellineIndex_Object = MibTableColumn
pm1001lhrCfgLabellineIndex = _Pm1001lhrCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 3, 2, 1, 1),
    _Pm1001lhrCfgLabellineIndex_Type()
)
pm1001lhrCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgLabellineIndex.setStatus("current")


class _Pm1001lhrCfgLabellinePortn_Type(DisplayString):
    """Custom type pm1001lhrCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1001lhrCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1001lhrCfgLabellinePortn_Object = MibTableColumn
pm1001lhrCfgLabellinePortn = _Pm1001lhrCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 3, 2, 1, 3),
    _Pm1001lhrCfgLabellinePortn_Type()
)
pm1001lhrCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgLabellinePortn.setStatus("current")
_Pm1001lhrCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm1001lhrCfgStartuptlh = _Pm1001lhrCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4)
)
_Pm1001lhrCfgOtxtlhTable_Object = MibTable
pm1001lhrCfgOtxtlhTable = _Pm1001lhrCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm1001lhrCfgOtxtlhTable.setStatus("current")
_Pm1001lhrCfgOtxtlhEntry_Object = MibTableRow
pm1001lhrCfgOtxtlhEntry = _Pm1001lhrCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1)
)
pm1001lhrCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCfgOtxtlhEntry.setStatus("current")


class _Pm1001lhrCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm1001lhrCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm1001lhrCfgOtxtlhIndex_Object = MibTableColumn
pm1001lhrCfgOtxtlhIndex = _Pm1001lhrCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 1),
    _Pm1001lhrCfgOtxtlhIndex_Type()
)
pm1001lhrCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgOtxtlhIndex.setStatus("current")


class _Pm1001lhrCfgNuPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgNuPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgNuPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgNuPortn_Object = MibTableColumn
pm1001lhrCfgNuPortn = _Pm1001lhrCfgNuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 3),
    _Pm1001lhrCfgNuPortn_Type()
)
pm1001lhrCfgNuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgNuPortn.setStatus("deprecated")


class _Pm1001lhrCfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgLineDitherRatePortn_Object = MibTableColumn
pm1001lhrCfgLineDitherRatePortn = _Pm1001lhrCfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 4),
    _Pm1001lhrCfgLineDitherRatePortn_Type()
)
pm1001lhrCfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgLineDitherRatePortn.setStatus("current")


class _Pm1001lhrCfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgLineDitherFhzPortn_Object = MibTableColumn
pm1001lhrCfgLineDitherFhzPortn = _Pm1001lhrCfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 5),
    _Pm1001lhrCfgLineDitherFhzPortn_Type()
)
pm1001lhrCfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgLineDitherFhzPortn.setStatus("current")


class _Pm1001lhrCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgLinePwrLaserPortn_Object = MibTableColumn
pm1001lhrCfgLinePwrLaserPortn = _Pm1001lhrCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 6),
    _Pm1001lhrCfgLinePwrLaserPortn_Type()
)
pm1001lhrCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgLinePwrLaserPortn.setStatus("current")


class _Pm1001lhrCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgLineFCurrentPortn_Object = MibTableColumn
pm1001lhrCfgLineFCurrentPortn = _Pm1001lhrCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 7),
    _Pm1001lhrCfgLineFCurrentPortn_Type()
)
pm1001lhrCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgLineFCurrentPortn.setStatus("current")


class _Pm1001lhrCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgLineGridCurrentPortn_Object = MibTableColumn
pm1001lhrCfgLineGridCurrentPortn = _Pm1001lhrCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 8),
    _Pm1001lhrCfgLineGridCurrentPortn_Type()
)
pm1001lhrCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgLineGridCurrentPortn.setStatus("current")


class _Pm1001lhrCfgFPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgFPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgFPortn_Object = MibTableColumn
pm1001lhrCfgFPortn = _Pm1001lhrCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 9),
    _Pm1001lhrCfgFPortn_Type()
)
pm1001lhrCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgFPortn.setStatus("current")


class _Pm1001lhrCfgReservedPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgReservedPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgReservedPortn_Object = MibTableColumn
pm1001lhrCfgReservedPortn = _Pm1001lhrCfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 10),
    _Pm1001lhrCfgReservedPortn_Type()
)
pm1001lhrCfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgReservedPortn.setStatus("deprecated")


class _Pm1001lhrCfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgLinePhotodiodeModePortn_Object = MibTableColumn
pm1001lhrCfgLinePhotodiodeModePortn = _Pm1001lhrCfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 11),
    _Pm1001lhrCfgLinePhotodiodeModePortn_Type()
)
pm1001lhrCfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgLinePhotodiodeModePortn.setStatus("current")


class _Pm1001lhrCfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgLinePhotodiodeValuePortn_Object = MibTableColumn
pm1001lhrCfgLinePhotodiodeValuePortn = _Pm1001lhrCfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 4, 1, 1, 12),
    _Pm1001lhrCfgLinePhotodiodeValuePortn_Type()
)
pm1001lhrCfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgLinePhotodiodeValuePortn.setStatus("current")
_Pm1001lhrCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm1001lhrCfgStartuptablefive = _Pm1001lhrCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 5)
)
_Pm1001lhrCfgOtxtlhcapabilitiesTable_Object = MibTable
pm1001lhrCfgOtxtlhcapabilitiesTable = _Pm1001lhrCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pm1001lhrCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm1001lhrCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm1001lhrCfgOtxtlhcapabilitiesEntry = _Pm1001lhrCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 5, 1, 1)
)
pm1001lhrCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm1001lhr-MIB", "pm1001lhrCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm1001lhrCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm1001lhrCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm1001lhrCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001lhrCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm1001lhrCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm1001lhrCfgOtxtlhcapabilitiesIndex = _Pm1001lhrCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 5, 1, 1, 1),
    _Pm1001lhrCfgOtxtlhcapabilitiesIndex_Type()
)
pm1001lhrCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm1001lhrCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgComponentTypePortn_Object = MibTableColumn
pm1001lhrCfgComponentTypePortn = _Pm1001lhrCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 5, 1, 1, 3),
    _Pm1001lhrCfgComponentTypePortn_Type()
)
pm1001lhrCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgComponentTypePortn.setStatus("current")


class _Pm1001lhrCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgMiscellaneousPortn_Object = MibTableColumn
pm1001lhrCfgMiscellaneousPortn = _Pm1001lhrCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 5, 1, 1, 4),
    _Pm1001lhrCfgMiscellaneousPortn_Type()
)
pm1001lhrCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgMiscellaneousPortn.setStatus("current")


class _Pm1001lhrCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgFirstChannelPortn_Object = MibTableColumn
pm1001lhrCfgFirstChannelPortn = _Pm1001lhrCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 5, 1, 1, 5),
    _Pm1001lhrCfgFirstChannelPortn_Type()
)
pm1001lhrCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgFirstChannelPortn.setStatus("current")


class _Pm1001lhrCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgLastChannelPortn_Object = MibTableColumn
pm1001lhrCfgLastChannelPortn = _Pm1001lhrCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 5, 1, 1, 6),
    _Pm1001lhrCfgLastChannelPortn_Type()
)
pm1001lhrCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgLastChannelPortn.setStatus("current")


class _Pm1001lhrCfgGridPortn_Type(Unsigned32):
    """Custom type pm1001lhrCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001lhrCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm1001lhrCfgGridPortn_Object = MibTableColumn
pm1001lhrCfgGridPortn = _Pm1001lhrCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 5, 1, 1, 7),
    _Pm1001lhrCfgGridPortn_Type()
)
pm1001lhrCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrCfgGridPortn.setStatus("current")
_Pm1001lhrCfgWriteConfiguration_Type = EkiOnOff
_Pm1001lhrCfgWriteConfiguration_Object = MibScalar
pm1001lhrCfgWriteConfiguration = _Pm1001lhrCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 9, 257),
    _Pm1001lhrCfgWriteConfiguration_Type()
)
pm1001lhrCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001lhrCfgWriteConfiguration.setStatus("current")
_Pm1001lhrtraps_ObjectIdentity = ObjectIdentity
pm1001lhrtraps = _Pm1001lhrtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10)
)


class _Pm1001lhrtrapLineNumber_Type(Integer32):
    """Custom type pm1001lhrtrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1001lhrtrapLineNumber_Type.__name__ = "Integer32"
_Pm1001lhrtrapLineNumber_Object = MibScalar
pm1001lhrtrapLineNumber = _Pm1001lhrtrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 3),
    _Pm1001lhrtrapLineNumber_Type()
)
pm1001lhrtrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrtrapLineNumber.setStatus("current")


class _Pm1001lhrtrapBoardNumber_Type(Integer32):
    """Custom type pm1001lhrtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1001lhrtrapBoardNumber_Type.__name__ = "Integer32"
_Pm1001lhrtrapBoardNumber_Object = MibScalar
pm1001lhrtrapBoardNumber = _Pm1001lhrtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 4),
    _Pm1001lhrtrapBoardNumber_Type()
)
pm1001lhrtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001lhrtrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pm1001lhrLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 30)
)
pm1001lhrLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapLineNumber"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001lhrLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1001lhrLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 31)
)
pm1001lhrLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapLineNumber"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001lhrLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1001lhrLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 32)
)
pm1001lhrLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapLineNumber"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001lhrLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1001lhrLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 33)
)
pm1001lhrLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapLineNumber"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001lhrLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1001lhrLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 34)
)
pm1001lhrLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmLineFailPortn"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmLineHwFailPortn"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapLineNumber"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001lhrLineTrapCritGoesOn.setStatus(
        "current"
    )

pm1001lhrLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 35)
)
pm1001lhrLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmLineFailPortn"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmLineHwFailPortn"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapLineNumber"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001lhrLineTrapCritGoesOff.setStatus(
        "current"
    )

pm1001lhrPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 50)
)
pm1001lhrPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmDefFuseB"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmDefFuseA"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001lhrPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1001lhrPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 22, 10, 51)
)
pm1001lhrPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmDefFuseB"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrAlmDefFuseA"),
        ("EKINOPS-Pm1001lhr-MIB", "pm1001lhrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001lhrPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1001lhr-MIB",
    **{"Pm1001lhrOtxMode": Pm1001lhrOtxMode,
       "Pm1001lhrOtxGrid": Pm1001lhrOtxGrid,
       "Pm1001lhrAdjustValue": Pm1001lhrAdjustValue,
       "Pm1001lhrOtxChannel": Pm1001lhrOtxChannel,
       "modulePm1001lhr": modulePm1001lhr,
       "pm1001lhralarms": pm1001lhralarms,
       "pm1001lhrAlmOther": pm1001lhrAlmOther,
       "pm1001lhrAlmOtherNurg": pm1001lhrAlmOtherNurg,
       "pm1001lhrAlmsynthAlm2": pm1001lhrAlmsynthAlm2,
       "pm1001lhrAlmConfTableSave": pm1001lhrAlmConfTableSave,
       "pm1001lhrAlmInvUpload": pm1001lhrAlmInvUpload,
       "pm1001lhrAlmConfTableLoad": pm1001lhrAlmConfTableLoad,
       "pm1001lhrAlmCorrelatOff": pm1001lhrAlmCorrelatOff,
       "pm1001lhrAlmOtherUrg": pm1001lhrAlmOtherUrg,
       "pm1001lhrAlmmodInitFailLevel2": pm1001lhrAlmmodInitFailLevel2,
       "pm1001lhrAlmLedFail": pm1001lhrAlmLedFail,
       "pm1001lhrAlmNextColdBootForced": pm1001lhrAlmNextColdBootForced,
       "pm1001lhrAlmBootUndone": pm1001lhrAlmBootUndone,
       "pm1001lhrAlmResetHwInitFail": pm1001lhrAlmResetHwInitFail,
       "pm1001lhrAlmSwInitFail": pm1001lhrAlmSwInitFail,
       "pm1001lhrAlmmodInitFailLevel3": pm1001lhrAlmmodInitFailLevel3,
       "pm1001lhrAlmGwIdentFail": pm1001lhrAlmGwIdentFail,
       "pm1001lhrAlmObmTypeReadFail": pm1001lhrAlmObmTypeReadFail,
       "pm1001lhrAlmInitModuleFail": pm1001lhrAlmInitModuleFail,
       "pm1001lhrAlmXfp1InitFail": pm1001lhrAlmXfp1InitFail,
       "pm1001lhrAlmXfp2InitFail": pm1001lhrAlmXfp2InitFail,
       "pm1001lhrAlmLine1InitFail": pm1001lhrAlmLine1InitFail,
       "pm1001lhrAlmLine2InitFail": pm1001lhrAlmLine2InitFail,
       "pm1001lhrAlmOtherCrit": pm1001lhrAlmOtherCrit,
       "pm1001lhrAlmsynthAlm0": pm1001lhrAlmsynthAlm0,
       "pm1001lhrAlmModGlobFail": pm1001lhrAlmModGlobFail,
       "pm1001lhrAlmDefFuseA": pm1001lhrAlmDefFuseA,
       "pm1001lhrAlmDefFuseB": pm1001lhrAlmDefFuseB,
       "pm1001lhrAlmClient": pm1001lhrAlmClient,
       "pm1001lhrAlmClientNurg": pm1001lhrAlmClientNurg,
       "pm1001lhrAlmClientUrg": pm1001lhrAlmClientUrg,
       "pm1001lhrAlmClientCrit": pm1001lhrAlmClientCrit,
       "pm1001lhrAlmLine": pm1001lhrAlmLine,
       "pm1001lhrAlmLineNurg": pm1001lhrAlmLineNurg,
       "pm1001lhrAlmlineXfp1WarningsTable": pm1001lhrAlmlineXfp1WarningsTable,
       "pm1001lhrAlmlineXfp1WarningsEntry": pm1001lhrAlmlineXfp1WarningsEntry,
       "pm1001lhrAlmlineXfp1WarningsIndex": pm1001lhrAlmlineXfp1WarningsIndex,
       "pm1001lhrAlmTxPowerLowWarningPortn": pm1001lhrAlmTxPowerLowWarningPortn,
       "pm1001lhrAlmTxPowerHighWarningPortn": pm1001lhrAlmTxPowerHighWarningPortn,
       "pm1001lhrAlmTxBiasLowWarningPortn": pm1001lhrAlmTxBiasLowWarningPortn,
       "pm1001lhrAlmTxBiasHighWarningPortn": pm1001lhrAlmTxBiasHighWarningPortn,
       "pm1001lhrAlmTempLowWarningPortn": pm1001lhrAlmTempLowWarningPortn,
       "pm1001lhrAlmTempHighWarningPortn": pm1001lhrAlmTempHighWarningPortn,
       "pm1001lhrAlmRxPowerLowWarningPortn": pm1001lhrAlmRxPowerLowWarningPortn,
       "pm1001lhrAlmRxPowerHighWarningPortn": pm1001lhrAlmRxPowerHighWarningPortn,
       "pm1001lhrAlmlineOtx1TlhWarningsTable": pm1001lhrAlmlineOtx1TlhWarningsTable,
       "pm1001lhrAlmlineOtx1TlhWarningsEntry": pm1001lhrAlmlineOtx1TlhWarningsEntry,
       "pm1001lhrAlmlineOtx1TlhWarningsIndex": pm1001lhrAlmlineOtx1TlhWarningsIndex,
       "pm1001lhrAlmLineModulatorAgingHighWarningPortn": pm1001lhrAlmLineModulatorAgingHighWarningPortn,
       "pm1001lhrAlmLineAgingHighWarningPortn": pm1001lhrAlmLineAgingHighWarningPortn,
       "pm1001lhrAlmLineFreqDevHighWarningPortn": pm1001lhrAlmLineFreqDevHighWarningPortn,
       "pm1001lhrAlmLineLaserTempHighWarningPortn": pm1001lhrAlmLineLaserTempHighWarningPortn,
       "pm1001lhrAlmLineUrg": pm1001lhrAlmLineUrg,
       "pm1001lhrAlmdfrmBerTable": pm1001lhrAlmdfrmBerTable,
       "pm1001lhrAlmdfrmBerEntry": pm1001lhrAlmdfrmBerEntry,
       "pm1001lhrAlmdfrmBerIndex": pm1001lhrAlmdfrmBerIndex,
       "pm1001lhrAlmLineSignalDegradePortn": pm1001lhrAlmLineSignalDegradePortn,
       "pm1001lhrAlmLineSignalFailPortn": pm1001lhrAlmLineSignalFailPortn,
       "pm1001lhrAlmLineDegradePortn": pm1001lhrAlmLineDegradePortn,
       "pm1001lhrAlmlineXfp1AlarmTable": pm1001lhrAlmlineXfp1AlarmTable,
       "pm1001lhrAlmlineXfp1AlarmEntry": pm1001lhrAlmlineXfp1AlarmEntry,
       "pm1001lhrAlmlineXfp1AlarmIndex": pm1001lhrAlmlineXfp1AlarmIndex,
       "pm1001lhrAlmTxPowerLowAlarmPortn": pm1001lhrAlmTxPowerLowAlarmPortn,
       "pm1001lhrAlmTxPowerHighAlarmPortn": pm1001lhrAlmTxPowerHighAlarmPortn,
       "pm1001lhrAlmTxBiasLowAlarmPortn": pm1001lhrAlmTxBiasLowAlarmPortn,
       "pm1001lhrAlmTxBiasHighAlarmPortn": pm1001lhrAlmTxBiasHighAlarmPortn,
       "pm1001lhrAlmTempLowAlarmPortn": pm1001lhrAlmTempLowAlarmPortn,
       "pm1001lhrAlmTempHighAlarmPortn": pm1001lhrAlmTempHighAlarmPortn,
       "pm1001lhrAlmRxPowerLowAlarmPortn": pm1001lhrAlmRxPowerLowAlarmPortn,
       "pm1001lhrAlmRxPowerHighAlarmPortn": pm1001lhrAlmRxPowerHighAlarmPortn,
       "pm1001lhrAlmlineXfp1SupplyAlarmTable": pm1001lhrAlmlineXfp1SupplyAlarmTable,
       "pm1001lhrAlmlineXfp1SupplyAlarmEntry": pm1001lhrAlmlineXfp1SupplyAlarmEntry,
       "pm1001lhrAlmlineXfp1SupplyAlarmIndex": pm1001lhrAlmlineXfp1SupplyAlarmIndex,
       "pm1001lhrAlmVee5LowAlarmPortn": pm1001lhrAlmVee5LowAlarmPortn,
       "pm1001lhrAlmVee5HighAlarmPortn": pm1001lhrAlmVee5HighAlarmPortn,
       "pm1001lhrAlmVcc2LowAlarmPortn": pm1001lhrAlmVcc2LowAlarmPortn,
       "pm1001lhrAlmVcc2HighAlarmPortn": pm1001lhrAlmVcc2HighAlarmPortn,
       "pm1001lhrAlmVcc3LowAlarmPortn": pm1001lhrAlmVcc3LowAlarmPortn,
       "pm1001lhrAlmVcc3HighAlarmPortn": pm1001lhrAlmVcc3HighAlarmPortn,
       "pm1001lhrAlmVcc5LowAlarmPortn": pm1001lhrAlmVcc5LowAlarmPortn,
       "pm1001lhrAlmVcc5HighAlarmPortn": pm1001lhrAlmVcc5HighAlarmPortn,
       "pm1001lhrAlmVee5LowWarningPortn": pm1001lhrAlmVee5LowWarningPortn,
       "pm1001lhrAlmVee5HighWarningPortn": pm1001lhrAlmVee5HighWarningPortn,
       "pm1001lhrAlmVcc2LowWarningPortn": pm1001lhrAlmVcc2LowWarningPortn,
       "pm1001lhrAlmVcc2HighWarningPortn": pm1001lhrAlmVcc2HighWarningPortn,
       "pm1001lhrAlmVcc3LowWarningPortn": pm1001lhrAlmVcc3LowWarningPortn,
       "pm1001lhrAlmVcc3HighWarningPortn": pm1001lhrAlmVcc3HighWarningPortn,
       "pm1001lhrAlmVcc5LowWarningPortn": pm1001lhrAlmVcc5LowWarningPortn,
       "pm1001lhrAlmVcc5HighWarningPortn": pm1001lhrAlmVcc5HighWarningPortn,
       "pm1001lhrAlmlineOtx1TlhAlarmsTable": pm1001lhrAlmlineOtx1TlhAlarmsTable,
       "pm1001lhrAlmlineOtx1TlhAlarmsEntry": pm1001lhrAlmlineOtx1TlhAlarmsEntry,
       "pm1001lhrAlmlineOtx1TlhAlarmsIndex": pm1001lhrAlmlineOtx1TlhAlarmsIndex,
       "pm1001lhrAlmLineModulatorAgingHighAlaPortn": pm1001lhrAlmLineModulatorAgingHighAlaPortn,
       "pm1001lhrAlmLineAgingHighAlaPortn": pm1001lhrAlmLineAgingHighAlaPortn,
       "pm1001lhrAlmLineFreqDevHighAlaPortn": pm1001lhrAlmLineFreqDevHighAlaPortn,
       "pm1001lhrAlmLineLaserTempHighAlaPortn": pm1001lhrAlmLineLaserTempHighAlaPortn,
       "pm1001lhrAlmLineCrit": pm1001lhrAlmLineCrit,
       "pm1001lhrAlmsynthAlmLineTable": pm1001lhrAlmsynthAlmLineTable,
       "pm1001lhrAlmsynthAlmLineEntry": pm1001lhrAlmsynthAlmLineEntry,
       "pm1001lhrAlmsynthAlmLineIndex": pm1001lhrAlmsynthAlmLineIndex,
       "pm1001lhrAlmXfpAbsentPortn": pm1001lhrAlmXfpAbsentPortn,
       "pm1001lhrAlmXfpInitNotComplPortn": pm1001lhrAlmXfpInitNotComplPortn,
       "pm1001lhrAlmLineHwFailPortn": pm1001lhrAlmLineHwFailPortn,
       "pm1001lhrAlmXfpTxOffPortn": pm1001lhrAlmXfpTxOffPortn,
       "pm1001lhrAlmLineLocalOosPortn": pm1001lhrAlmLineLocalOosPortn,
       "pm1001lhrAlmLineDdmWarningPortn": pm1001lhrAlmLineDdmWarningPortn,
       "pm1001lhrAlmLineDdmAlmPortn": pm1001lhrAlmLineDdmAlmPortn,
       "pm1001lhrAlmLineFailPortn": pm1001lhrAlmLineFailPortn,
       "pm1001lhrAlmdfrmAlmTable": pm1001lhrAlmdfrmAlmTable,
       "pm1001lhrAlmdfrmAlmEntry": pm1001lhrAlmdfrmAlmEntry,
       "pm1001lhrAlmdfrmAlmIndex": pm1001lhrAlmdfrmAlmIndex,
       "pm1001lhrAlmDwAisDetPortn": pm1001lhrAlmDwAisDetPortn,
       "pm1001lhrAlmDwRdiDetPortn": pm1001lhrAlmDwRdiDetPortn,
       "pm1001lhrAlmDwOofPortn": pm1001lhrAlmDwOofPortn,
       "pm1001lhrAlmDwLofPortn": pm1001lhrAlmDwLofPortn,
       "pm1001lhrAlmlineSyncAlarmsTable": pm1001lhrAlmlineSyncAlarmsTable,
       "pm1001lhrAlmlineSyncAlarmsEntry": pm1001lhrAlmlineSyncAlarmsEntry,
       "pm1001lhrAlmlineSyncAlarmsIndex": pm1001lhrAlmlineSyncAlarmsIndex,
       "pm1001lhrAlmDwLockerrPortn": pm1001lhrAlmDwLockerrPortn,
       "pm1001lhrAlmUpLockerrPortn": pm1001lhrAlmUpLockerrPortn,
       "pm1001lhrAlmDwLosPortn": pm1001lhrAlmDwLosPortn,
       "pm1001lhrAlmlineXfp1AlarmsTable": pm1001lhrAlmlineXfp1AlarmsTable,
       "pm1001lhrAlmlineXfp1AlarmsEntry": pm1001lhrAlmlineXfp1AlarmsEntry,
       "pm1001lhrAlmlineXfp1AlarmsIndex": pm1001lhrAlmlineXfp1AlarmsIndex,
       "pm1001lhrAlmModNrPortn": pm1001lhrAlmModNrPortn,
       "pm1001lhrAlmRxCdrNotLockedPortn": pm1001lhrAlmRxCdrNotLockedPortn,
       "pm1001lhrAlmRxNrPortn": pm1001lhrAlmRxNrPortn,
       "pm1001lhrAlmTxCdrNotLockedPortn": pm1001lhrAlmTxCdrNotLockedPortn,
       "pm1001lhrAlmTxFaultPortn": pm1001lhrAlmTxFaultPortn,
       "pm1001lhrAlmTxNrPortn": pm1001lhrAlmTxNrPortn,
       "pm1001lhrAlmWavelengthUnlockedPortn": pm1001lhrAlmWavelengthUnlockedPortn,
       "pm1001lhrAlmTecFaultPortn": pm1001lhrAlmTecFaultPortn,
       "pm1001lhrAlmApdSupplyFaultPortn": pm1001lhrAlmApdSupplyFaultPortn,
       "pm1001lhrmeasures": pm1001lhrmeasures,
       "pm1001lhrMesrOther": pm1001lhrMesrOther,
       "pm1001lhrMesrsynth0": pm1001lhrMesrsynth0,
       "pm1001lhrMesrsynth1": pm1001lhrMesrsynth1,
       "pm1001lhrMesrClient": pm1001lhrMesrClient,
       "pm1001lhrMesrLine": pm1001lhrMesrLine,
       "pm1001lhrMesrxfp1LxModTempMeasTable": pm1001lhrMesrxfp1LxModTempMeasTable,
       "pm1001lhrMesrxfp1LxModTempMeasEntry": pm1001lhrMesrxfp1LxModTempMeasEntry,
       "pm1001lhrMesrxfp1LxModTempMeasIndex": pm1001lhrMesrxfp1LxModTempMeasIndex,
       "pm1001lhrMesrxfp1LxModTempMeasPortn": pm1001lhrMesrxfp1LxModTempMeasPortn,
       "pm1001lhrMesrxfp1ReservedTable": pm1001lhrMesrxfp1ReservedTable,
       "pm1001lhrMesrxfp1ReservedEntry": pm1001lhrMesrxfp1ReservedEntry,
       "pm1001lhrMesrxfp1ReservedIndex": pm1001lhrMesrxfp1ReservedIndex,
       "pm1001lhrMesrxfp1ReservedPortn": pm1001lhrMesrxfp1ReservedPortn,
       "pm1001lhrMesrxfp1LoBiasCurrentMeasTable": pm1001lhrMesrxfp1LoBiasCurrentMeasTable,
       "pm1001lhrMesrxfp1LoBiasCurrentMeasEntry": pm1001lhrMesrxfp1LoBiasCurrentMeasEntry,
       "pm1001lhrMesrxfp1LoBiasCurrentMeasIndex": pm1001lhrMesrxfp1LoBiasCurrentMeasIndex,
       "pm1001lhrMesrxfp1LoBiasCurrentMeasPortn": pm1001lhrMesrxfp1LoBiasCurrentMeasPortn,
       "pm1001lhrMesrxfp1LoTxPowerMeasTable": pm1001lhrMesrxfp1LoTxPowerMeasTable,
       "pm1001lhrMesrxfp1LoTxPowerMeasEntry": pm1001lhrMesrxfp1LoTxPowerMeasEntry,
       "pm1001lhrMesrxfp1LoTxPowerMeasIndex": pm1001lhrMesrxfp1LoTxPowerMeasIndex,
       "pm1001lhrMesrxfp1LoTxPowerMeasPortn": pm1001lhrMesrxfp1LoTxPowerMeasPortn,
       "pm1001lhrMesrxfp1LiRxPowerMeasTable": pm1001lhrMesrxfp1LiRxPowerMeasTable,
       "pm1001lhrMesrxfp1LiRxPowerMeasEntry": pm1001lhrMesrxfp1LiRxPowerMeasEntry,
       "pm1001lhrMesrxfp1LiRxPowerMeasIndex": pm1001lhrMesrxfp1LiRxPowerMeasIndex,
       "pm1001lhrMesrxfp1LiRxPowerMeasPortn": pm1001lhrMesrxfp1LiRxPowerMeasPortn,
       "pm1001lhrMesrxfp1LxAux1MeasTable": pm1001lhrMesrxfp1LxAux1MeasTable,
       "pm1001lhrMesrxfp1LxAux1MeasEntry": pm1001lhrMesrxfp1LxAux1MeasEntry,
       "pm1001lhrMesrxfp1LxAux1MeasIndex": pm1001lhrMesrxfp1LxAux1MeasIndex,
       "pm1001lhrMesrxfp1LxAux1MeasPortn": pm1001lhrMesrxfp1LxAux1MeasPortn,
       "pm1001lhrMesrxfp1LxAux2MeasTable": pm1001lhrMesrxfp1LxAux2MeasTable,
       "pm1001lhrMesrxfp1LxAux2MeasEntry": pm1001lhrMesrxfp1LxAux2MeasEntry,
       "pm1001lhrMesrxfp1LxAux2MeasIndex": pm1001lhrMesrxfp1LxAux2MeasIndex,
       "pm1001lhrMesrxfp1LxAux2MeasPortn": pm1001lhrMesrxfp1LxAux2MeasPortn,
       "pm1001lhrMesrotx1AgingTable": pm1001lhrMesrotx1AgingTable,
       "pm1001lhrMesrotx1AgingEntry": pm1001lhrMesrotx1AgingEntry,
       "pm1001lhrMesrotx1AgingIndex": pm1001lhrMesrotx1AgingIndex,
       "pm1001lhrMesrotx1AgingPortn": pm1001lhrMesrotx1AgingPortn,
       "pm1001lhrMesrotx1LaserTemperatureTable": pm1001lhrMesrotx1LaserTemperatureTable,
       "pm1001lhrMesrotx1LaserTemperatureEntry": pm1001lhrMesrotx1LaserTemperatureEntry,
       "pm1001lhrMesrotx1LaserTemperatureIndex": pm1001lhrMesrotx1LaserTemperatureIndex,
       "pm1001lhrMesrotx1LaserTemperaturePortn": pm1001lhrMesrotx1LaserTemperaturePortn,
       "pm1001lhrMesrotx1FreqDeviationTable": pm1001lhrMesrotx1FreqDeviationTable,
       "pm1001lhrMesrotx1FreqDeviationEntry": pm1001lhrMesrotx1FreqDeviationEntry,
       "pm1001lhrMesrotx1FreqDeviationIndex": pm1001lhrMesrotx1FreqDeviationIndex,
       "pm1001lhrMesrotx1FreqDeviationPortn": pm1001lhrMesrotx1FreqDeviationPortn,
       "pm1001lhrMesrotx1LaserWvlengthTable": pm1001lhrMesrotx1LaserWvlengthTable,
       "pm1001lhrMesrotx1LaserWvlengthEntry": pm1001lhrMesrotx1LaserWvlengthEntry,
       "pm1001lhrMesrotx1LaserWvlengthIndex": pm1001lhrMesrotx1LaserWvlengthIndex,
       "pm1001lhrMesrotx1LaserWvlengthPortn": pm1001lhrMesrotx1LaserWvlengthPortn,
       "pm1001lhrcounters": pm1001lhrcounters,
       "pm1001lhrCntOther": pm1001lhrCntOther,
       "pm1001lhrCntClient": pm1001lhrCntClient,
       "pm1001lhrCntLine": pm1001lhrCntLine,
       "pm1001lhrCntdfrmB1ErrCntTable": pm1001lhrCntdfrmB1ErrCntTable,
       "pm1001lhrCntdfrmB1ErrCntEntry": pm1001lhrCntdfrmB1ErrCntEntry,
       "pm1001lhrCntdfrmB1ErrCntIndex": pm1001lhrCntdfrmB1ErrCntIndex,
       "pm1001lhrCntdfrmB1ErrCntValuePortn": pm1001lhrCntdfrmB1ErrCntValuePortn,
       "pm1001lhrCntdfrmB1ErrCntErrorPortn": pm1001lhrCntdfrmB1ErrCntErrorPortn,
       "pm1001lhrCntdfrmB1ErrCntOverloadPortn": pm1001lhrCntdfrmB1ErrCntOverloadPortn,
       "pm1001lhrCntdfrmTimCntTable": pm1001lhrCntdfrmTimCntTable,
       "pm1001lhrCntdfrmTimCntEntry": pm1001lhrCntdfrmTimCntEntry,
       "pm1001lhrCntdfrmTimCntIndex": pm1001lhrCntdfrmTimCntIndex,
       "pm1001lhrCntdfrmTimCntValuePortn": pm1001lhrCntdfrmTimCntValuePortn,
       "pm1001lhrCntdfrmTimCntErrorPortn": pm1001lhrCntdfrmTimCntErrorPortn,
       "pm1001lhrCntdfrmTimCntOverloadPortn": pm1001lhrCntdfrmTimCntOverloadPortn,
       "pm1001lhrCntdfrmPrimLineErrCntTable": pm1001lhrCntdfrmPrimLineErrCntTable,
       "pm1001lhrCntdfrmPrimLineErrCntEntry": pm1001lhrCntdfrmPrimLineErrCntEntry,
       "pm1001lhrCntdfrmPrimLineErrCntIndex": pm1001lhrCntdfrmPrimLineErrCntIndex,
       "pm1001lhrCntdfrmPrimLineErrCntValuePortn": pm1001lhrCntdfrmPrimLineErrCntValuePortn,
       "pm1001lhrCntdfrmPrimLineErrCntErrorPortn": pm1001lhrCntdfrmPrimLineErrCntErrorPortn,
       "pm1001lhrCntdfrmPrimLineErrCntOverloadPortn": pm1001lhrCntdfrmPrimLineErrCntOverloadPortn,
       "pm1001lhrCntCountersReset": pm1001lhrCntCountersReset,
       "pm1001lhrCntCountersStop": pm1001lhrCntCountersStop,
       "pm1001lhrcontrolsWrite": pm1001lhrcontrolsWrite,
       "pm1001lhrCtrlOther": pm1001lhrCtrlOther,
       "pm1001lhrCtrlconfMgnt1": pm1001lhrCtrlconfMgnt1,
       "pm1001lhrCtrlConf1Load1": pm1001lhrCtrlConf1Load1,
       "pm1001lhrCtrlConf2Load1": pm1001lhrCtrlConf2Load1,
       "pm1001lhrCtrlConf2Flash1": pm1001lhrCtrlConf2Flash1,
       "pm1001lhrCtrlConf2Clear1": pm1001lhrCtrlConf2Clear1,
       "pm1001lhrCtrlsynth4": pm1001lhrCtrlsynth4,
       "pm1001lhrCtrlCorrelatOn": pm1001lhrCtrlCorrelatOn,
       "pm1001lhrCtrlCorrelatOff": pm1001lhrCtrlCorrelatOff,
       "pm1001lhrCtrlswMgnt": pm1001lhrCtrlswMgnt,
       "pm1001lhrCtrlColdReset": pm1001lhrCtrlColdReset,
       "pm1001lhrCtrlWarmReset": pm1001lhrCtrlWarmReset,
       "pm1001lhrCtrlLoadSwBank1": pm1001lhrCtrlLoadSwBank1,
       "pm1001lhrCtrlLoadSwBank2": pm1001lhrCtrlLoadSwBank2,
       "pm1001lhrCtrlgwMgnt": pm1001lhrCtrlgwMgnt,
       "pm1001lhrCtrlCurrentGwReset": pm1001lhrCtrlCurrentGwReset,
       "pm1001lhrCtrlLoadGwBank1": pm1001lhrCtrlLoadGwBank1,
       "pm1001lhrCtrlLoadGwBank2": pm1001lhrCtrlLoadGwBank2,
       "pm1001lhrCtrlLoadGwBank3": pm1001lhrCtrlLoadGwBank3,
       "pm1001lhrCtrlLoadGwBank4": pm1001lhrCtrlLoadGwBank4,
       "pm1001lhrCtrlledTest": pm1001lhrCtrlledTest,
       "pm1001lhrCtrlGreenLed": pm1001lhrCtrlGreenLed,
       "pm1001lhrCtrlRedLed": pm1001lhrCtrlRedLed,
       "pm1001lhrCtrlLedOff": pm1001lhrCtrlLedOff,
       "pm1001lhrCtrlmoduleOosMode": pm1001lhrCtrlmoduleOosMode,
       "pm1001lhrCtrlModuleOosMode": pm1001lhrCtrlModuleOosMode,
       "pm1001lhrCtrlClient": pm1001lhrCtrlClient,
       "pm1001lhrCtrlaccessLoopTable": pm1001lhrCtrlaccessLoopTable,
       "pm1001lhrCtrlaccessLoopEntry": pm1001lhrCtrlaccessLoopEntry,
       "pm1001lhrCtrlaccessLoopIndex": pm1001lhrCtrlaccessLoopIndex,
       "pm1001lhrCtrlaccessLoopPortn": pm1001lhrCtrlaccessLoopPortn,
       "pm1001lhrCtrlclientAccessTermLoopTable": pm1001lhrCtrlclientAccessTermLoopTable,
       "pm1001lhrCtrlclientAccessTermLoopEntry": pm1001lhrCtrlclientAccessTermLoopEntry,
       "pm1001lhrCtrlclientAccessTermLoopIndex": pm1001lhrCtrlclientAccessTermLoopIndex,
       "pm1001lhrCtrlclientAccessTermLoopPortn": pm1001lhrCtrlclientAccessTermLoopPortn,
       "pm1001lhrCtrlLine": pm1001lhrCtrlLine,
       "pm1001lhrCtrlprotocol": pm1001lhrCtrlprotocol,
       "pm1001lhrCtrlfecDisableTable": pm1001lhrCtrlfecDisableTable,
       "pm1001lhrCtrlfecDisableEntry": pm1001lhrCtrlfecDisableEntry,
       "pm1001lhrCtrlfecDisableIndex": pm1001lhrCtrlfecDisableIndex,
       "pm1001lhrCtrlfecDisablePortn": pm1001lhrCtrlfecDisablePortn,
       "pm1001lhrCtrllineOosModeTable": pm1001lhrCtrllineOosModeTable,
       "pm1001lhrCtrllineOosModeEntry": pm1001lhrCtrllineOosModeEntry,
       "pm1001lhrCtrllineOosModeIndex": pm1001lhrCtrllineOosModeIndex,
       "pm1001lhrCtrllineOosModePortn": pm1001lhrCtrllineOosModePortn,
       "pm1001lhrCtrlxfpOnoffTable": pm1001lhrCtrlxfpOnoffTable,
       "pm1001lhrCtrlxfpOnoffEntry": pm1001lhrCtrlxfpOnoffEntry,
       "pm1001lhrCtrlxfpOnoffIndex": pm1001lhrCtrlxfpOnoffIndex,
       "pm1001lhrCtrlxfpOnoffPortn": pm1001lhrCtrlxfpOnoffPortn,
       "pm1001lhrCtrlxfpLineLoopTable": pm1001lhrCtrlxfpLineLoopTable,
       "pm1001lhrCtrlxfpLineLoopEntry": pm1001lhrCtrlxfpLineLoopEntry,
       "pm1001lhrCtrlxfpLineLoopIndex": pm1001lhrCtrlxfpLineLoopIndex,
       "pm1001lhrCtrlxfpLineLoopPortn": pm1001lhrCtrlxfpLineLoopPortn,
       "pm1001lhrCtrlxfpXfiLoopTable": pm1001lhrCtrlxfpXfiLoopTable,
       "pm1001lhrCtrlxfpXfiLoopEntry": pm1001lhrCtrlxfpXfiLoopEntry,
       "pm1001lhrCtrlxfpXfiLoopIndex": pm1001lhrCtrlxfpXfiLoopIndex,
       "pm1001lhrCtrlxfpXfiLoopPortn": pm1001lhrCtrlxfpXfiLoopPortn,
       "pm1001lhrCtrllineTunableChannelTable": pm1001lhrCtrllineTunableChannelTable,
       "pm1001lhrCtrllineTunableChannelEntry": pm1001lhrCtrllineTunableChannelEntry,
       "pm1001lhrCtrllineTunableChannelIndex": pm1001lhrCtrllineTunableChannelIndex,
       "pm1001lhrCtrllineTunableChannelPortn": pm1001lhrCtrllineTunableChannelPortn,
       "pm1001lhrCtrllinePhotodiodeModeTable": pm1001lhrCtrllinePhotodiodeModeTable,
       "pm1001lhrCtrllinePhotodiodeModeEntry": pm1001lhrCtrllinePhotodiodeModeEntry,
       "pm1001lhrCtrllinePhotodiodeModeIndex": pm1001lhrCtrllinePhotodiodeModeIndex,
       "pm1001lhrCtrllinePhotodiodeModePortn": pm1001lhrCtrllinePhotodiodeModePortn,
       "pm1001lhrCtrllinePhotodiodeValueTable": pm1001lhrCtrllinePhotodiodeValueTable,
       "pm1001lhrCtrllinePhotodiodeValueEntry": pm1001lhrCtrllinePhotodiodeValueEntry,
       "pm1001lhrCtrllinePhotodiodeValueIndex": pm1001lhrCtrllinePhotodiodeValueIndex,
       "pm1001lhrCtrllinePhotodiodeValuePortn": pm1001lhrCtrllinePhotodiodeValuePortn,
       "pm1001lhrCtrllinePowerLaserTable": pm1001lhrCtrllinePowerLaserTable,
       "pm1001lhrCtrllinePowerLaserEntry": pm1001lhrCtrllinePowerLaserEntry,
       "pm1001lhrCtrllinePowerLaserIndex": pm1001lhrCtrllinePowerLaserIndex,
       "pm1001lhrCtrllinePowerLaserPortn": pm1001lhrCtrllinePowerLaserPortn,
       "pm1001lhrri": pm1001lhrri,
       "pm1001lhrriTable": pm1001lhrriTable,
       "pm1001lhrRinvLineTable": pm1001lhrRinvLineTable,
       "pm1001lhrRinvLineEntry": pm1001lhrRinvLineEntry,
       "pm1001lhrRinvLineIndex": pm1001lhrRinvLineIndex,
       "pm1001lhrRinvxfpLine": pm1001lhrRinvxfpLine,
       "pm1001lhrRinvReloadInventory": pm1001lhrRinvReloadInventory,
       "pm1001lhrRinvHwPlatform": pm1001lhrRinvHwPlatform,
       "pm1001lhrRinvModulePlatform": pm1001lhrRinvModulePlatform,
       "pm1001lhrRinvSwPlatform": pm1001lhrRinvSwPlatform,
       "pm1001lhrRinvGwPlatform": pm1001lhrRinvGwPlatform,
       "pm1001lhrdownload": pm1001lhrdownload,
       "pm1001lhrDwlOther": pm1001lhrDwlOther,
       "pm1001lhrDwlrestartProcess": pm1001lhrDwlrestartProcess,
       "pm1001lhrDwlWarmRestartProcessed": pm1001lhrDwlWarmRestartProcessed,
       "pm1001lhrDwlColdRestartProcessed": pm1001lhrDwlColdRestartProcessed,
       "pm1001lhrDwlswBanksUsed": pm1001lhrDwlswBanksUsed,
       "pm1001lhrDwlSwBank1Used": pm1001lhrDwlSwBank1Used,
       "pm1001lhrDwlSwBank2Used": pm1001lhrDwlSwBank2Used,
       "pm1001lhrDwlSwBank1Notempty": pm1001lhrDwlSwBank1Notempty,
       "pm1001lhrDwlSwBank2Notempty": pm1001lhrDwlSwBank2Notempty,
       "pm1001lhrDwlgwBanksUsed": pm1001lhrDwlgwBanksUsed,
       "pm1001lhrDwlGwBank1Used": pm1001lhrDwlGwBank1Used,
       "pm1001lhrDwlGwBank2Used": pm1001lhrDwlGwBank2Used,
       "pm1001lhrDwlGwBank3Used": pm1001lhrDwlGwBank3Used,
       "pm1001lhrDwlGwBank4Used": pm1001lhrDwlGwBank4Used,
       "pm1001lhrDwlGwBank1Notempty": pm1001lhrDwlGwBank1Notempty,
       "pm1001lhrDwlGwBank2Notempty": pm1001lhrDwlGwBank2Notempty,
       "pm1001lhrDwlGwBank3Notempty": pm1001lhrDwlGwBank3Notempty,
       "pm1001lhrDwlGwBank4Notempty": pm1001lhrDwlGwBank4Notempty,
       "pm1001lhrDwlClient": pm1001lhrDwlClient,
       "pm1001lhrDwlLine": pm1001lhrDwlLine,
       "pm1001lhrConfig": pm1001lhrConfig,
       "pm1001lhrCfgAccessCAisCsf": pm1001lhrCfgAccessCAisCsf,
       "pm1001lhrCfgStartup": pm1001lhrCfgStartup,
       "pm1001lhrtablelineStartup": pm1001lhrtablelineStartup,
       "pm1001lhrCfgsystConfLine1": pm1001lhrCfgsystConfLine1,
       "pm1001lhrCfgnetConfMod": pm1001lhrCfgnetConfMod,
       "pm1001lhrCfglineOptions1": pm1001lhrCfglineOptions1,
       "pm1001lhrCfgsystConfLine2": pm1001lhrCfgsystConfLine2,
       "pm1001lhrCfglineOptions2": pm1001lhrCfglineOptions2,
       "pm1001lhrCfgXfpTable": pm1001lhrCfgXfpTable,
       "pm1001lhrCfgXfpEntry": pm1001lhrCfgXfpEntry,
       "pm1001lhrCfgXfpIndex": pm1001lhrCfgXfpIndex,
       "pm1001lhrCfgSystConfXfpPortn": pm1001lhrCfgSystConfXfpPortn,
       "pm1001lhrCfgDataRateConfXfpPortn": pm1001lhrCfgDataRateConfXfpPortn,
       "pm1001lhrCfgLabels": pm1001lhrCfgLabels,
       "pm1001lhrCfgLabelclientTable": pm1001lhrCfgLabelclientTable,
       "pm1001lhrCfgLabelclientEntry": pm1001lhrCfgLabelclientEntry,
       "pm1001lhrCfgLabelclientIndex": pm1001lhrCfgLabelclientIndex,
       "pm1001lhrCfgLabelclientPortn": pm1001lhrCfgLabelclientPortn,
       "pm1001lhrCfgLabellineTable": pm1001lhrCfgLabellineTable,
       "pm1001lhrCfgLabellineEntry": pm1001lhrCfgLabellineEntry,
       "pm1001lhrCfgLabellineIndex": pm1001lhrCfgLabellineIndex,
       "pm1001lhrCfgLabellinePortn": pm1001lhrCfgLabellinePortn,
       "pm1001lhrCfgStartuptlh": pm1001lhrCfgStartuptlh,
       "pm1001lhrCfgOtxtlhTable": pm1001lhrCfgOtxtlhTable,
       "pm1001lhrCfgOtxtlhEntry": pm1001lhrCfgOtxtlhEntry,
       "pm1001lhrCfgOtxtlhIndex": pm1001lhrCfgOtxtlhIndex,
       "pm1001lhrCfgNuPortn": pm1001lhrCfgNuPortn,
       "pm1001lhrCfgLineDitherRatePortn": pm1001lhrCfgLineDitherRatePortn,
       "pm1001lhrCfgLineDitherFhzPortn": pm1001lhrCfgLineDitherFhzPortn,
       "pm1001lhrCfgLinePwrLaserPortn": pm1001lhrCfgLinePwrLaserPortn,
       "pm1001lhrCfgLineFCurrentPortn": pm1001lhrCfgLineFCurrentPortn,
       "pm1001lhrCfgLineGridCurrentPortn": pm1001lhrCfgLineGridCurrentPortn,
       "pm1001lhrCfgFPortn": pm1001lhrCfgFPortn,
       "pm1001lhrCfgReservedPortn": pm1001lhrCfgReservedPortn,
       "pm1001lhrCfgLinePhotodiodeModePortn": pm1001lhrCfgLinePhotodiodeModePortn,
       "pm1001lhrCfgLinePhotodiodeValuePortn": pm1001lhrCfgLinePhotodiodeValuePortn,
       "pm1001lhrCfgStartuptablefive": pm1001lhrCfgStartuptablefive,
       "pm1001lhrCfgOtxtlhcapabilitiesTable": pm1001lhrCfgOtxtlhcapabilitiesTable,
       "pm1001lhrCfgOtxtlhcapabilitiesEntry": pm1001lhrCfgOtxtlhcapabilitiesEntry,
       "pm1001lhrCfgOtxtlhcapabilitiesIndex": pm1001lhrCfgOtxtlhcapabilitiesIndex,
       "pm1001lhrCfgComponentTypePortn": pm1001lhrCfgComponentTypePortn,
       "pm1001lhrCfgMiscellaneousPortn": pm1001lhrCfgMiscellaneousPortn,
       "pm1001lhrCfgFirstChannelPortn": pm1001lhrCfgFirstChannelPortn,
       "pm1001lhrCfgLastChannelPortn": pm1001lhrCfgLastChannelPortn,
       "pm1001lhrCfgGridPortn": pm1001lhrCfgGridPortn,
       "pm1001lhrCfgWriteConfiguration": pm1001lhrCfgWriteConfiguration,
       "pm1001lhrtraps": pm1001lhrtraps,
       "pm1001lhrtrapLineNumber": pm1001lhrtrapLineNumber,
       "pm1001lhrtrapBoardNumber": pm1001lhrtrapBoardNumber,
       "pm1001lhrLineTrapNotUrgentGoesOn": pm1001lhrLineTrapNotUrgentGoesOn,
       "pm1001lhrLineTrapNotUrgentGoesOff": pm1001lhrLineTrapNotUrgentGoesOff,
       "pm1001lhrLineTrapUrgentGoesOn": pm1001lhrLineTrapUrgentGoesOn,
       "pm1001lhrLineTrapUrgentGoesOff": pm1001lhrLineTrapUrgentGoesOff,
       "pm1001lhrLineTrapCritGoesOn": pm1001lhrLineTrapCritGoesOn,
       "pm1001lhrLineTrapCritGoesOff": pm1001lhrLineTrapCritGoesOff,
       "pm1001lhrPowerTrapUrgentGoesOn": pm1001lhrPowerTrapUrgentGoesOn,
       "pm1001lhrPowerTrapUrgentGoesOff": pm1001lhrPowerTrapUrgentGoesOff}
)
