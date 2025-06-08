# SNMP MIB module (EKINOPS-Pm1004venc-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1004venc-MIB.mib
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

modulePm1004venc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43)
)
if mibBuilder.loadTexts:
    modulePm1004venc.setRevisions(
        ("2009-09-18 00:00",
         "2009-10-27 00:00",
         "2009-10-28 00:00",
         "2010-03-03 00:00",
         "2010-05-25 00:00",
         "2010-12-13 00:00",
         "2011-02-04 00:00",
         "2012-07-04 00:00",
         "2014-03-28 00:00",
         "2014-12-24 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1004vencModeTimeSlot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            256
        )
    )
    namedValues = NamedValues(
        ("singleSplitSelect", 256)
    )



class Pm1004vencModeAddDrop(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            256
        )
    )
    namedValues = NamedValues(
        ("singleSplitSelect", 256)
    )



class Pm1004vencProtectionTimeSlot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              257,
              513)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manualX2Line2", 257),
          ("manualX1Line1", 513))
    )



class Pm1004vencProtectionStartUp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manualX2Line2", 0),
          ("manualX1Line1", 1),
          ("auto", 2))
    )



class Pm1004vencDccMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dccNo", 0),
          ("dcctermLine1", 1),
          ("dcctermLine2", 2),
          ("dcctermLines12", 3),
          ("dccmaster", 4),
          ("dccslaveLine12", 7))
    )



class Pm1004vencClientOosMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clientportis", 0),
          ("clienttxoos", 1),
          ("clientrxoos", 2),
          ("clientportoos", 3))
    )



class Pm1004vencKeyMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("key1", 0),
          ("key2", 1))
    )



class Pm1004vencOtxMode(TextualConvention, Integer32):
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



class Pm1004vencOtxGrid(TextualConvention, Integer32):
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



class Pm1004vencAdjustValue(TextualConvention, Integer32):
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



class Pm1004vencOtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm1004vencalarms_ObjectIdentity = ObjectIdentity
pm1004vencalarms = _Pm1004vencalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2)
)
_Pm1004vencAlmOther_ObjectIdentity = ObjectIdentity
pm1004vencAlmOther = _Pm1004vencAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1)
)
_Pm1004vencAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1004vencAlmOtherNurg = _Pm1004vencAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 1)
)
_Pm1004vencAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm1004vencAlmsynthAlm2 = _Pm1004vencAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 1, 2)
)
_Pm1004vencAlmConfTableSave_Type = EkiOnOff
_Pm1004vencAlmConfTableSave_Object = MibScalar
pm1004vencAlmConfTableSave = _Pm1004vencAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 1, 2, 1),
    _Pm1004vencAlmConfTableSave_Type()
)
pm1004vencAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmConfTableSave.setStatus("current")
_Pm1004vencAlmInvUpload_Type = EkiOnOff
_Pm1004vencAlmInvUpload_Object = MibScalar
pm1004vencAlmInvUpload = _Pm1004vencAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 1, 2, 2),
    _Pm1004vencAlmInvUpload_Type()
)
pm1004vencAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmInvUpload.setStatus("current")
_Pm1004vencAlmConfTableLoad_Type = EkiOnOff
_Pm1004vencAlmConfTableLoad_Object = MibScalar
pm1004vencAlmConfTableLoad = _Pm1004vencAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 1, 2, 3),
    _Pm1004vencAlmConfTableLoad_Type()
)
pm1004vencAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmConfTableLoad.setStatus("current")
_Pm1004vencAlmCorrelatOff_Type = EkiOnOff
_Pm1004vencAlmCorrelatOff_Object = MibScalar
pm1004vencAlmCorrelatOff = _Pm1004vencAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 1, 2, 4),
    _Pm1004vencAlmCorrelatOff_Type()
)
pm1004vencAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmCorrelatOff.setStatus("current")
_Pm1004vencAlmMaintenanceOn_Type = EkiOnOff
_Pm1004vencAlmMaintenanceOn_Object = MibScalar
pm1004vencAlmMaintenanceOn = _Pm1004vencAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 1, 2, 5),
    _Pm1004vencAlmMaintenanceOn_Type()
)
pm1004vencAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmMaintenanceOn.setStatus("current")
_Pm1004vencAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1004vencAlmOtherUrg = _Pm1004vencAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2)
)
_Pm1004vencAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm1004vencAlmmodInitFailLevel2 = _Pm1004vencAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 194)
)
_Pm1004vencAlmLedFail_Type = EkiOnOff
_Pm1004vencAlmLedFail_Object = MibScalar
pm1004vencAlmLedFail = _Pm1004vencAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 194, 1),
    _Pm1004vencAlmLedFail_Type()
)
pm1004vencAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLedFail.setStatus("current")
_Pm1004vencAlmNextColdBootForced_Type = EkiOnOff
_Pm1004vencAlmNextColdBootForced_Object = MibScalar
pm1004vencAlmNextColdBootForced = _Pm1004vencAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 194, 2),
    _Pm1004vencAlmNextColdBootForced_Type()
)
pm1004vencAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmNextColdBootForced.setStatus("current")
_Pm1004vencAlmBootUndone_Type = EkiOnOff
_Pm1004vencAlmBootUndone_Object = MibScalar
pm1004vencAlmBootUndone = _Pm1004vencAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 194, 3),
    _Pm1004vencAlmBootUndone_Type()
)
pm1004vencAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmBootUndone.setStatus("current")
_Pm1004vencAlmResetHwInitFail_Type = EkiOnOff
_Pm1004vencAlmResetHwInitFail_Object = MibScalar
pm1004vencAlmResetHwInitFail = _Pm1004vencAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 194, 4),
    _Pm1004vencAlmResetHwInitFail_Type()
)
pm1004vencAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmResetHwInitFail.setStatus("current")
_Pm1004vencAlmSwInitFail_Type = EkiOnOff
_Pm1004vencAlmSwInitFail_Object = MibScalar
pm1004vencAlmSwInitFail = _Pm1004vencAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 194, 5),
    _Pm1004vencAlmSwInitFail_Type()
)
pm1004vencAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmSwInitFail.setStatus("current")
_Pm1004vencAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm1004vencAlmmodInitFailLevel3 = _Pm1004vencAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195)
)
_Pm1004vencAlmGwIdentFail_Type = EkiOnOff
_Pm1004vencAlmGwIdentFail_Object = MibScalar
pm1004vencAlmGwIdentFail = _Pm1004vencAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 1),
    _Pm1004vencAlmGwIdentFail_Type()
)
pm1004vencAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmGwIdentFail.setStatus("current")
_Pm1004vencAlmObmTypeReadFail_Type = EkiOnOff
_Pm1004vencAlmObmTypeReadFail_Object = MibScalar
pm1004vencAlmObmTypeReadFail = _Pm1004vencAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 2),
    _Pm1004vencAlmObmTypeReadFail_Type()
)
pm1004vencAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmObmTypeReadFail.setStatus("current")
_Pm1004vencAlmInitModuleFail_Type = EkiOnOff
_Pm1004vencAlmInitModuleFail_Object = MibScalar
pm1004vencAlmInitModuleFail = _Pm1004vencAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 3),
    _Pm1004vencAlmInitModuleFail_Type()
)
pm1004vencAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmInitModuleFail.setStatus("current")
_Pm1004vencAlmXfp1InitFail_Type = EkiOnOff
_Pm1004vencAlmXfp1InitFail_Object = MibScalar
pm1004vencAlmXfp1InitFail = _Pm1004vencAlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 5),
    _Pm1004vencAlmXfp1InitFail_Type()
)
pm1004vencAlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmXfp1InitFail.setStatus("current")
_Pm1004vencAlmXfp2InitFail_Type = EkiOnOff
_Pm1004vencAlmXfp2InitFail_Object = MibScalar
pm1004vencAlmXfp2InitFail = _Pm1004vencAlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 6),
    _Pm1004vencAlmXfp2InitFail_Type()
)
pm1004vencAlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmXfp2InitFail.setStatus("current")
_Pm1004vencAlmLine1InitFail_Type = EkiOnOff
_Pm1004vencAlmLine1InitFail_Object = MibScalar
pm1004vencAlmLine1InitFail = _Pm1004vencAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 7),
    _Pm1004vencAlmLine1InitFail_Type()
)
pm1004vencAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLine1InitFail.setStatus("current")
_Pm1004vencAlmLine2InitFail_Type = EkiOnOff
_Pm1004vencAlmLine2InitFail_Object = MibScalar
pm1004vencAlmLine2InitFail = _Pm1004vencAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 8),
    _Pm1004vencAlmLine2InitFail_Type()
)
pm1004vencAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLine2InitFail.setStatus("current")
_Pm1004vencAlmClient1InitFail_Type = EkiOnOff
_Pm1004vencAlmClient1InitFail_Object = MibScalar
pm1004vencAlmClient1InitFail = _Pm1004vencAlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 9),
    _Pm1004vencAlmClient1InitFail_Type()
)
pm1004vencAlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmClient1InitFail.setStatus("current")
_Pm1004vencAlmClient2InitFail_Type = EkiOnOff
_Pm1004vencAlmClient2InitFail_Object = MibScalar
pm1004vencAlmClient2InitFail = _Pm1004vencAlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 10),
    _Pm1004vencAlmClient2InitFail_Type()
)
pm1004vencAlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmClient2InitFail.setStatus("current")
_Pm1004vencAlmClient3InitFail_Type = EkiOnOff
_Pm1004vencAlmClient3InitFail_Object = MibScalar
pm1004vencAlmClient3InitFail = _Pm1004vencAlmClient3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 11),
    _Pm1004vencAlmClient3InitFail_Type()
)
pm1004vencAlmClient3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmClient3InitFail.setStatus("current")
_Pm1004vencAlmClient4InitFail_Type = EkiOnOff
_Pm1004vencAlmClient4InitFail_Object = MibScalar
pm1004vencAlmClient4InitFail = _Pm1004vencAlmClient4InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 195, 12),
    _Pm1004vencAlmClient4InitFail_Type()
)
pm1004vencAlmClient4InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmClient4InitFail.setStatus("current")
_Pm1004vencAlmclientRxProt_ObjectIdentity = ObjectIdentity
pm1004vencAlmclientRxProt = _Pm1004vencAlmclientRxProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 198)
)
_Pm1004vencAlmAdddropClient1West_Type = EkiOnOff
_Pm1004vencAlmAdddropClient1West_Object = MibScalar
pm1004vencAlmAdddropClient1West = _Pm1004vencAlmAdddropClient1West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 198, 1),
    _Pm1004vencAlmAdddropClient1West_Type()
)
pm1004vencAlmAdddropClient1West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmAdddropClient1West.setStatus("current")
_Pm1004vencAlmAdddropClient2West_Type = EkiOnOff
_Pm1004vencAlmAdddropClient2West_Object = MibScalar
pm1004vencAlmAdddropClient2West = _Pm1004vencAlmAdddropClient2West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 198, 2),
    _Pm1004vencAlmAdddropClient2West_Type()
)
pm1004vencAlmAdddropClient2West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmAdddropClient2West.setStatus("current")
_Pm1004vencAlmAdddropClient3West_Type = EkiOnOff
_Pm1004vencAlmAdddropClient3West_Object = MibScalar
pm1004vencAlmAdddropClient3West = _Pm1004vencAlmAdddropClient3West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 198, 3),
    _Pm1004vencAlmAdddropClient3West_Type()
)
pm1004vencAlmAdddropClient3West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmAdddropClient3West.setStatus("current")
_Pm1004vencAlmAdddropClient4West_Type = EkiOnOff
_Pm1004vencAlmAdddropClient4West_Object = MibScalar
pm1004vencAlmAdddropClient4West = _Pm1004vencAlmAdddropClient4West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 198, 4),
    _Pm1004vencAlmAdddropClient4West_Type()
)
pm1004vencAlmAdddropClient4West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmAdddropClient4West.setStatus("current")
_Pm1004vencAlmAdddropClient1East_Type = EkiOnOff
_Pm1004vencAlmAdddropClient1East_Object = MibScalar
pm1004vencAlmAdddropClient1East = _Pm1004vencAlmAdddropClient1East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 198, 9),
    _Pm1004vencAlmAdddropClient1East_Type()
)
pm1004vencAlmAdddropClient1East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmAdddropClient1East.setStatus("current")
_Pm1004vencAlmAdddropClient2East_Type = EkiOnOff
_Pm1004vencAlmAdddropClient2East_Object = MibScalar
pm1004vencAlmAdddropClient2East = _Pm1004vencAlmAdddropClient2East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 198, 10),
    _Pm1004vencAlmAdddropClient2East_Type()
)
pm1004vencAlmAdddropClient2East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmAdddropClient2East.setStatus("current")
_Pm1004vencAlmAdddropClient3East_Type = EkiOnOff
_Pm1004vencAlmAdddropClient3East_Object = MibScalar
pm1004vencAlmAdddropClient3East = _Pm1004vencAlmAdddropClient3East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 198, 11),
    _Pm1004vencAlmAdddropClient3East_Type()
)
pm1004vencAlmAdddropClient3East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmAdddropClient3East.setStatus("current")
_Pm1004vencAlmAdddropClient4East_Type = EkiOnOff
_Pm1004vencAlmAdddropClient4East_Object = MibScalar
pm1004vencAlmAdddropClient4East = _Pm1004vencAlmAdddropClient4East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 198, 12),
    _Pm1004vencAlmAdddropClient4East_Type()
)
pm1004vencAlmAdddropClient4East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmAdddropClient4East.setStatus("current")
_Pm1004vencAlmmodOther_ObjectIdentity = ObjectIdentity
pm1004vencAlmmodOther = _Pm1004vencAlmmodOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 199)
)
_Pm1004vencAlmAesDecodFail_Type = EkiOnOff
_Pm1004vencAlmAesDecodFail_Object = MibScalar
pm1004vencAlmAesDecodFail = _Pm1004vencAlmAesDecodFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 2, 199, 1),
    _Pm1004vencAlmAesDecodFail_Type()
)
pm1004vencAlmAesDecodFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmAesDecodFail.setStatus("current")
_Pm1004vencAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1004vencAlmOtherCrit = _Pm1004vencAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 3)
)
_Pm1004vencAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1004vencAlmsynthAlm0 = _Pm1004vencAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 3, 0)
)
_Pm1004vencAlmModGlobFail_Type = EkiOnOff
_Pm1004vencAlmModGlobFail_Object = MibScalar
pm1004vencAlmModGlobFail = _Pm1004vencAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 3, 0, 9),
    _Pm1004vencAlmModGlobFail_Type()
)
pm1004vencAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmModGlobFail.setStatus("current")
_Pm1004vencAlmDefFuseA_Type = EkiOnOff
_Pm1004vencAlmDefFuseA_Object = MibScalar
pm1004vencAlmDefFuseA = _Pm1004vencAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 3, 0, 15),
    _Pm1004vencAlmDefFuseA_Type()
)
pm1004vencAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDefFuseA.setStatus("current")
_Pm1004vencAlmDefFuseB_Type = EkiOnOff
_Pm1004vencAlmDefFuseB_Object = MibScalar
pm1004vencAlmDefFuseB = _Pm1004vencAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 1, 3, 0, 16),
    _Pm1004vencAlmDefFuseB_Type()
)
pm1004vencAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDefFuseB.setStatus("current")
_Pm1004vencAlmClient_ObjectIdentity = ObjectIdentity
pm1004vencAlmClient = _Pm1004vencAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2)
)
_Pm1004vencAlmClientNurg_ObjectIdentity = ObjectIdentity
pm1004vencAlmClientNurg = _Pm1004vencAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 1)
)
_Pm1004vencAlmClientUrg_ObjectIdentity = ObjectIdentity
pm1004vencAlmClientUrg = _Pm1004vencAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 2)
)
_Pm1004vencAlmClientCrit_ObjectIdentity = ObjectIdentity
pm1004vencAlmClientCrit = _Pm1004vencAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3)
)
_Pm1004vencAlmsynthAlmPortTable_Object = MibTable
pm1004vencAlmsynthAlmPortTable = _Pm1004vencAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm1004vencAlmsynthAlmPortTable.setStatus("current")
_Pm1004vencAlmsynthAlmPortEntry_Object = MibTableRow
pm1004vencAlmsynthAlmPortEntry = _Pm1004vencAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8, 1)
)
pm1004vencAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmsynthAlmPortEntry.setStatus("current")


class _Pm1004vencAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm1004vencAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmsynthAlmPortIndex_Object = MibTableColumn
pm1004vencAlmsynthAlmPortIndex = _Pm1004vencAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8, 1, 1),
    _Pm1004vencAlmsynthAlmPortIndex_Type()
)
pm1004vencAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmsynthAlmPortIndex.setStatus("current")
_Pm1004vencAlmHwFailAccPortn_Type = EkiOnOff
_Pm1004vencAlmHwFailAccPortn_Object = MibTableColumn
pm1004vencAlmHwFailAccPortn = _Pm1004vencAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8, 1, 5),
    _Pm1004vencAlmHwFailAccPortn_Type()
)
pm1004vencAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmHwFailAccPortn.setStatus("current")
_Pm1004vencAlmDwLsdPortn_Type = EkiOnOff
_Pm1004vencAlmDwLsdPortn_Object = MibTableColumn
pm1004vencAlmDwLsdPortn = _Pm1004vencAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8, 1, 6),
    _Pm1004vencAlmDwLsdPortn_Type()
)
pm1004vencAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDwLsdPortn.setStatus("current")
_Pm1004vencAlmClientLocalOosTxPortn_Type = EkiOnOff
_Pm1004vencAlmClientLocalOosTxPortn_Object = MibTableColumn
pm1004vencAlmClientLocalOosTxPortn = _Pm1004vencAlmClientLocalOosTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8, 1, 7),
    _Pm1004vencAlmClientLocalOosTxPortn_Type()
)
pm1004vencAlmClientLocalOosTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmClientLocalOosTxPortn.setStatus("current")
_Pm1004vencAlmClientLocalOosRxPortn_Type = EkiOnOff
_Pm1004vencAlmClientLocalOosRxPortn_Object = MibTableColumn
pm1004vencAlmClientLocalOosRxPortn = _Pm1004vencAlmClientLocalOosRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8, 1, 8),
    _Pm1004vencAlmClientLocalOosRxPortn_Type()
)
pm1004vencAlmClientLocalOosRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmClientLocalOosRxPortn.setStatus("current")
_Pm1004vencAlmDwCaisPortn_Type = EkiOnOff
_Pm1004vencAlmDwCaisPortn_Object = MibTableColumn
pm1004vencAlmDwCaisPortn = _Pm1004vencAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8, 1, 9),
    _Pm1004vencAlmDwCaisPortn_Type()
)
pm1004vencAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDwCaisPortn.setStatus("current")
_Pm1004vencAlmFailAccPortn_Type = EkiOnOff
_Pm1004vencAlmFailAccPortn_Object = MibTableColumn
pm1004vencAlmFailAccPortn = _Pm1004vencAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8, 1, 13),
    _Pm1004vencAlmFailAccPortn_Type()
)
pm1004vencAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmFailAccPortn.setStatus("current")
_Pm1004vencAlmUpCsfPortn_Type = EkiOnOff
_Pm1004vencAlmUpCsfPortn_Object = MibTableColumn
pm1004vencAlmUpCsfPortn = _Pm1004vencAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 8, 1, 17),
    _Pm1004vencAlmUpCsfPortn_Type()
)
pm1004vencAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmUpCsfPortn.setStatus("current")
_Pm1004vencAlmaccessioAlmTable_Object = MibTable
pm1004vencAlmaccessioAlmTable = _Pm1004vencAlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm1004vencAlmaccessioAlmTable.setStatus("current")
_Pm1004vencAlmaccessioAlmEntry_Object = MibTableRow
pm1004vencAlmaccessioAlmEntry = _Pm1004vencAlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 16, 1)
)
pm1004vencAlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmaccessioAlmEntry.setStatus("current")


class _Pm1004vencAlmaccessioAlmIndex_Type(Integer32):
    """Custom type pm1004vencAlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmaccessioAlmIndex_Object = MibTableColumn
pm1004vencAlmaccessioAlmIndex = _Pm1004vencAlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 16, 1, 1),
    _Pm1004vencAlmaccessioAlmIndex_Type()
)
pm1004vencAlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmaccessioAlmIndex.setStatus("current")
_Pm1004vencAlmUpLosPortn_Type = EkiOnOff
_Pm1004vencAlmUpLosPortn_Object = MibTableColumn
pm1004vencAlmUpLosPortn = _Pm1004vencAlmUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 16, 1, 5),
    _Pm1004vencAlmUpLosPortn_Type()
)
pm1004vencAlmUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmUpLosPortn.setStatus("current")
_Pm1004vencAlmmapperDeAlmTable_Object = MibTable
pm1004vencAlmmapperDeAlmTable = _Pm1004vencAlmmapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pm1004vencAlmmapperDeAlmTable.setStatus("current")
_Pm1004vencAlmmapperDeAlmEntry_Object = MibTableRow
pm1004vencAlmmapperDeAlmEntry = _Pm1004vencAlmmapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 72, 1)
)
pm1004vencAlmmapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmmapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmmapperDeAlmEntry.setStatus("current")


class _Pm1004vencAlmmapperDeAlmIndex_Type(Integer32):
    """Custom type pm1004vencAlmmapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmmapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmmapperDeAlmIndex_Object = MibTableColumn
pm1004vencAlmmapperDeAlmIndex = _Pm1004vencAlmmapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 72, 1, 1),
    _Pm1004vencAlmmapperDeAlmIndex_Type()
)
pm1004vencAlmmapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmmapperDeAlmIndex.setStatus("current")
_Pm1004vencAlmUpAccOosPortn_Type = EkiOnOff
_Pm1004vencAlmUpAccOosPortn_Object = MibTableColumn
pm1004vencAlmUpAccOosPortn = _Pm1004vencAlmUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 72, 1, 2),
    _Pm1004vencAlmUpAccOosPortn_Type()
)
pm1004vencAlmUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmUpAccOosPortn.setStatus("current")
_Pm1004vencAlmUpBufferOvlPortn_Type = EkiOnOff
_Pm1004vencAlmUpBufferOvlPortn_Object = MibTableColumn
pm1004vencAlmUpBufferOvlPortn = _Pm1004vencAlmUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 72, 1, 11),
    _Pm1004vencAlmUpBufferOvlPortn_Type()
)
pm1004vencAlmUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmUpBufferOvlPortn.setStatus("current")
_Pm1004vencAlmDwCsfDetPortn_Type = EkiOnOff
_Pm1004vencAlmDwCsfDetPortn_Object = MibTableColumn
pm1004vencAlmDwCsfDetPortn = _Pm1004vencAlmDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 72, 1, 12),
    _Pm1004vencAlmDwCsfDetPortn_Type()
)
pm1004vencAlmDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDwCsfDetPortn.setStatus("current")
_Pm1004vencAlmDwBufferOvlPortn_Type = EkiOnOff
_Pm1004vencAlmDwBufferOvlPortn_Object = MibTableColumn
pm1004vencAlmDwBufferOvlPortn = _Pm1004vencAlmDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 72, 1, 15),
    _Pm1004vencAlmDwBufferOvlPortn_Type()
)
pm1004vencAlmDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDwBufferOvlPortn.setStatus("current")
_Pm1004vencAlmvideoProtocolStatusTable_Object = MibTable
pm1004vencAlmvideoProtocolStatusTable = _Pm1004vencAlmvideoProtocolStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112)
)
if mibBuilder.loadTexts:
    pm1004vencAlmvideoProtocolStatusTable.setStatus("current")
_Pm1004vencAlmvideoProtocolStatusEntry_Object = MibTableRow
pm1004vencAlmvideoProtocolStatusEntry = _Pm1004vencAlmvideoProtocolStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1)
)
pm1004vencAlmvideoProtocolStatusEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmvideoProtocolStatusIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmvideoProtocolStatusEntry.setStatus("current")


class _Pm1004vencAlmvideoProtocolStatusIndex_Type(Integer32):
    """Custom type pm1004vencAlmvideoProtocolStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmvideoProtocolStatusIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmvideoProtocolStatusIndex_Object = MibTableColumn
pm1004vencAlmvideoProtocolStatusIndex = _Pm1004vencAlmvideoProtocolStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1, 1),
    _Pm1004vencAlmvideoProtocolStatusIndex_Type()
)
pm1004vencAlmvideoProtocolStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmvideoProtocolStatusIndex.setStatus("current")
_Pm1004vencAlmSdiTxPortn_Type = EkiOnOff
_Pm1004vencAlmSdiTxPortn_Object = MibTableColumn
pm1004vencAlmSdiTxPortn = _Pm1004vencAlmSdiTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1, 2),
    _Pm1004vencAlmSdiTxPortn_Type()
)
pm1004vencAlmSdiTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmSdiTxPortn.setStatus("current")
_Pm1004vencAlmHdSdiPalTxPortn_Type = EkiOnOff
_Pm1004vencAlmHdSdiPalTxPortn_Object = MibTableColumn
pm1004vencAlmHdSdiPalTxPortn = _Pm1004vencAlmHdSdiPalTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1, 3),
    _Pm1004vencAlmHdSdiPalTxPortn_Type()
)
pm1004vencAlmHdSdiPalTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmHdSdiPalTxPortn.setStatus("current")
_Pm1004vencAlmHdSdiNtscTxPortn_Type = EkiOnOff
_Pm1004vencAlmHdSdiNtscTxPortn_Object = MibTableColumn
pm1004vencAlmHdSdiNtscTxPortn = _Pm1004vencAlmHdSdiNtscTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1, 4),
    _Pm1004vencAlmHdSdiNtscTxPortn_Type()
)
pm1004vencAlmHdSdiNtscTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmHdSdiNtscTxPortn.setStatus("current")
_Pm1004vencAlmDvbAsiTxPortn_Type = EkiOnOff
_Pm1004vencAlmDvbAsiTxPortn_Object = MibTableColumn
pm1004vencAlmDvbAsiTxPortn = _Pm1004vencAlmDvbAsiTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1, 5),
    _Pm1004vencAlmDvbAsiTxPortn_Type()
)
pm1004vencAlmDvbAsiTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDvbAsiTxPortn.setStatus("current")
_Pm1004vencAlmSdiRxPortn_Type = EkiOnOff
_Pm1004vencAlmSdiRxPortn_Object = MibTableColumn
pm1004vencAlmSdiRxPortn = _Pm1004vencAlmSdiRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1, 10),
    _Pm1004vencAlmSdiRxPortn_Type()
)
pm1004vencAlmSdiRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmSdiRxPortn.setStatus("current")
_Pm1004vencAlmHdSdiPalRxPortn_Type = EkiOnOff
_Pm1004vencAlmHdSdiPalRxPortn_Object = MibTableColumn
pm1004vencAlmHdSdiPalRxPortn = _Pm1004vencAlmHdSdiPalRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1, 11),
    _Pm1004vencAlmHdSdiPalRxPortn_Type()
)
pm1004vencAlmHdSdiPalRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmHdSdiPalRxPortn.setStatus("current")
_Pm1004vencAlmHdSdiNtscRxPortn_Type = EkiOnOff
_Pm1004vencAlmHdSdiNtscRxPortn_Object = MibTableColumn
pm1004vencAlmHdSdiNtscRxPortn = _Pm1004vencAlmHdSdiNtscRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1, 12),
    _Pm1004vencAlmHdSdiNtscRxPortn_Type()
)
pm1004vencAlmHdSdiNtscRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmHdSdiNtscRxPortn.setStatus("current")
_Pm1004vencAlmDvbAsiRxPortn_Type = EkiOnOff
_Pm1004vencAlmDvbAsiRxPortn_Object = MibTableColumn
pm1004vencAlmDvbAsiRxPortn = _Pm1004vencAlmDvbAsiRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 2, 3, 112, 1, 13),
    _Pm1004vencAlmDvbAsiRxPortn_Type()
)
pm1004vencAlmDvbAsiRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDvbAsiRxPortn.setStatus("current")
_Pm1004vencAlmLine_ObjectIdentity = ObjectIdentity
pm1004vencAlmLine = _Pm1004vencAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3)
)
_Pm1004vencAlmLineNurg_ObjectIdentity = ObjectIdentity
pm1004vencAlmLineNurg = _Pm1004vencAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1)
)
_Pm1004vencAlmlineXfp1WarningsTable_Object = MibTable
pm1004vencAlmlineXfp1WarningsTable = _Pm1004vencAlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1WarningsTable.setStatus("current")
_Pm1004vencAlmlineXfp1WarningsEntry_Object = MibTableRow
pm1004vencAlmlineXfp1WarningsEntry = _Pm1004vencAlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1)
)
pm1004vencAlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1WarningsEntry.setStatus("current")


class _Pm1004vencAlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pm1004vencAlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmlineXfp1WarningsIndex_Object = MibTableColumn
pm1004vencAlmlineXfp1WarningsIndex = _Pm1004vencAlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1, 1),
    _Pm1004vencAlmlineXfp1WarningsIndex_Type()
)
pm1004vencAlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1WarningsIndex.setStatus("current")
_Pm1004vencAlmTxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004vencAlmTxPowerLowWarningPortn_Object = MibTableColumn
pm1004vencAlmTxPowerLowWarningPortn = _Pm1004vencAlmTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1, 2),
    _Pm1004vencAlmTxPowerLowWarningPortn_Type()
)
pm1004vencAlmTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxPowerLowWarningPortn.setStatus("current")
_Pm1004vencAlmTxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmTxPowerHighWarningPortn_Object = MibTableColumn
pm1004vencAlmTxPowerHighWarningPortn = _Pm1004vencAlmTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1, 3),
    _Pm1004vencAlmTxPowerHighWarningPortn_Type()
)
pm1004vencAlmTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxPowerHighWarningPortn.setStatus("current")
_Pm1004vencAlmTxBiasLowWarningPortn_Type = EkiOnOff
_Pm1004vencAlmTxBiasLowWarningPortn_Object = MibTableColumn
pm1004vencAlmTxBiasLowWarningPortn = _Pm1004vencAlmTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1, 4),
    _Pm1004vencAlmTxBiasLowWarningPortn_Type()
)
pm1004vencAlmTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxBiasLowWarningPortn.setStatus("current")
_Pm1004vencAlmTxBiasHighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmTxBiasHighWarningPortn_Object = MibTableColumn
pm1004vencAlmTxBiasHighWarningPortn = _Pm1004vencAlmTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1, 5),
    _Pm1004vencAlmTxBiasHighWarningPortn_Type()
)
pm1004vencAlmTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxBiasHighWarningPortn.setStatus("current")
_Pm1004vencAlmTempLowWarningPortn_Type = EkiOnOff
_Pm1004vencAlmTempLowWarningPortn_Object = MibTableColumn
pm1004vencAlmTempLowWarningPortn = _Pm1004vencAlmTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1, 8),
    _Pm1004vencAlmTempLowWarningPortn_Type()
)
pm1004vencAlmTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTempLowWarningPortn.setStatus("current")
_Pm1004vencAlmTempHighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmTempHighWarningPortn_Object = MibTableColumn
pm1004vencAlmTempHighWarningPortn = _Pm1004vencAlmTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1, 9),
    _Pm1004vencAlmTempHighWarningPortn_Type()
)
pm1004vencAlmTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTempHighWarningPortn.setStatus("current")
_Pm1004vencAlmRxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004vencAlmRxPowerLowWarningPortn_Object = MibTableColumn
pm1004vencAlmRxPowerLowWarningPortn = _Pm1004vencAlmRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1, 16),
    _Pm1004vencAlmRxPowerLowWarningPortn_Type()
)
pm1004vencAlmRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmRxPowerLowWarningPortn.setStatus("current")
_Pm1004vencAlmRxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmRxPowerHighWarningPortn_Object = MibTableColumn
pm1004vencAlmRxPowerHighWarningPortn = _Pm1004vencAlmRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 209, 1, 17),
    _Pm1004vencAlmRxPowerHighWarningPortn_Type()
)
pm1004vencAlmRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmRxPowerHighWarningPortn.setStatus("current")
_Pm1004vencAlmlineOtx1TlhWarningsTable_Object = MibTable
pm1004vencAlmlineOtx1TlhWarningsTable = _Pm1004vencAlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineOtx1TlhWarningsTable.setStatus("current")
_Pm1004vencAlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pm1004vencAlmlineOtx1TlhWarningsEntry = _Pm1004vencAlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 225, 1)
)
pm1004vencAlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pm1004vencAlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pm1004vencAlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pm1004vencAlmlineOtx1TlhWarningsIndex = _Pm1004vencAlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 225, 1, 1),
    _Pm1004vencAlmlineOtx1TlhWarningsIndex_Type()
)
pm1004vencAlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pm1004vencAlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pm1004vencAlmLineModulatorAgingHighWarningPortn = _Pm1004vencAlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 225, 1, 6),
    _Pm1004vencAlmLineModulatorAgingHighWarningPortn_Type()
)
pm1004vencAlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pm1004vencAlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmLineAgingHighWarningPortn_Object = MibTableColumn
pm1004vencAlmLineAgingHighWarningPortn = _Pm1004vencAlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 225, 1, 7),
    _Pm1004vencAlmLineAgingHighWarningPortn_Type()
)
pm1004vencAlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineAgingHighWarningPortn.setStatus("current")
_Pm1004vencAlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pm1004vencAlmLineFreqDevHighWarningPortn = _Pm1004vencAlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 225, 1, 13),
    _Pm1004vencAlmLineFreqDevHighWarningPortn_Type()
)
pm1004vencAlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineFreqDevHighWarningPortn.setStatus("current")
_Pm1004vencAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm1004vencAlmLineLaserTempHighWarningPortn = _Pm1004vencAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 1, 225, 1, 15),
    _Pm1004vencAlmLineLaserTempHighWarningPortn_Type()
)
pm1004vencAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm1004vencAlmLineUrg_ObjectIdentity = ObjectIdentity
pm1004vencAlmLineUrg = _Pm1004vencAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2)
)
_Pm1004vencAlmlineXfp1AlarmTable_Object = MibTable
pm1004vencAlmlineXfp1AlarmTable = _Pm1004vencAlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1AlarmTable.setStatus("current")
_Pm1004vencAlmlineXfp1AlarmEntry_Object = MibTableRow
pm1004vencAlmlineXfp1AlarmEntry = _Pm1004vencAlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1)
)
pm1004vencAlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1AlarmEntry.setStatus("current")


class _Pm1004vencAlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pm1004vencAlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmlineXfp1AlarmIndex_Object = MibTableColumn
pm1004vencAlmlineXfp1AlarmIndex = _Pm1004vencAlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1, 1),
    _Pm1004vencAlmlineXfp1AlarmIndex_Type()
)
pm1004vencAlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1AlarmIndex.setStatus("current")
_Pm1004vencAlmTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmTxPowerLowAlarmPortn_Object = MibTableColumn
pm1004vencAlmTxPowerLowAlarmPortn = _Pm1004vencAlmTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1, 2),
    _Pm1004vencAlmTxPowerLowAlarmPortn_Type()
)
pm1004vencAlmTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxPowerLowAlarmPortn.setStatus("current")
_Pm1004vencAlmTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmTxPowerHighAlarmPortn_Object = MibTableColumn
pm1004vencAlmTxPowerHighAlarmPortn = _Pm1004vencAlmTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1, 3),
    _Pm1004vencAlmTxPowerHighAlarmPortn_Type()
)
pm1004vencAlmTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxPowerHighAlarmPortn.setStatus("current")
_Pm1004vencAlmTxBiasLowAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmTxBiasLowAlarmPortn_Object = MibTableColumn
pm1004vencAlmTxBiasLowAlarmPortn = _Pm1004vencAlmTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1, 4),
    _Pm1004vencAlmTxBiasLowAlarmPortn_Type()
)
pm1004vencAlmTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxBiasLowAlarmPortn.setStatus("current")
_Pm1004vencAlmTxBiasHighAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmTxBiasHighAlarmPortn_Object = MibTableColumn
pm1004vencAlmTxBiasHighAlarmPortn = _Pm1004vencAlmTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1, 5),
    _Pm1004vencAlmTxBiasHighAlarmPortn_Type()
)
pm1004vencAlmTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxBiasHighAlarmPortn.setStatus("current")
_Pm1004vencAlmTempLowAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmTempLowAlarmPortn_Object = MibTableColumn
pm1004vencAlmTempLowAlarmPortn = _Pm1004vencAlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1, 8),
    _Pm1004vencAlmTempLowAlarmPortn_Type()
)
pm1004vencAlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTempLowAlarmPortn.setStatus("current")
_Pm1004vencAlmTempHighAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmTempHighAlarmPortn_Object = MibTableColumn
pm1004vencAlmTempHighAlarmPortn = _Pm1004vencAlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1, 9),
    _Pm1004vencAlmTempHighAlarmPortn_Type()
)
pm1004vencAlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTempHighAlarmPortn.setStatus("current")
_Pm1004vencAlmRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmRxPowerLowAlarmPortn_Object = MibTableColumn
pm1004vencAlmRxPowerLowAlarmPortn = _Pm1004vencAlmRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1, 16),
    _Pm1004vencAlmRxPowerLowAlarmPortn_Type()
)
pm1004vencAlmRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmRxPowerLowAlarmPortn.setStatus("current")
_Pm1004vencAlmRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmRxPowerHighAlarmPortn_Object = MibTableColumn
pm1004vencAlmRxPowerHighAlarmPortn = _Pm1004vencAlmRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 208, 1, 17),
    _Pm1004vencAlmRxPowerHighAlarmPortn_Type()
)
pm1004vencAlmRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmRxPowerHighAlarmPortn.setStatus("current")
_Pm1004vencAlmlineXfp1CritTable_Object = MibTable
pm1004vencAlmlineXfp1CritTable = _Pm1004vencAlmlineXfp1CritTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 210)
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1CritTable.setStatus("current")
_Pm1004vencAlmlineXfp1CritEntry_Object = MibTableRow
pm1004vencAlmlineXfp1CritEntry = _Pm1004vencAlmlineXfp1CritEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 210, 1)
)
pm1004vencAlmlineXfp1CritEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmlineXfp1CritIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1CritEntry.setStatus("current")


class _Pm1004vencAlmlineXfp1CritIndex_Type(Integer32):
    """Custom type pm1004vencAlmlineXfp1CritIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmlineXfp1CritIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmlineXfp1CritIndex_Object = MibTableColumn
pm1004vencAlmlineXfp1CritIndex = _Pm1004vencAlmlineXfp1CritIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 210, 1, 1),
    _Pm1004vencAlmlineXfp1CritIndex_Type()
)
pm1004vencAlmlineXfp1CritIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1CritIndex.setStatus("current")
_Pm1004vencAlmTxPowerLowCritPortn_Type = EkiOnOff
_Pm1004vencAlmTxPowerLowCritPortn_Object = MibTableColumn
pm1004vencAlmTxPowerLowCritPortn = _Pm1004vencAlmTxPowerLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 210, 1, 2),
    _Pm1004vencAlmTxPowerLowCritPortn_Type()
)
pm1004vencAlmTxPowerLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxPowerLowCritPortn.setStatus("current")
_Pm1004vencAlmTxPowerHighCritPortn_Type = EkiOnOff
_Pm1004vencAlmTxPowerHighCritPortn_Object = MibTableColumn
pm1004vencAlmTxPowerHighCritPortn = _Pm1004vencAlmTxPowerHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 210, 1, 3),
    _Pm1004vencAlmTxPowerHighCritPortn_Type()
)
pm1004vencAlmTxPowerHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxPowerHighCritPortn.setStatus("current")
_Pm1004vencAlmRxPowerLowCritPortn_Type = EkiOnOff
_Pm1004vencAlmRxPowerLowCritPortn_Object = MibTableColumn
pm1004vencAlmRxPowerLowCritPortn = _Pm1004vencAlmRxPowerLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 210, 1, 16),
    _Pm1004vencAlmRxPowerLowCritPortn_Type()
)
pm1004vencAlmRxPowerLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmRxPowerLowCritPortn.setStatus("current")
_Pm1004vencAlmRxPowerHighCritPortn_Type = EkiOnOff
_Pm1004vencAlmRxPowerHighCritPortn_Object = MibTableColumn
pm1004vencAlmRxPowerHighCritPortn = _Pm1004vencAlmRxPowerHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 210, 1, 17),
    _Pm1004vencAlmRxPowerHighCritPortn_Type()
)
pm1004vencAlmRxPowerHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmRxPowerHighCritPortn.setStatus("current")
_Pm1004vencAlmlineXfp1SupplyAlarmTable_Object = MibTable
pm1004vencAlmlineXfp1SupplyAlarmTable = _Pm1004vencAlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pm1004vencAlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pm1004vencAlmlineXfp1SupplyAlarmEntry = _Pm1004vencAlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1)
)
pm1004vencAlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pm1004vencAlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pm1004vencAlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pm1004vencAlmlineXfp1SupplyAlarmIndex = _Pm1004vencAlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 1),
    _Pm1004vencAlmlineXfp1SupplyAlarmIndex_Type()
)
pm1004vencAlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pm1004vencAlmVee5LowAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmVee5LowAlarmPortn_Object = MibTableColumn
pm1004vencAlmVee5LowAlarmPortn = _Pm1004vencAlmVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 2),
    _Pm1004vencAlmVee5LowAlarmPortn_Type()
)
pm1004vencAlmVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVee5LowAlarmPortn.setStatus("current")
_Pm1004vencAlmVee5HighAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmVee5HighAlarmPortn_Object = MibTableColumn
pm1004vencAlmVee5HighAlarmPortn = _Pm1004vencAlmVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 3),
    _Pm1004vencAlmVee5HighAlarmPortn_Type()
)
pm1004vencAlmVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVee5HighAlarmPortn.setStatus("current")
_Pm1004vencAlmVcc2LowAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmVcc2LowAlarmPortn_Object = MibTableColumn
pm1004vencAlmVcc2LowAlarmPortn = _Pm1004vencAlmVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 4),
    _Pm1004vencAlmVcc2LowAlarmPortn_Type()
)
pm1004vencAlmVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc2LowAlarmPortn.setStatus("current")
_Pm1004vencAlmVcc2HighAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmVcc2HighAlarmPortn_Object = MibTableColumn
pm1004vencAlmVcc2HighAlarmPortn = _Pm1004vencAlmVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 5),
    _Pm1004vencAlmVcc2HighAlarmPortn_Type()
)
pm1004vencAlmVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc2HighAlarmPortn.setStatus("current")
_Pm1004vencAlmVcc3LowAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmVcc3LowAlarmPortn_Object = MibTableColumn
pm1004vencAlmVcc3LowAlarmPortn = _Pm1004vencAlmVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 6),
    _Pm1004vencAlmVcc3LowAlarmPortn_Type()
)
pm1004vencAlmVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc3LowAlarmPortn.setStatus("current")
_Pm1004vencAlmVcc3HighAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmVcc3HighAlarmPortn_Object = MibTableColumn
pm1004vencAlmVcc3HighAlarmPortn = _Pm1004vencAlmVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 7),
    _Pm1004vencAlmVcc3HighAlarmPortn_Type()
)
pm1004vencAlmVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc3HighAlarmPortn.setStatus("current")
_Pm1004vencAlmVcc5LowAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmVcc5LowAlarmPortn_Object = MibTableColumn
pm1004vencAlmVcc5LowAlarmPortn = _Pm1004vencAlmVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 8),
    _Pm1004vencAlmVcc5LowAlarmPortn_Type()
)
pm1004vencAlmVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc5LowAlarmPortn.setStatus("current")
_Pm1004vencAlmVcc5HighAlarmPortn_Type = EkiOnOff
_Pm1004vencAlmVcc5HighAlarmPortn_Object = MibTableColumn
pm1004vencAlmVcc5HighAlarmPortn = _Pm1004vencAlmVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 9),
    _Pm1004vencAlmVcc5HighAlarmPortn_Type()
)
pm1004vencAlmVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc5HighAlarmPortn.setStatus("current")
_Pm1004vencAlmVee5LowWarningPortn_Type = EkiOnOff
_Pm1004vencAlmVee5LowWarningPortn_Object = MibTableColumn
pm1004vencAlmVee5LowWarningPortn = _Pm1004vencAlmVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 10),
    _Pm1004vencAlmVee5LowWarningPortn_Type()
)
pm1004vencAlmVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVee5LowWarningPortn.setStatus("current")
_Pm1004vencAlmVee5HighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmVee5HighWarningPortn_Object = MibTableColumn
pm1004vencAlmVee5HighWarningPortn = _Pm1004vencAlmVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 11),
    _Pm1004vencAlmVee5HighWarningPortn_Type()
)
pm1004vencAlmVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVee5HighWarningPortn.setStatus("current")
_Pm1004vencAlmVcc2LowWarningPortn_Type = EkiOnOff
_Pm1004vencAlmVcc2LowWarningPortn_Object = MibTableColumn
pm1004vencAlmVcc2LowWarningPortn = _Pm1004vencAlmVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 12),
    _Pm1004vencAlmVcc2LowWarningPortn_Type()
)
pm1004vencAlmVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc2LowWarningPortn.setStatus("current")
_Pm1004vencAlmVcc2HighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmVcc2HighWarningPortn_Object = MibTableColumn
pm1004vencAlmVcc2HighWarningPortn = _Pm1004vencAlmVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 13),
    _Pm1004vencAlmVcc2HighWarningPortn_Type()
)
pm1004vencAlmVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc2HighWarningPortn.setStatus("current")
_Pm1004vencAlmVcc3LowWarningPortn_Type = EkiOnOff
_Pm1004vencAlmVcc3LowWarningPortn_Object = MibTableColumn
pm1004vencAlmVcc3LowWarningPortn = _Pm1004vencAlmVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 14),
    _Pm1004vencAlmVcc3LowWarningPortn_Type()
)
pm1004vencAlmVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc3LowWarningPortn.setStatus("current")
_Pm1004vencAlmVcc3HighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmVcc3HighWarningPortn_Object = MibTableColumn
pm1004vencAlmVcc3HighWarningPortn = _Pm1004vencAlmVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 15),
    _Pm1004vencAlmVcc3HighWarningPortn_Type()
)
pm1004vencAlmVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc3HighWarningPortn.setStatus("current")
_Pm1004vencAlmVcc5LowWarningPortn_Type = EkiOnOff
_Pm1004vencAlmVcc5LowWarningPortn_Object = MibTableColumn
pm1004vencAlmVcc5LowWarningPortn = _Pm1004vencAlmVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 16),
    _Pm1004vencAlmVcc5LowWarningPortn_Type()
)
pm1004vencAlmVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc5LowWarningPortn.setStatus("current")
_Pm1004vencAlmVcc5HighWarningPortn_Type = EkiOnOff
_Pm1004vencAlmVcc5HighWarningPortn_Object = MibTableColumn
pm1004vencAlmVcc5HighWarningPortn = _Pm1004vencAlmVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 212, 1, 17),
    _Pm1004vencAlmVcc5HighWarningPortn_Type()
)
pm1004vencAlmVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmVcc5HighWarningPortn.setStatus("current")
_Pm1004vencAlmlineOtx1TlhAlarmsTable_Object = MibTable
pm1004vencAlmlineOtx1TlhAlarmsTable = _Pm1004vencAlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pm1004vencAlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pm1004vencAlmlineOtx1TlhAlarmsEntry = _Pm1004vencAlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 224, 1)
)
pm1004vencAlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pm1004vencAlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pm1004vencAlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pm1004vencAlmlineOtx1TlhAlarmsIndex = _Pm1004vencAlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 224, 1, 1),
    _Pm1004vencAlmlineOtx1TlhAlarmsIndex_Type()
)
pm1004vencAlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pm1004vencAlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pm1004vencAlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pm1004vencAlmLineModulatorAgingHighAlaPortn = _Pm1004vencAlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 224, 1, 6),
    _Pm1004vencAlmLineModulatorAgingHighAlaPortn_Type()
)
pm1004vencAlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pm1004vencAlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pm1004vencAlmLineAgingHighAlaPortn_Object = MibTableColumn
pm1004vencAlmLineAgingHighAlaPortn = _Pm1004vencAlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 224, 1, 7),
    _Pm1004vencAlmLineAgingHighAlaPortn_Type()
)
pm1004vencAlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineAgingHighAlaPortn.setStatus("current")
_Pm1004vencAlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pm1004vencAlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pm1004vencAlmLineFreqDevHighAlaPortn = _Pm1004vencAlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 224, 1, 13),
    _Pm1004vencAlmLineFreqDevHighAlaPortn_Type()
)
pm1004vencAlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineFreqDevHighAlaPortn.setStatus("current")
_Pm1004vencAlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pm1004vencAlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pm1004vencAlmLineLaserTempHighAlaPortn = _Pm1004vencAlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 2, 224, 1, 15),
    _Pm1004vencAlmLineLaserTempHighAlaPortn_Type()
)
pm1004vencAlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineLaserTempHighAlaPortn.setStatus("current")
_Pm1004vencAlmLineCrit_ObjectIdentity = ObjectIdentity
pm1004vencAlmLineCrit = _Pm1004vencAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3)
)
_Pm1004vencAlmsynthAlmLineTable_Object = MibTable
pm1004vencAlmsynthAlmLineTable = _Pm1004vencAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm1004vencAlmsynthAlmLineTable.setStatus("current")
_Pm1004vencAlmsynthAlmLineEntry_Object = MibTableRow
pm1004vencAlmsynthAlmLineEntry = _Pm1004vencAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1)
)
pm1004vencAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmsynthAlmLineEntry.setStatus("current")


class _Pm1004vencAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm1004vencAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmsynthAlmLineIndex_Object = MibTableColumn
pm1004vencAlmsynthAlmLineIndex = _Pm1004vencAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 1),
    _Pm1004vencAlmsynthAlmLineIndex_Type()
)
pm1004vencAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmsynthAlmLineIndex.setStatus("current")
_Pm1004vencAlmXfpAbsentPortn_Type = EkiOnOff
_Pm1004vencAlmXfpAbsentPortn_Object = MibTableColumn
pm1004vencAlmXfpAbsentPortn = _Pm1004vencAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 2),
    _Pm1004vencAlmXfpAbsentPortn_Type()
)
pm1004vencAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmXfpAbsentPortn.setStatus("current")
_Pm1004vencAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm1004vencAlmXfpInitNotComplPortn_Object = MibTableColumn
pm1004vencAlmXfpInitNotComplPortn = _Pm1004vencAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 3),
    _Pm1004vencAlmXfpInitNotComplPortn_Type()
)
pm1004vencAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmXfpInitNotComplPortn.setStatus("current")
_Pm1004vencAlmLineHwFailPortn_Type = EkiOnOff
_Pm1004vencAlmLineHwFailPortn_Object = MibTableColumn
pm1004vencAlmLineHwFailPortn = _Pm1004vencAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 5),
    _Pm1004vencAlmLineHwFailPortn_Type()
)
pm1004vencAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineHwFailPortn.setStatus("current")
_Pm1004vencAlmXfpTxOffPortn_Type = EkiOnOff
_Pm1004vencAlmXfpTxOffPortn_Object = MibTableColumn
pm1004vencAlmXfpTxOffPortn = _Pm1004vencAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 6),
    _Pm1004vencAlmXfpTxOffPortn_Type()
)
pm1004vencAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmXfpTxOffPortn.setStatus("current")
_Pm1004vencAlmLineLocalOosPortn_Type = EkiOnOff
_Pm1004vencAlmLineLocalOosPortn_Object = MibTableColumn
pm1004vencAlmLineLocalOosPortn = _Pm1004vencAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 7),
    _Pm1004vencAlmLineLocalOosPortn_Type()
)
pm1004vencAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineLocalOosPortn.setStatus("current")
_Pm1004vencAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm1004vencAlmLineDdmWarningPortn_Object = MibTableColumn
pm1004vencAlmLineDdmWarningPortn = _Pm1004vencAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 10),
    _Pm1004vencAlmLineDdmWarningPortn_Type()
)
pm1004vencAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineDdmWarningPortn.setStatus("current")
_Pm1004vencAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm1004vencAlmLineDdmAlmPortn_Object = MibTableColumn
pm1004vencAlmLineDdmAlmPortn = _Pm1004vencAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 11),
    _Pm1004vencAlmLineDdmAlmPortn_Type()
)
pm1004vencAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineDdmAlmPortn.setStatus("current")
_Pm1004vencAlmLineDdmCritPortn_Type = EkiOnOff
_Pm1004vencAlmLineDdmCritPortn_Object = MibTableColumn
pm1004vencAlmLineDdmCritPortn = _Pm1004vencAlmLineDdmCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 12),
    _Pm1004vencAlmLineDdmCritPortn_Type()
)
pm1004vencAlmLineDdmCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineDdmCritPortn.setStatus("current")
_Pm1004vencAlmLineFailPortn_Type = EkiOnOff
_Pm1004vencAlmLineFailPortn_Object = MibTableColumn
pm1004vencAlmLineFailPortn = _Pm1004vencAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 13),
    _Pm1004vencAlmLineFailPortn_Type()
)
pm1004vencAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineFailPortn.setStatus("current")
_Pm1004vencAlmLineActivePortn_Type = EkiOnOff
_Pm1004vencAlmLineActivePortn_Object = MibTableColumn
pm1004vencAlmLineActivePortn = _Pm1004vencAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 7, 1, 17),
    _Pm1004vencAlmLineActivePortn_Type()
)
pm1004vencAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineActivePortn.setStatus("current")
_Pm1004vencAlmdfrmAlmTable_Object = MibTable
pm1004vencAlmdfrmAlmTable = _Pm1004vencAlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm1004vencAlmdfrmAlmTable.setStatus("current")
_Pm1004vencAlmdfrmAlmEntry_Object = MibTableRow
pm1004vencAlmdfrmAlmEntry = _Pm1004vencAlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 128, 1)
)
pm1004vencAlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmdfrmAlmEntry.setStatus("current")


class _Pm1004vencAlmdfrmAlmIndex_Type(Integer32):
    """Custom type pm1004vencAlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmdfrmAlmIndex_Object = MibTableColumn
pm1004vencAlmdfrmAlmIndex = _Pm1004vencAlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 128, 1, 1),
    _Pm1004vencAlmdfrmAlmIndex_Type()
)
pm1004vencAlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmdfrmAlmIndex.setStatus("current")
_Pm1004vencAlmLineLossofsyncPortn_Type = EkiOnOff
_Pm1004vencAlmLineLossofsyncPortn_Object = MibTableColumn
pm1004vencAlmLineLossofsyncPortn = _Pm1004vencAlmLineLossofsyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 128, 1, 5),
    _Pm1004vencAlmLineLossofsyncPortn_Type()
)
pm1004vencAlmLineLossofsyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmLineLossofsyncPortn.setStatus("current")
_Pm1004vencAlmlineSyncAlarmsTable_Object = MibTable
pm1004vencAlmlineSyncAlarmsTable = _Pm1004vencAlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineSyncAlarmsTable.setStatus("current")
_Pm1004vencAlmlineSyncAlarmsEntry_Object = MibTableRow
pm1004vencAlmlineSyncAlarmsEntry = _Pm1004vencAlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 133, 1)
)
pm1004vencAlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineSyncAlarmsEntry.setStatus("current")


class _Pm1004vencAlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pm1004vencAlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmlineSyncAlarmsIndex_Object = MibTableColumn
pm1004vencAlmlineSyncAlarmsIndex = _Pm1004vencAlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 133, 1, 1),
    _Pm1004vencAlmlineSyncAlarmsIndex_Type()
)
pm1004vencAlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmlineSyncAlarmsIndex.setStatus("current")
_Pm1004vencAlmDwLockerrPortn_Type = EkiOnOff
_Pm1004vencAlmDwLockerrPortn_Object = MibTableColumn
pm1004vencAlmDwLockerrPortn = _Pm1004vencAlmDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 133, 1, 13),
    _Pm1004vencAlmDwLockerrPortn_Type()
)
pm1004vencAlmDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDwLockerrPortn.setStatus("current")
_Pm1004vencAlmUpLockerrPortn_Type = EkiOnOff
_Pm1004vencAlmUpLockerrPortn_Object = MibTableColumn
pm1004vencAlmUpLockerrPortn = _Pm1004vencAlmUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 133, 1, 14),
    _Pm1004vencAlmUpLockerrPortn_Type()
)
pm1004vencAlmUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmUpLockerrPortn.setStatus("current")
_Pm1004vencAlmDwLosPortn_Type = EkiOnOff
_Pm1004vencAlmDwLosPortn_Object = MibTableColumn
pm1004vencAlmDwLosPortn = _Pm1004vencAlmDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 133, 1, 17),
    _Pm1004vencAlmDwLosPortn_Type()
)
pm1004vencAlmDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmDwLosPortn.setStatus("current")
_Pm1004vencAlmlineXfp1AlarmsTable_Object = MibTable
pm1004vencAlmlineXfp1AlarmsTable = _Pm1004vencAlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1AlarmsTable.setStatus("current")
_Pm1004vencAlmlineXfp1AlarmsEntry_Object = MibTableRow
pm1004vencAlmlineXfp1AlarmsEntry = _Pm1004vencAlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1)
)
pm1004vencAlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencAlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1AlarmsEntry.setStatus("current")


class _Pm1004vencAlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pm1004vencAlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencAlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pm1004vencAlmlineXfp1AlarmsIndex_Object = MibTableColumn
pm1004vencAlmlineXfp1AlarmsIndex = _Pm1004vencAlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 1),
    _Pm1004vencAlmlineXfp1AlarmsIndex_Type()
)
pm1004vencAlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmlineXfp1AlarmsIndex.setStatus("current")
_Pm1004vencAlmModNrPortn_Type = EkiOnOff
_Pm1004vencAlmModNrPortn_Object = MibTableColumn
pm1004vencAlmModNrPortn = _Pm1004vencAlmModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 3),
    _Pm1004vencAlmModNrPortn_Type()
)
pm1004vencAlmModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmModNrPortn.setStatus("current")
_Pm1004vencAlmRxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004vencAlmRxCdrNotLockedPortn_Object = MibTableColumn
pm1004vencAlmRxCdrNotLockedPortn = _Pm1004vencAlmRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 4),
    _Pm1004vencAlmRxCdrNotLockedPortn_Type()
)
pm1004vencAlmRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmRxCdrNotLockedPortn.setStatus("current")
_Pm1004vencAlmRxNrPortn_Type = EkiOnOff
_Pm1004vencAlmRxNrPortn_Object = MibTableColumn
pm1004vencAlmRxNrPortn = _Pm1004vencAlmRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 6),
    _Pm1004vencAlmRxNrPortn_Type()
)
pm1004vencAlmRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmRxNrPortn.setStatus("current")
_Pm1004vencAlmTxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004vencAlmTxCdrNotLockedPortn_Object = MibTableColumn
pm1004vencAlmTxCdrNotLockedPortn = _Pm1004vencAlmTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 7),
    _Pm1004vencAlmTxCdrNotLockedPortn_Type()
)
pm1004vencAlmTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxCdrNotLockedPortn.setStatus("current")
_Pm1004vencAlmTxFaultPortn_Type = EkiOnOff
_Pm1004vencAlmTxFaultPortn_Object = MibTableColumn
pm1004vencAlmTxFaultPortn = _Pm1004vencAlmTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 8),
    _Pm1004vencAlmTxFaultPortn_Type()
)
pm1004vencAlmTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxFaultPortn.setStatus("current")
_Pm1004vencAlmTxNrPortn_Type = EkiOnOff
_Pm1004vencAlmTxNrPortn_Object = MibTableColumn
pm1004vencAlmTxNrPortn = _Pm1004vencAlmTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 9),
    _Pm1004vencAlmTxNrPortn_Type()
)
pm1004vencAlmTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTxNrPortn.setStatus("current")
_Pm1004vencAlmWavelengthUnlockedPortn_Type = EkiOnOff
_Pm1004vencAlmWavelengthUnlockedPortn_Object = MibTableColumn
pm1004vencAlmWavelengthUnlockedPortn = _Pm1004vencAlmWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 15),
    _Pm1004vencAlmWavelengthUnlockedPortn_Type()
)
pm1004vencAlmWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmWavelengthUnlockedPortn.setStatus("current")
_Pm1004vencAlmTecFaultPortn_Type = EkiOnOff
_Pm1004vencAlmTecFaultPortn_Object = MibTableColumn
pm1004vencAlmTecFaultPortn = _Pm1004vencAlmTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 16),
    _Pm1004vencAlmTecFaultPortn_Type()
)
pm1004vencAlmTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmTecFaultPortn.setStatus("current")
_Pm1004vencAlmApdSupplyFaultPortn_Type = EkiOnOff
_Pm1004vencAlmApdSupplyFaultPortn_Object = MibTableColumn
pm1004vencAlmApdSupplyFaultPortn = _Pm1004vencAlmApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 2, 3, 3, 211, 1, 17),
    _Pm1004vencAlmApdSupplyFaultPortn_Type()
)
pm1004vencAlmApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencAlmApdSupplyFaultPortn.setStatus("current")
_Pm1004vencmeasures_ObjectIdentity = ObjectIdentity
pm1004vencmeasures = _Pm1004vencmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3)
)
_Pm1004vencMesrOther_ObjectIdentity = ObjectIdentity
pm1004vencMesrOther = _Pm1004vencMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 1)
)
_Pm1004vencMesrsynth0_Type = EkiMeasureType
_Pm1004vencMesrsynth0_Object = MibScalar
pm1004vencMesrsynth0 = _Pm1004vencMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 1, 0),
    _Pm1004vencMesrsynth0_Type()
)
pm1004vencMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrsynth0.setStatus("deprecated")
_Pm1004vencMesrsynth1_Type = EkiMeasureType
_Pm1004vencMesrsynth1_Object = MibScalar
pm1004vencMesrsynth1 = _Pm1004vencMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 1, 1),
    _Pm1004vencMesrsynth1_Type()
)
pm1004vencMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrsynth1.setStatus("deprecated")
_Pm1004vencMesrClient_ObjectIdentity = ObjectIdentity
pm1004vencMesrClient = _Pm1004vencMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 2)
)
_Pm1004vencMesrLine_ObjectIdentity = ObjectIdentity
pm1004vencMesrLine = _Pm1004vencMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3)
)
_Pm1004vencMesrxfp1LxModTempMeasTable_Object = MibTable
pm1004vencMesrxfp1LxModTempMeasTable = _Pm1004vencMesrxfp1LxModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxModTempMeasTable.setStatus("current")
_Pm1004vencMesrxfp1LxModTempMeasEntry_Object = MibTableRow
pm1004vencMesrxfp1LxModTempMeasEntry = _Pm1004vencMesrxfp1LxModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 208, 1)
)
pm1004vencMesrxfp1LxModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrxfp1LxModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxModTempMeasEntry.setStatus("current")


class _Pm1004vencMesrxfp1LxModTempMeasIndex_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LxModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrxfp1LxModTempMeasIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LxModTempMeasIndex_Object = MibTableColumn
pm1004vencMesrxfp1LxModTempMeasIndex = _Pm1004vencMesrxfp1LxModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 208, 1, 1),
    _Pm1004vencMesrxfp1LxModTempMeasIndex_Type()
)
pm1004vencMesrxfp1LxModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxModTempMeasIndex.setStatus("current")


class _Pm1004vencMesrxfp1LxModTempMeasPortn_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LxModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrxfp1LxModTempMeasPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LxModTempMeasPortn_Object = MibTableColumn
pm1004vencMesrxfp1LxModTempMeasPortn = _Pm1004vencMesrxfp1LxModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 208, 1, 2),
    _Pm1004vencMesrxfp1LxModTempMeasPortn_Type()
)
pm1004vencMesrxfp1LxModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxModTempMeasPortn.setStatus("current")
_Pm1004vencMesrxfp1ReservedTable_Object = MibTable
pm1004vencMesrxfp1ReservedTable = _Pm1004vencMesrxfp1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1ReservedTable.setStatus("deprecated")
_Pm1004vencMesrxfp1ReservedEntry_Object = MibTableRow
pm1004vencMesrxfp1ReservedEntry = _Pm1004vencMesrxfp1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 209, 1)
)
pm1004vencMesrxfp1ReservedEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrxfp1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1ReservedEntry.setStatus("deprecated")


class _Pm1004vencMesrxfp1ReservedIndex_Type(Integer32):
    """Custom type pm1004vencMesrxfp1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrxfp1ReservedIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1ReservedIndex_Object = MibTableColumn
pm1004vencMesrxfp1ReservedIndex = _Pm1004vencMesrxfp1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 209, 1, 1),
    _Pm1004vencMesrxfp1ReservedIndex_Type()
)
pm1004vencMesrxfp1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1ReservedIndex.setStatus("deprecated")


class _Pm1004vencMesrxfp1ReservedPortn_Type(Integer32):
    """Custom type pm1004vencMesrxfp1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrxfp1ReservedPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1ReservedPortn_Object = MibTableColumn
pm1004vencMesrxfp1ReservedPortn = _Pm1004vencMesrxfp1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 209, 1, 2),
    _Pm1004vencMesrxfp1ReservedPortn_Type()
)
pm1004vencMesrxfp1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1ReservedPortn.setStatus("deprecated")
_Pm1004vencMesrxfp1LoBiasCurrentMeasTable_Object = MibTable
pm1004vencMesrxfp1LoBiasCurrentMeasTable = _Pm1004vencMesrxfp1LoBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LoBiasCurrentMeasTable.setStatus("current")
_Pm1004vencMesrxfp1LoBiasCurrentMeasEntry_Object = MibTableRow
pm1004vencMesrxfp1LoBiasCurrentMeasEntry = _Pm1004vencMesrxfp1LoBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 210, 1)
)
pm1004vencMesrxfp1LoBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrxfp1LoBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LoBiasCurrentMeasEntry.setStatus("current")


class _Pm1004vencMesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LoBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrxfp1LoBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LoBiasCurrentMeasIndex_Object = MibTableColumn
pm1004vencMesrxfp1LoBiasCurrentMeasIndex = _Pm1004vencMesrxfp1LoBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 210, 1, 1),
    _Pm1004vencMesrxfp1LoBiasCurrentMeasIndex_Type()
)
pm1004vencMesrxfp1LoBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LoBiasCurrentMeasIndex.setStatus("current")


class _Pm1004vencMesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LoBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrxfp1LoBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LoBiasCurrentMeasPortn_Object = MibTableColumn
pm1004vencMesrxfp1LoBiasCurrentMeasPortn = _Pm1004vencMesrxfp1LoBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 210, 1, 2),
    _Pm1004vencMesrxfp1LoBiasCurrentMeasPortn_Type()
)
pm1004vencMesrxfp1LoBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LoBiasCurrentMeasPortn.setStatus("current")
_Pm1004vencMesrxfp1LoTxPowerMeasTable_Object = MibTable
pm1004vencMesrxfp1LoTxPowerMeasTable = _Pm1004vencMesrxfp1LoTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LoTxPowerMeasTable.setStatus("current")
_Pm1004vencMesrxfp1LoTxPowerMeasEntry_Object = MibTableRow
pm1004vencMesrxfp1LoTxPowerMeasEntry = _Pm1004vencMesrxfp1LoTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 211, 1)
)
pm1004vencMesrxfp1LoTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrxfp1LoTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LoTxPowerMeasEntry.setStatus("current")


class _Pm1004vencMesrxfp1LoTxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LoTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrxfp1LoTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LoTxPowerMeasIndex_Object = MibTableColumn
pm1004vencMesrxfp1LoTxPowerMeasIndex = _Pm1004vencMesrxfp1LoTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 211, 1, 1),
    _Pm1004vencMesrxfp1LoTxPowerMeasIndex_Type()
)
pm1004vencMesrxfp1LoTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LoTxPowerMeasIndex.setStatus("current")


class _Pm1004vencMesrxfp1LoTxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LoTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrxfp1LoTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LoTxPowerMeasPortn_Object = MibTableColumn
pm1004vencMesrxfp1LoTxPowerMeasPortn = _Pm1004vencMesrxfp1LoTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 211, 1, 2),
    _Pm1004vencMesrxfp1LoTxPowerMeasPortn_Type()
)
pm1004vencMesrxfp1LoTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LoTxPowerMeasPortn.setStatus("current")
_Pm1004vencMesrxfp1LiRxPowerMeasTable_Object = MibTable
pm1004vencMesrxfp1LiRxPowerMeasTable = _Pm1004vencMesrxfp1LiRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LiRxPowerMeasTable.setStatus("current")
_Pm1004vencMesrxfp1LiRxPowerMeasEntry_Object = MibTableRow
pm1004vencMesrxfp1LiRxPowerMeasEntry = _Pm1004vencMesrxfp1LiRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 212, 1)
)
pm1004vencMesrxfp1LiRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrxfp1LiRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LiRxPowerMeasEntry.setStatus("current")


class _Pm1004vencMesrxfp1LiRxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LiRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrxfp1LiRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LiRxPowerMeasIndex_Object = MibTableColumn
pm1004vencMesrxfp1LiRxPowerMeasIndex = _Pm1004vencMesrxfp1LiRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 212, 1, 1),
    _Pm1004vencMesrxfp1LiRxPowerMeasIndex_Type()
)
pm1004vencMesrxfp1LiRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LiRxPowerMeasIndex.setStatus("current")


class _Pm1004vencMesrxfp1LiRxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LiRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrxfp1LiRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LiRxPowerMeasPortn_Object = MibTableColumn
pm1004vencMesrxfp1LiRxPowerMeasPortn = _Pm1004vencMesrxfp1LiRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 212, 1, 2),
    _Pm1004vencMesrxfp1LiRxPowerMeasPortn_Type()
)
pm1004vencMesrxfp1LiRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LiRxPowerMeasPortn.setStatus("current")
_Pm1004vencMesrxfp1LxAux1MeasTable_Object = MibTable
pm1004vencMesrxfp1LxAux1MeasTable = _Pm1004vencMesrxfp1LxAux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxAux1MeasTable.setStatus("deprecated")
_Pm1004vencMesrxfp1LxAux1MeasEntry_Object = MibTableRow
pm1004vencMesrxfp1LxAux1MeasEntry = _Pm1004vencMesrxfp1LxAux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 213, 1)
)
pm1004vencMesrxfp1LxAux1MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrxfp1LxAux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxAux1MeasEntry.setStatus("deprecated")


class _Pm1004vencMesrxfp1LxAux1MeasIndex_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LxAux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrxfp1LxAux1MeasIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LxAux1MeasIndex_Object = MibTableColumn
pm1004vencMesrxfp1LxAux1MeasIndex = _Pm1004vencMesrxfp1LxAux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 213, 1, 1),
    _Pm1004vencMesrxfp1LxAux1MeasIndex_Type()
)
pm1004vencMesrxfp1LxAux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxAux1MeasIndex.setStatus("deprecated")


class _Pm1004vencMesrxfp1LxAux1MeasPortn_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LxAux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrxfp1LxAux1MeasPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LxAux1MeasPortn_Object = MibTableColumn
pm1004vencMesrxfp1LxAux1MeasPortn = _Pm1004vencMesrxfp1LxAux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 213, 1, 2),
    _Pm1004vencMesrxfp1LxAux1MeasPortn_Type()
)
pm1004vencMesrxfp1LxAux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxAux1MeasPortn.setStatus("deprecated")
_Pm1004vencMesrxfp1LxAux2MeasTable_Object = MibTable
pm1004vencMesrxfp1LxAux2MeasTable = _Pm1004vencMesrxfp1LxAux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxAux2MeasTable.setStatus("deprecated")
_Pm1004vencMesrxfp1LxAux2MeasEntry_Object = MibTableRow
pm1004vencMesrxfp1LxAux2MeasEntry = _Pm1004vencMesrxfp1LxAux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 214, 1)
)
pm1004vencMesrxfp1LxAux2MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrxfp1LxAux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxAux2MeasEntry.setStatus("deprecated")


class _Pm1004vencMesrxfp1LxAux2MeasIndex_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LxAux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrxfp1LxAux2MeasIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LxAux2MeasIndex_Object = MibTableColumn
pm1004vencMesrxfp1LxAux2MeasIndex = _Pm1004vencMesrxfp1LxAux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 214, 1, 1),
    _Pm1004vencMesrxfp1LxAux2MeasIndex_Type()
)
pm1004vencMesrxfp1LxAux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxAux2MeasIndex.setStatus("deprecated")


class _Pm1004vencMesrxfp1LxAux2MeasPortn_Type(Integer32):
    """Custom type pm1004vencMesrxfp1LxAux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrxfp1LxAux2MeasPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrxfp1LxAux2MeasPortn_Object = MibTableColumn
pm1004vencMesrxfp1LxAux2MeasPortn = _Pm1004vencMesrxfp1LxAux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 214, 1, 2),
    _Pm1004vencMesrxfp1LxAux2MeasPortn_Type()
)
pm1004vencMesrxfp1LxAux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrxfp1LxAux2MeasPortn.setStatus("deprecated")
_Pm1004vencMesrotx1AgingTable_Object = MibTable
pm1004vencMesrotx1AgingTable = _Pm1004vencMesrotx1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pm1004vencMesrotx1AgingTable.setStatus("current")
_Pm1004vencMesrotx1AgingEntry_Object = MibTableRow
pm1004vencMesrotx1AgingEntry = _Pm1004vencMesrotx1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 224, 1)
)
pm1004vencMesrotx1AgingEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrotx1AgingIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrotx1AgingEntry.setStatus("current")


class _Pm1004vencMesrotx1AgingIndex_Type(Integer32):
    """Custom type pm1004vencMesrotx1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrotx1AgingIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrotx1AgingIndex_Object = MibTableColumn
pm1004vencMesrotx1AgingIndex = _Pm1004vencMesrotx1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 224, 1, 1),
    _Pm1004vencMesrotx1AgingIndex_Type()
)
pm1004vencMesrotx1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrotx1AgingIndex.setStatus("current")


class _Pm1004vencMesrotx1AgingPortn_Type(Integer32):
    """Custom type pm1004vencMesrotx1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrotx1AgingPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrotx1AgingPortn_Object = MibTableColumn
pm1004vencMesrotx1AgingPortn = _Pm1004vencMesrotx1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 224, 1, 2),
    _Pm1004vencMesrotx1AgingPortn_Type()
)
pm1004vencMesrotx1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrotx1AgingPortn.setStatus("current")
_Pm1004vencMesrotx1LaserTemperatureTable_Object = MibTable
pm1004vencMesrotx1LaserTemperatureTable = _Pm1004vencMesrotx1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pm1004vencMesrotx1LaserTemperatureTable.setStatus("deprecated")
_Pm1004vencMesrotx1LaserTemperatureEntry_Object = MibTableRow
pm1004vencMesrotx1LaserTemperatureEntry = _Pm1004vencMesrotx1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 225, 1)
)
pm1004vencMesrotx1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrotx1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrotx1LaserTemperatureEntry.setStatus("deprecated")


class _Pm1004vencMesrotx1LaserTemperatureIndex_Type(Integer32):
    """Custom type pm1004vencMesrotx1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrotx1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrotx1LaserTemperatureIndex_Object = MibTableColumn
pm1004vencMesrotx1LaserTemperatureIndex = _Pm1004vencMesrotx1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 225, 1, 1),
    _Pm1004vencMesrotx1LaserTemperatureIndex_Type()
)
pm1004vencMesrotx1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrotx1LaserTemperatureIndex.setStatus("deprecated")


class _Pm1004vencMesrotx1LaserTemperaturePortn_Type(Integer32):
    """Custom type pm1004vencMesrotx1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrotx1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pm1004vencMesrotx1LaserTemperaturePortn_Object = MibTableColumn
pm1004vencMesrotx1LaserTemperaturePortn = _Pm1004vencMesrotx1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 225, 1, 2),
    _Pm1004vencMesrotx1LaserTemperaturePortn_Type()
)
pm1004vencMesrotx1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrotx1LaserTemperaturePortn.setStatus("deprecated")
_Pm1004vencMesrotx1FreqDeviationTable_Object = MibTable
pm1004vencMesrotx1FreqDeviationTable = _Pm1004vencMesrotx1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pm1004vencMesrotx1FreqDeviationTable.setStatus("current")
_Pm1004vencMesrotx1FreqDeviationEntry_Object = MibTableRow
pm1004vencMesrotx1FreqDeviationEntry = _Pm1004vencMesrotx1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 226, 1)
)
pm1004vencMesrotx1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrotx1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrotx1FreqDeviationEntry.setStatus("current")


class _Pm1004vencMesrotx1FreqDeviationIndex_Type(Integer32):
    """Custom type pm1004vencMesrotx1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrotx1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrotx1FreqDeviationIndex_Object = MibTableColumn
pm1004vencMesrotx1FreqDeviationIndex = _Pm1004vencMesrotx1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 226, 1, 1),
    _Pm1004vencMesrotx1FreqDeviationIndex_Type()
)
pm1004vencMesrotx1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrotx1FreqDeviationIndex.setStatus("current")


class _Pm1004vencMesrotx1FreqDeviationPortn_Type(Integer32):
    """Custom type pm1004vencMesrotx1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrotx1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrotx1FreqDeviationPortn_Object = MibTableColumn
pm1004vencMesrotx1FreqDeviationPortn = _Pm1004vencMesrotx1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 226, 1, 2),
    _Pm1004vencMesrotx1FreqDeviationPortn_Type()
)
pm1004vencMesrotx1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrotx1FreqDeviationPortn.setStatus("current")
_Pm1004vencMesrotx1LaserWvlengthTable_Object = MibTable
pm1004vencMesrotx1LaserWvlengthTable = _Pm1004vencMesrotx1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pm1004vencMesrotx1LaserWvlengthTable.setStatus("current")
_Pm1004vencMesrotx1LaserWvlengthEntry_Object = MibTableRow
pm1004vencMesrotx1LaserWvlengthEntry = _Pm1004vencMesrotx1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 227, 1)
)
pm1004vencMesrotx1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMesrotx1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMesrotx1LaserWvlengthEntry.setStatus("current")


class _Pm1004vencMesrotx1LaserWvlengthIndex_Type(Integer32):
    """Custom type pm1004vencMesrotx1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMesrotx1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pm1004vencMesrotx1LaserWvlengthIndex_Object = MibTableColumn
pm1004vencMesrotx1LaserWvlengthIndex = _Pm1004vencMesrotx1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 227, 1, 1),
    _Pm1004vencMesrotx1LaserWvlengthIndex_Type()
)
pm1004vencMesrotx1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrotx1LaserWvlengthIndex.setStatus("current")


class _Pm1004vencMesrotx1LaserWvlengthPortn_Type(Integer32):
    """Custom type pm1004vencMesrotx1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vencMesrotx1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pm1004vencMesrotx1LaserWvlengthPortn_Object = MibTableColumn
pm1004vencMesrotx1LaserWvlengthPortn = _Pm1004vencMesrotx1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 3, 3, 227, 1, 2),
    _Pm1004vencMesrotx1LaserWvlengthPortn_Type()
)
pm1004vencMesrotx1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMesrotx1LaserWvlengthPortn.setStatus("current")
_Pm1004venccounters_ObjectIdentity = ObjectIdentity
pm1004venccounters = _Pm1004venccounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4)
)
_Pm1004vencCntOther_ObjectIdentity = ObjectIdentity
pm1004vencCntOther = _Pm1004vencCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 1)
)
_Pm1004vencCntClient_ObjectIdentity = ObjectIdentity
pm1004vencCntClient = _Pm1004vencCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 2)
)
_Pm1004vencCntLine_ObjectIdentity = ObjectIdentity
pm1004vencCntLine = _Pm1004vencCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3)
)
_Pm1004vencCntdfrmB1ErrCntTable_Object = MibTable
pm1004vencCntdfrmB1ErrCntTable = _Pm1004vencCntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm1004vencCntdfrmB1ErrCntTable.setStatus("current")
_Pm1004vencCntdfrmB1ErrCntEntry_Object = MibTableRow
pm1004vencCntdfrmB1ErrCntEntry = _Pm1004vencCntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 152, 1)
)
pm1004vencCntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCntdfrmB1ErrCntEntry.setStatus("current")


class _Pm1004vencCntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm1004vencCntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm1004vencCntdfrmB1ErrCntIndex_Object = MibTableColumn
pm1004vencCntdfrmB1ErrCntIndex = _Pm1004vencCntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 152, 1, 1),
    _Pm1004vencCntdfrmB1ErrCntIndex_Type()
)
pm1004vencCntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCntdfrmB1ErrCntIndex.setStatus("current")
_Pm1004vencCntdfrmB1ErrCntValuePortn_Type = Counter32
_Pm1004vencCntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pm1004vencCntdfrmB1ErrCntValuePortn = _Pm1004vencCntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 152, 1, 2),
    _Pm1004vencCntdfrmB1ErrCntValuePortn_Type()
)
pm1004vencCntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCntdfrmB1ErrCntValuePortn.setStatus("current")
_Pm1004vencCntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm1004vencCntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm1004vencCntdfrmB1ErrCntErrorPortn = _Pm1004vencCntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 152, 1, 3),
    _Pm1004vencCntdfrmB1ErrCntErrorPortn_Type()
)
pm1004vencCntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pm1004vencCntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm1004vencCntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm1004vencCntdfrmB1ErrCntOverloadPortn = _Pm1004vencCntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 152, 1, 4),
    _Pm1004vencCntdfrmB1ErrCntOverloadPortn_Type()
)
pm1004vencCntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm1004vencCntdfrmTimCntTable_Object = MibTable
pm1004vencCntdfrmTimCntTable = _Pm1004vencCntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm1004vencCntdfrmTimCntTable.setStatus("current")
_Pm1004vencCntdfrmTimCntEntry_Object = MibTableRow
pm1004vencCntdfrmTimCntEntry = _Pm1004vencCntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 153, 1)
)
pm1004vencCntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCntdfrmTimCntEntry.setStatus("current")


class _Pm1004vencCntdfrmTimCntIndex_Type(Integer32):
    """Custom type pm1004vencCntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm1004vencCntdfrmTimCntIndex_Object = MibTableColumn
pm1004vencCntdfrmTimCntIndex = _Pm1004vencCntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 153, 1, 1),
    _Pm1004vencCntdfrmTimCntIndex_Type()
)
pm1004vencCntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCntdfrmTimCntIndex.setStatus("current")
_Pm1004vencCntdfrmTimCntValuePortn_Type = Counter32
_Pm1004vencCntdfrmTimCntValuePortn_Object = MibTableColumn
pm1004vencCntdfrmTimCntValuePortn = _Pm1004vencCntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 153, 1, 2),
    _Pm1004vencCntdfrmTimCntValuePortn_Type()
)
pm1004vencCntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCntdfrmTimCntValuePortn.setStatus("current")
_Pm1004vencCntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pm1004vencCntdfrmTimCntErrorPortn_Object = MibTableColumn
pm1004vencCntdfrmTimCntErrorPortn = _Pm1004vencCntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 153, 1, 3),
    _Pm1004vencCntdfrmTimCntErrorPortn_Type()
)
pm1004vencCntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCntdfrmTimCntErrorPortn.setStatus("current")
_Pm1004vencCntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm1004vencCntdfrmTimCntOverloadPortn_Object = MibTableColumn
pm1004vencCntdfrmTimCntOverloadPortn = _Pm1004vencCntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 3, 153, 1, 4),
    _Pm1004vencCntdfrmTimCntOverloadPortn_Type()
)
pm1004vencCntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCntdfrmTimCntOverloadPortn.setStatus("current")
_Pm1004vencCntCountersReset_Type = EkiOnOff
_Pm1004vencCntCountersReset_Object = MibScalar
pm1004vencCntCountersReset = _Pm1004vencCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 259),
    _Pm1004vencCntCountersReset_Type()
)
pm1004vencCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCntCountersReset.setStatus("current")
_Pm1004vencCntCountersStop_Type = EkiOnOff
_Pm1004vencCntCountersStop_Object = MibScalar
pm1004vencCntCountersStop = _Pm1004vencCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 4, 260),
    _Pm1004vencCntCountersStop_Type()
)
pm1004vencCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCntCountersStop.setStatus("current")
_Pm1004venccontrolsWrite_ObjectIdentity = ObjectIdentity
pm1004venccontrolsWrite = _Pm1004venccontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6)
)
_Pm1004vencCtrlOther_ObjectIdentity = ObjectIdentity
pm1004vencCtrlOther = _Pm1004vencCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1)
)
_Pm1004vencCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm1004vencCtrlconfMgnt1 = _Pm1004vencCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 1)
)
_Pm1004vencCtrlConf1Load1_Type = EkiOnOff
_Pm1004vencCtrlConf1Load1_Object = MibScalar
pm1004vencCtrlConf1Load1 = _Pm1004vencCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 1, 1),
    _Pm1004vencCtrlConf1Load1_Type()
)
pm1004vencCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlConf1Load1.setStatus("current")
_Pm1004vencCtrlConf2Load1_Type = EkiOnOff
_Pm1004vencCtrlConf2Load1_Object = MibScalar
pm1004vencCtrlConf2Load1 = _Pm1004vencCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 1, 2),
    _Pm1004vencCtrlConf2Load1_Type()
)
pm1004vencCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlConf2Load1.setStatus("current")
_Pm1004vencCtrlConf2Flash1_Type = EkiOnOff
_Pm1004vencCtrlConf2Flash1_Object = MibScalar
pm1004vencCtrlConf2Flash1 = _Pm1004vencCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 1, 10),
    _Pm1004vencCtrlConf2Flash1_Type()
)
pm1004vencCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlConf2Flash1.setStatus("current")
_Pm1004vencCtrlConf2Clear1_Type = EkiOnOff
_Pm1004vencCtrlConf2Clear1_Object = MibScalar
pm1004vencCtrlConf2Clear1 = _Pm1004vencCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 1, 14),
    _Pm1004vencCtrlConf2Clear1_Type()
)
pm1004vencCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlConf2Clear1.setStatus("current")
_Pm1004vencCtrlsynth4_ObjectIdentity = ObjectIdentity
pm1004vencCtrlsynth4 = _Pm1004vencCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 4)
)
_Pm1004vencCtrlCorrelatOn_Type = EkiOnOff
_Pm1004vencCtrlCorrelatOn_Object = MibScalar
pm1004vencCtrlCorrelatOn = _Pm1004vencCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 4, 1),
    _Pm1004vencCtrlCorrelatOn_Type()
)
pm1004vencCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlCorrelatOn.setStatus("current")
_Pm1004vencCtrlCorrelatOff_Type = EkiOnOff
_Pm1004vencCtrlCorrelatOff_Object = MibScalar
pm1004vencCtrlCorrelatOff = _Pm1004vencCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 4, 2),
    _Pm1004vencCtrlCorrelatOff_Type()
)
pm1004vencCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlCorrelatOff.setStatus("current")
_Pm1004vencCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1004vencCtrlswMgnt = _Pm1004vencCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 5)
)
_Pm1004vencCtrlColdReset_Type = EkiOnOff
_Pm1004vencCtrlColdReset_Object = MibScalar
pm1004vencCtrlColdReset = _Pm1004vencCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 5, 2),
    _Pm1004vencCtrlColdReset_Type()
)
pm1004vencCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlColdReset.setStatus("current")
_Pm1004vencCtrlWarmReset_Type = EkiOnOff
_Pm1004vencCtrlWarmReset_Object = MibScalar
pm1004vencCtrlWarmReset = _Pm1004vencCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 5, 3),
    _Pm1004vencCtrlWarmReset_Type()
)
pm1004vencCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlWarmReset.setStatus("current")
_Pm1004vencCtrlLoadSwBank1_Type = EkiOnOff
_Pm1004vencCtrlLoadSwBank1_Object = MibScalar
pm1004vencCtrlLoadSwBank1 = _Pm1004vencCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 5, 5),
    _Pm1004vencCtrlLoadSwBank1_Type()
)
pm1004vencCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlLoadSwBank1.setStatus("current")
_Pm1004vencCtrlLoadSwBank2_Type = EkiOnOff
_Pm1004vencCtrlLoadSwBank2_Object = MibScalar
pm1004vencCtrlLoadSwBank2 = _Pm1004vencCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 5, 6),
    _Pm1004vencCtrlLoadSwBank2_Type()
)
pm1004vencCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlLoadSwBank2.setStatus("current")
_Pm1004vencCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm1004vencCtrlgwMgnt = _Pm1004vencCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 6)
)
_Pm1004vencCtrlCurrentGwReset_Type = EkiOnOff
_Pm1004vencCtrlCurrentGwReset_Object = MibScalar
pm1004vencCtrlCurrentGwReset = _Pm1004vencCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 6, 1),
    _Pm1004vencCtrlCurrentGwReset_Type()
)
pm1004vencCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlCurrentGwReset.setStatus("current")
_Pm1004vencCtrlLoadGwBank1_Type = EkiOnOff
_Pm1004vencCtrlLoadGwBank1_Object = MibScalar
pm1004vencCtrlLoadGwBank1 = _Pm1004vencCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 6, 5),
    _Pm1004vencCtrlLoadGwBank1_Type()
)
pm1004vencCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlLoadGwBank1.setStatus("current")
_Pm1004vencCtrlLoadGwBank2_Type = EkiOnOff
_Pm1004vencCtrlLoadGwBank2_Object = MibScalar
pm1004vencCtrlLoadGwBank2 = _Pm1004vencCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 6, 6),
    _Pm1004vencCtrlLoadGwBank2_Type()
)
pm1004vencCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlLoadGwBank2.setStatus("current")
_Pm1004vencCtrlLoadGwBank3_Type = EkiOnOff
_Pm1004vencCtrlLoadGwBank3_Object = MibScalar
pm1004vencCtrlLoadGwBank3 = _Pm1004vencCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 6, 7),
    _Pm1004vencCtrlLoadGwBank3_Type()
)
pm1004vencCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlLoadGwBank3.setStatus("current")
_Pm1004vencCtrlLoadGwBank4_Type = EkiOnOff
_Pm1004vencCtrlLoadGwBank4_Object = MibScalar
pm1004vencCtrlLoadGwBank4 = _Pm1004vencCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 6, 8),
    _Pm1004vencCtrlLoadGwBank4_Type()
)
pm1004vencCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlLoadGwBank4.setStatus("current")
_Pm1004vencCtrlledTest_ObjectIdentity = ObjectIdentity
pm1004vencCtrlledTest = _Pm1004vencCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 192)
)
_Pm1004vencCtrlGreenLed_Type = EkiOnOff
_Pm1004vencCtrlGreenLed_Object = MibScalar
pm1004vencCtrlGreenLed = _Pm1004vencCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 192, 1),
    _Pm1004vencCtrlGreenLed_Type()
)
pm1004vencCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlGreenLed.setStatus("current")
_Pm1004vencCtrlRedLed_Type = EkiOnOff
_Pm1004vencCtrlRedLed_Object = MibScalar
pm1004vencCtrlRedLed = _Pm1004vencCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 192, 2),
    _Pm1004vencCtrlRedLed_Type()
)
pm1004vencCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlRedLed.setStatus("current")
_Pm1004vencCtrlLedOff_Type = EkiOnOff
_Pm1004vencCtrlLedOff_Object = MibScalar
pm1004vencCtrlLedOff = _Pm1004vencCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 192, 3),
    _Pm1004vencCtrlLedOff_Type()
)
pm1004vencCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlLedOff.setStatus("current")
_Pm1004vencCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm1004vencCtrlmoduleOosMode = _Pm1004vencCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 193)
)
_Pm1004vencCtrlModuleOosMode_Type = EkiOnOff
_Pm1004vencCtrlModuleOosMode_Object = MibScalar
pm1004vencCtrlModuleOosMode = _Pm1004vencCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 193, 1),
    _Pm1004vencCtrlModuleOosMode_Type()
)
pm1004vencCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlModuleOosMode.setStatus("current")
_Pm1004vencCtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm1004vencCtrlmaintenanceMode = _Pm1004vencCtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 197)
)
_Pm1004vencCtrlMaintenanceMode_Type = EkiOnOff
_Pm1004vencCtrlMaintenanceMode_Object = MibScalar
pm1004vencCtrlMaintenanceMode = _Pm1004vencCtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 197, 1),
    _Pm1004vencCtrlMaintenanceMode_Type()
)
pm1004vencCtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlMaintenanceMode.setStatus("current")
_Pm1004vencCtrlencryptionSelect_Type = Pm1004vencKeyMode
_Pm1004vencCtrlencryptionSelect_Object = MibScalar
pm1004vencCtrlencryptionSelect = _Pm1004vencCtrlencryptionSelect_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 1, 200),
    _Pm1004vencCtrlencryptionSelect_Type()
)
pm1004vencCtrlencryptionSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlencryptionSelect.setStatus("current")
_Pm1004vencCtrlClient_ObjectIdentity = ObjectIdentity
pm1004vencCtrlClient = _Pm1004vencCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2)
)
_Pm1004vencCtrlaccessLoopTable_Object = MibTable
pm1004vencCtrlaccessLoopTable = _Pm1004vencCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlaccessLoopTable.setStatus("current")
_Pm1004vencCtrlaccessLoopEntry_Object = MibTableRow
pm1004vencCtrlaccessLoopEntry = _Pm1004vencCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 16, 1)
)
pm1004vencCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlaccessLoopEntry.setStatus("current")


class _Pm1004vencCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm1004vencCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlaccessLoopIndex_Object = MibTableColumn
pm1004vencCtrlaccessLoopIndex = _Pm1004vencCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 16, 1, 1),
    _Pm1004vencCtrlaccessLoopIndex_Type()
)
pm1004vencCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlaccessLoopIndex.setStatus("current")
_Pm1004vencCtrlaccessLoopPortn_Type = EkiState
_Pm1004vencCtrlaccessLoopPortn_Object = MibTableColumn
pm1004vencCtrlaccessLoopPortn = _Pm1004vencCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 16, 1, 2),
    _Pm1004vencCtrlaccessLoopPortn_Type()
)
pm1004vencCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlaccessLoopPortn.setStatus("current")
_Pm1004vencCtrlportOosModeTable_Object = MibTable
pm1004vencCtrlportOosModeTable = _Pm1004vencCtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlportOosModeTable.setStatus("current")
_Pm1004vencCtrlportOosModeEntry_Object = MibTableRow
pm1004vencCtrlportOosModeEntry = _Pm1004vencCtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 18, 1)
)
pm1004vencCtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlportOosModeEntry.setStatus("current")


class _Pm1004vencCtrlportOosModeIndex_Type(Integer32):
    """Custom type pm1004vencCtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlportOosModeIndex_Object = MibTableColumn
pm1004vencCtrlportOosModeIndex = _Pm1004vencCtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 18, 1, 1),
    _Pm1004vencCtrlportOosModeIndex_Type()
)
pm1004vencCtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlportOosModeIndex.setStatus("current")
_Pm1004vencCtrlportOosModePortn_Type = Pm1004vencClientOosMode
_Pm1004vencCtrlportOosModePortn_Object = MibTableColumn
pm1004vencCtrlportOosModePortn = _Pm1004vencCtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 18, 1, 2),
    _Pm1004vencCtrlportOosModePortn_Type()
)
pm1004vencCtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlportOosModePortn.setStatus("current")
_Pm1004vencCtrlsfpOffCtrlTable_Object = MibTable
pm1004vencCtrlsfpOffCtrlTable = _Pm1004vencCtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlsfpOffCtrlTable.setStatus("current")
_Pm1004vencCtrlsfpOffCtrlEntry_Object = MibTableRow
pm1004vencCtrlsfpOffCtrlEntry = _Pm1004vencCtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 20, 1)
)
pm1004vencCtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlsfpOffCtrlEntry.setStatus("current")


class _Pm1004vencCtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pm1004vencCtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlsfpOffCtrlIndex_Object = MibTableColumn
pm1004vencCtrlsfpOffCtrlIndex = _Pm1004vencCtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 20, 1, 1),
    _Pm1004vencCtrlsfpOffCtrlIndex_Type()
)
pm1004vencCtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlsfpOffCtrlIndex.setStatus("current")
_Pm1004vencCtrlsfpOffCtrlPortn_Type = EkiState
_Pm1004vencCtrlsfpOffCtrlPortn_Object = MibTableColumn
pm1004vencCtrlsfpOffCtrlPortn = _Pm1004vencCtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 20, 1, 2),
    _Pm1004vencCtrlsfpOffCtrlPortn_Type()
)
pm1004vencCtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlsfpOffCtrlPortn.setStatus("current")
_Pm1004vencCtrlcsfUpInsTable_Object = MibTable
pm1004vencCtrlcsfUpInsTable = _Pm1004vencCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlcsfUpInsTable.setStatus("current")
_Pm1004vencCtrlcsfUpInsEntry_Object = MibTableRow
pm1004vencCtrlcsfUpInsEntry = _Pm1004vencCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 21, 1)
)
pm1004vencCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlcsfUpInsEntry.setStatus("current")


class _Pm1004vencCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm1004vencCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlcsfUpInsIndex_Object = MibTableColumn
pm1004vencCtrlcsfUpInsIndex = _Pm1004vencCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 21, 1, 1),
    _Pm1004vencCtrlcsfUpInsIndex_Type()
)
pm1004vencCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlcsfUpInsIndex.setStatus("current")
_Pm1004vencCtrlcsfUpInsPortn_Type = EkiState
_Pm1004vencCtrlcsfUpInsPortn_Object = MibTableColumn
pm1004vencCtrlcsfUpInsPortn = _Pm1004vencCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 21, 1, 2),
    _Pm1004vencCtrlcsfUpInsPortn_Type()
)
pm1004vencCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlcsfUpInsPortn.setStatus("current")
_Pm1004vencCtrlcaisDwInsTable_Object = MibTable
pm1004vencCtrlcaisDwInsTable = _Pm1004vencCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlcaisDwInsTable.setStatus("current")
_Pm1004vencCtrlcaisDwInsEntry_Object = MibTableRow
pm1004vencCtrlcaisDwInsEntry = _Pm1004vencCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 22, 1)
)
pm1004vencCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlcaisDwInsEntry.setStatus("current")


class _Pm1004vencCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm1004vencCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlcaisDwInsIndex_Object = MibTableColumn
pm1004vencCtrlcaisDwInsIndex = _Pm1004vencCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 22, 1, 1),
    _Pm1004vencCtrlcaisDwInsIndex_Type()
)
pm1004vencCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlcaisDwInsIndex.setStatus("current")
_Pm1004vencCtrlcaisDwInsPortn_Type = EkiState
_Pm1004vencCtrlcaisDwInsPortn_Object = MibTableColumn
pm1004vencCtrlcaisDwInsPortn = _Pm1004vencCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 22, 1, 2),
    _Pm1004vencCtrlcaisDwInsPortn_Type()
)
pm1004vencCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlcaisDwInsPortn.setStatus("current")
_Pm1004vencCtrlclientAccessTermLoopTable_Object = MibTable
pm1004vencCtrlclientAccessTermLoopTable = _Pm1004vencCtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlclientAccessTermLoopTable.setStatus("current")
_Pm1004vencCtrlclientAccessTermLoopEntry_Object = MibTableRow
pm1004vencCtrlclientAccessTermLoopEntry = _Pm1004vencCtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 26, 1)
)
pm1004vencCtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm1004vencCtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm1004vencCtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm1004vencCtrlclientAccessTermLoopIndex = _Pm1004vencCtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 26, 1, 1),
    _Pm1004vencCtrlclientAccessTermLoopIndex_Type()
)
pm1004vencCtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlclientAccessTermLoopIndex.setStatus("current")
_Pm1004vencCtrlclientAccessTermLoopPortn_Type = EkiState
_Pm1004vencCtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm1004vencCtrlclientAccessTermLoopPortn = _Pm1004vencCtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 26, 1, 2),
    _Pm1004vencCtrlclientAccessTermLoopPortn_Type()
)
pm1004vencCtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlclientAccessTermLoopPortn.setStatus("current")
_Pm1004vencCtrlrxVideoProtocolTable_Object = MibTable
pm1004vencCtrlrxVideoProtocolTable = _Pm1004vencCtrlrxVideoProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 43)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlrxVideoProtocolTable.setStatus("current")
_Pm1004vencCtrlrxVideoProtocolEntry_Object = MibTableRow
pm1004vencCtrlrxVideoProtocolEntry = _Pm1004vencCtrlrxVideoProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 43, 1)
)
pm1004vencCtrlrxVideoProtocolEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlrxVideoProtocolIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlrxVideoProtocolEntry.setStatus("current")


class _Pm1004vencCtrlrxVideoProtocolIndex_Type(Integer32):
    """Custom type pm1004vencCtrlrxVideoProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlrxVideoProtocolIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlrxVideoProtocolIndex_Object = MibTableColumn
pm1004vencCtrlrxVideoProtocolIndex = _Pm1004vencCtrlrxVideoProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 43, 1, 1),
    _Pm1004vencCtrlrxVideoProtocolIndex_Type()
)
pm1004vencCtrlrxVideoProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlrxVideoProtocolIndex.setStatus("current")
_Pm1004vencCtrlrxVideoProtocolPortn_Type = EkiState
_Pm1004vencCtrlrxVideoProtocolPortn_Object = MibTableColumn
pm1004vencCtrlrxVideoProtocolPortn = _Pm1004vencCtrlrxVideoProtocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 43, 1, 2),
    _Pm1004vencCtrlrxVideoProtocolPortn_Type()
)
pm1004vencCtrlrxVideoProtocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlrxVideoProtocolPortn.setStatus("current")
_Pm1004vencCtrladddropClientRxProtectTable_Object = MibTable
pm1004vencCtrladddropClientRxProtectTable = _Pm1004vencCtrladddropClientRxProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 128)
)
if mibBuilder.loadTexts:
    pm1004vencCtrladddropClientRxProtectTable.setStatus("current")
_Pm1004vencCtrladddropClientRxProtectEntry_Object = MibTableRow
pm1004vencCtrladddropClientRxProtectEntry = _Pm1004vencCtrladddropClientRxProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 128, 1)
)
pm1004vencCtrladddropClientRxProtectEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrladddropClientRxProtectIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrladddropClientRxProtectEntry.setStatus("current")


class _Pm1004vencCtrladddropClientRxProtectIndex_Type(Integer32):
    """Custom type pm1004vencCtrladddropClientRxProtectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrladddropClientRxProtectIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrladddropClientRxProtectIndex_Object = MibTableColumn
pm1004vencCtrladddropClientRxProtectIndex = _Pm1004vencCtrladddropClientRxProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 128, 1, 1),
    _Pm1004vencCtrladddropClientRxProtectIndex_Type()
)
pm1004vencCtrladddropClientRxProtectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrladddropClientRxProtectIndex.setStatus("current")
_Pm1004vencCtrladddropClientRxProtectPortn_Type = Pm1004vencProtectionTimeSlot
_Pm1004vencCtrladddropClientRxProtectPortn_Object = MibTableColumn
pm1004vencCtrladddropClientRxProtectPortn = _Pm1004vencCtrladddropClientRxProtectPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 128, 1, 2),
    _Pm1004vencCtrladddropClientRxProtectPortn_Type()
)
pm1004vencCtrladddropClientRxProtectPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrladddropClientRxProtectPortn.setStatus("current")
_Pm1004vencCtrladddropTsClientModeTable_Object = MibTable
pm1004vencCtrladddropTsClientModeTable = _Pm1004vencCtrladddropTsClientModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 136)
)
if mibBuilder.loadTexts:
    pm1004vencCtrladddropTsClientModeTable.setStatus("current")
_Pm1004vencCtrladddropTsClientModeEntry_Object = MibTableRow
pm1004vencCtrladddropTsClientModeEntry = _Pm1004vencCtrladddropTsClientModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 136, 1)
)
pm1004vencCtrladddropTsClientModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrladddropTsClientModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrladddropTsClientModeEntry.setStatus("current")


class _Pm1004vencCtrladddropTsClientModeIndex_Type(Integer32):
    """Custom type pm1004vencCtrladddropTsClientModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrladddropTsClientModeIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrladddropTsClientModeIndex_Object = MibTableColumn
pm1004vencCtrladddropTsClientModeIndex = _Pm1004vencCtrladddropTsClientModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 136, 1, 1),
    _Pm1004vencCtrladddropTsClientModeIndex_Type()
)
pm1004vencCtrladddropTsClientModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrladddropTsClientModeIndex.setStatus("current")
_Pm1004vencCtrladddropTsClientModePortn_Type = Pm1004vencModeTimeSlot
_Pm1004vencCtrladddropTsClientModePortn_Object = MibTableColumn
pm1004vencCtrladddropTsClientModePortn = _Pm1004vencCtrladddropTsClientModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 2, 136, 1, 2),
    _Pm1004vencCtrladddropTsClientModePortn_Type()
)
pm1004vencCtrladddropTsClientModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrladddropTsClientModePortn.setStatus("current")
_Pm1004vencCtrlLine_ObjectIdentity = ObjectIdentity
pm1004vencCtrlLine = _Pm1004vencCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3)
)
_Pm1004vencCtrlcommAccessLoop_ObjectIdentity = ObjectIdentity
pm1004vencCtrlcommAccessLoop = _Pm1004vencCtrlcommAccessLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 64)
)
_Pm1004vencCtrlCommAccessloop_Type = EkiOnOff
_Pm1004vencCtrlCommAccessloop_Object = MibScalar
pm1004vencCtrlCommAccessloop = _Pm1004vencCtrlCommAccessloop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 64, 1),
    _Pm1004vencCtrlCommAccessloop_Type()
)
pm1004vencCtrlCommAccessloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlCommAccessloop.setStatus("deprecated")
_Pm1004vencCtrllineLoop_ObjectIdentity = ObjectIdentity
pm1004vencCtrllineLoop = _Pm1004vencCtrllineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 66)
)
_Pm1004vencCtrlLineLoop_Type = EkiOnOff
_Pm1004vencCtrlLineLoop_Object = MibScalar
pm1004vencCtrlLineLoop = _Pm1004vencCtrlLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 66, 1),
    _Pm1004vencCtrlLineLoop_Type()
)
pm1004vencCtrlLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlLineLoop.setStatus("deprecated")
_Pm1004vencCtrlProtMgnt_ObjectIdentity = ObjectIdentity
pm1004vencCtrlProtMgnt = _Pm1004vencCtrlProtMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 73)
)


class _Pm1004vencCtrlLineNumber_Type(Unsigned32):
    """Custom type pm1004vencCtrlLineNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Pm1004vencCtrlLineNumber_Type.__name__ = "Unsigned32"
_Pm1004vencCtrlLineNumber_Object = MibScalar
pm1004vencCtrlLineNumber = _Pm1004vencCtrlLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 73, 1),
    _Pm1004vencCtrlLineNumber_Type()
)
pm1004vencCtrlLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlLineNumber.setStatus("current")
_Pm1004vencCtrlProtMode_Type = EkiMode
_Pm1004vencCtrlProtMode_Object = MibScalar
pm1004vencCtrlProtMode = _Pm1004vencCtrlProtMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 73, 2),
    _Pm1004vencCtrlProtMode_Type()
)
pm1004vencCtrlProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlProtMode.setStatus("current")
_Pm1004vencCtrllineOosModeTable_Object = MibTable
pm1004vencCtrllineOosModeTable = _Pm1004vencCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm1004vencCtrllineOosModeTable.setStatus("current")
_Pm1004vencCtrllineOosModeEntry_Object = MibTableRow
pm1004vencCtrllineOosModeEntry = _Pm1004vencCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 74, 1)
)
pm1004vencCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrllineOosModeEntry.setStatus("current")


class _Pm1004vencCtrllineOosModeIndex_Type(Integer32):
    """Custom type pm1004vencCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrllineOosModeIndex_Object = MibTableColumn
pm1004vencCtrllineOosModeIndex = _Pm1004vencCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 74, 1, 1),
    _Pm1004vencCtrllineOosModeIndex_Type()
)
pm1004vencCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrllineOosModeIndex.setStatus("current")
_Pm1004vencCtrllineOosModePortn_Type = EkiState
_Pm1004vencCtrllineOosModePortn_Object = MibTableColumn
pm1004vencCtrllineOosModePortn = _Pm1004vencCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 74, 1, 2),
    _Pm1004vencCtrllineOosModePortn_Type()
)
pm1004vencCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrllineOosModePortn.setStatus("current")
_Pm1004vencCtrldccEnableTable_Object = MibTable
pm1004vencCtrldccEnableTable = _Pm1004vencCtrldccEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 198)
)
if mibBuilder.loadTexts:
    pm1004vencCtrldccEnableTable.setStatus("current")
_Pm1004vencCtrldccEnableEntry_Object = MibTableRow
pm1004vencCtrldccEnableEntry = _Pm1004vencCtrldccEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 198, 1)
)
pm1004vencCtrldccEnableEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrldccEnableIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrldccEnableEntry.setStatus("current")


class _Pm1004vencCtrldccEnableIndex_Type(Integer32):
    """Custom type pm1004vencCtrldccEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrldccEnableIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrldccEnableIndex_Object = MibTableColumn
pm1004vencCtrldccEnableIndex = _Pm1004vencCtrldccEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 198, 1, 1),
    _Pm1004vencCtrldccEnableIndex_Type()
)
pm1004vencCtrldccEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrldccEnableIndex.setStatus("current")
_Pm1004vencCtrldccEnablePortn_Type = EkiState
_Pm1004vencCtrldccEnablePortn_Object = MibTableColumn
pm1004vencCtrldccEnablePortn = _Pm1004vencCtrldccEnablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 198, 1, 2),
    _Pm1004vencCtrldccEnablePortn_Type()
)
pm1004vencCtrldccEnablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrldccEnablePortn.setStatus("current")
_Pm1004vencCtrlxfpOnoffTable_Object = MibTable
pm1004vencCtrlxfpOnoffTable = _Pm1004vencCtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpOnoffTable.setStatus("current")
_Pm1004vencCtrlxfpOnoffEntry_Object = MibTableRow
pm1004vencCtrlxfpOnoffEntry = _Pm1004vencCtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 208, 1)
)
pm1004vencCtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpOnoffEntry.setStatus("current")


class _Pm1004vencCtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pm1004vencCtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlxfpOnoffIndex_Object = MibTableColumn
pm1004vencCtrlxfpOnoffIndex = _Pm1004vencCtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 208, 1, 1),
    _Pm1004vencCtrlxfpOnoffIndex_Type()
)
pm1004vencCtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpOnoffIndex.setStatus("current")
_Pm1004vencCtrlxfpOnoffPortn_Type = EkiState
_Pm1004vencCtrlxfpOnoffPortn_Object = MibTableColumn
pm1004vencCtrlxfpOnoffPortn = _Pm1004vencCtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 208, 1, 2),
    _Pm1004vencCtrlxfpOnoffPortn_Type()
)
pm1004vencCtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpOnoffPortn.setStatus("current")
_Pm1004vencCtrlxfpLineLoopTable_Object = MibTable
pm1004vencCtrlxfpLineLoopTable = _Pm1004vencCtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpLineLoopTable.setStatus("current")
_Pm1004vencCtrlxfpLineLoopEntry_Object = MibTableRow
pm1004vencCtrlxfpLineLoopEntry = _Pm1004vencCtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 209, 1)
)
pm1004vencCtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpLineLoopEntry.setStatus("current")


class _Pm1004vencCtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pm1004vencCtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlxfpLineLoopIndex_Object = MibTableColumn
pm1004vencCtrlxfpLineLoopIndex = _Pm1004vencCtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 209, 1, 1),
    _Pm1004vencCtrlxfpLineLoopIndex_Type()
)
pm1004vencCtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpLineLoopIndex.setStatus("current")
_Pm1004vencCtrlxfpLineLoopPortn_Type = EkiState
_Pm1004vencCtrlxfpLineLoopPortn_Object = MibTableColumn
pm1004vencCtrlxfpLineLoopPortn = _Pm1004vencCtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 209, 1, 2),
    _Pm1004vencCtrlxfpLineLoopPortn_Type()
)
pm1004vencCtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpLineLoopPortn.setStatus("current")
_Pm1004vencCtrlxfpXfiLoopTable_Object = MibTable
pm1004vencCtrlxfpXfiLoopTable = _Pm1004vencCtrlxfpXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpXfiLoopTable.setStatus("current")
_Pm1004vencCtrlxfpXfiLoopEntry_Object = MibTableRow
pm1004vencCtrlxfpXfiLoopEntry = _Pm1004vencCtrlxfpXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 210, 1)
)
pm1004vencCtrlxfpXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrlxfpXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpXfiLoopEntry.setStatus("current")


class _Pm1004vencCtrlxfpXfiLoopIndex_Type(Integer32):
    """Custom type pm1004vencCtrlxfpXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrlxfpXfiLoopIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrlxfpXfiLoopIndex_Object = MibTableColumn
pm1004vencCtrlxfpXfiLoopIndex = _Pm1004vencCtrlxfpXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 210, 1, 1),
    _Pm1004vencCtrlxfpXfiLoopIndex_Type()
)
pm1004vencCtrlxfpXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpXfiLoopIndex.setStatus("current")
_Pm1004vencCtrlxfpXfiLoopPortn_Type = EkiState
_Pm1004vencCtrlxfpXfiLoopPortn_Object = MibTableColumn
pm1004vencCtrlxfpXfiLoopPortn = _Pm1004vencCtrlxfpXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 210, 1, 2),
    _Pm1004vencCtrlxfpXfiLoopPortn_Type()
)
pm1004vencCtrlxfpXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrlxfpXfiLoopPortn.setStatus("current")
_Pm1004vencCtrllineTunableChannelTable_Object = MibTable
pm1004vencCtrllineTunableChannelTable = _Pm1004vencCtrllineTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm1004vencCtrllineTunableChannelTable.setStatus("current")
_Pm1004vencCtrllineTunableChannelEntry_Object = MibTableRow
pm1004vencCtrllineTunableChannelEntry = _Pm1004vencCtrllineTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 212, 1)
)
pm1004vencCtrllineTunableChannelEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrllineTunableChannelIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrllineTunableChannelEntry.setStatus("current")


class _Pm1004vencCtrllineTunableChannelIndex_Type(Integer32):
    """Custom type pm1004vencCtrllineTunableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrllineTunableChannelIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrllineTunableChannelIndex_Object = MibTableColumn
pm1004vencCtrllineTunableChannelIndex = _Pm1004vencCtrllineTunableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 212, 1, 1),
    _Pm1004vencCtrllineTunableChannelIndex_Type()
)
pm1004vencCtrllineTunableChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrllineTunableChannelIndex.setStatus("current")
_Pm1004vencCtrllineTunableChannelPortn_Type = Pm1004vencOtxChannel
_Pm1004vencCtrllineTunableChannelPortn_Object = MibTableColumn
pm1004vencCtrllineTunableChannelPortn = _Pm1004vencCtrllineTunableChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 212, 1, 2),
    _Pm1004vencCtrllineTunableChannelPortn_Type()
)
pm1004vencCtrllineTunableChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrllineTunableChannelPortn.setStatus("current")
_Pm1004vencCtrllinePhotodiodeModeTable_Object = MibTable
pm1004vencCtrllinePhotodiodeModeTable = _Pm1004vencCtrllinePhotodiodeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 213)
)
if mibBuilder.loadTexts:
    pm1004vencCtrllinePhotodiodeModeTable.setStatus("current")
_Pm1004vencCtrllinePhotodiodeModeEntry_Object = MibTableRow
pm1004vencCtrllinePhotodiodeModeEntry = _Pm1004vencCtrllinePhotodiodeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 213, 1)
)
pm1004vencCtrllinePhotodiodeModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrllinePhotodiodeModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrllinePhotodiodeModeEntry.setStatus("current")


class _Pm1004vencCtrllinePhotodiodeModeIndex_Type(Integer32):
    """Custom type pm1004vencCtrllinePhotodiodeModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrllinePhotodiodeModeIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrllinePhotodiodeModeIndex_Object = MibTableColumn
pm1004vencCtrllinePhotodiodeModeIndex = _Pm1004vencCtrllinePhotodiodeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 213, 1, 1),
    _Pm1004vencCtrllinePhotodiodeModeIndex_Type()
)
pm1004vencCtrllinePhotodiodeModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrllinePhotodiodeModeIndex.setStatus("current")
_Pm1004vencCtrllinePhotodiodeModePortn_Type = Pm1004vencOtxMode
_Pm1004vencCtrllinePhotodiodeModePortn_Object = MibTableColumn
pm1004vencCtrllinePhotodiodeModePortn = _Pm1004vencCtrllinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 213, 1, 2),
    _Pm1004vencCtrllinePhotodiodeModePortn_Type()
)
pm1004vencCtrllinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrllinePhotodiodeModePortn.setStatus("current")
_Pm1004vencCtrllinePhotodiodeValueTable_Object = MibTable
pm1004vencCtrllinePhotodiodeValueTable = _Pm1004vencCtrllinePhotodiodeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 214)
)
if mibBuilder.loadTexts:
    pm1004vencCtrllinePhotodiodeValueTable.setStatus("current")
_Pm1004vencCtrllinePhotodiodeValueEntry_Object = MibTableRow
pm1004vencCtrllinePhotodiodeValueEntry = _Pm1004vencCtrllinePhotodiodeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 214, 1)
)
pm1004vencCtrllinePhotodiodeValueEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrllinePhotodiodeValueIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrllinePhotodiodeValueEntry.setStatus("current")


class _Pm1004vencCtrllinePhotodiodeValueIndex_Type(Integer32):
    """Custom type pm1004vencCtrllinePhotodiodeValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrllinePhotodiodeValueIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrllinePhotodiodeValueIndex_Object = MibTableColumn
pm1004vencCtrllinePhotodiodeValueIndex = _Pm1004vencCtrllinePhotodiodeValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 214, 1, 1),
    _Pm1004vencCtrllinePhotodiodeValueIndex_Type()
)
pm1004vencCtrllinePhotodiodeValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrllinePhotodiodeValueIndex.setStatus("current")
_Pm1004vencCtrllinePhotodiodeValuePortn_Type = Pm1004vencAdjustValue
_Pm1004vencCtrllinePhotodiodeValuePortn_Object = MibTableColumn
pm1004vencCtrllinePhotodiodeValuePortn = _Pm1004vencCtrllinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 214, 1, 2),
    _Pm1004vencCtrllinePhotodiodeValuePortn_Type()
)
pm1004vencCtrllinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrllinePhotodiodeValuePortn.setStatus("current")
_Pm1004vencCtrllinePowerLaserTable_Object = MibTable
pm1004vencCtrllinePowerLaserTable = _Pm1004vencCtrllinePowerLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 215)
)
if mibBuilder.loadTexts:
    pm1004vencCtrllinePowerLaserTable.setStatus("current")
_Pm1004vencCtrllinePowerLaserEntry_Object = MibTableRow
pm1004vencCtrllinePowerLaserEntry = _Pm1004vencCtrllinePowerLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 215, 1)
)
pm1004vencCtrllinePowerLaserEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCtrllinePowerLaserIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCtrllinePowerLaserEntry.setStatus("current")


class _Pm1004vencCtrllinePowerLaserIndex_Type(Integer32):
    """Custom type pm1004vencCtrllinePowerLaserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCtrllinePowerLaserIndex_Type.__name__ = "Integer32"
_Pm1004vencCtrllinePowerLaserIndex_Object = MibTableColumn
pm1004vencCtrllinePowerLaserIndex = _Pm1004vencCtrllinePowerLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 215, 1, 1),
    _Pm1004vencCtrllinePowerLaserIndex_Type()
)
pm1004vencCtrllinePowerLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCtrllinePowerLaserIndex.setStatus("current")
_Pm1004vencCtrllinePowerLaserPortn_Type = Integer32
_Pm1004vencCtrllinePowerLaserPortn_Object = MibTableColumn
pm1004vencCtrllinePowerLaserPortn = _Pm1004vencCtrllinePowerLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 6, 3, 215, 1, 2),
    _Pm1004vencCtrllinePowerLaserPortn_Type()
)
pm1004vencCtrllinePowerLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCtrllinePowerLaserPortn.setStatus("current")
_Pm1004vencri_ObjectIdentity = ObjectIdentity
pm1004vencri = _Pm1004vencri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7)
)
_Pm1004vencriTable_ObjectIdentity = ObjectIdentity
pm1004vencriTable = _Pm1004vencriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 1)
)
_Pm1004vencRinvClientTable_Object = MibTable
pm1004vencRinvClientTable = _Pm1004vencRinvClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004vencRinvClientTable.setStatus("current")
_Pm1004vencRinvClientEntry_Object = MibTableRow
pm1004vencRinvClientEntry = _Pm1004vencRinvClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 1, 1, 1)
)
pm1004vencRinvClientEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencRinvClientIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencRinvClientEntry.setStatus("current")


class _Pm1004vencRinvClientIndex_Type(Integer32):
    """Custom type pm1004vencRinvClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004vencRinvClientIndex_Type.__name__ = "Integer32"
_Pm1004vencRinvClientIndex_Object = MibTableColumn
pm1004vencRinvClientIndex = _Pm1004vencRinvClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 1, 1, 1, 1),
    _Pm1004vencRinvClientIndex_Type()
)
pm1004vencRinvClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencRinvClientIndex.setStatus("current")
_Pm1004vencRinvClient_Type = DisplayString
_Pm1004vencRinvClient_Object = MibTableColumn
pm1004vencRinvClient = _Pm1004vencRinvClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 1, 1, 1, 2),
    _Pm1004vencRinvClient_Type()
)
pm1004vencRinvClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencRinvClient.setStatus("current")
_Pm1004vencRinvLineTable_Object = MibTable
pm1004vencRinvLineTable = _Pm1004vencRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm1004vencRinvLineTable.setStatus("current")
_Pm1004vencRinvLineEntry_Object = MibTableRow
pm1004vencRinvLineEntry = _Pm1004vencRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 1, 2, 1)
)
pm1004vencRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencRinvLineEntry.setStatus("current")


class _Pm1004vencRinvLineIndex_Type(Integer32):
    """Custom type pm1004vencRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004vencRinvLineIndex_Type.__name__ = "Integer32"
_Pm1004vencRinvLineIndex_Object = MibTableColumn
pm1004vencRinvLineIndex = _Pm1004vencRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 1, 2, 1, 1),
    _Pm1004vencRinvLineIndex_Type()
)
pm1004vencRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencRinvLineIndex.setStatus("current")
_Pm1004vencRinvxfpLine_Type = DisplayString
_Pm1004vencRinvxfpLine_Object = MibTableColumn
pm1004vencRinvxfpLine = _Pm1004vencRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 1, 2, 1, 2),
    _Pm1004vencRinvxfpLine_Type()
)
pm1004vencRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencRinvxfpLine.setStatus("current")
_Pm1004vencRinvReloadInventory_Type = EkiOnOff
_Pm1004vencRinvReloadInventory_Object = MibScalar
pm1004vencRinvReloadInventory = _Pm1004vencRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 2),
    _Pm1004vencRinvReloadInventory_Type()
)
pm1004vencRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencRinvReloadInventory.setStatus("current")
_Pm1004vencRinvHwPlatform_Type = DisplayString
_Pm1004vencRinvHwPlatform_Object = MibScalar
pm1004vencRinvHwPlatform = _Pm1004vencRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 3),
    _Pm1004vencRinvHwPlatform_Type()
)
pm1004vencRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencRinvHwPlatform.setStatus("current")
_Pm1004vencRinvModulePlatform_Type = DisplayString
_Pm1004vencRinvModulePlatform_Object = MibScalar
pm1004vencRinvModulePlatform = _Pm1004vencRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 4),
    _Pm1004vencRinvModulePlatform_Type()
)
pm1004vencRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencRinvModulePlatform.setStatus("current")
_Pm1004vencRinvSwPlatform_Type = DisplayString
_Pm1004vencRinvSwPlatform_Object = MibScalar
pm1004vencRinvSwPlatform = _Pm1004vencRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 5),
    _Pm1004vencRinvSwPlatform_Type()
)
pm1004vencRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencRinvSwPlatform.setStatus("current")
_Pm1004vencRinvGwPlatform_Type = DisplayString
_Pm1004vencRinvGwPlatform_Object = MibScalar
pm1004vencRinvGwPlatform = _Pm1004vencRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 7, 6),
    _Pm1004vencRinvGwPlatform_Type()
)
pm1004vencRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencRinvGwPlatform.setStatus("current")
_Pm1004vencdownload_ObjectIdentity = ObjectIdentity
pm1004vencdownload = _Pm1004vencdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8)
)
_Pm1004vencDwlOther_ObjectIdentity = ObjectIdentity
pm1004vencDwlOther = _Pm1004vencDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1)
)
_Pm1004vencDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm1004vencDwlrestartProcess = _Pm1004vencDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 0)
)
_Pm1004vencDwlWarmRestartProcessed_Type = EkiOnOff
_Pm1004vencDwlWarmRestartProcessed_Object = MibScalar
pm1004vencDwlWarmRestartProcessed = _Pm1004vencDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 0, 1),
    _Pm1004vencDwlWarmRestartProcessed_Type()
)
pm1004vencDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlWarmRestartProcessed.setStatus("current")
_Pm1004vencDwlColdRestartProcessed_Type = EkiOnOff
_Pm1004vencDwlColdRestartProcessed_Object = MibScalar
pm1004vencDwlColdRestartProcessed = _Pm1004vencDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 0, 2),
    _Pm1004vencDwlColdRestartProcessed_Type()
)
pm1004vencDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlColdRestartProcessed.setStatus("current")
_Pm1004vencDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm1004vencDwlswBanksUsed = _Pm1004vencDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 1)
)
_Pm1004vencDwlSwBank1Used_Type = EkiOnOff
_Pm1004vencDwlSwBank1Used_Object = MibScalar
pm1004vencDwlSwBank1Used = _Pm1004vencDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 1, 1),
    _Pm1004vencDwlSwBank1Used_Type()
)
pm1004vencDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlSwBank1Used.setStatus("current")
_Pm1004vencDwlSwBank2Used_Type = EkiOnOff
_Pm1004vencDwlSwBank2Used_Object = MibScalar
pm1004vencDwlSwBank2Used = _Pm1004vencDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 1, 2),
    _Pm1004vencDwlSwBank2Used_Type()
)
pm1004vencDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlSwBank2Used.setStatus("current")
_Pm1004vencDwlSwBank1Notempty_Type = EkiOnOff
_Pm1004vencDwlSwBank1Notempty_Object = MibScalar
pm1004vencDwlSwBank1Notempty = _Pm1004vencDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 1, 5),
    _Pm1004vencDwlSwBank1Notempty_Type()
)
pm1004vencDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlSwBank1Notempty.setStatus("current")
_Pm1004vencDwlSwBank2Notempty_Type = EkiOnOff
_Pm1004vencDwlSwBank2Notempty_Object = MibScalar
pm1004vencDwlSwBank2Notempty = _Pm1004vencDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 1, 6),
    _Pm1004vencDwlSwBank2Notempty_Type()
)
pm1004vencDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlSwBank2Notempty.setStatus("current")
_Pm1004vencDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm1004vencDwlgwBanksUsed = _Pm1004vencDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 2)
)
_Pm1004vencDwlGwBank1Used_Type = EkiOnOff
_Pm1004vencDwlGwBank1Used_Object = MibScalar
pm1004vencDwlGwBank1Used = _Pm1004vencDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 2, 1),
    _Pm1004vencDwlGwBank1Used_Type()
)
pm1004vencDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlGwBank1Used.setStatus("current")
_Pm1004vencDwlGwBank2Used_Type = EkiOnOff
_Pm1004vencDwlGwBank2Used_Object = MibScalar
pm1004vencDwlGwBank2Used = _Pm1004vencDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 2, 2),
    _Pm1004vencDwlGwBank2Used_Type()
)
pm1004vencDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlGwBank2Used.setStatus("current")
_Pm1004vencDwlGwBank3Used_Type = EkiOnOff
_Pm1004vencDwlGwBank3Used_Object = MibScalar
pm1004vencDwlGwBank3Used = _Pm1004vencDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 2, 3),
    _Pm1004vencDwlGwBank3Used_Type()
)
pm1004vencDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlGwBank3Used.setStatus("current")
_Pm1004vencDwlGwBank4Used_Type = EkiOnOff
_Pm1004vencDwlGwBank4Used_Object = MibScalar
pm1004vencDwlGwBank4Used = _Pm1004vencDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 2, 4),
    _Pm1004vencDwlGwBank4Used_Type()
)
pm1004vencDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlGwBank4Used.setStatus("current")
_Pm1004vencDwlGwBank1Notempty_Type = EkiOnOff
_Pm1004vencDwlGwBank1Notempty_Object = MibScalar
pm1004vencDwlGwBank1Notempty = _Pm1004vencDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 2, 5),
    _Pm1004vencDwlGwBank1Notempty_Type()
)
pm1004vencDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlGwBank1Notempty.setStatus("current")
_Pm1004vencDwlGwBank2Notempty_Type = EkiOnOff
_Pm1004vencDwlGwBank2Notempty_Object = MibScalar
pm1004vencDwlGwBank2Notempty = _Pm1004vencDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 2, 6),
    _Pm1004vencDwlGwBank2Notempty_Type()
)
pm1004vencDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlGwBank2Notempty.setStatus("current")
_Pm1004vencDwlGwBank3Notempty_Type = EkiOnOff
_Pm1004vencDwlGwBank3Notempty_Object = MibScalar
pm1004vencDwlGwBank3Notempty = _Pm1004vencDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 2, 7),
    _Pm1004vencDwlGwBank3Notempty_Type()
)
pm1004vencDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlGwBank3Notempty.setStatus("current")
_Pm1004vencDwlGwBank4Notempty_Type = EkiOnOff
_Pm1004vencDwlGwBank4Notempty_Object = MibScalar
pm1004vencDwlGwBank4Notempty = _Pm1004vencDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 1, 2, 8),
    _Pm1004vencDwlGwBank4Notempty_Type()
)
pm1004vencDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencDwlGwBank4Notempty.setStatus("current")
_Pm1004vencDwlClient_ObjectIdentity = ObjectIdentity
pm1004vencDwlClient = _Pm1004vencDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 2)
)
_Pm1004vencDwlLine_ObjectIdentity = ObjectIdentity
pm1004vencDwlLine = _Pm1004vencDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 8, 3)
)
_Pm1004vencConfig_ObjectIdentity = ObjectIdentity
pm1004vencConfig = _Pm1004vencConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9)
)
_Pm1004vencCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm1004vencCfgAccessCAisCsf = _Pm1004vencCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1)
)
_Pm1004vencCfgClientcaiscsfTable_Object = MibTable
pm1004vencCfgClientcaiscsfTable = _Pm1004vencCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004vencCfgClientcaiscsfTable.setStatus("current")
_Pm1004vencCfgClientcaiscsfEntry_Object = MibTableRow
pm1004vencCfgClientcaiscsfEntry = _Pm1004vencCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1, 1)
)
pm1004vencCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCfgClientcaiscsfEntry.setStatus("current")


class _Pm1004vencCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm1004vencCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm1004vencCfgClientcaiscsfIndex_Object = MibTableColumn
pm1004vencCfgClientcaiscsfIndex = _Pm1004vencCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1, 1, 1),
    _Pm1004vencCfgClientcaiscsfIndex_Type()
)
pm1004vencCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgClientcaiscsfIndex.setStatus("current")


class _Pm1004vencCfgCAisModePortn_Type(Unsigned32):
    """Custom type pm1004vencCfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgCAisModePortn_Object = MibTableColumn
pm1004vencCfgCAisModePortn = _Pm1004vencCfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1, 1, 3),
    _Pm1004vencCfgCAisModePortn_Type()
)
pm1004vencCfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgCAisModePortn.setStatus("current")


class _Pm1004vencCfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgUpAccessioAlmPortn_Object = MibTableColumn
pm1004vencCfgUpAccessioAlmPortn = _Pm1004vencCfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1, 1, 9),
    _Pm1004vencCfgUpAccessioAlmPortn_Type()
)
pm1004vencCfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgUpAccessioAlmPortn.setStatus("current")


class _Pm1004vencCfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgUpMapperDeAlmPortn_Object = MibTableColumn
pm1004vencCfgUpMapperDeAlmPortn = _Pm1004vencCfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1, 1, 10),
    _Pm1004vencCfgUpMapperDeAlmPortn_Type()
)
pm1004vencCfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgUpMapperDeAlmPortn.setStatus("current")


class _Pm1004vencCfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgDownAccessioAlmPortn_Object = MibTableColumn
pm1004vencCfgDownAccessioAlmPortn = _Pm1004vencCfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1, 1, 17),
    _Pm1004vencCfgDownAccessioAlmPortn_Type()
)
pm1004vencCfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgDownAccessioAlmPortn.setStatus("current")


class _Pm1004vencCfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgDownMapperDeAlmPortn_Object = MibTableColumn
pm1004vencCfgDownMapperDeAlmPortn = _Pm1004vencCfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1, 1, 18),
    _Pm1004vencCfgDownMapperDeAlmPortn_Type()
)
pm1004vencCfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgDownMapperDeAlmPortn.setStatus("current")


class _Pm1004vencCfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgDownDfrmAlmPortn_Object = MibTableColumn
pm1004vencCfgDownDfrmAlmPortn = _Pm1004vencCfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1, 1, 19),
    _Pm1004vencCfgDownDfrmAlmPortn_Type()
)
pm1004vencCfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgDownDfrmAlmPortn.setStatus("current")


class _Pm1004vencCfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pm1004vencCfgDownLineSyncAlarmsPortn = _Pm1004vencCfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 1, 1, 1, 20),
    _Pm1004vencCfgDownLineSyncAlarmsPortn_Type()
)
pm1004vencCfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgDownLineSyncAlarmsPortn.setStatus("deprecated")
_Pm1004vencCfgStartup_ObjectIdentity = ObjectIdentity
pm1004vencCfgStartup = _Pm1004vencCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2)
)
_Pm1004vencCfgClientStartupTable_Object = MibTable
pm1004vencCfgClientStartupTable = _Pm1004vencCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm1004vencCfgClientStartupTable.setStatus("current")
_Pm1004vencCfgClientStartupEntry_Object = MibTableRow
pm1004vencCfgClientStartupEntry = _Pm1004vencCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 1, 1)
)
pm1004vencCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCfgClientStartupEntry.setStatus("current")


class _Pm1004vencCfgClientStartupIndex_Type(Integer32):
    """Custom type pm1004vencCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm1004vencCfgClientStartupIndex_Object = MibTableColumn
pm1004vencCfgClientStartupIndex = _Pm1004vencCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 1, 1, 1),
    _Pm1004vencCfgClientStartupIndex_Type()
)
pm1004vencCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgClientStartupIndex.setStatus("current")


class _Pm1004vencCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgSystConfPortPortn_Object = MibTableColumn
pm1004vencCfgSystConfPortPortn = _Pm1004vencCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 1, 1, 3),
    _Pm1004vencCfgSystConfPortPortn_Type()
)
pm1004vencCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgSystConfPortPortn.setStatus("current")


class _Pm1004vencCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgNetConfPortPortn_Object = MibTableColumn
pm1004vencCfgNetConfPortPortn = _Pm1004vencCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 1, 1, 4),
    _Pm1004vencCfgNetConfPortPortn_Type()
)
pm1004vencCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgNetConfPortPortn.setStatus("current")


class _Pm1004vencCfgAdddropConfPortPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgAdddropConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgAdddropConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgAdddropConfPortPortn_Object = MibTableColumn
pm1004vencCfgAdddropConfPortPortn = _Pm1004vencCfgAdddropConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 1, 1, 5),
    _Pm1004vencCfgAdddropConfPortPortn_Type()
)
pm1004vencCfgAdddropConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgAdddropConfPortPortn.setStatus("deprecated")
_Pm1004venctablelineStartup_ObjectIdentity = ObjectIdentity
pm1004venctablelineStartup = _Pm1004venctablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 2)
)


class _Pm1004vencCfgsystConfLine1_Type(Unsigned32):
    """Custom type pm1004vencCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm1004vencCfgsystConfLine1_Object = MibScalar
pm1004vencCfgsystConfLine1 = _Pm1004vencCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 2, 2),
    _Pm1004vencCfgsystConfLine1_Type()
)
pm1004vencCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgsystConfLine1.setStatus("current")


class _Pm1004vencCfglineOptions1_Type(Unsigned32):
    """Custom type pm1004vencCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfglineOptions1_Type.__name__ = "Unsigned32"
_Pm1004vencCfglineOptions1_Object = MibScalar
pm1004vencCfglineOptions1 = _Pm1004vencCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 2, 5),
    _Pm1004vencCfglineOptions1_Type()
)
pm1004vencCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfglineOptions1.setStatus("current")


class _Pm1004vencCfgsystConfLine2_Type(Unsigned32):
    """Custom type pm1004vencCfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm1004vencCfgsystConfLine2_Object = MibScalar
pm1004vencCfgsystConfLine2 = _Pm1004vencCfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 2, 6),
    _Pm1004vencCfgsystConfLine2_Type()
)
pm1004vencCfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgsystConfLine2.setStatus("current")


class _Pm1004vencCfglineSelection_Type(Unsigned32):
    """Custom type pm1004vencCfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfglineSelection_Type.__name__ = "Unsigned32"
_Pm1004vencCfglineSelection_Object = MibScalar
pm1004vencCfglineSelection = _Pm1004vencCfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 2, 7),
    _Pm1004vencCfglineSelection_Type()
)
pm1004vencCfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfglineSelection.setStatus("current")


class _Pm1004vencCfglineOptions2_Type(Unsigned32):
    """Custom type pm1004vencCfglineOptions2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfglineOptions2_Type.__name__ = "Unsigned32"
_Pm1004vencCfglineOptions2_Object = MibScalar
pm1004vencCfglineOptions2 = _Pm1004vencCfglineOptions2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 2, 9),
    _Pm1004vencCfglineOptions2_Type()
)
pm1004vencCfglineOptions2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfglineOptions2.setStatus("current")
_Pm1004vencCfgXfpTable_Object = MibTable
pm1004vencCfgXfpTable = _Pm1004vencCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm1004vencCfgXfpTable.setStatus("current")
_Pm1004vencCfgXfpEntry_Object = MibTableRow
pm1004vencCfgXfpEntry = _Pm1004vencCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 3, 1)
)
pm1004vencCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCfgXfpEntry.setStatus("current")


class _Pm1004vencCfgXfpIndex_Type(Integer32):
    """Custom type pm1004vencCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCfgXfpIndex_Type.__name__ = "Integer32"
_Pm1004vencCfgXfpIndex_Object = MibTableColumn
pm1004vencCfgXfpIndex = _Pm1004vencCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 3, 1, 1),
    _Pm1004vencCfgXfpIndex_Type()
)
pm1004vencCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgXfpIndex.setStatus("current")


class _Pm1004vencCfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgSystConfXfpPortn_Object = MibTableColumn
pm1004vencCfgSystConfXfpPortn = _Pm1004vencCfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 3, 1, 3),
    _Pm1004vencCfgSystConfXfpPortn_Type()
)
pm1004vencCfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgSystConfXfpPortn.setStatus("current")


class _Pm1004vencCfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgDataRateConfXfpPortn_Object = MibTableColumn
pm1004vencCfgDataRateConfXfpPortn = _Pm1004vencCfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 2, 3, 1, 4),
    _Pm1004vencCfgDataRateConfXfpPortn_Type()
)
pm1004vencCfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgDataRateConfXfpPortn.setStatus("deprecated")
_Pm1004vencCfgLabels_ObjectIdentity = ObjectIdentity
pm1004vencCfgLabels = _Pm1004vencCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 3)
)
_Pm1004vencCfgLabelclientTable_Object = MibTable
pm1004vencCfgLabelclientTable = _Pm1004vencCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm1004vencCfgLabelclientTable.setStatus("current")
_Pm1004vencCfgLabelclientEntry_Object = MibTableRow
pm1004vencCfgLabelclientEntry = _Pm1004vencCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 3, 1, 1)
)
pm1004vencCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCfgLabelclientEntry.setStatus("current")


class _Pm1004vencCfgLabelclientIndex_Type(Integer32):
    """Custom type pm1004vencCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1004vencCfgLabelclientIndex_Object = MibTableColumn
pm1004vencCfgLabelclientIndex = _Pm1004vencCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 3, 1, 1, 1),
    _Pm1004vencCfgLabelclientIndex_Type()
)
pm1004vencCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgLabelclientIndex.setStatus("current")


class _Pm1004vencCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1004vencCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004vencCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1004vencCfgLabelclientPortn_Object = MibTableColumn
pm1004vencCfgLabelclientPortn = _Pm1004vencCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 3, 1, 1, 3),
    _Pm1004vencCfgLabelclientPortn_Type()
)
pm1004vencCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLabelclientPortn.setStatus("current")
_Pm1004vencCfgLabellineTable_Object = MibTable
pm1004vencCfgLabellineTable = _Pm1004vencCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm1004vencCfgLabellineTable.setStatus("current")
_Pm1004vencCfgLabellineEntry_Object = MibTableRow
pm1004vencCfgLabellineEntry = _Pm1004vencCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 3, 2, 1)
)
pm1004vencCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCfgLabellineEntry.setStatus("current")


class _Pm1004vencCfgLabellineIndex_Type(Integer32):
    """Custom type pm1004vencCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1004vencCfgLabellineIndex_Object = MibTableColumn
pm1004vencCfgLabellineIndex = _Pm1004vencCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 3, 2, 1, 1),
    _Pm1004vencCfgLabellineIndex_Type()
)
pm1004vencCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgLabellineIndex.setStatus("current")


class _Pm1004vencCfgLabellinePortn_Type(DisplayString):
    """Custom type pm1004vencCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004vencCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1004vencCfgLabellinePortn_Object = MibTableColumn
pm1004vencCfgLabellinePortn = _Pm1004vencCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 3, 2, 1, 3),
    _Pm1004vencCfgLabellinePortn_Type()
)
pm1004vencCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLabellinePortn.setStatus("current")
_Pm1004vencCfgStartupthresholds_ObjectIdentity = ObjectIdentity
pm1004vencCfgStartupthresholds = _Pm1004vencCfgStartupthresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4)
)
_Pm1004vencCfgClientStartupThreshTable_Object = MibTable
pm1004vencCfgClientStartupThreshTable = _Pm1004vencCfgClientStartupThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm1004vencCfgClientStartupThreshTable.setStatus("current")
_Pm1004vencCfgClientStartupThreshEntry_Object = MibTableRow
pm1004vencCfgClientStartupThreshEntry = _Pm1004vencCfgClientStartupThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 1, 1)
)
pm1004vencCfgClientStartupThreshEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCfgClientStartupThreshIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCfgClientStartupThreshEntry.setStatus("current")


class _Pm1004vencCfgClientStartupThreshIndex_Type(Integer32):
    """Custom type pm1004vencCfgClientStartupThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCfgClientStartupThreshIndex_Type.__name__ = "Integer32"
_Pm1004vencCfgClientStartupThreshIndex_Object = MibTableColumn
pm1004vencCfgClientStartupThreshIndex = _Pm1004vencCfgClientStartupThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 1, 1, 1),
    _Pm1004vencCfgClientStartupThreshIndex_Type()
)
pm1004vencCfgClientStartupThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgClientStartupThreshIndex.setStatus("current")


class _Pm1004vencCfgClientThreshtxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgClientThreshtxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgClientThreshtxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgClientThreshtxpowhighPortn_Object = MibTableColumn
pm1004vencCfgClientThreshtxpowhighPortn = _Pm1004vencCfgClientThreshtxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 1, 1, 15),
    _Pm1004vencCfgClientThreshtxpowhighPortn_Type()
)
pm1004vencCfgClientThreshtxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgClientThreshtxpowhighPortn.setStatus("current")


class _Pm1004vencCfgClientThreshtxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgClientThreshtxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgClientThreshtxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgClientThreshtxpowlowPortn_Object = MibTableColumn
pm1004vencCfgClientThreshtxpowlowPortn = _Pm1004vencCfgClientThreshtxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 1, 1, 16),
    _Pm1004vencCfgClientThreshtxpowlowPortn_Type()
)
pm1004vencCfgClientThreshtxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgClientThreshtxpowlowPortn.setStatus("current")


class _Pm1004vencCfgClientThreshrxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgClientThreshrxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgClientThreshrxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgClientThreshrxpowhighPortn_Object = MibTableColumn
pm1004vencCfgClientThreshrxpowhighPortn = _Pm1004vencCfgClientThreshrxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 1, 1, 19),
    _Pm1004vencCfgClientThreshrxpowhighPortn_Type()
)
pm1004vencCfgClientThreshrxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgClientThreshrxpowhighPortn.setStatus("current")


class _Pm1004vencCfgClientThreshrxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgClientThreshrxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgClientThreshrxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgClientThreshrxpowlowPortn_Object = MibTableColumn
pm1004vencCfgClientThreshrxpowlowPortn = _Pm1004vencCfgClientThreshrxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 1, 1, 20),
    _Pm1004vencCfgClientThreshrxpowlowPortn_Type()
)
pm1004vencCfgClientThreshrxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgClientThreshrxpowlowPortn.setStatus("current")
_Pm1004vencCfgLineStartupThreshTable_Object = MibTable
pm1004vencCfgLineStartupThreshTable = _Pm1004vencCfgLineStartupThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pm1004vencCfgLineStartupThreshTable.setStatus("current")
_Pm1004vencCfgLineStartupThreshEntry_Object = MibTableRow
pm1004vencCfgLineStartupThreshEntry = _Pm1004vencCfgLineStartupThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 2, 1)
)
pm1004vencCfgLineStartupThreshEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCfgLineStartupThreshIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCfgLineStartupThreshEntry.setStatus("current")


class _Pm1004vencCfgLineStartupThreshIndex_Type(Integer32):
    """Custom type pm1004vencCfgLineStartupThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCfgLineStartupThreshIndex_Type.__name__ = "Integer32"
_Pm1004vencCfgLineStartupThreshIndex_Object = MibTableColumn
pm1004vencCfgLineStartupThreshIndex = _Pm1004vencCfgLineStartupThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 2, 1, 1),
    _Pm1004vencCfgLineStartupThreshIndex_Type()
)
pm1004vencCfgLineStartupThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgLineStartupThreshIndex.setStatus("current")


class _Pm1004vencCfgLineThreshtxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLineThreshtxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLineThreshtxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLineThreshtxpowhighPortn_Object = MibTableColumn
pm1004vencCfgLineThreshtxpowhighPortn = _Pm1004vencCfgLineThreshtxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 2, 1, 15),
    _Pm1004vencCfgLineThreshtxpowhighPortn_Type()
)
pm1004vencCfgLineThreshtxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLineThreshtxpowhighPortn.setStatus("current")


class _Pm1004vencCfgLineThreshtxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLineThreshtxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLineThreshtxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLineThreshtxpowlowPortn_Object = MibTableColumn
pm1004vencCfgLineThreshtxpowlowPortn = _Pm1004vencCfgLineThreshtxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 2, 1, 16),
    _Pm1004vencCfgLineThreshtxpowlowPortn_Type()
)
pm1004vencCfgLineThreshtxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLineThreshtxpowlowPortn.setStatus("current")


class _Pm1004vencCfgLineThreshrxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLineThreshrxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLineThreshrxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLineThreshrxpowhighPortn_Object = MibTableColumn
pm1004vencCfgLineThreshrxpowhighPortn = _Pm1004vencCfgLineThreshrxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 2, 1, 19),
    _Pm1004vencCfgLineThreshrxpowhighPortn_Type()
)
pm1004vencCfgLineThreshrxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLineThreshrxpowhighPortn.setStatus("current")


class _Pm1004vencCfgLineThreshrxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLineThreshrxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLineThreshrxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLineThreshrxpowlowPortn_Object = MibTableColumn
pm1004vencCfgLineThreshrxpowlowPortn = _Pm1004vencCfgLineThreshrxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 4, 2, 1, 20),
    _Pm1004vencCfgLineThreshrxpowlowPortn_Type()
)
pm1004vencCfgLineThreshrxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLineThreshrxpowlowPortn.setStatus("current")
_Pm1004vencCfgOther_ObjectIdentity = ObjectIdentity
pm1004vencCfgOther = _Pm1004vencCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 5)
)
_Pm1004venctablemoduleOther_ObjectIdentity = ObjectIdentity
pm1004venctablemoduleOther = _Pm1004venctablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 5, 1)
)


class _Pm1004vencCfgmode_Type(Unsigned32):
    """Custom type pm1004vencCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgmode_Type.__name__ = "Unsigned32"
_Pm1004vencCfgmode_Object = MibScalar
pm1004vencCfgmode = _Pm1004vencCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 5, 1, 2),
    _Pm1004vencCfgmode_Type()
)
pm1004vencCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgmode.setStatus("current")
_Pm1004vencCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm1004vencCfgStartuptlh = _Pm1004vencCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6)
)
_Pm1004vencCfgOtxtlhTable_Object = MibTable
pm1004vencCfgOtxtlhTable = _Pm1004vencCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm1004vencCfgOtxtlhTable.setStatus("current")
_Pm1004vencCfgOtxtlhEntry_Object = MibTableRow
pm1004vencCfgOtxtlhEntry = _Pm1004vencCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1)
)
pm1004vencCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCfgOtxtlhEntry.setStatus("current")


class _Pm1004vencCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm1004vencCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm1004vencCfgOtxtlhIndex_Object = MibTableColumn
pm1004vencCfgOtxtlhIndex = _Pm1004vencCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 1),
    _Pm1004vencCfgOtxtlhIndex_Type()
)
pm1004vencCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgOtxtlhIndex.setStatus("current")


class _Pm1004vencCfgNuPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgNuPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgNuPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgNuPortn_Object = MibTableColumn
pm1004vencCfgNuPortn = _Pm1004vencCfgNuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 3),
    _Pm1004vencCfgNuPortn_Type()
)
pm1004vencCfgNuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgNuPortn.setStatus("deprecated")


class _Pm1004vencCfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLineDitherRatePortn_Object = MibTableColumn
pm1004vencCfgLineDitherRatePortn = _Pm1004vencCfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 4),
    _Pm1004vencCfgLineDitherRatePortn_Type()
)
pm1004vencCfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLineDitherRatePortn.setStatus("current")


class _Pm1004vencCfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLineDitherFhzPortn_Object = MibTableColumn
pm1004vencCfgLineDitherFhzPortn = _Pm1004vencCfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 5),
    _Pm1004vencCfgLineDitherFhzPortn_Type()
)
pm1004vencCfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLineDitherFhzPortn.setStatus("current")


class _Pm1004vencCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLinePwrLaserPortn_Object = MibTableColumn
pm1004vencCfgLinePwrLaserPortn = _Pm1004vencCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 6),
    _Pm1004vencCfgLinePwrLaserPortn_Type()
)
pm1004vencCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLinePwrLaserPortn.setStatus("current")


class _Pm1004vencCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLineFCurrentPortn_Object = MibTableColumn
pm1004vencCfgLineFCurrentPortn = _Pm1004vencCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 7),
    _Pm1004vencCfgLineFCurrentPortn_Type()
)
pm1004vencCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLineFCurrentPortn.setStatus("current")


class _Pm1004vencCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLineGridCurrentPortn_Object = MibTableColumn
pm1004vencCfgLineGridCurrentPortn = _Pm1004vencCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 8),
    _Pm1004vencCfgLineGridCurrentPortn_Type()
)
pm1004vencCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLineGridCurrentPortn.setStatus("current")


class _Pm1004vencCfgFPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgFPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgFPortn_Object = MibTableColumn
pm1004vencCfgFPortn = _Pm1004vencCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 9),
    _Pm1004vencCfgFPortn_Type()
)
pm1004vencCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgFPortn.setStatus("current")


class _Pm1004vencCfgReservedPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgReservedPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgReservedPortn_Object = MibTableColumn
pm1004vencCfgReservedPortn = _Pm1004vencCfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 10),
    _Pm1004vencCfgReservedPortn_Type()
)
pm1004vencCfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgReservedPortn.setStatus("deprecated")


class _Pm1004vencCfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLinePhotodiodeModePortn_Object = MibTableColumn
pm1004vencCfgLinePhotodiodeModePortn = _Pm1004vencCfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 11),
    _Pm1004vencCfgLinePhotodiodeModePortn_Type()
)
pm1004vencCfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLinePhotodiodeModePortn.setStatus("current")


class _Pm1004vencCfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLinePhotodiodeValuePortn_Object = MibTableColumn
pm1004vencCfgLinePhotodiodeValuePortn = _Pm1004vencCfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 6, 1, 1, 12),
    _Pm1004vencCfgLinePhotodiodeValuePortn_Type()
)
pm1004vencCfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgLinePhotodiodeValuePortn.setStatus("current")
_Pm1004vencCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm1004vencCfgStartuptablefive = _Pm1004vencCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 7)
)
_Pm1004vencCfgOtxtlhcapabilitiesTable_Object = MibTable
pm1004vencCfgOtxtlhcapabilitiesTable = _Pm1004vencCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 7, 1)
)
if mibBuilder.loadTexts:
    pm1004vencCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm1004vencCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm1004vencCfgOtxtlhcapabilitiesEntry = _Pm1004vencCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 7, 1, 1)
)
pm1004vencCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm1004vencCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm1004vencCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm1004vencCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm1004vencCfgOtxtlhcapabilitiesIndex = _Pm1004vencCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 7, 1, 1, 1),
    _Pm1004vencCfgOtxtlhcapabilitiesIndex_Type()
)
pm1004vencCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm1004vencCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm1004vencCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgComponentTypePortn_Object = MibTableColumn
pm1004vencCfgComponentTypePortn = _Pm1004vencCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 7, 1, 1, 3),
    _Pm1004vencCfgComponentTypePortn_Type()
)
pm1004vencCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgComponentTypePortn.setStatus("current")


class _Pm1004vencCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgMiscellaneousPortn_Object = MibTableColumn
pm1004vencCfgMiscellaneousPortn = _Pm1004vencCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 7, 1, 1, 4),
    _Pm1004vencCfgMiscellaneousPortn_Type()
)
pm1004vencCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgMiscellaneousPortn.setStatus("current")


class _Pm1004vencCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgFirstChannelPortn_Object = MibTableColumn
pm1004vencCfgFirstChannelPortn = _Pm1004vencCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 7, 1, 1, 5),
    _Pm1004vencCfgFirstChannelPortn_Type()
)
pm1004vencCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgFirstChannelPortn.setStatus("current")


class _Pm1004vencCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgLastChannelPortn_Object = MibTableColumn
pm1004vencCfgLastChannelPortn = _Pm1004vencCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 7, 1, 1, 6),
    _Pm1004vencCfgLastChannelPortn_Type()
)
pm1004vencCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgLastChannelPortn.setStatus("current")


class _Pm1004vencCfgGridPortn_Type(Unsigned32):
    """Custom type pm1004vencCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vencCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm1004vencCfgGridPortn_Object = MibTableColumn
pm1004vencCfgGridPortn = _Pm1004vencCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 7, 1, 1, 7),
    _Pm1004vencCfgGridPortn_Type()
)
pm1004vencCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencCfgGridPortn.setStatus("current")
_Pm1004vencCfgWriteConfiguration_Type = EkiOnOff
_Pm1004vencCfgWriteConfiguration_Object = MibScalar
pm1004vencCfgWriteConfiguration = _Pm1004vencCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 9, 257),
    _Pm1004vencCfgWriteConfiguration_Type()
)
pm1004vencCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencCfgWriteConfiguration.setStatus("current")
_Pm1004venctraps_ObjectIdentity = ObjectIdentity
pm1004venctraps = _Pm1004venctraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10)
)


class _Pm1004venctrapPortNumber_Type(Integer32):
    """Custom type pm1004venctrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004venctrapPortNumber_Type.__name__ = "Integer32"
_Pm1004venctrapPortNumber_Object = MibScalar
pm1004venctrapPortNumber = _Pm1004venctrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 2),
    _Pm1004venctrapPortNumber_Type()
)
pm1004venctrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004venctrapPortNumber.setStatus("current")


class _Pm1004venctrapLineNumber_Type(Integer32):
    """Custom type pm1004venctrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004venctrapLineNumber_Type.__name__ = "Integer32"
_Pm1004venctrapLineNumber_Object = MibScalar
pm1004venctrapLineNumber = _Pm1004venctrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 3),
    _Pm1004venctrapLineNumber_Type()
)
pm1004venctrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004venctrapLineNumber.setStatus("current")


class _Pm1004venctrapBoardNumber_Type(Integer32):
    """Custom type pm1004venctrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004venctrapBoardNumber_Type.__name__ = "Integer32"
_Pm1004venctrapBoardNumber_Object = MibScalar
pm1004venctrapBoardNumber = _Pm1004venctrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 4),
    _Pm1004venctrapBoardNumber_Type()
)
pm1004venctrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004venctrapBoardNumber.setStatus("current")
_Pm1004vencMonitoring_ObjectIdentity = ObjectIdentity
pm1004vencMonitoring = _Pm1004vencMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11)
)
_Pm1004vencMonOther_ObjectIdentity = ObjectIdentity
pm1004vencMonOther = _Pm1004vencMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 1)
)
_Pm1004vencMonRmon_ObjectIdentity = ObjectIdentity
pm1004vencMonRmon = _Pm1004vencMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 1, 3)
)
_Pm1004vencMonCountersReset_Type = EkiOnOff
_Pm1004vencMonCountersReset_Object = MibScalar
pm1004vencMonCountersReset = _Pm1004vencMonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 1, 3, 359),
    _Pm1004vencMonCountersReset_Type()
)
pm1004vencMonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencMonCountersReset.setStatus("current")
_Pm1004vencMonCountersStop_Type = EkiOnOff
_Pm1004vencMonCountersStop_Object = MibScalar
pm1004vencMonCountersStop = _Pm1004vencMonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 1, 3, 360),
    _Pm1004vencMonCountersStop_Type()
)
pm1004vencMonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vencMonCountersStop.setStatus("current")
_Pm1004vencMonClient_ObjectIdentity = ObjectIdentity
pm1004vencMonClient = _Pm1004vencMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2)
)
_Pm1004vencMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm1004vencMonClientRmonCounter = _Pm1004vencMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4)
)
_Pm1004vencMonupRmonByteCntTable_Object = MibTable
pm1004vencMonupRmonByteCntTable = _Pm1004vencMonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonByteCntTable.setStatus("current")
_Pm1004vencMonupRmonByteCntEntry_Object = MibTableRow
pm1004vencMonupRmonByteCntEntry = _Pm1004vencMonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 16, 1)
)
pm1004vencMonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonByteCntEntry.setStatus("current")


class _Pm1004vencMonupRmonByteCntIndex_Type(Integer32):
    """Custom type pm1004vencMonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1004vencMonupRmonByteCntIndex_Object = MibTableColumn
pm1004vencMonupRmonByteCntIndex = _Pm1004vencMonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 16, 1, 1),
    _Pm1004vencMonupRmonByteCntIndex_Type()
)
pm1004vencMonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonByteCntIndex.setStatus("current")
_Pm1004vencMonupRmonByteCntValuePortn_Type = Counter64
_Pm1004vencMonupRmonByteCntValuePortn_Object = MibTableColumn
pm1004vencMonupRmonByteCntValuePortn = _Pm1004vencMonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 16, 1, 2),
    _Pm1004vencMonupRmonByteCntValuePortn_Type()
)
pm1004vencMonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonByteCntValuePortn.setStatus("current")
_Pm1004vencMonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1004vencMonupRmonByteCntErrorPortn_Object = MibTableColumn
pm1004vencMonupRmonByteCntErrorPortn = _Pm1004vencMonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 16, 1, 3),
    _Pm1004vencMonupRmonByteCntErrorPortn_Type()
)
pm1004vencMonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonByteCntErrorPortn.setStatus("current")
_Pm1004vencMonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1004vencMonupRmonByteCntOverloadPortn_Object = MibTableColumn
pm1004vencMonupRmonByteCntOverloadPortn = _Pm1004vencMonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 16, 1, 4),
    _Pm1004vencMonupRmonByteCntOverloadPortn_Type()
)
pm1004vencMonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonByteCntOverloadPortn.setStatus("current")
_Pm1004vencMonupRmonCrcErrorCntTable_Object = MibTable
pm1004vencMonupRmonCrcErrorCntTable = _Pm1004vencMonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 24)
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonCrcErrorCntTable.setStatus("current")
_Pm1004vencMonupRmonCrcErrorCntEntry_Object = MibTableRow
pm1004vencMonupRmonCrcErrorCntEntry = _Pm1004vencMonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 24, 1)
)
pm1004vencMonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonCrcErrorCntEntry.setStatus("current")


class _Pm1004vencMonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1004vencMonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1004vencMonupRmonCrcErrorCntIndex_Object = MibTableColumn
pm1004vencMonupRmonCrcErrorCntIndex = _Pm1004vencMonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 24, 1, 1),
    _Pm1004vencMonupRmonCrcErrorCntIndex_Type()
)
pm1004vencMonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonCrcErrorCntIndex.setStatus("current")
_Pm1004vencMonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1004vencMonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1004vencMonupRmonCrcErrorCntValuePortn = _Pm1004vencMonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 24, 1, 2),
    _Pm1004vencMonupRmonCrcErrorCntValuePortn_Type()
)
pm1004vencMonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1004vencMonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1004vencMonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1004vencMonupRmonCrcErrorCntErrorPortn = _Pm1004vencMonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 24, 1, 3),
    _Pm1004vencMonupRmonCrcErrorCntErrorPortn_Type()
)
pm1004vencMonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1004vencMonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1004vencMonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1004vencMonupRmonCrcErrorCntOverloadPortn = _Pm1004vencMonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 24, 1, 4),
    _Pm1004vencMonupRmonCrcErrorCntOverloadPortn_Type()
)
pm1004vencMonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1004vencMonupRmonPacketsCntTable_Object = MibTable
pm1004vencMonupRmonPacketsCntTable = _Pm1004vencMonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonPacketsCntTable.setStatus("current")
_Pm1004vencMonupRmonPacketsCntEntry_Object = MibTableRow
pm1004vencMonupRmonPacketsCntEntry = _Pm1004vencMonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 32, 1)
)
pm1004vencMonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonPacketsCntEntry.setStatus("current")


class _Pm1004vencMonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1004vencMonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1004vencMonupRmonPacketsCntIndex_Object = MibTableColumn
pm1004vencMonupRmonPacketsCntIndex = _Pm1004vencMonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 32, 1, 1),
    _Pm1004vencMonupRmonPacketsCntIndex_Type()
)
pm1004vencMonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonPacketsCntIndex.setStatus("current")
_Pm1004vencMonupRmonPacketsCntValuePortn_Type = Counter64
_Pm1004vencMonupRmonPacketsCntValuePortn_Object = MibTableColumn
pm1004vencMonupRmonPacketsCntValuePortn = _Pm1004vencMonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 32, 1, 2),
    _Pm1004vencMonupRmonPacketsCntValuePortn_Type()
)
pm1004vencMonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonPacketsCntValuePortn.setStatus("current")
_Pm1004vencMonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1004vencMonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1004vencMonupRmonPacketsCntErrorPortn = _Pm1004vencMonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 32, 1, 3),
    _Pm1004vencMonupRmonPacketsCntErrorPortn_Type()
)
pm1004vencMonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonPacketsCntErrorPortn.setStatus("current")
_Pm1004vencMonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1004vencMonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1004vencMonupRmonPacketsCntOverloadPortn = _Pm1004vencMonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 32, 1, 4),
    _Pm1004vencMonupRmonPacketsCntOverloadPortn_Type()
)
pm1004vencMonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1004vencMonupRmonBroadcastCntTable_Object = MibTable
pm1004vencMonupRmonBroadcastCntTable = _Pm1004vencMonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 40)
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonBroadcastCntTable.setStatus("current")
_Pm1004vencMonupRmonBroadcastCntEntry_Object = MibTableRow
pm1004vencMonupRmonBroadcastCntEntry = _Pm1004vencMonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 40, 1)
)
pm1004vencMonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonBroadcastCntEntry.setStatus("current")


class _Pm1004vencMonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pm1004vencMonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pm1004vencMonupRmonBroadcastCntIndex_Object = MibTableColumn
pm1004vencMonupRmonBroadcastCntIndex = _Pm1004vencMonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 40, 1, 1),
    _Pm1004vencMonupRmonBroadcastCntIndex_Type()
)
pm1004vencMonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonBroadcastCntIndex.setStatus("current")
_Pm1004vencMonupRmonBroadcastCntValuePortn_Type = Counter64
_Pm1004vencMonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pm1004vencMonupRmonBroadcastCntValuePortn = _Pm1004vencMonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 40, 1, 2),
    _Pm1004vencMonupRmonBroadcastCntValuePortn_Type()
)
pm1004vencMonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonBroadcastCntValuePortn.setStatus("current")
_Pm1004vencMonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pm1004vencMonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pm1004vencMonupRmonBroadcastCntErrorPortn = _Pm1004vencMonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 40, 1, 3),
    _Pm1004vencMonupRmonBroadcastCntErrorPortn_Type()
)
pm1004vencMonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pm1004vencMonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pm1004vencMonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pm1004vencMonupRmonBroadcastCntOverloadPortn = _Pm1004vencMonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 40, 1, 4),
    _Pm1004vencMonupRmonBroadcastCntOverloadPortn_Type()
)
pm1004vencMonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pm1004vencMonupRmonMulticastCntTable_Object = MibTable
pm1004vencMonupRmonMulticastCntTable = _Pm1004vencMonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonMulticastCntTable.setStatus("current")
_Pm1004vencMonupRmonMulticastCntEntry_Object = MibTableRow
pm1004vencMonupRmonMulticastCntEntry = _Pm1004vencMonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 48, 1)
)
pm1004vencMonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMonupRmonMulticastCntEntry.setStatus("current")


class _Pm1004vencMonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pm1004vencMonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pm1004vencMonupRmonMulticastCntIndex_Object = MibTableColumn
pm1004vencMonupRmonMulticastCntIndex = _Pm1004vencMonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 48, 1, 1),
    _Pm1004vencMonupRmonMulticastCntIndex_Type()
)
pm1004vencMonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonMulticastCntIndex.setStatus("current")
_Pm1004vencMonupRmonMulticastCntValuePortn_Type = Counter64
_Pm1004vencMonupRmonMulticastCntValuePortn_Object = MibTableColumn
pm1004vencMonupRmonMulticastCntValuePortn = _Pm1004vencMonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 48, 1, 2),
    _Pm1004vencMonupRmonMulticastCntValuePortn_Type()
)
pm1004vencMonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonMulticastCntValuePortn.setStatus("current")
_Pm1004vencMonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pm1004vencMonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pm1004vencMonupRmonMulticastCntErrorPortn = _Pm1004vencMonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 48, 1, 3),
    _Pm1004vencMonupRmonMulticastCntErrorPortn_Type()
)
pm1004vencMonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonMulticastCntErrorPortn.setStatus("current")
_Pm1004vencMonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pm1004vencMonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pm1004vencMonupRmonMulticastCntOverloadPortn = _Pm1004vencMonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 48, 1, 4),
    _Pm1004vencMonupRmonMulticastCntOverloadPortn_Type()
)
pm1004vencMonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupRmonMulticastCntOverloadPortn.setStatus("current")
_Pm1004vencMonupLineRmonByteCntTable_Object = MibTable
pm1004vencMonupLineRmonByteCntTable = _Pm1004vencMonupLineRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 208)
)
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonByteCntTable.setStatus("current")
_Pm1004vencMonupLineRmonByteCntEntry_Object = MibTableRow
pm1004vencMonupLineRmonByteCntEntry = _Pm1004vencMonupLineRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 208, 1)
)
pm1004vencMonupLineRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMonupLineRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonByteCntEntry.setStatus("current")


class _Pm1004vencMonupLineRmonByteCntIndex_Type(Integer32):
    """Custom type pm1004vencMonupLineRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMonupLineRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1004vencMonupLineRmonByteCntIndex_Object = MibTableColumn
pm1004vencMonupLineRmonByteCntIndex = _Pm1004vencMonupLineRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 208, 1, 1),
    _Pm1004vencMonupLineRmonByteCntIndex_Type()
)
pm1004vencMonupLineRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonByteCntIndex.setStatus("current")
_Pm1004vencMonupLineRmonByteCntValuePortn_Type = Counter64
_Pm1004vencMonupLineRmonByteCntValuePortn_Object = MibTableColumn
pm1004vencMonupLineRmonByteCntValuePortn = _Pm1004vencMonupLineRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 208, 1, 2),
    _Pm1004vencMonupLineRmonByteCntValuePortn_Type()
)
pm1004vencMonupLineRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonByteCntValuePortn.setStatus("current")
_Pm1004vencMonupLineRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1004vencMonupLineRmonByteCntErrorPortn_Object = MibTableColumn
pm1004vencMonupLineRmonByteCntErrorPortn = _Pm1004vencMonupLineRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 208, 1, 3),
    _Pm1004vencMonupLineRmonByteCntErrorPortn_Type()
)
pm1004vencMonupLineRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonByteCntErrorPortn.setStatus("current")
_Pm1004vencMonupLineRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1004vencMonupLineRmonByteCntOverloadPortn_Object = MibTableColumn
pm1004vencMonupLineRmonByteCntOverloadPortn = _Pm1004vencMonupLineRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 208, 1, 4),
    _Pm1004vencMonupLineRmonByteCntOverloadPortn_Type()
)
pm1004vencMonupLineRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonByteCntOverloadPortn.setStatus("current")
_Pm1004vencMonupLineRmonCrcErrorCntTable_Object = MibTable
pm1004vencMonupLineRmonCrcErrorCntTable = _Pm1004vencMonupLineRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 209)
)
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonCrcErrorCntTable.setStatus("current")
_Pm1004vencMonupLineRmonCrcErrorCntEntry_Object = MibTableRow
pm1004vencMonupLineRmonCrcErrorCntEntry = _Pm1004vencMonupLineRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 209, 1)
)
pm1004vencMonupLineRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMonupLineRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonCrcErrorCntEntry.setStatus("current")


class _Pm1004vencMonupLineRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1004vencMonupLineRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMonupLineRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1004vencMonupLineRmonCrcErrorCntIndex_Object = MibTableColumn
pm1004vencMonupLineRmonCrcErrorCntIndex = _Pm1004vencMonupLineRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 209, 1, 1),
    _Pm1004vencMonupLineRmonCrcErrorCntIndex_Type()
)
pm1004vencMonupLineRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonCrcErrorCntIndex.setStatus("current")
_Pm1004vencMonupLineRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1004vencMonupLineRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1004vencMonupLineRmonCrcErrorCntValuePortn = _Pm1004vencMonupLineRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 209, 1, 2),
    _Pm1004vencMonupLineRmonCrcErrorCntValuePortn_Type()
)
pm1004vencMonupLineRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1004vencMonupLineRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1004vencMonupLineRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1004vencMonupLineRmonCrcErrorCntErrorPortn = _Pm1004vencMonupLineRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 209, 1, 3),
    _Pm1004vencMonupLineRmonCrcErrorCntErrorPortn_Type()
)
pm1004vencMonupLineRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1004vencMonupLineRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1004vencMonupLineRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1004vencMonupLineRmonCrcErrorCntOverloadPortn = _Pm1004vencMonupLineRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 209, 1, 4),
    _Pm1004vencMonupLineRmonCrcErrorCntOverloadPortn_Type()
)
pm1004vencMonupLineRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1004vencMonupLineRmonPacketsCntTable_Object = MibTable
pm1004vencMonupLineRmonPacketsCntTable = _Pm1004vencMonupLineRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 210)
)
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonPacketsCntTable.setStatus("current")
_Pm1004vencMonupLineRmonPacketsCntEntry_Object = MibTableRow
pm1004vencMonupLineRmonPacketsCntEntry = _Pm1004vencMonupLineRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 210, 1)
)
pm1004vencMonupLineRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004venc-MIB", "pm1004vencMonupLineRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonPacketsCntEntry.setStatus("current")


class _Pm1004vencMonupLineRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1004vencMonupLineRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vencMonupLineRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1004vencMonupLineRmonPacketsCntIndex_Object = MibTableColumn
pm1004vencMonupLineRmonPacketsCntIndex = _Pm1004vencMonupLineRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 210, 1, 1),
    _Pm1004vencMonupLineRmonPacketsCntIndex_Type()
)
pm1004vencMonupLineRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonPacketsCntIndex.setStatus("current")
_Pm1004vencMonupLineRmonPacketsCntValuePortn_Type = Counter64
_Pm1004vencMonupLineRmonPacketsCntValuePortn_Object = MibTableColumn
pm1004vencMonupLineRmonPacketsCntValuePortn = _Pm1004vencMonupLineRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 210, 1, 2),
    _Pm1004vencMonupLineRmonPacketsCntValuePortn_Type()
)
pm1004vencMonupLineRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonPacketsCntValuePortn.setStatus("current")
_Pm1004vencMonupLineRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1004vencMonupLineRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1004vencMonupLineRmonPacketsCntErrorPortn = _Pm1004vencMonupLineRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 210, 1, 3),
    _Pm1004vencMonupLineRmonPacketsCntErrorPortn_Type()
)
pm1004vencMonupLineRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonPacketsCntErrorPortn.setStatus("current")
_Pm1004vencMonupLineRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1004vencMonupLineRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1004vencMonupLineRmonPacketsCntOverloadPortn = _Pm1004vencMonupLineRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 2, 4, 210, 1, 4),
    _Pm1004vencMonupLineRmonPacketsCntOverloadPortn_Type()
)
pm1004vencMonupLineRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vencMonupLineRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1004vencMonLine_ObjectIdentity = ObjectIdentity
pm1004vencMonLine = _Pm1004vencMonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 3)
)
_Pm1004vencMonLineRmonCounter_ObjectIdentity = ObjectIdentity
pm1004vencMonLineRmonCounter = _Pm1004vencMonLineRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 43, 11, 3, 4)
)

# Managed Objects groups


# Notification objects

pm1004vencLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 30)
)
pm1004vencLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapLineNumber"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1004vencLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 31)
)
pm1004vencLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapLineNumber"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1004vencLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 32)
)
pm1004vencLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapLineNumber"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004vencLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 33)
)
pm1004vencLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapLineNumber"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1004vencLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 34)
)
pm1004vencLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmLineFailPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapLineNumber"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencLineTrapCritGoesOn.setStatus(
        "current"
    )

pm1004vencLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 35)
)
pm1004vencLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmLineFailPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapLineNumber"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencLineTrapCritGoesOff.setStatus(
        "current"
    )

pm1004vencClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 44)
)
pm1004vencClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmFailAccPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapPortNumber"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencClientTrapCritGoesOn.setStatus(
        "current"
    )

pm1004vencClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 45)
)
pm1004vencClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmFailAccPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapPortNumber"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencClientTrapCritGoesOff.setStatus(
        "current"
    )

pm1004vencPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 50)
)
pm1004vencPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmDefFuseB"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmDefFuseA"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004vencPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 43, 10, 51)
)
pm1004vencPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmDefFuseB"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004vencAlmDefFuseA"),
        ("EKINOPS-Pm1004venc-MIB", "pm1004venctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vencPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1004venc-MIB",
    **{"Pm1004vencModeTimeSlot": Pm1004vencModeTimeSlot,
       "Pm1004vencModeAddDrop": Pm1004vencModeAddDrop,
       "Pm1004vencProtectionTimeSlot": Pm1004vencProtectionTimeSlot,
       "Pm1004vencProtectionStartUp": Pm1004vencProtectionStartUp,
       "Pm1004vencDccMode": Pm1004vencDccMode,
       "Pm1004vencClientOosMode": Pm1004vencClientOosMode,
       "Pm1004vencKeyMode": Pm1004vencKeyMode,
       "Pm1004vencOtxMode": Pm1004vencOtxMode,
       "Pm1004vencOtxGrid": Pm1004vencOtxGrid,
       "Pm1004vencAdjustValue": Pm1004vencAdjustValue,
       "Pm1004vencOtxChannel": Pm1004vencOtxChannel,
       "modulePm1004venc": modulePm1004venc,
       "pm1004vencalarms": pm1004vencalarms,
       "pm1004vencAlmOther": pm1004vencAlmOther,
       "pm1004vencAlmOtherNurg": pm1004vencAlmOtherNurg,
       "pm1004vencAlmsynthAlm2": pm1004vencAlmsynthAlm2,
       "pm1004vencAlmConfTableSave": pm1004vencAlmConfTableSave,
       "pm1004vencAlmInvUpload": pm1004vencAlmInvUpload,
       "pm1004vencAlmConfTableLoad": pm1004vencAlmConfTableLoad,
       "pm1004vencAlmCorrelatOff": pm1004vencAlmCorrelatOff,
       "pm1004vencAlmMaintenanceOn": pm1004vencAlmMaintenanceOn,
       "pm1004vencAlmOtherUrg": pm1004vencAlmOtherUrg,
       "pm1004vencAlmmodInitFailLevel2": pm1004vencAlmmodInitFailLevel2,
       "pm1004vencAlmLedFail": pm1004vencAlmLedFail,
       "pm1004vencAlmNextColdBootForced": pm1004vencAlmNextColdBootForced,
       "pm1004vencAlmBootUndone": pm1004vencAlmBootUndone,
       "pm1004vencAlmResetHwInitFail": pm1004vencAlmResetHwInitFail,
       "pm1004vencAlmSwInitFail": pm1004vencAlmSwInitFail,
       "pm1004vencAlmmodInitFailLevel3": pm1004vencAlmmodInitFailLevel3,
       "pm1004vencAlmGwIdentFail": pm1004vencAlmGwIdentFail,
       "pm1004vencAlmObmTypeReadFail": pm1004vencAlmObmTypeReadFail,
       "pm1004vencAlmInitModuleFail": pm1004vencAlmInitModuleFail,
       "pm1004vencAlmXfp1InitFail": pm1004vencAlmXfp1InitFail,
       "pm1004vencAlmXfp2InitFail": pm1004vencAlmXfp2InitFail,
       "pm1004vencAlmLine1InitFail": pm1004vencAlmLine1InitFail,
       "pm1004vencAlmLine2InitFail": pm1004vencAlmLine2InitFail,
       "pm1004vencAlmClient1InitFail": pm1004vencAlmClient1InitFail,
       "pm1004vencAlmClient2InitFail": pm1004vencAlmClient2InitFail,
       "pm1004vencAlmClient3InitFail": pm1004vencAlmClient3InitFail,
       "pm1004vencAlmClient4InitFail": pm1004vencAlmClient4InitFail,
       "pm1004vencAlmclientRxProt": pm1004vencAlmclientRxProt,
       "pm1004vencAlmAdddropClient1West": pm1004vencAlmAdddropClient1West,
       "pm1004vencAlmAdddropClient2West": pm1004vencAlmAdddropClient2West,
       "pm1004vencAlmAdddropClient3West": pm1004vencAlmAdddropClient3West,
       "pm1004vencAlmAdddropClient4West": pm1004vencAlmAdddropClient4West,
       "pm1004vencAlmAdddropClient1East": pm1004vencAlmAdddropClient1East,
       "pm1004vencAlmAdddropClient2East": pm1004vencAlmAdddropClient2East,
       "pm1004vencAlmAdddropClient3East": pm1004vencAlmAdddropClient3East,
       "pm1004vencAlmAdddropClient4East": pm1004vencAlmAdddropClient4East,
       "pm1004vencAlmmodOther": pm1004vencAlmmodOther,
       "pm1004vencAlmAesDecodFail": pm1004vencAlmAesDecodFail,
       "pm1004vencAlmOtherCrit": pm1004vencAlmOtherCrit,
       "pm1004vencAlmsynthAlm0": pm1004vencAlmsynthAlm0,
       "pm1004vencAlmModGlobFail": pm1004vencAlmModGlobFail,
       "pm1004vencAlmDefFuseA": pm1004vencAlmDefFuseA,
       "pm1004vencAlmDefFuseB": pm1004vencAlmDefFuseB,
       "pm1004vencAlmClient": pm1004vencAlmClient,
       "pm1004vencAlmClientNurg": pm1004vencAlmClientNurg,
       "pm1004vencAlmClientUrg": pm1004vencAlmClientUrg,
       "pm1004vencAlmClientCrit": pm1004vencAlmClientCrit,
       "pm1004vencAlmsynthAlmPortTable": pm1004vencAlmsynthAlmPortTable,
       "pm1004vencAlmsynthAlmPortEntry": pm1004vencAlmsynthAlmPortEntry,
       "pm1004vencAlmsynthAlmPortIndex": pm1004vencAlmsynthAlmPortIndex,
       "pm1004vencAlmHwFailAccPortn": pm1004vencAlmHwFailAccPortn,
       "pm1004vencAlmDwLsdPortn": pm1004vencAlmDwLsdPortn,
       "pm1004vencAlmClientLocalOosTxPortn": pm1004vencAlmClientLocalOosTxPortn,
       "pm1004vencAlmClientLocalOosRxPortn": pm1004vencAlmClientLocalOosRxPortn,
       "pm1004vencAlmDwCaisPortn": pm1004vencAlmDwCaisPortn,
       "pm1004vencAlmFailAccPortn": pm1004vencAlmFailAccPortn,
       "pm1004vencAlmUpCsfPortn": pm1004vencAlmUpCsfPortn,
       "pm1004vencAlmaccessioAlmTable": pm1004vencAlmaccessioAlmTable,
       "pm1004vencAlmaccessioAlmEntry": pm1004vencAlmaccessioAlmEntry,
       "pm1004vencAlmaccessioAlmIndex": pm1004vencAlmaccessioAlmIndex,
       "pm1004vencAlmUpLosPortn": pm1004vencAlmUpLosPortn,
       "pm1004vencAlmmapperDeAlmTable": pm1004vencAlmmapperDeAlmTable,
       "pm1004vencAlmmapperDeAlmEntry": pm1004vencAlmmapperDeAlmEntry,
       "pm1004vencAlmmapperDeAlmIndex": pm1004vencAlmmapperDeAlmIndex,
       "pm1004vencAlmUpAccOosPortn": pm1004vencAlmUpAccOosPortn,
       "pm1004vencAlmUpBufferOvlPortn": pm1004vencAlmUpBufferOvlPortn,
       "pm1004vencAlmDwCsfDetPortn": pm1004vencAlmDwCsfDetPortn,
       "pm1004vencAlmDwBufferOvlPortn": pm1004vencAlmDwBufferOvlPortn,
       "pm1004vencAlmvideoProtocolStatusTable": pm1004vencAlmvideoProtocolStatusTable,
       "pm1004vencAlmvideoProtocolStatusEntry": pm1004vencAlmvideoProtocolStatusEntry,
       "pm1004vencAlmvideoProtocolStatusIndex": pm1004vencAlmvideoProtocolStatusIndex,
       "pm1004vencAlmSdiTxPortn": pm1004vencAlmSdiTxPortn,
       "pm1004vencAlmHdSdiPalTxPortn": pm1004vencAlmHdSdiPalTxPortn,
       "pm1004vencAlmHdSdiNtscTxPortn": pm1004vencAlmHdSdiNtscTxPortn,
       "pm1004vencAlmDvbAsiTxPortn": pm1004vencAlmDvbAsiTxPortn,
       "pm1004vencAlmSdiRxPortn": pm1004vencAlmSdiRxPortn,
       "pm1004vencAlmHdSdiPalRxPortn": pm1004vencAlmHdSdiPalRxPortn,
       "pm1004vencAlmHdSdiNtscRxPortn": pm1004vencAlmHdSdiNtscRxPortn,
       "pm1004vencAlmDvbAsiRxPortn": pm1004vencAlmDvbAsiRxPortn,
       "pm1004vencAlmLine": pm1004vencAlmLine,
       "pm1004vencAlmLineNurg": pm1004vencAlmLineNurg,
       "pm1004vencAlmlineXfp1WarningsTable": pm1004vencAlmlineXfp1WarningsTable,
       "pm1004vencAlmlineXfp1WarningsEntry": pm1004vencAlmlineXfp1WarningsEntry,
       "pm1004vencAlmlineXfp1WarningsIndex": pm1004vencAlmlineXfp1WarningsIndex,
       "pm1004vencAlmTxPowerLowWarningPortn": pm1004vencAlmTxPowerLowWarningPortn,
       "pm1004vencAlmTxPowerHighWarningPortn": pm1004vencAlmTxPowerHighWarningPortn,
       "pm1004vencAlmTxBiasLowWarningPortn": pm1004vencAlmTxBiasLowWarningPortn,
       "pm1004vencAlmTxBiasHighWarningPortn": pm1004vencAlmTxBiasHighWarningPortn,
       "pm1004vencAlmTempLowWarningPortn": pm1004vencAlmTempLowWarningPortn,
       "pm1004vencAlmTempHighWarningPortn": pm1004vencAlmTempHighWarningPortn,
       "pm1004vencAlmRxPowerLowWarningPortn": pm1004vencAlmRxPowerLowWarningPortn,
       "pm1004vencAlmRxPowerHighWarningPortn": pm1004vencAlmRxPowerHighWarningPortn,
       "pm1004vencAlmlineOtx1TlhWarningsTable": pm1004vencAlmlineOtx1TlhWarningsTable,
       "pm1004vencAlmlineOtx1TlhWarningsEntry": pm1004vencAlmlineOtx1TlhWarningsEntry,
       "pm1004vencAlmlineOtx1TlhWarningsIndex": pm1004vencAlmlineOtx1TlhWarningsIndex,
       "pm1004vencAlmLineModulatorAgingHighWarningPortn": pm1004vencAlmLineModulatorAgingHighWarningPortn,
       "pm1004vencAlmLineAgingHighWarningPortn": pm1004vencAlmLineAgingHighWarningPortn,
       "pm1004vencAlmLineFreqDevHighWarningPortn": pm1004vencAlmLineFreqDevHighWarningPortn,
       "pm1004vencAlmLineLaserTempHighWarningPortn": pm1004vencAlmLineLaserTempHighWarningPortn,
       "pm1004vencAlmLineUrg": pm1004vencAlmLineUrg,
       "pm1004vencAlmlineXfp1AlarmTable": pm1004vencAlmlineXfp1AlarmTable,
       "pm1004vencAlmlineXfp1AlarmEntry": pm1004vencAlmlineXfp1AlarmEntry,
       "pm1004vencAlmlineXfp1AlarmIndex": pm1004vencAlmlineXfp1AlarmIndex,
       "pm1004vencAlmTxPowerLowAlarmPortn": pm1004vencAlmTxPowerLowAlarmPortn,
       "pm1004vencAlmTxPowerHighAlarmPortn": pm1004vencAlmTxPowerHighAlarmPortn,
       "pm1004vencAlmTxBiasLowAlarmPortn": pm1004vencAlmTxBiasLowAlarmPortn,
       "pm1004vencAlmTxBiasHighAlarmPortn": pm1004vencAlmTxBiasHighAlarmPortn,
       "pm1004vencAlmTempLowAlarmPortn": pm1004vencAlmTempLowAlarmPortn,
       "pm1004vencAlmTempHighAlarmPortn": pm1004vencAlmTempHighAlarmPortn,
       "pm1004vencAlmRxPowerLowAlarmPortn": pm1004vencAlmRxPowerLowAlarmPortn,
       "pm1004vencAlmRxPowerHighAlarmPortn": pm1004vencAlmRxPowerHighAlarmPortn,
       "pm1004vencAlmlineXfp1CritTable": pm1004vencAlmlineXfp1CritTable,
       "pm1004vencAlmlineXfp1CritEntry": pm1004vencAlmlineXfp1CritEntry,
       "pm1004vencAlmlineXfp1CritIndex": pm1004vencAlmlineXfp1CritIndex,
       "pm1004vencAlmTxPowerLowCritPortn": pm1004vencAlmTxPowerLowCritPortn,
       "pm1004vencAlmTxPowerHighCritPortn": pm1004vencAlmTxPowerHighCritPortn,
       "pm1004vencAlmRxPowerLowCritPortn": pm1004vencAlmRxPowerLowCritPortn,
       "pm1004vencAlmRxPowerHighCritPortn": pm1004vencAlmRxPowerHighCritPortn,
       "pm1004vencAlmlineXfp1SupplyAlarmTable": pm1004vencAlmlineXfp1SupplyAlarmTable,
       "pm1004vencAlmlineXfp1SupplyAlarmEntry": pm1004vencAlmlineXfp1SupplyAlarmEntry,
       "pm1004vencAlmlineXfp1SupplyAlarmIndex": pm1004vencAlmlineXfp1SupplyAlarmIndex,
       "pm1004vencAlmVee5LowAlarmPortn": pm1004vencAlmVee5LowAlarmPortn,
       "pm1004vencAlmVee5HighAlarmPortn": pm1004vencAlmVee5HighAlarmPortn,
       "pm1004vencAlmVcc2LowAlarmPortn": pm1004vencAlmVcc2LowAlarmPortn,
       "pm1004vencAlmVcc2HighAlarmPortn": pm1004vencAlmVcc2HighAlarmPortn,
       "pm1004vencAlmVcc3LowAlarmPortn": pm1004vencAlmVcc3LowAlarmPortn,
       "pm1004vencAlmVcc3HighAlarmPortn": pm1004vencAlmVcc3HighAlarmPortn,
       "pm1004vencAlmVcc5LowAlarmPortn": pm1004vencAlmVcc5LowAlarmPortn,
       "pm1004vencAlmVcc5HighAlarmPortn": pm1004vencAlmVcc5HighAlarmPortn,
       "pm1004vencAlmVee5LowWarningPortn": pm1004vencAlmVee5LowWarningPortn,
       "pm1004vencAlmVee5HighWarningPortn": pm1004vencAlmVee5HighWarningPortn,
       "pm1004vencAlmVcc2LowWarningPortn": pm1004vencAlmVcc2LowWarningPortn,
       "pm1004vencAlmVcc2HighWarningPortn": pm1004vencAlmVcc2HighWarningPortn,
       "pm1004vencAlmVcc3LowWarningPortn": pm1004vencAlmVcc3LowWarningPortn,
       "pm1004vencAlmVcc3HighWarningPortn": pm1004vencAlmVcc3HighWarningPortn,
       "pm1004vencAlmVcc5LowWarningPortn": pm1004vencAlmVcc5LowWarningPortn,
       "pm1004vencAlmVcc5HighWarningPortn": pm1004vencAlmVcc5HighWarningPortn,
       "pm1004vencAlmlineOtx1TlhAlarmsTable": pm1004vencAlmlineOtx1TlhAlarmsTable,
       "pm1004vencAlmlineOtx1TlhAlarmsEntry": pm1004vencAlmlineOtx1TlhAlarmsEntry,
       "pm1004vencAlmlineOtx1TlhAlarmsIndex": pm1004vencAlmlineOtx1TlhAlarmsIndex,
       "pm1004vencAlmLineModulatorAgingHighAlaPortn": pm1004vencAlmLineModulatorAgingHighAlaPortn,
       "pm1004vencAlmLineAgingHighAlaPortn": pm1004vencAlmLineAgingHighAlaPortn,
       "pm1004vencAlmLineFreqDevHighAlaPortn": pm1004vencAlmLineFreqDevHighAlaPortn,
       "pm1004vencAlmLineLaserTempHighAlaPortn": pm1004vencAlmLineLaserTempHighAlaPortn,
       "pm1004vencAlmLineCrit": pm1004vencAlmLineCrit,
       "pm1004vencAlmsynthAlmLineTable": pm1004vencAlmsynthAlmLineTable,
       "pm1004vencAlmsynthAlmLineEntry": pm1004vencAlmsynthAlmLineEntry,
       "pm1004vencAlmsynthAlmLineIndex": pm1004vencAlmsynthAlmLineIndex,
       "pm1004vencAlmXfpAbsentPortn": pm1004vencAlmXfpAbsentPortn,
       "pm1004vencAlmXfpInitNotComplPortn": pm1004vencAlmXfpInitNotComplPortn,
       "pm1004vencAlmLineHwFailPortn": pm1004vencAlmLineHwFailPortn,
       "pm1004vencAlmXfpTxOffPortn": pm1004vencAlmXfpTxOffPortn,
       "pm1004vencAlmLineLocalOosPortn": pm1004vencAlmLineLocalOosPortn,
       "pm1004vencAlmLineDdmWarningPortn": pm1004vencAlmLineDdmWarningPortn,
       "pm1004vencAlmLineDdmAlmPortn": pm1004vencAlmLineDdmAlmPortn,
       "pm1004vencAlmLineDdmCritPortn": pm1004vencAlmLineDdmCritPortn,
       "pm1004vencAlmLineFailPortn": pm1004vencAlmLineFailPortn,
       "pm1004vencAlmLineActivePortn": pm1004vencAlmLineActivePortn,
       "pm1004vencAlmdfrmAlmTable": pm1004vencAlmdfrmAlmTable,
       "pm1004vencAlmdfrmAlmEntry": pm1004vencAlmdfrmAlmEntry,
       "pm1004vencAlmdfrmAlmIndex": pm1004vencAlmdfrmAlmIndex,
       "pm1004vencAlmLineLossofsyncPortn": pm1004vencAlmLineLossofsyncPortn,
       "pm1004vencAlmlineSyncAlarmsTable": pm1004vencAlmlineSyncAlarmsTable,
       "pm1004vencAlmlineSyncAlarmsEntry": pm1004vencAlmlineSyncAlarmsEntry,
       "pm1004vencAlmlineSyncAlarmsIndex": pm1004vencAlmlineSyncAlarmsIndex,
       "pm1004vencAlmDwLockerrPortn": pm1004vencAlmDwLockerrPortn,
       "pm1004vencAlmUpLockerrPortn": pm1004vencAlmUpLockerrPortn,
       "pm1004vencAlmDwLosPortn": pm1004vencAlmDwLosPortn,
       "pm1004vencAlmlineXfp1AlarmsTable": pm1004vencAlmlineXfp1AlarmsTable,
       "pm1004vencAlmlineXfp1AlarmsEntry": pm1004vencAlmlineXfp1AlarmsEntry,
       "pm1004vencAlmlineXfp1AlarmsIndex": pm1004vencAlmlineXfp1AlarmsIndex,
       "pm1004vencAlmModNrPortn": pm1004vencAlmModNrPortn,
       "pm1004vencAlmRxCdrNotLockedPortn": pm1004vencAlmRxCdrNotLockedPortn,
       "pm1004vencAlmRxNrPortn": pm1004vencAlmRxNrPortn,
       "pm1004vencAlmTxCdrNotLockedPortn": pm1004vencAlmTxCdrNotLockedPortn,
       "pm1004vencAlmTxFaultPortn": pm1004vencAlmTxFaultPortn,
       "pm1004vencAlmTxNrPortn": pm1004vencAlmTxNrPortn,
       "pm1004vencAlmWavelengthUnlockedPortn": pm1004vencAlmWavelengthUnlockedPortn,
       "pm1004vencAlmTecFaultPortn": pm1004vencAlmTecFaultPortn,
       "pm1004vencAlmApdSupplyFaultPortn": pm1004vencAlmApdSupplyFaultPortn,
       "pm1004vencmeasures": pm1004vencmeasures,
       "pm1004vencMesrOther": pm1004vencMesrOther,
       "pm1004vencMesrsynth0": pm1004vencMesrsynth0,
       "pm1004vencMesrsynth1": pm1004vencMesrsynth1,
       "pm1004vencMesrClient": pm1004vencMesrClient,
       "pm1004vencMesrLine": pm1004vencMesrLine,
       "pm1004vencMesrxfp1LxModTempMeasTable": pm1004vencMesrxfp1LxModTempMeasTable,
       "pm1004vencMesrxfp1LxModTempMeasEntry": pm1004vencMesrxfp1LxModTempMeasEntry,
       "pm1004vencMesrxfp1LxModTempMeasIndex": pm1004vencMesrxfp1LxModTempMeasIndex,
       "pm1004vencMesrxfp1LxModTempMeasPortn": pm1004vencMesrxfp1LxModTempMeasPortn,
       "pm1004vencMesrxfp1ReservedTable": pm1004vencMesrxfp1ReservedTable,
       "pm1004vencMesrxfp1ReservedEntry": pm1004vencMesrxfp1ReservedEntry,
       "pm1004vencMesrxfp1ReservedIndex": pm1004vencMesrxfp1ReservedIndex,
       "pm1004vencMesrxfp1ReservedPortn": pm1004vencMesrxfp1ReservedPortn,
       "pm1004vencMesrxfp1LoBiasCurrentMeasTable": pm1004vencMesrxfp1LoBiasCurrentMeasTable,
       "pm1004vencMesrxfp1LoBiasCurrentMeasEntry": pm1004vencMesrxfp1LoBiasCurrentMeasEntry,
       "pm1004vencMesrxfp1LoBiasCurrentMeasIndex": pm1004vencMesrxfp1LoBiasCurrentMeasIndex,
       "pm1004vencMesrxfp1LoBiasCurrentMeasPortn": pm1004vencMesrxfp1LoBiasCurrentMeasPortn,
       "pm1004vencMesrxfp1LoTxPowerMeasTable": pm1004vencMesrxfp1LoTxPowerMeasTable,
       "pm1004vencMesrxfp1LoTxPowerMeasEntry": pm1004vencMesrxfp1LoTxPowerMeasEntry,
       "pm1004vencMesrxfp1LoTxPowerMeasIndex": pm1004vencMesrxfp1LoTxPowerMeasIndex,
       "pm1004vencMesrxfp1LoTxPowerMeasPortn": pm1004vencMesrxfp1LoTxPowerMeasPortn,
       "pm1004vencMesrxfp1LiRxPowerMeasTable": pm1004vencMesrxfp1LiRxPowerMeasTable,
       "pm1004vencMesrxfp1LiRxPowerMeasEntry": pm1004vencMesrxfp1LiRxPowerMeasEntry,
       "pm1004vencMesrxfp1LiRxPowerMeasIndex": pm1004vencMesrxfp1LiRxPowerMeasIndex,
       "pm1004vencMesrxfp1LiRxPowerMeasPortn": pm1004vencMesrxfp1LiRxPowerMeasPortn,
       "pm1004vencMesrxfp1LxAux1MeasTable": pm1004vencMesrxfp1LxAux1MeasTable,
       "pm1004vencMesrxfp1LxAux1MeasEntry": pm1004vencMesrxfp1LxAux1MeasEntry,
       "pm1004vencMesrxfp1LxAux1MeasIndex": pm1004vencMesrxfp1LxAux1MeasIndex,
       "pm1004vencMesrxfp1LxAux1MeasPortn": pm1004vencMesrxfp1LxAux1MeasPortn,
       "pm1004vencMesrxfp1LxAux2MeasTable": pm1004vencMesrxfp1LxAux2MeasTable,
       "pm1004vencMesrxfp1LxAux2MeasEntry": pm1004vencMesrxfp1LxAux2MeasEntry,
       "pm1004vencMesrxfp1LxAux2MeasIndex": pm1004vencMesrxfp1LxAux2MeasIndex,
       "pm1004vencMesrxfp1LxAux2MeasPortn": pm1004vencMesrxfp1LxAux2MeasPortn,
       "pm1004vencMesrotx1AgingTable": pm1004vencMesrotx1AgingTable,
       "pm1004vencMesrotx1AgingEntry": pm1004vencMesrotx1AgingEntry,
       "pm1004vencMesrotx1AgingIndex": pm1004vencMesrotx1AgingIndex,
       "pm1004vencMesrotx1AgingPortn": pm1004vencMesrotx1AgingPortn,
       "pm1004vencMesrotx1LaserTemperatureTable": pm1004vencMesrotx1LaserTemperatureTable,
       "pm1004vencMesrotx1LaserTemperatureEntry": pm1004vencMesrotx1LaserTemperatureEntry,
       "pm1004vencMesrotx1LaserTemperatureIndex": pm1004vencMesrotx1LaserTemperatureIndex,
       "pm1004vencMesrotx1LaserTemperaturePortn": pm1004vencMesrotx1LaserTemperaturePortn,
       "pm1004vencMesrotx1FreqDeviationTable": pm1004vencMesrotx1FreqDeviationTable,
       "pm1004vencMesrotx1FreqDeviationEntry": pm1004vencMesrotx1FreqDeviationEntry,
       "pm1004vencMesrotx1FreqDeviationIndex": pm1004vencMesrotx1FreqDeviationIndex,
       "pm1004vencMesrotx1FreqDeviationPortn": pm1004vencMesrotx1FreqDeviationPortn,
       "pm1004vencMesrotx1LaserWvlengthTable": pm1004vencMesrotx1LaserWvlengthTable,
       "pm1004vencMesrotx1LaserWvlengthEntry": pm1004vencMesrotx1LaserWvlengthEntry,
       "pm1004vencMesrotx1LaserWvlengthIndex": pm1004vencMesrotx1LaserWvlengthIndex,
       "pm1004vencMesrotx1LaserWvlengthPortn": pm1004vencMesrotx1LaserWvlengthPortn,
       "pm1004venccounters": pm1004venccounters,
       "pm1004vencCntOther": pm1004vencCntOther,
       "pm1004vencCntClient": pm1004vencCntClient,
       "pm1004vencCntLine": pm1004vencCntLine,
       "pm1004vencCntdfrmB1ErrCntTable": pm1004vencCntdfrmB1ErrCntTable,
       "pm1004vencCntdfrmB1ErrCntEntry": pm1004vencCntdfrmB1ErrCntEntry,
       "pm1004vencCntdfrmB1ErrCntIndex": pm1004vencCntdfrmB1ErrCntIndex,
       "pm1004vencCntdfrmB1ErrCntValuePortn": pm1004vencCntdfrmB1ErrCntValuePortn,
       "pm1004vencCntdfrmB1ErrCntErrorPortn": pm1004vencCntdfrmB1ErrCntErrorPortn,
       "pm1004vencCntdfrmB1ErrCntOverloadPortn": pm1004vencCntdfrmB1ErrCntOverloadPortn,
       "pm1004vencCntdfrmTimCntTable": pm1004vencCntdfrmTimCntTable,
       "pm1004vencCntdfrmTimCntEntry": pm1004vencCntdfrmTimCntEntry,
       "pm1004vencCntdfrmTimCntIndex": pm1004vencCntdfrmTimCntIndex,
       "pm1004vencCntdfrmTimCntValuePortn": pm1004vencCntdfrmTimCntValuePortn,
       "pm1004vencCntdfrmTimCntErrorPortn": pm1004vencCntdfrmTimCntErrorPortn,
       "pm1004vencCntdfrmTimCntOverloadPortn": pm1004vencCntdfrmTimCntOverloadPortn,
       "pm1004vencCntCountersReset": pm1004vencCntCountersReset,
       "pm1004vencCntCountersStop": pm1004vencCntCountersStop,
       "pm1004venccontrolsWrite": pm1004venccontrolsWrite,
       "pm1004vencCtrlOther": pm1004vencCtrlOther,
       "pm1004vencCtrlconfMgnt1": pm1004vencCtrlconfMgnt1,
       "pm1004vencCtrlConf1Load1": pm1004vencCtrlConf1Load1,
       "pm1004vencCtrlConf2Load1": pm1004vencCtrlConf2Load1,
       "pm1004vencCtrlConf2Flash1": pm1004vencCtrlConf2Flash1,
       "pm1004vencCtrlConf2Clear1": pm1004vencCtrlConf2Clear1,
       "pm1004vencCtrlsynth4": pm1004vencCtrlsynth4,
       "pm1004vencCtrlCorrelatOn": pm1004vencCtrlCorrelatOn,
       "pm1004vencCtrlCorrelatOff": pm1004vencCtrlCorrelatOff,
       "pm1004vencCtrlswMgnt": pm1004vencCtrlswMgnt,
       "pm1004vencCtrlColdReset": pm1004vencCtrlColdReset,
       "pm1004vencCtrlWarmReset": pm1004vencCtrlWarmReset,
       "pm1004vencCtrlLoadSwBank1": pm1004vencCtrlLoadSwBank1,
       "pm1004vencCtrlLoadSwBank2": pm1004vencCtrlLoadSwBank2,
       "pm1004vencCtrlgwMgnt": pm1004vencCtrlgwMgnt,
       "pm1004vencCtrlCurrentGwReset": pm1004vencCtrlCurrentGwReset,
       "pm1004vencCtrlLoadGwBank1": pm1004vencCtrlLoadGwBank1,
       "pm1004vencCtrlLoadGwBank2": pm1004vencCtrlLoadGwBank2,
       "pm1004vencCtrlLoadGwBank3": pm1004vencCtrlLoadGwBank3,
       "pm1004vencCtrlLoadGwBank4": pm1004vencCtrlLoadGwBank4,
       "pm1004vencCtrlledTest": pm1004vencCtrlledTest,
       "pm1004vencCtrlGreenLed": pm1004vencCtrlGreenLed,
       "pm1004vencCtrlRedLed": pm1004vencCtrlRedLed,
       "pm1004vencCtrlLedOff": pm1004vencCtrlLedOff,
       "pm1004vencCtrlmoduleOosMode": pm1004vencCtrlmoduleOosMode,
       "pm1004vencCtrlModuleOosMode": pm1004vencCtrlModuleOosMode,
       "pm1004vencCtrlmaintenanceMode": pm1004vencCtrlmaintenanceMode,
       "pm1004vencCtrlMaintenanceMode": pm1004vencCtrlMaintenanceMode,
       "pm1004vencCtrlencryptionSelect": pm1004vencCtrlencryptionSelect,
       "pm1004vencCtrlClient": pm1004vencCtrlClient,
       "pm1004vencCtrlaccessLoopTable": pm1004vencCtrlaccessLoopTable,
       "pm1004vencCtrlaccessLoopEntry": pm1004vencCtrlaccessLoopEntry,
       "pm1004vencCtrlaccessLoopIndex": pm1004vencCtrlaccessLoopIndex,
       "pm1004vencCtrlaccessLoopPortn": pm1004vencCtrlaccessLoopPortn,
       "pm1004vencCtrlportOosModeTable": pm1004vencCtrlportOosModeTable,
       "pm1004vencCtrlportOosModeEntry": pm1004vencCtrlportOosModeEntry,
       "pm1004vencCtrlportOosModeIndex": pm1004vencCtrlportOosModeIndex,
       "pm1004vencCtrlportOosModePortn": pm1004vencCtrlportOosModePortn,
       "pm1004vencCtrlsfpOffCtrlTable": pm1004vencCtrlsfpOffCtrlTable,
       "pm1004vencCtrlsfpOffCtrlEntry": pm1004vencCtrlsfpOffCtrlEntry,
       "pm1004vencCtrlsfpOffCtrlIndex": pm1004vencCtrlsfpOffCtrlIndex,
       "pm1004vencCtrlsfpOffCtrlPortn": pm1004vencCtrlsfpOffCtrlPortn,
       "pm1004vencCtrlcsfUpInsTable": pm1004vencCtrlcsfUpInsTable,
       "pm1004vencCtrlcsfUpInsEntry": pm1004vencCtrlcsfUpInsEntry,
       "pm1004vencCtrlcsfUpInsIndex": pm1004vencCtrlcsfUpInsIndex,
       "pm1004vencCtrlcsfUpInsPortn": pm1004vencCtrlcsfUpInsPortn,
       "pm1004vencCtrlcaisDwInsTable": pm1004vencCtrlcaisDwInsTable,
       "pm1004vencCtrlcaisDwInsEntry": pm1004vencCtrlcaisDwInsEntry,
       "pm1004vencCtrlcaisDwInsIndex": pm1004vencCtrlcaisDwInsIndex,
       "pm1004vencCtrlcaisDwInsPortn": pm1004vencCtrlcaisDwInsPortn,
       "pm1004vencCtrlclientAccessTermLoopTable": pm1004vencCtrlclientAccessTermLoopTable,
       "pm1004vencCtrlclientAccessTermLoopEntry": pm1004vencCtrlclientAccessTermLoopEntry,
       "pm1004vencCtrlclientAccessTermLoopIndex": pm1004vencCtrlclientAccessTermLoopIndex,
       "pm1004vencCtrlclientAccessTermLoopPortn": pm1004vencCtrlclientAccessTermLoopPortn,
       "pm1004vencCtrlrxVideoProtocolTable": pm1004vencCtrlrxVideoProtocolTable,
       "pm1004vencCtrlrxVideoProtocolEntry": pm1004vencCtrlrxVideoProtocolEntry,
       "pm1004vencCtrlrxVideoProtocolIndex": pm1004vencCtrlrxVideoProtocolIndex,
       "pm1004vencCtrlrxVideoProtocolPortn": pm1004vencCtrlrxVideoProtocolPortn,
       "pm1004vencCtrladddropClientRxProtectTable": pm1004vencCtrladddropClientRxProtectTable,
       "pm1004vencCtrladddropClientRxProtectEntry": pm1004vencCtrladddropClientRxProtectEntry,
       "pm1004vencCtrladddropClientRxProtectIndex": pm1004vencCtrladddropClientRxProtectIndex,
       "pm1004vencCtrladddropClientRxProtectPortn": pm1004vencCtrladddropClientRxProtectPortn,
       "pm1004vencCtrladddropTsClientModeTable": pm1004vencCtrladddropTsClientModeTable,
       "pm1004vencCtrladddropTsClientModeEntry": pm1004vencCtrladddropTsClientModeEntry,
       "pm1004vencCtrladddropTsClientModeIndex": pm1004vencCtrladddropTsClientModeIndex,
       "pm1004vencCtrladddropTsClientModePortn": pm1004vencCtrladddropTsClientModePortn,
       "pm1004vencCtrlLine": pm1004vencCtrlLine,
       "pm1004vencCtrlcommAccessLoop": pm1004vencCtrlcommAccessLoop,
       "pm1004vencCtrlCommAccessloop": pm1004vencCtrlCommAccessloop,
       "pm1004vencCtrllineLoop": pm1004vencCtrllineLoop,
       "pm1004vencCtrlLineLoop": pm1004vencCtrlLineLoop,
       "pm1004vencCtrlProtMgnt": pm1004vencCtrlProtMgnt,
       "pm1004vencCtrlLineNumber": pm1004vencCtrlLineNumber,
       "pm1004vencCtrlProtMode": pm1004vencCtrlProtMode,
       "pm1004vencCtrllineOosModeTable": pm1004vencCtrllineOosModeTable,
       "pm1004vencCtrllineOosModeEntry": pm1004vencCtrllineOosModeEntry,
       "pm1004vencCtrllineOosModeIndex": pm1004vencCtrllineOosModeIndex,
       "pm1004vencCtrllineOosModePortn": pm1004vencCtrllineOosModePortn,
       "pm1004vencCtrldccEnableTable": pm1004vencCtrldccEnableTable,
       "pm1004vencCtrldccEnableEntry": pm1004vencCtrldccEnableEntry,
       "pm1004vencCtrldccEnableIndex": pm1004vencCtrldccEnableIndex,
       "pm1004vencCtrldccEnablePortn": pm1004vencCtrldccEnablePortn,
       "pm1004vencCtrlxfpOnoffTable": pm1004vencCtrlxfpOnoffTable,
       "pm1004vencCtrlxfpOnoffEntry": pm1004vencCtrlxfpOnoffEntry,
       "pm1004vencCtrlxfpOnoffIndex": pm1004vencCtrlxfpOnoffIndex,
       "pm1004vencCtrlxfpOnoffPortn": pm1004vencCtrlxfpOnoffPortn,
       "pm1004vencCtrlxfpLineLoopTable": pm1004vencCtrlxfpLineLoopTable,
       "pm1004vencCtrlxfpLineLoopEntry": pm1004vencCtrlxfpLineLoopEntry,
       "pm1004vencCtrlxfpLineLoopIndex": pm1004vencCtrlxfpLineLoopIndex,
       "pm1004vencCtrlxfpLineLoopPortn": pm1004vencCtrlxfpLineLoopPortn,
       "pm1004vencCtrlxfpXfiLoopTable": pm1004vencCtrlxfpXfiLoopTable,
       "pm1004vencCtrlxfpXfiLoopEntry": pm1004vencCtrlxfpXfiLoopEntry,
       "pm1004vencCtrlxfpXfiLoopIndex": pm1004vencCtrlxfpXfiLoopIndex,
       "pm1004vencCtrlxfpXfiLoopPortn": pm1004vencCtrlxfpXfiLoopPortn,
       "pm1004vencCtrllineTunableChannelTable": pm1004vencCtrllineTunableChannelTable,
       "pm1004vencCtrllineTunableChannelEntry": pm1004vencCtrllineTunableChannelEntry,
       "pm1004vencCtrllineTunableChannelIndex": pm1004vencCtrllineTunableChannelIndex,
       "pm1004vencCtrllineTunableChannelPortn": pm1004vencCtrllineTunableChannelPortn,
       "pm1004vencCtrllinePhotodiodeModeTable": pm1004vencCtrllinePhotodiodeModeTable,
       "pm1004vencCtrllinePhotodiodeModeEntry": pm1004vencCtrllinePhotodiodeModeEntry,
       "pm1004vencCtrllinePhotodiodeModeIndex": pm1004vencCtrllinePhotodiodeModeIndex,
       "pm1004vencCtrllinePhotodiodeModePortn": pm1004vencCtrllinePhotodiodeModePortn,
       "pm1004vencCtrllinePhotodiodeValueTable": pm1004vencCtrllinePhotodiodeValueTable,
       "pm1004vencCtrllinePhotodiodeValueEntry": pm1004vencCtrllinePhotodiodeValueEntry,
       "pm1004vencCtrllinePhotodiodeValueIndex": pm1004vencCtrllinePhotodiodeValueIndex,
       "pm1004vencCtrllinePhotodiodeValuePortn": pm1004vencCtrllinePhotodiodeValuePortn,
       "pm1004vencCtrllinePowerLaserTable": pm1004vencCtrllinePowerLaserTable,
       "pm1004vencCtrllinePowerLaserEntry": pm1004vencCtrllinePowerLaserEntry,
       "pm1004vencCtrllinePowerLaserIndex": pm1004vencCtrllinePowerLaserIndex,
       "pm1004vencCtrllinePowerLaserPortn": pm1004vencCtrllinePowerLaserPortn,
       "pm1004vencri": pm1004vencri,
       "pm1004vencriTable": pm1004vencriTable,
       "pm1004vencRinvClientTable": pm1004vencRinvClientTable,
       "pm1004vencRinvClientEntry": pm1004vencRinvClientEntry,
       "pm1004vencRinvClientIndex": pm1004vencRinvClientIndex,
       "pm1004vencRinvClient": pm1004vencRinvClient,
       "pm1004vencRinvLineTable": pm1004vencRinvLineTable,
       "pm1004vencRinvLineEntry": pm1004vencRinvLineEntry,
       "pm1004vencRinvLineIndex": pm1004vencRinvLineIndex,
       "pm1004vencRinvxfpLine": pm1004vencRinvxfpLine,
       "pm1004vencRinvReloadInventory": pm1004vencRinvReloadInventory,
       "pm1004vencRinvHwPlatform": pm1004vencRinvHwPlatform,
       "pm1004vencRinvModulePlatform": pm1004vencRinvModulePlatform,
       "pm1004vencRinvSwPlatform": pm1004vencRinvSwPlatform,
       "pm1004vencRinvGwPlatform": pm1004vencRinvGwPlatform,
       "pm1004vencdownload": pm1004vencdownload,
       "pm1004vencDwlOther": pm1004vencDwlOther,
       "pm1004vencDwlrestartProcess": pm1004vencDwlrestartProcess,
       "pm1004vencDwlWarmRestartProcessed": pm1004vencDwlWarmRestartProcessed,
       "pm1004vencDwlColdRestartProcessed": pm1004vencDwlColdRestartProcessed,
       "pm1004vencDwlswBanksUsed": pm1004vencDwlswBanksUsed,
       "pm1004vencDwlSwBank1Used": pm1004vencDwlSwBank1Used,
       "pm1004vencDwlSwBank2Used": pm1004vencDwlSwBank2Used,
       "pm1004vencDwlSwBank1Notempty": pm1004vencDwlSwBank1Notempty,
       "pm1004vencDwlSwBank2Notempty": pm1004vencDwlSwBank2Notempty,
       "pm1004vencDwlgwBanksUsed": pm1004vencDwlgwBanksUsed,
       "pm1004vencDwlGwBank1Used": pm1004vencDwlGwBank1Used,
       "pm1004vencDwlGwBank2Used": pm1004vencDwlGwBank2Used,
       "pm1004vencDwlGwBank3Used": pm1004vencDwlGwBank3Used,
       "pm1004vencDwlGwBank4Used": pm1004vencDwlGwBank4Used,
       "pm1004vencDwlGwBank1Notempty": pm1004vencDwlGwBank1Notempty,
       "pm1004vencDwlGwBank2Notempty": pm1004vencDwlGwBank2Notempty,
       "pm1004vencDwlGwBank3Notempty": pm1004vencDwlGwBank3Notempty,
       "pm1004vencDwlGwBank4Notempty": pm1004vencDwlGwBank4Notempty,
       "pm1004vencDwlClient": pm1004vencDwlClient,
       "pm1004vencDwlLine": pm1004vencDwlLine,
       "pm1004vencConfig": pm1004vencConfig,
       "pm1004vencCfgAccessCAisCsf": pm1004vencCfgAccessCAisCsf,
       "pm1004vencCfgClientcaiscsfTable": pm1004vencCfgClientcaiscsfTable,
       "pm1004vencCfgClientcaiscsfEntry": pm1004vencCfgClientcaiscsfEntry,
       "pm1004vencCfgClientcaiscsfIndex": pm1004vencCfgClientcaiscsfIndex,
       "pm1004vencCfgCAisModePortn": pm1004vencCfgCAisModePortn,
       "pm1004vencCfgUpAccessioAlmPortn": pm1004vencCfgUpAccessioAlmPortn,
       "pm1004vencCfgUpMapperDeAlmPortn": pm1004vencCfgUpMapperDeAlmPortn,
       "pm1004vencCfgDownAccessioAlmPortn": pm1004vencCfgDownAccessioAlmPortn,
       "pm1004vencCfgDownMapperDeAlmPortn": pm1004vencCfgDownMapperDeAlmPortn,
       "pm1004vencCfgDownDfrmAlmPortn": pm1004vencCfgDownDfrmAlmPortn,
       "pm1004vencCfgDownLineSyncAlarmsPortn": pm1004vencCfgDownLineSyncAlarmsPortn,
       "pm1004vencCfgStartup": pm1004vencCfgStartup,
       "pm1004vencCfgClientStartupTable": pm1004vencCfgClientStartupTable,
       "pm1004vencCfgClientStartupEntry": pm1004vencCfgClientStartupEntry,
       "pm1004vencCfgClientStartupIndex": pm1004vencCfgClientStartupIndex,
       "pm1004vencCfgSystConfPortPortn": pm1004vencCfgSystConfPortPortn,
       "pm1004vencCfgNetConfPortPortn": pm1004vencCfgNetConfPortPortn,
       "pm1004vencCfgAdddropConfPortPortn": pm1004vencCfgAdddropConfPortPortn,
       "pm1004venctablelineStartup": pm1004venctablelineStartup,
       "pm1004vencCfgsystConfLine1": pm1004vencCfgsystConfLine1,
       "pm1004vencCfglineOptions1": pm1004vencCfglineOptions1,
       "pm1004vencCfgsystConfLine2": pm1004vencCfgsystConfLine2,
       "pm1004vencCfglineSelection": pm1004vencCfglineSelection,
       "pm1004vencCfglineOptions2": pm1004vencCfglineOptions2,
       "pm1004vencCfgXfpTable": pm1004vencCfgXfpTable,
       "pm1004vencCfgXfpEntry": pm1004vencCfgXfpEntry,
       "pm1004vencCfgXfpIndex": pm1004vencCfgXfpIndex,
       "pm1004vencCfgSystConfXfpPortn": pm1004vencCfgSystConfXfpPortn,
       "pm1004vencCfgDataRateConfXfpPortn": pm1004vencCfgDataRateConfXfpPortn,
       "pm1004vencCfgLabels": pm1004vencCfgLabels,
       "pm1004vencCfgLabelclientTable": pm1004vencCfgLabelclientTable,
       "pm1004vencCfgLabelclientEntry": pm1004vencCfgLabelclientEntry,
       "pm1004vencCfgLabelclientIndex": pm1004vencCfgLabelclientIndex,
       "pm1004vencCfgLabelclientPortn": pm1004vencCfgLabelclientPortn,
       "pm1004vencCfgLabellineTable": pm1004vencCfgLabellineTable,
       "pm1004vencCfgLabellineEntry": pm1004vencCfgLabellineEntry,
       "pm1004vencCfgLabellineIndex": pm1004vencCfgLabellineIndex,
       "pm1004vencCfgLabellinePortn": pm1004vencCfgLabellinePortn,
       "pm1004vencCfgStartupthresholds": pm1004vencCfgStartupthresholds,
       "pm1004vencCfgClientStartupThreshTable": pm1004vencCfgClientStartupThreshTable,
       "pm1004vencCfgClientStartupThreshEntry": pm1004vencCfgClientStartupThreshEntry,
       "pm1004vencCfgClientStartupThreshIndex": pm1004vencCfgClientStartupThreshIndex,
       "pm1004vencCfgClientThreshtxpowhighPortn": pm1004vencCfgClientThreshtxpowhighPortn,
       "pm1004vencCfgClientThreshtxpowlowPortn": pm1004vencCfgClientThreshtxpowlowPortn,
       "pm1004vencCfgClientThreshrxpowhighPortn": pm1004vencCfgClientThreshrxpowhighPortn,
       "pm1004vencCfgClientThreshrxpowlowPortn": pm1004vencCfgClientThreshrxpowlowPortn,
       "pm1004vencCfgLineStartupThreshTable": pm1004vencCfgLineStartupThreshTable,
       "pm1004vencCfgLineStartupThreshEntry": pm1004vencCfgLineStartupThreshEntry,
       "pm1004vencCfgLineStartupThreshIndex": pm1004vencCfgLineStartupThreshIndex,
       "pm1004vencCfgLineThreshtxpowhighPortn": pm1004vencCfgLineThreshtxpowhighPortn,
       "pm1004vencCfgLineThreshtxpowlowPortn": pm1004vencCfgLineThreshtxpowlowPortn,
       "pm1004vencCfgLineThreshrxpowhighPortn": pm1004vencCfgLineThreshrxpowhighPortn,
       "pm1004vencCfgLineThreshrxpowlowPortn": pm1004vencCfgLineThreshrxpowlowPortn,
       "pm1004vencCfgOther": pm1004vencCfgOther,
       "pm1004venctablemoduleOther": pm1004venctablemoduleOther,
       "pm1004vencCfgmode": pm1004vencCfgmode,
       "pm1004vencCfgStartuptlh": pm1004vencCfgStartuptlh,
       "pm1004vencCfgOtxtlhTable": pm1004vencCfgOtxtlhTable,
       "pm1004vencCfgOtxtlhEntry": pm1004vencCfgOtxtlhEntry,
       "pm1004vencCfgOtxtlhIndex": pm1004vencCfgOtxtlhIndex,
       "pm1004vencCfgNuPortn": pm1004vencCfgNuPortn,
       "pm1004vencCfgLineDitherRatePortn": pm1004vencCfgLineDitherRatePortn,
       "pm1004vencCfgLineDitherFhzPortn": pm1004vencCfgLineDitherFhzPortn,
       "pm1004vencCfgLinePwrLaserPortn": pm1004vencCfgLinePwrLaserPortn,
       "pm1004vencCfgLineFCurrentPortn": pm1004vencCfgLineFCurrentPortn,
       "pm1004vencCfgLineGridCurrentPortn": pm1004vencCfgLineGridCurrentPortn,
       "pm1004vencCfgFPortn": pm1004vencCfgFPortn,
       "pm1004vencCfgReservedPortn": pm1004vencCfgReservedPortn,
       "pm1004vencCfgLinePhotodiodeModePortn": pm1004vencCfgLinePhotodiodeModePortn,
       "pm1004vencCfgLinePhotodiodeValuePortn": pm1004vencCfgLinePhotodiodeValuePortn,
       "pm1004vencCfgStartuptablefive": pm1004vencCfgStartuptablefive,
       "pm1004vencCfgOtxtlhcapabilitiesTable": pm1004vencCfgOtxtlhcapabilitiesTable,
       "pm1004vencCfgOtxtlhcapabilitiesEntry": pm1004vencCfgOtxtlhcapabilitiesEntry,
       "pm1004vencCfgOtxtlhcapabilitiesIndex": pm1004vencCfgOtxtlhcapabilitiesIndex,
       "pm1004vencCfgComponentTypePortn": pm1004vencCfgComponentTypePortn,
       "pm1004vencCfgMiscellaneousPortn": pm1004vencCfgMiscellaneousPortn,
       "pm1004vencCfgFirstChannelPortn": pm1004vencCfgFirstChannelPortn,
       "pm1004vencCfgLastChannelPortn": pm1004vencCfgLastChannelPortn,
       "pm1004vencCfgGridPortn": pm1004vencCfgGridPortn,
       "pm1004vencCfgWriteConfiguration": pm1004vencCfgWriteConfiguration,
       "pm1004venctraps": pm1004venctraps,
       "pm1004venctrapPortNumber": pm1004venctrapPortNumber,
       "pm1004venctrapLineNumber": pm1004venctrapLineNumber,
       "pm1004venctrapBoardNumber": pm1004venctrapBoardNumber,
       "pm1004vencLineTrapNotUrgentGoesOn": pm1004vencLineTrapNotUrgentGoesOn,
       "pm1004vencLineTrapNotUrgentGoesOff": pm1004vencLineTrapNotUrgentGoesOff,
       "pm1004vencLineTrapUrgentGoesOn": pm1004vencLineTrapUrgentGoesOn,
       "pm1004vencLineTrapUrgentGoesOff": pm1004vencLineTrapUrgentGoesOff,
       "pm1004vencLineTrapCritGoesOn": pm1004vencLineTrapCritGoesOn,
       "pm1004vencLineTrapCritGoesOff": pm1004vencLineTrapCritGoesOff,
       "pm1004vencClientTrapCritGoesOn": pm1004vencClientTrapCritGoesOn,
       "pm1004vencClientTrapCritGoesOff": pm1004vencClientTrapCritGoesOff,
       "pm1004vencPowerTrapUrgentGoesOn": pm1004vencPowerTrapUrgentGoesOn,
       "pm1004vencPowerTrapUrgentGoesOff": pm1004vencPowerTrapUrgentGoesOff,
       "pm1004vencMonitoring": pm1004vencMonitoring,
       "pm1004vencMonOther": pm1004vencMonOther,
       "pm1004vencMonRmon": pm1004vencMonRmon,
       "pm1004vencMonCountersReset": pm1004vencMonCountersReset,
       "pm1004vencMonCountersStop": pm1004vencMonCountersStop,
       "pm1004vencMonClient": pm1004vencMonClient,
       "pm1004vencMonClientRmonCounter": pm1004vencMonClientRmonCounter,
       "pm1004vencMonupRmonByteCntTable": pm1004vencMonupRmonByteCntTable,
       "pm1004vencMonupRmonByteCntEntry": pm1004vencMonupRmonByteCntEntry,
       "pm1004vencMonupRmonByteCntIndex": pm1004vencMonupRmonByteCntIndex,
       "pm1004vencMonupRmonByteCntValuePortn": pm1004vencMonupRmonByteCntValuePortn,
       "pm1004vencMonupRmonByteCntErrorPortn": pm1004vencMonupRmonByteCntErrorPortn,
       "pm1004vencMonupRmonByteCntOverloadPortn": pm1004vencMonupRmonByteCntOverloadPortn,
       "pm1004vencMonupRmonCrcErrorCntTable": pm1004vencMonupRmonCrcErrorCntTable,
       "pm1004vencMonupRmonCrcErrorCntEntry": pm1004vencMonupRmonCrcErrorCntEntry,
       "pm1004vencMonupRmonCrcErrorCntIndex": pm1004vencMonupRmonCrcErrorCntIndex,
       "pm1004vencMonupRmonCrcErrorCntValuePortn": pm1004vencMonupRmonCrcErrorCntValuePortn,
       "pm1004vencMonupRmonCrcErrorCntErrorPortn": pm1004vencMonupRmonCrcErrorCntErrorPortn,
       "pm1004vencMonupRmonCrcErrorCntOverloadPortn": pm1004vencMonupRmonCrcErrorCntOverloadPortn,
       "pm1004vencMonupRmonPacketsCntTable": pm1004vencMonupRmonPacketsCntTable,
       "pm1004vencMonupRmonPacketsCntEntry": pm1004vencMonupRmonPacketsCntEntry,
       "pm1004vencMonupRmonPacketsCntIndex": pm1004vencMonupRmonPacketsCntIndex,
       "pm1004vencMonupRmonPacketsCntValuePortn": pm1004vencMonupRmonPacketsCntValuePortn,
       "pm1004vencMonupRmonPacketsCntErrorPortn": pm1004vencMonupRmonPacketsCntErrorPortn,
       "pm1004vencMonupRmonPacketsCntOverloadPortn": pm1004vencMonupRmonPacketsCntOverloadPortn,
       "pm1004vencMonupRmonBroadcastCntTable": pm1004vencMonupRmonBroadcastCntTable,
       "pm1004vencMonupRmonBroadcastCntEntry": pm1004vencMonupRmonBroadcastCntEntry,
       "pm1004vencMonupRmonBroadcastCntIndex": pm1004vencMonupRmonBroadcastCntIndex,
       "pm1004vencMonupRmonBroadcastCntValuePortn": pm1004vencMonupRmonBroadcastCntValuePortn,
       "pm1004vencMonupRmonBroadcastCntErrorPortn": pm1004vencMonupRmonBroadcastCntErrorPortn,
       "pm1004vencMonupRmonBroadcastCntOverloadPortn": pm1004vencMonupRmonBroadcastCntOverloadPortn,
       "pm1004vencMonupRmonMulticastCntTable": pm1004vencMonupRmonMulticastCntTable,
       "pm1004vencMonupRmonMulticastCntEntry": pm1004vencMonupRmonMulticastCntEntry,
       "pm1004vencMonupRmonMulticastCntIndex": pm1004vencMonupRmonMulticastCntIndex,
       "pm1004vencMonupRmonMulticastCntValuePortn": pm1004vencMonupRmonMulticastCntValuePortn,
       "pm1004vencMonupRmonMulticastCntErrorPortn": pm1004vencMonupRmonMulticastCntErrorPortn,
       "pm1004vencMonupRmonMulticastCntOverloadPortn": pm1004vencMonupRmonMulticastCntOverloadPortn,
       "pm1004vencMonupLineRmonByteCntTable": pm1004vencMonupLineRmonByteCntTable,
       "pm1004vencMonupLineRmonByteCntEntry": pm1004vencMonupLineRmonByteCntEntry,
       "pm1004vencMonupLineRmonByteCntIndex": pm1004vencMonupLineRmonByteCntIndex,
       "pm1004vencMonupLineRmonByteCntValuePortn": pm1004vencMonupLineRmonByteCntValuePortn,
       "pm1004vencMonupLineRmonByteCntErrorPortn": pm1004vencMonupLineRmonByteCntErrorPortn,
       "pm1004vencMonupLineRmonByteCntOverloadPortn": pm1004vencMonupLineRmonByteCntOverloadPortn,
       "pm1004vencMonupLineRmonCrcErrorCntTable": pm1004vencMonupLineRmonCrcErrorCntTable,
       "pm1004vencMonupLineRmonCrcErrorCntEntry": pm1004vencMonupLineRmonCrcErrorCntEntry,
       "pm1004vencMonupLineRmonCrcErrorCntIndex": pm1004vencMonupLineRmonCrcErrorCntIndex,
       "pm1004vencMonupLineRmonCrcErrorCntValuePortn": pm1004vencMonupLineRmonCrcErrorCntValuePortn,
       "pm1004vencMonupLineRmonCrcErrorCntErrorPortn": pm1004vencMonupLineRmonCrcErrorCntErrorPortn,
       "pm1004vencMonupLineRmonCrcErrorCntOverloadPortn": pm1004vencMonupLineRmonCrcErrorCntOverloadPortn,
       "pm1004vencMonupLineRmonPacketsCntTable": pm1004vencMonupLineRmonPacketsCntTable,
       "pm1004vencMonupLineRmonPacketsCntEntry": pm1004vencMonupLineRmonPacketsCntEntry,
       "pm1004vencMonupLineRmonPacketsCntIndex": pm1004vencMonupLineRmonPacketsCntIndex,
       "pm1004vencMonupLineRmonPacketsCntValuePortn": pm1004vencMonupLineRmonPacketsCntValuePortn,
       "pm1004vencMonupLineRmonPacketsCntErrorPortn": pm1004vencMonupLineRmonPacketsCntErrorPortn,
       "pm1004vencMonupLineRmonPacketsCntOverloadPortn": pm1004vencMonupLineRmonPacketsCntOverloadPortn,
       "pm1004vencMonLine": pm1004vencMonLine,
       "pm1004vencMonLineRmonCounter": pm1004vencMonLineRmonCounter}
)
