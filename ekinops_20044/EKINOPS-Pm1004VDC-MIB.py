# SNMP MIB module (EKINOPS-Pm1004VDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1004VDC-MIB.mib
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

modulePm1004vdc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38)
)
if mibBuilder.loadTexts:
    modulePm1004vdc.setRevisions(
        ("2008-03-11 00:00",
         "2008-08-18 00:00",
         "2008-12-02 00:00",
         "2008-12-08 00:00",
         "2009-05-26 00:00",
         "2009-07-22 00:00",
         "2009-09-02 00:00",
         "2009-10-27 00:00",
         "2010-03-03 00:00",
         "2011-02-04 00:00",
         "2011-04-29 00:00",
         "2012-03-08 00:00",
         "2014-03-28 00:00",
         "2014-12-23 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1004vdcModeTimeSlot(TextualConvention, Integer32):
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



class Pm1004vdcModeAddDrop(TextualConvention, Integer32):
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



class Pm1004vdcProtectionTimeSlot(TextualConvention, Integer32):
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



class Pm1004vdcProtectionStartUp(TextualConvention, Integer32):
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



class Pm1004vdcDccMode(TextualConvention, Integer32):
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



class Pm1004vdcClientOosMode(TextualConvention, Integer32):
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



class Pm1004vdcOtxMode(TextualConvention, Integer32):
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



class Pm1004vdcOtxGrid(TextualConvention, Integer32):
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



class Pm1004vdcAdjustValue(TextualConvention, Integer32):
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



class Pm1004vdcOtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm1004vdcalarms_ObjectIdentity = ObjectIdentity
pm1004vdcalarms = _Pm1004vdcalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2)
)
_Pm1004vdcAlmOther_ObjectIdentity = ObjectIdentity
pm1004vdcAlmOther = _Pm1004vdcAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1)
)
_Pm1004vdcAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1004vdcAlmOtherNurg = _Pm1004vdcAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 1)
)
_Pm1004vdcAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm1004vdcAlmsynthAlm2 = _Pm1004vdcAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 1, 2)
)
_Pm1004vdcAlmConfTableSave_Type = EkiOnOff
_Pm1004vdcAlmConfTableSave_Object = MibScalar
pm1004vdcAlmConfTableSave = _Pm1004vdcAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 1, 2, 1),
    _Pm1004vdcAlmConfTableSave_Type()
)
pm1004vdcAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmConfTableSave.setStatus("current")
_Pm1004vdcAlmInvUpload_Type = EkiOnOff
_Pm1004vdcAlmInvUpload_Object = MibScalar
pm1004vdcAlmInvUpload = _Pm1004vdcAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 1, 2, 2),
    _Pm1004vdcAlmInvUpload_Type()
)
pm1004vdcAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmInvUpload.setStatus("current")
_Pm1004vdcAlmConfTableLoad_Type = EkiOnOff
_Pm1004vdcAlmConfTableLoad_Object = MibScalar
pm1004vdcAlmConfTableLoad = _Pm1004vdcAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 1, 2, 3),
    _Pm1004vdcAlmConfTableLoad_Type()
)
pm1004vdcAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmConfTableLoad.setStatus("current")
_Pm1004vdcAlmCorrelatOff_Type = EkiOnOff
_Pm1004vdcAlmCorrelatOff_Object = MibScalar
pm1004vdcAlmCorrelatOff = _Pm1004vdcAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 1, 2, 4),
    _Pm1004vdcAlmCorrelatOff_Type()
)
pm1004vdcAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmCorrelatOff.setStatus("current")
_Pm1004vdcAlmMaintenanceOn_Type = EkiOnOff
_Pm1004vdcAlmMaintenanceOn_Object = MibScalar
pm1004vdcAlmMaintenanceOn = _Pm1004vdcAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 1, 2, 5),
    _Pm1004vdcAlmMaintenanceOn_Type()
)
pm1004vdcAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmMaintenanceOn.setStatus("current")
_Pm1004vdcAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1004vdcAlmOtherUrg = _Pm1004vdcAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2)
)
_Pm1004vdcAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm1004vdcAlmmodInitFailLevel2 = _Pm1004vdcAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 194)
)
_Pm1004vdcAlmLedFail_Type = EkiOnOff
_Pm1004vdcAlmLedFail_Object = MibScalar
pm1004vdcAlmLedFail = _Pm1004vdcAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 194, 1),
    _Pm1004vdcAlmLedFail_Type()
)
pm1004vdcAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLedFail.setStatus("current")
_Pm1004vdcAlmNextColdBootForced_Type = EkiOnOff
_Pm1004vdcAlmNextColdBootForced_Object = MibScalar
pm1004vdcAlmNextColdBootForced = _Pm1004vdcAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 194, 2),
    _Pm1004vdcAlmNextColdBootForced_Type()
)
pm1004vdcAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmNextColdBootForced.setStatus("current")
_Pm1004vdcAlmBootUndone_Type = EkiOnOff
_Pm1004vdcAlmBootUndone_Object = MibScalar
pm1004vdcAlmBootUndone = _Pm1004vdcAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 194, 3),
    _Pm1004vdcAlmBootUndone_Type()
)
pm1004vdcAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmBootUndone.setStatus("current")
_Pm1004vdcAlmResetHwInitFail_Type = EkiOnOff
_Pm1004vdcAlmResetHwInitFail_Object = MibScalar
pm1004vdcAlmResetHwInitFail = _Pm1004vdcAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 194, 4),
    _Pm1004vdcAlmResetHwInitFail_Type()
)
pm1004vdcAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmResetHwInitFail.setStatus("current")
_Pm1004vdcAlmSwInitFail_Type = EkiOnOff
_Pm1004vdcAlmSwInitFail_Object = MibScalar
pm1004vdcAlmSwInitFail = _Pm1004vdcAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 194, 5),
    _Pm1004vdcAlmSwInitFail_Type()
)
pm1004vdcAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmSwInitFail.setStatus("current")
_Pm1004vdcAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm1004vdcAlmmodInitFailLevel3 = _Pm1004vdcAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195)
)
_Pm1004vdcAlmGwIdentFail_Type = EkiOnOff
_Pm1004vdcAlmGwIdentFail_Object = MibScalar
pm1004vdcAlmGwIdentFail = _Pm1004vdcAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 1),
    _Pm1004vdcAlmGwIdentFail_Type()
)
pm1004vdcAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmGwIdentFail.setStatus("current")
_Pm1004vdcAlmObmTypeReadFail_Type = EkiOnOff
_Pm1004vdcAlmObmTypeReadFail_Object = MibScalar
pm1004vdcAlmObmTypeReadFail = _Pm1004vdcAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 2),
    _Pm1004vdcAlmObmTypeReadFail_Type()
)
pm1004vdcAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmObmTypeReadFail.setStatus("current")
_Pm1004vdcAlmInitModuleFail_Type = EkiOnOff
_Pm1004vdcAlmInitModuleFail_Object = MibScalar
pm1004vdcAlmInitModuleFail = _Pm1004vdcAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 3),
    _Pm1004vdcAlmInitModuleFail_Type()
)
pm1004vdcAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmInitModuleFail.setStatus("current")
_Pm1004vdcAlmXfp1InitFail_Type = EkiOnOff
_Pm1004vdcAlmXfp1InitFail_Object = MibScalar
pm1004vdcAlmXfp1InitFail = _Pm1004vdcAlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 5),
    _Pm1004vdcAlmXfp1InitFail_Type()
)
pm1004vdcAlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmXfp1InitFail.setStatus("current")
_Pm1004vdcAlmXfp2InitFail_Type = EkiOnOff
_Pm1004vdcAlmXfp2InitFail_Object = MibScalar
pm1004vdcAlmXfp2InitFail = _Pm1004vdcAlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 6),
    _Pm1004vdcAlmXfp2InitFail_Type()
)
pm1004vdcAlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmXfp2InitFail.setStatus("current")
_Pm1004vdcAlmLine1InitFail_Type = EkiOnOff
_Pm1004vdcAlmLine1InitFail_Object = MibScalar
pm1004vdcAlmLine1InitFail = _Pm1004vdcAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 7),
    _Pm1004vdcAlmLine1InitFail_Type()
)
pm1004vdcAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLine1InitFail.setStatus("current")
_Pm1004vdcAlmLine2InitFail_Type = EkiOnOff
_Pm1004vdcAlmLine2InitFail_Object = MibScalar
pm1004vdcAlmLine2InitFail = _Pm1004vdcAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 8),
    _Pm1004vdcAlmLine2InitFail_Type()
)
pm1004vdcAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLine2InitFail.setStatus("current")
_Pm1004vdcAlmClient1InitFail_Type = EkiOnOff
_Pm1004vdcAlmClient1InitFail_Object = MibScalar
pm1004vdcAlmClient1InitFail = _Pm1004vdcAlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 9),
    _Pm1004vdcAlmClient1InitFail_Type()
)
pm1004vdcAlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmClient1InitFail.setStatus("current")
_Pm1004vdcAlmClient2InitFail_Type = EkiOnOff
_Pm1004vdcAlmClient2InitFail_Object = MibScalar
pm1004vdcAlmClient2InitFail = _Pm1004vdcAlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 10),
    _Pm1004vdcAlmClient2InitFail_Type()
)
pm1004vdcAlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmClient2InitFail.setStatus("current")
_Pm1004vdcAlmClient3InitFail_Type = EkiOnOff
_Pm1004vdcAlmClient3InitFail_Object = MibScalar
pm1004vdcAlmClient3InitFail = _Pm1004vdcAlmClient3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 11),
    _Pm1004vdcAlmClient3InitFail_Type()
)
pm1004vdcAlmClient3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmClient3InitFail.setStatus("current")
_Pm1004vdcAlmClient4InitFail_Type = EkiOnOff
_Pm1004vdcAlmClient4InitFail_Object = MibScalar
pm1004vdcAlmClient4InitFail = _Pm1004vdcAlmClient4InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 12),
    _Pm1004vdcAlmClient4InitFail_Type()
)
pm1004vdcAlmClient4InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmClient4InitFail.setStatus("current")
_Pm1004vdcAlmClient5InitFail_Type = EkiOnOff
_Pm1004vdcAlmClient5InitFail_Object = MibScalar
pm1004vdcAlmClient5InitFail = _Pm1004vdcAlmClient5InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 13),
    _Pm1004vdcAlmClient5InitFail_Type()
)
pm1004vdcAlmClient5InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmClient5InitFail.setStatus("current")
_Pm1004vdcAlmClient6InitFail_Type = EkiOnOff
_Pm1004vdcAlmClient6InitFail_Object = MibScalar
pm1004vdcAlmClient6InitFail = _Pm1004vdcAlmClient6InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 195, 14),
    _Pm1004vdcAlmClient6InitFail_Type()
)
pm1004vdcAlmClient6InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmClient6InitFail.setStatus("current")
_Pm1004vdcAlmclientRxProt_ObjectIdentity = ObjectIdentity
pm1004vdcAlmclientRxProt = _Pm1004vdcAlmclientRxProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198)
)
_Pm1004vdcAlmAdddropClient1West_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient1West_Object = MibScalar
pm1004vdcAlmAdddropClient1West = _Pm1004vdcAlmAdddropClient1West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 1),
    _Pm1004vdcAlmAdddropClient1West_Type()
)
pm1004vdcAlmAdddropClient1West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient1West.setStatus("current")
_Pm1004vdcAlmAdddropClient2West_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient2West_Object = MibScalar
pm1004vdcAlmAdddropClient2West = _Pm1004vdcAlmAdddropClient2West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 2),
    _Pm1004vdcAlmAdddropClient2West_Type()
)
pm1004vdcAlmAdddropClient2West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient2West.setStatus("current")
_Pm1004vdcAlmAdddropClient3West_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient3West_Object = MibScalar
pm1004vdcAlmAdddropClient3West = _Pm1004vdcAlmAdddropClient3West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 3),
    _Pm1004vdcAlmAdddropClient3West_Type()
)
pm1004vdcAlmAdddropClient3West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient3West.setStatus("current")
_Pm1004vdcAlmAdddropClient4West_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient4West_Object = MibScalar
pm1004vdcAlmAdddropClient4West = _Pm1004vdcAlmAdddropClient4West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 4),
    _Pm1004vdcAlmAdddropClient4West_Type()
)
pm1004vdcAlmAdddropClient4West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient4West.setStatus("current")
_Pm1004vdcAlmAdddropClient5West_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient5West_Object = MibScalar
pm1004vdcAlmAdddropClient5West = _Pm1004vdcAlmAdddropClient5West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 5),
    _Pm1004vdcAlmAdddropClient5West_Type()
)
pm1004vdcAlmAdddropClient5West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient5West.setStatus("current")
_Pm1004vdcAlmAdddropClient6West_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient6West_Object = MibScalar
pm1004vdcAlmAdddropClient6West = _Pm1004vdcAlmAdddropClient6West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 6),
    _Pm1004vdcAlmAdddropClient6West_Type()
)
pm1004vdcAlmAdddropClient6West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient6West.setStatus("current")
_Pm1004vdcAlmAdddropClient1East_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient1East_Object = MibScalar
pm1004vdcAlmAdddropClient1East = _Pm1004vdcAlmAdddropClient1East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 9),
    _Pm1004vdcAlmAdddropClient1East_Type()
)
pm1004vdcAlmAdddropClient1East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient1East.setStatus("current")
_Pm1004vdcAlmAdddropClient2East_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient2East_Object = MibScalar
pm1004vdcAlmAdddropClient2East = _Pm1004vdcAlmAdddropClient2East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 10),
    _Pm1004vdcAlmAdddropClient2East_Type()
)
pm1004vdcAlmAdddropClient2East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient2East.setStatus("current")
_Pm1004vdcAlmAdddropClient3East_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient3East_Object = MibScalar
pm1004vdcAlmAdddropClient3East = _Pm1004vdcAlmAdddropClient3East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 11),
    _Pm1004vdcAlmAdddropClient3East_Type()
)
pm1004vdcAlmAdddropClient3East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient3East.setStatus("current")
_Pm1004vdcAlmAdddropClient4East_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient4East_Object = MibScalar
pm1004vdcAlmAdddropClient4East = _Pm1004vdcAlmAdddropClient4East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 12),
    _Pm1004vdcAlmAdddropClient4East_Type()
)
pm1004vdcAlmAdddropClient4East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient4East.setStatus("current")
_Pm1004vdcAlmAdddropClient5East_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient5East_Object = MibScalar
pm1004vdcAlmAdddropClient5East = _Pm1004vdcAlmAdddropClient5East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 13),
    _Pm1004vdcAlmAdddropClient5East_Type()
)
pm1004vdcAlmAdddropClient5East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient5East.setStatus("current")
_Pm1004vdcAlmAdddropClient6East_Type = EkiOnOff
_Pm1004vdcAlmAdddropClient6East_Object = MibScalar
pm1004vdcAlmAdddropClient6East = _Pm1004vdcAlmAdddropClient6East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 2, 198, 14),
    _Pm1004vdcAlmAdddropClient6East_Type()
)
pm1004vdcAlmAdddropClient6East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmAdddropClient6East.setStatus("current")
_Pm1004vdcAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1004vdcAlmOtherCrit = _Pm1004vdcAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 3)
)
_Pm1004vdcAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1004vdcAlmsynthAlm0 = _Pm1004vdcAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 3, 0)
)
_Pm1004vdcAlmModGlobFail_Type = EkiOnOff
_Pm1004vdcAlmModGlobFail_Object = MibScalar
pm1004vdcAlmModGlobFail = _Pm1004vdcAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 3, 0, 9),
    _Pm1004vdcAlmModGlobFail_Type()
)
pm1004vdcAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmModGlobFail.setStatus("current")
_Pm1004vdcAlmDefFuseA_Type = EkiOnOff
_Pm1004vdcAlmDefFuseA_Object = MibScalar
pm1004vdcAlmDefFuseA = _Pm1004vdcAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 3, 0, 15),
    _Pm1004vdcAlmDefFuseA_Type()
)
pm1004vdcAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDefFuseA.setStatus("current")
_Pm1004vdcAlmDefFuseB_Type = EkiOnOff
_Pm1004vdcAlmDefFuseB_Object = MibScalar
pm1004vdcAlmDefFuseB = _Pm1004vdcAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 1, 3, 0, 16),
    _Pm1004vdcAlmDefFuseB_Type()
)
pm1004vdcAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDefFuseB.setStatus("current")
_Pm1004vdcAlmClient_ObjectIdentity = ObjectIdentity
pm1004vdcAlmClient = _Pm1004vdcAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2)
)
_Pm1004vdcAlmClientNurg_ObjectIdentity = ObjectIdentity
pm1004vdcAlmClientNurg = _Pm1004vdcAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1)
)
_Pm1004vdcAlmsfpWarnDdmTable_Object = MibTable
pm1004vdcAlmsfpWarnDdmTable = _Pm1004vdcAlmsfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsfpWarnDdmTable.setStatus("current")
_Pm1004vdcAlmsfpWarnDdmEntry_Object = MibTableRow
pm1004vdcAlmsfpWarnDdmEntry = _Pm1004vdcAlmsfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1)
)
pm1004vdcAlmsfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmsfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsfpWarnDdmEntry.setStatus("current")


class _Pm1004vdcAlmsfpWarnDdmIndex_Type(Integer32):
    """Custom type pm1004vdcAlmsfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmsfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmsfpWarnDdmIndex_Object = MibTableColumn
pm1004vdcAlmsfpWarnDdmIndex = _Pm1004vdcAlmsfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 1),
    _Pm1004vdcAlmsfpWarnDdmIndex_Type()
)
pm1004vdcAlmsfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmsfpWarnDdmIndex.setStatus("current")
_Pm1004vdcAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPwLowWngPortn_Object = MibTableColumn
pm1004vdcAlmTxPwLowWngPortn = _Pm1004vdcAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 2),
    _Pm1004vdcAlmTxPwLowWngPortn_Type()
)
pm1004vdcAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPwLowWngPortn.setStatus("current")
_Pm1004vdcAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPwrHighWngPortn_Object = MibTableColumn
pm1004vdcAlmTxPwrHighWngPortn = _Pm1004vdcAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 3),
    _Pm1004vdcAlmTxPwrHighWngPortn_Type()
)
pm1004vdcAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPwrHighWngPortn.setStatus("current")
_Pm1004vdcAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm1004vdcAlmTxBiasLowWngPortn_Object = MibTableColumn
pm1004vdcAlmTxBiasLowWngPortn = _Pm1004vdcAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 4),
    _Pm1004vdcAlmTxBiasLowWngPortn_Type()
)
pm1004vdcAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxBiasLowWngPortn.setStatus("current")
_Pm1004vdcAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm1004vdcAlmTxBiasHighWngPortn_Object = MibTableColumn
pm1004vdcAlmTxBiasHighWngPortn = _Pm1004vdcAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 5),
    _Pm1004vdcAlmTxBiasHighWngPortn_Type()
)
pm1004vdcAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxBiasHighWngPortn.setStatus("current")
_Pm1004vdcAlmVccLowWngPortn_Type = EkiOnOff
_Pm1004vdcAlmVccLowWngPortn_Object = MibTableColumn
pm1004vdcAlmVccLowWngPortn = _Pm1004vdcAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 6),
    _Pm1004vdcAlmVccLowWngPortn_Type()
)
pm1004vdcAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVccLowWngPortn.setStatus("current")
_Pm1004vdcAlmVccHighWngPortn_Type = EkiOnOff
_Pm1004vdcAlmVccHighWngPortn_Object = MibTableColumn
pm1004vdcAlmVccHighWngPortn = _Pm1004vdcAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 7),
    _Pm1004vdcAlmVccHighWngPortn_Type()
)
pm1004vdcAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVccHighWngPortn.setStatus("current")
_Pm1004vdcAlmTempLowWngPortn_Type = EkiOnOff
_Pm1004vdcAlmTempLowWngPortn_Object = MibTableColumn
pm1004vdcAlmTempLowWngPortn = _Pm1004vdcAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 8),
    _Pm1004vdcAlmTempLowWngPortn_Type()
)
pm1004vdcAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTempLowWngPortn.setStatus("current")
_Pm1004vdcAlmTempHighWngPortn_Type = EkiOnOff
_Pm1004vdcAlmTempHighWngPortn_Object = MibTableColumn
pm1004vdcAlmTempHighWngPortn = _Pm1004vdcAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 9),
    _Pm1004vdcAlmTempHighWngPortn_Type()
)
pm1004vdcAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTempHighWngPortn.setStatus("current")
_Pm1004vdcAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPwrLowWngPortn_Object = MibTableColumn
pm1004vdcAlmRxPwrLowWngPortn = _Pm1004vdcAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 16),
    _Pm1004vdcAlmRxPwrLowWngPortn_Type()
)
pm1004vdcAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPwrLowWngPortn.setStatus("current")
_Pm1004vdcAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPwrHighWngPortn_Object = MibTableColumn
pm1004vdcAlmRxPwrHighWngPortn = _Pm1004vdcAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 48, 1, 17),
    _Pm1004vdcAlmRxPwrHighWngPortn_Type()
)
pm1004vdcAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPwrHighWngPortn.setStatus("current")
_Pm1004vdcAlmsfpCritDdmTable_Object = MibTable
pm1004vdcAlmsfpCritDdmTable = _Pm1004vdcAlmsfpCritDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsfpCritDdmTable.setStatus("current")
_Pm1004vdcAlmsfpCritDdmEntry_Object = MibTableRow
pm1004vdcAlmsfpCritDdmEntry = _Pm1004vdcAlmsfpCritDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 56, 1)
)
pm1004vdcAlmsfpCritDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmsfpCritDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsfpCritDdmEntry.setStatus("current")


class _Pm1004vdcAlmsfpCritDdmIndex_Type(Integer32):
    """Custom type pm1004vdcAlmsfpCritDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmsfpCritDdmIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmsfpCritDdmIndex_Object = MibTableColumn
pm1004vdcAlmsfpCritDdmIndex = _Pm1004vdcAlmsfpCritDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 56, 1, 1),
    _Pm1004vdcAlmsfpCritDdmIndex_Type()
)
pm1004vdcAlmsfpCritDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmsfpCritDdmIndex.setStatus("current")
_Pm1004vdcAlmTxPwrLowCritPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPwrLowCritPortn_Object = MibTableColumn
pm1004vdcAlmTxPwrLowCritPortn = _Pm1004vdcAlmTxPwrLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 56, 1, 2),
    _Pm1004vdcAlmTxPwrLowCritPortn_Type()
)
pm1004vdcAlmTxPwrLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPwrLowCritPortn.setStatus("current")
_Pm1004vdcAlmTxPwrHighCritPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPwrHighCritPortn_Object = MibTableColumn
pm1004vdcAlmTxPwrHighCritPortn = _Pm1004vdcAlmTxPwrHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 56, 1, 3),
    _Pm1004vdcAlmTxPwrHighCritPortn_Type()
)
pm1004vdcAlmTxPwrHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPwrHighCritPortn.setStatus("current")
_Pm1004vdcAlmRxPwrLowCritPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPwrLowCritPortn_Object = MibTableColumn
pm1004vdcAlmRxPwrLowCritPortn = _Pm1004vdcAlmRxPwrLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 56, 1, 16),
    _Pm1004vdcAlmRxPwrLowCritPortn_Type()
)
pm1004vdcAlmRxPwrLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPwrLowCritPortn.setStatus("current")
_Pm1004vdcAlmRxPwrHighCritPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPwrHighCritPortn_Object = MibTableColumn
pm1004vdcAlmRxPwrHighCritPortn = _Pm1004vdcAlmRxPwrHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 1, 56, 1, 17),
    _Pm1004vdcAlmRxPwrHighCritPortn_Type()
)
pm1004vdcAlmRxPwrHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPwrHighCritPortn.setStatus("current")
_Pm1004vdcAlmClientUrg_ObjectIdentity = ObjectIdentity
pm1004vdcAlmClientUrg = _Pm1004vdcAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2)
)
_Pm1004vdcAlmsfpAlmDdmTable_Object = MibTable
pm1004vdcAlmsfpAlmDdmTable = _Pm1004vdcAlmsfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsfpAlmDdmTable.setStatus("current")
_Pm1004vdcAlmsfpAlmDdmEntry_Object = MibTableRow
pm1004vdcAlmsfpAlmDdmEntry = _Pm1004vdcAlmsfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1)
)
pm1004vdcAlmsfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmsfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsfpAlmDdmEntry.setStatus("current")


class _Pm1004vdcAlmsfpAlmDdmIndex_Type(Integer32):
    """Custom type pm1004vdcAlmsfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmsfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmsfpAlmDdmIndex_Object = MibTableColumn
pm1004vdcAlmsfpAlmDdmIndex = _Pm1004vdcAlmsfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 1),
    _Pm1004vdcAlmsfpAlmDdmIndex_Type()
)
pm1004vdcAlmsfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmsfpAlmDdmIndex.setStatus("current")
_Pm1004vdcAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm1004vdcAlmTxPwrLowAlaPortn = _Pm1004vdcAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 2),
    _Pm1004vdcAlmTxPwrLowAlaPortn_Type()
)
pm1004vdcAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPwrLowAlaPortn.setStatus("current")
_Pm1004vdcAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm1004vdcAlmTxPwrHighAlaPortn = _Pm1004vdcAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 3),
    _Pm1004vdcAlmTxPwrHighAlaPortn_Type()
)
pm1004vdcAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPwrHighAlaPortn.setStatus("current")
_Pm1004vdcAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm1004vdcAlmTxBiasLowAlaPortn = _Pm1004vdcAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 4),
    _Pm1004vdcAlmTxBiasLowAlaPortn_Type()
)
pm1004vdcAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxBiasLowAlaPortn.setStatus("current")
_Pm1004vdcAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm1004vdcAlmTxBiasHighAlaPortn = _Pm1004vdcAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 5),
    _Pm1004vdcAlmTxBiasHighAlaPortn_Type()
)
pm1004vdcAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxBiasHighAlaPortn.setStatus("current")
_Pm1004vdcAlmVccLowAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmVccLowAlaPortn_Object = MibTableColumn
pm1004vdcAlmVccLowAlaPortn = _Pm1004vdcAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 6),
    _Pm1004vdcAlmVccLowAlaPortn_Type()
)
pm1004vdcAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVccLowAlaPortn.setStatus("current")
_Pm1004vdcAlmVccHighAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmVccHighAlaPortn_Object = MibTableColumn
pm1004vdcAlmVccHighAlaPortn = _Pm1004vdcAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 7),
    _Pm1004vdcAlmVccHighAlaPortn_Type()
)
pm1004vdcAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVccHighAlaPortn.setStatus("current")
_Pm1004vdcAlmTempLowAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmTempLowAlaPortn_Object = MibTableColumn
pm1004vdcAlmTempLowAlaPortn = _Pm1004vdcAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 8),
    _Pm1004vdcAlmTempLowAlaPortn_Type()
)
pm1004vdcAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTempLowAlaPortn.setStatus("current")
_Pm1004vdcAlmTempHighAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmTempHighAlaPortn_Object = MibTableColumn
pm1004vdcAlmTempHighAlaPortn = _Pm1004vdcAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 9),
    _Pm1004vdcAlmTempHighAlaPortn_Type()
)
pm1004vdcAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTempHighAlaPortn.setStatus("current")
_Pm1004vdcAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm1004vdcAlmRxPwrLowAlaPortn = _Pm1004vdcAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 16),
    _Pm1004vdcAlmRxPwrLowAlaPortn_Type()
)
pm1004vdcAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPwrLowAlaPortn.setStatus("current")
_Pm1004vdcAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm1004vdcAlmRxPwrHighAlaPortn = _Pm1004vdcAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 2, 32, 1, 17),
    _Pm1004vdcAlmRxPwrHighAlaPortn_Type()
)
pm1004vdcAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPwrHighAlaPortn.setStatus("current")
_Pm1004vdcAlmClientCrit_ObjectIdentity = ObjectIdentity
pm1004vdcAlmClientCrit = _Pm1004vdcAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3)
)
_Pm1004vdcAlmsynthAlmPortTable_Object = MibTable
pm1004vdcAlmsynthAlmPortTable = _Pm1004vdcAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsynthAlmPortTable.setStatus("current")
_Pm1004vdcAlmsynthAlmPortEntry_Object = MibTableRow
pm1004vdcAlmsynthAlmPortEntry = _Pm1004vdcAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1)
)
pm1004vdcAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsynthAlmPortEntry.setStatus("current")


class _Pm1004vdcAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm1004vdcAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmsynthAlmPortIndex_Object = MibTableColumn
pm1004vdcAlmsynthAlmPortIndex = _Pm1004vdcAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 1),
    _Pm1004vdcAlmsynthAlmPortIndex_Type()
)
pm1004vdcAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmsynthAlmPortIndex.setStatus("current")
_Pm1004vdcAlmSfpAbsentPortn_Type = EkiOnOff
_Pm1004vdcAlmSfpAbsentPortn_Object = MibTableColumn
pm1004vdcAlmSfpAbsentPortn = _Pm1004vdcAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 2),
    _Pm1004vdcAlmSfpAbsentPortn_Type()
)
pm1004vdcAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmSfpAbsentPortn.setStatus("current")
_Pm1004vdcAlmDdmAbsentPortn_Type = EkiOnOff
_Pm1004vdcAlmDdmAbsentPortn_Object = MibTableColumn
pm1004vdcAlmDdmAbsentPortn = _Pm1004vdcAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 3),
    _Pm1004vdcAlmDdmAbsentPortn_Type()
)
pm1004vdcAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDdmAbsentPortn.setStatus("current")
_Pm1004vdcAlmHwFailAccPortn_Type = EkiOnOff
_Pm1004vdcAlmHwFailAccPortn_Object = MibTableColumn
pm1004vdcAlmHwFailAccPortn = _Pm1004vdcAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 5),
    _Pm1004vdcAlmHwFailAccPortn_Type()
)
pm1004vdcAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmHwFailAccPortn.setStatus("current")
_Pm1004vdcAlmDwLsdPortn_Type = EkiOnOff
_Pm1004vdcAlmDwLsdPortn_Object = MibTableColumn
pm1004vdcAlmDwLsdPortn = _Pm1004vdcAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 6),
    _Pm1004vdcAlmDwLsdPortn_Type()
)
pm1004vdcAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDwLsdPortn.setStatus("current")
_Pm1004vdcAlmClientLocalOosTxPortn_Type = EkiOnOff
_Pm1004vdcAlmClientLocalOosTxPortn_Object = MibTableColumn
pm1004vdcAlmClientLocalOosTxPortn = _Pm1004vdcAlmClientLocalOosTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 7),
    _Pm1004vdcAlmClientLocalOosTxPortn_Type()
)
pm1004vdcAlmClientLocalOosTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmClientLocalOosTxPortn.setStatus("current")
_Pm1004vdcAlmClientLocalOosRxPortn_Type = EkiOnOff
_Pm1004vdcAlmClientLocalOosRxPortn_Object = MibTableColumn
pm1004vdcAlmClientLocalOosRxPortn = _Pm1004vdcAlmClientLocalOosRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 8),
    _Pm1004vdcAlmClientLocalOosRxPortn_Type()
)
pm1004vdcAlmClientLocalOosRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmClientLocalOosRxPortn.setStatus("current")
_Pm1004vdcAlmDwCaisPortn_Type = EkiOnOff
_Pm1004vdcAlmDwCaisPortn_Object = MibTableColumn
pm1004vdcAlmDwCaisPortn = _Pm1004vdcAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 9),
    _Pm1004vdcAlmDwCaisPortn_Type()
)
pm1004vdcAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDwCaisPortn.setStatus("current")
_Pm1004vdcAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmSfpDdmWarningPortn_Object = MibTableColumn
pm1004vdcAlmSfpDdmWarningPortn = _Pm1004vdcAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 10),
    _Pm1004vdcAlmSfpDdmWarningPortn_Type()
)
pm1004vdcAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmSfpDdmWarningPortn.setStatus("current")
_Pm1004vdcAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm1004vdcAlmSfpDdmAlmPortn_Object = MibTableColumn
pm1004vdcAlmSfpDdmAlmPortn = _Pm1004vdcAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 11),
    _Pm1004vdcAlmSfpDdmAlmPortn_Type()
)
pm1004vdcAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmSfpDdmAlmPortn.setStatus("current")
_Pm1004vdcAlmSfpDdmCritPortn_Type = EkiOnOff
_Pm1004vdcAlmSfpDdmCritPortn_Object = MibTableColumn
pm1004vdcAlmSfpDdmCritPortn = _Pm1004vdcAlmSfpDdmCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 12),
    _Pm1004vdcAlmSfpDdmCritPortn_Type()
)
pm1004vdcAlmSfpDdmCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmSfpDdmCritPortn.setStatus("current")
_Pm1004vdcAlmFailAccPortn_Type = EkiOnOff
_Pm1004vdcAlmFailAccPortn_Object = MibTableColumn
pm1004vdcAlmFailAccPortn = _Pm1004vdcAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 13),
    _Pm1004vdcAlmFailAccPortn_Type()
)
pm1004vdcAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmFailAccPortn.setStatus("current")
_Pm1004vdcAlmClientActivePortn_Type = EkiOnOff
_Pm1004vdcAlmClientActivePortn_Object = MibTableColumn
pm1004vdcAlmClientActivePortn = _Pm1004vdcAlmClientActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 16),
    _Pm1004vdcAlmClientActivePortn_Type()
)
pm1004vdcAlmClientActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmClientActivePortn.setStatus("current")
_Pm1004vdcAlmUpCsfPortn_Type = EkiOnOff
_Pm1004vdcAlmUpCsfPortn_Object = MibTableColumn
pm1004vdcAlmUpCsfPortn = _Pm1004vdcAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 8, 1, 17),
    _Pm1004vdcAlmUpCsfPortn_Type()
)
pm1004vdcAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmUpCsfPortn.setStatus("current")
_Pm1004vdcAlmaccessioAlmTable_Object = MibTable
pm1004vdcAlmaccessioAlmTable = _Pm1004vdcAlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmaccessioAlmTable.setStatus("current")
_Pm1004vdcAlmaccessioAlmEntry_Object = MibTableRow
pm1004vdcAlmaccessioAlmEntry = _Pm1004vdcAlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 16, 1)
)
pm1004vdcAlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmaccessioAlmEntry.setStatus("current")


class _Pm1004vdcAlmaccessioAlmIndex_Type(Integer32):
    """Custom type pm1004vdcAlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmaccessioAlmIndex_Object = MibTableColumn
pm1004vdcAlmaccessioAlmIndex = _Pm1004vdcAlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 16, 1, 1),
    _Pm1004vdcAlmaccessioAlmIndex_Type()
)
pm1004vdcAlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmaccessioAlmIndex.setStatus("current")
_Pm1004vdcAlmDwLasFailPortn_Type = EkiOnOff
_Pm1004vdcAlmDwLasFailPortn_Object = MibTableColumn
pm1004vdcAlmDwLasFailPortn = _Pm1004vdcAlmDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 16, 1, 2),
    _Pm1004vdcAlmDwLasFailPortn_Type()
)
pm1004vdcAlmDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDwLasFailPortn.setStatus("current")
_Pm1004vdcAlmUpLosPortn_Type = EkiOnOff
_Pm1004vdcAlmUpLosPortn_Object = MibTableColumn
pm1004vdcAlmUpLosPortn = _Pm1004vdcAlmUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 16, 1, 5),
    _Pm1004vdcAlmUpLosPortn_Type()
)
pm1004vdcAlmUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmUpLosPortn.setStatus("current")
_Pm1004vdcAlmmapperDeAlmTable_Object = MibTable
pm1004vdcAlmmapperDeAlmTable = _Pm1004vdcAlmmapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmmapperDeAlmTable.setStatus("current")
_Pm1004vdcAlmmapperDeAlmEntry_Object = MibTableRow
pm1004vdcAlmmapperDeAlmEntry = _Pm1004vdcAlmmapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 72, 1)
)
pm1004vdcAlmmapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmmapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmmapperDeAlmEntry.setStatus("current")


class _Pm1004vdcAlmmapperDeAlmIndex_Type(Integer32):
    """Custom type pm1004vdcAlmmapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmmapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmmapperDeAlmIndex_Object = MibTableColumn
pm1004vdcAlmmapperDeAlmIndex = _Pm1004vdcAlmmapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 72, 1, 1),
    _Pm1004vdcAlmmapperDeAlmIndex_Type()
)
pm1004vdcAlmmapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmmapperDeAlmIndex.setStatus("current")
_Pm1004vdcAlmUpAccOosPortn_Type = EkiOnOff
_Pm1004vdcAlmUpAccOosPortn_Object = MibTableColumn
pm1004vdcAlmUpAccOosPortn = _Pm1004vdcAlmUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 72, 1, 2),
    _Pm1004vdcAlmUpAccOosPortn_Type()
)
pm1004vdcAlmUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmUpAccOosPortn.setStatus("current")
_Pm1004vdcAlmUpBufferOvlPortn_Type = EkiOnOff
_Pm1004vdcAlmUpBufferOvlPortn_Object = MibTableColumn
pm1004vdcAlmUpBufferOvlPortn = _Pm1004vdcAlmUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 72, 1, 11),
    _Pm1004vdcAlmUpBufferOvlPortn_Type()
)
pm1004vdcAlmUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmUpBufferOvlPortn.setStatus("current")
_Pm1004vdcAlmDwCsfDetPortn_Type = EkiOnOff
_Pm1004vdcAlmDwCsfDetPortn_Object = MibTableColumn
pm1004vdcAlmDwCsfDetPortn = _Pm1004vdcAlmDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 72, 1, 12),
    _Pm1004vdcAlmDwCsfDetPortn_Type()
)
pm1004vdcAlmDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDwCsfDetPortn.setStatus("current")
_Pm1004vdcAlmDwBufferOvlPortn_Type = EkiOnOff
_Pm1004vdcAlmDwBufferOvlPortn_Object = MibTableColumn
pm1004vdcAlmDwBufferOvlPortn = _Pm1004vdcAlmDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 72, 1, 15),
    _Pm1004vdcAlmDwBufferOvlPortn_Type()
)
pm1004vdcAlmDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDwBufferOvlPortn.setStatus("current")
_Pm1004vdcAlmvideoProtocolStatusTable_Object = MibTable
pm1004vdcAlmvideoProtocolStatusTable = _Pm1004vdcAlmvideoProtocolStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmvideoProtocolStatusTable.setStatus("current")
_Pm1004vdcAlmvideoProtocolStatusEntry_Object = MibTableRow
pm1004vdcAlmvideoProtocolStatusEntry = _Pm1004vdcAlmvideoProtocolStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1)
)
pm1004vdcAlmvideoProtocolStatusEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmvideoProtocolStatusIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmvideoProtocolStatusEntry.setStatus("current")


class _Pm1004vdcAlmvideoProtocolStatusIndex_Type(Integer32):
    """Custom type pm1004vdcAlmvideoProtocolStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmvideoProtocolStatusIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmvideoProtocolStatusIndex_Object = MibTableColumn
pm1004vdcAlmvideoProtocolStatusIndex = _Pm1004vdcAlmvideoProtocolStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 1),
    _Pm1004vdcAlmvideoProtocolStatusIndex_Type()
)
pm1004vdcAlmvideoProtocolStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmvideoProtocolStatusIndex.setStatus("current")
_Pm1004vdcAlmSdiTxPortn_Type = EkiOnOff
_Pm1004vdcAlmSdiTxPortn_Object = MibTableColumn
pm1004vdcAlmSdiTxPortn = _Pm1004vdcAlmSdiTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 2),
    _Pm1004vdcAlmSdiTxPortn_Type()
)
pm1004vdcAlmSdiTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmSdiTxPortn.setStatus("current")
_Pm1004vdcAlmHdSdiPalTxPortn_Type = EkiOnOff
_Pm1004vdcAlmHdSdiPalTxPortn_Object = MibTableColumn
pm1004vdcAlmHdSdiPalTxPortn = _Pm1004vdcAlmHdSdiPalTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 3),
    _Pm1004vdcAlmHdSdiPalTxPortn_Type()
)
pm1004vdcAlmHdSdiPalTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmHdSdiPalTxPortn.setStatus("current")
_Pm1004vdcAlmHdSdiNtscTxPortn_Type = EkiOnOff
_Pm1004vdcAlmHdSdiNtscTxPortn_Object = MibTableColumn
pm1004vdcAlmHdSdiNtscTxPortn = _Pm1004vdcAlmHdSdiNtscTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 4),
    _Pm1004vdcAlmHdSdiNtscTxPortn_Type()
)
pm1004vdcAlmHdSdiNtscTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmHdSdiNtscTxPortn.setStatus("current")
_Pm1004vdcAlmDvbAsiTxPortn_Type = EkiOnOff
_Pm1004vdcAlmDvbAsiTxPortn_Object = MibTableColumn
pm1004vdcAlmDvbAsiTxPortn = _Pm1004vdcAlmDvbAsiTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 5),
    _Pm1004vdcAlmDvbAsiTxPortn_Type()
)
pm1004vdcAlmDvbAsiTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDvbAsiTxPortn.setStatus("current")
_Pm1004vdcAlmFastEtherTxPortn_Type = EkiOnOff
_Pm1004vdcAlmFastEtherTxPortn_Object = MibTableColumn
pm1004vdcAlmFastEtherTxPortn = _Pm1004vdcAlmFastEtherTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 6),
    _Pm1004vdcAlmFastEtherTxPortn_Type()
)
pm1004vdcAlmFastEtherTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmFastEtherTxPortn.setStatus("current")
_Pm1004vdcAlmGbeTxPortn_Type = EkiOnOff
_Pm1004vdcAlmGbeTxPortn_Object = MibTableColumn
pm1004vdcAlmGbeTxPortn = _Pm1004vdcAlmGbeTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 7),
    _Pm1004vdcAlmGbeTxPortn_Type()
)
pm1004vdcAlmGbeTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmGbeTxPortn.setStatus("current")
_Pm1004vdcAlmSdiRxPortn_Type = EkiOnOff
_Pm1004vdcAlmSdiRxPortn_Object = MibTableColumn
pm1004vdcAlmSdiRxPortn = _Pm1004vdcAlmSdiRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 10),
    _Pm1004vdcAlmSdiRxPortn_Type()
)
pm1004vdcAlmSdiRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmSdiRxPortn.setStatus("current")
_Pm1004vdcAlmHdSdiPalRxPortn_Type = EkiOnOff
_Pm1004vdcAlmHdSdiPalRxPortn_Object = MibTableColumn
pm1004vdcAlmHdSdiPalRxPortn = _Pm1004vdcAlmHdSdiPalRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 11),
    _Pm1004vdcAlmHdSdiPalRxPortn_Type()
)
pm1004vdcAlmHdSdiPalRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmHdSdiPalRxPortn.setStatus("current")
_Pm1004vdcAlmHdSdiNtscRxPortn_Type = EkiOnOff
_Pm1004vdcAlmHdSdiNtscRxPortn_Object = MibTableColumn
pm1004vdcAlmHdSdiNtscRxPortn = _Pm1004vdcAlmHdSdiNtscRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 12),
    _Pm1004vdcAlmHdSdiNtscRxPortn_Type()
)
pm1004vdcAlmHdSdiNtscRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmHdSdiNtscRxPortn.setStatus("current")
_Pm1004vdcAlmDvbAsiRxPortn_Type = EkiOnOff
_Pm1004vdcAlmDvbAsiRxPortn_Object = MibTableColumn
pm1004vdcAlmDvbAsiRxPortn = _Pm1004vdcAlmDvbAsiRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 13),
    _Pm1004vdcAlmDvbAsiRxPortn_Type()
)
pm1004vdcAlmDvbAsiRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDvbAsiRxPortn.setStatus("current")
_Pm1004vdcAlmFastEtherRxPortn_Type = EkiOnOff
_Pm1004vdcAlmFastEtherRxPortn_Object = MibTableColumn
pm1004vdcAlmFastEtherRxPortn = _Pm1004vdcAlmFastEtherRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 14),
    _Pm1004vdcAlmFastEtherRxPortn_Type()
)
pm1004vdcAlmFastEtherRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmFastEtherRxPortn.setStatus("current")
_Pm1004vdcAlmGbeRxPortn_Type = EkiOnOff
_Pm1004vdcAlmGbeRxPortn_Object = MibTableColumn
pm1004vdcAlmGbeRxPortn = _Pm1004vdcAlmGbeRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 2, 3, 112, 1, 15),
    _Pm1004vdcAlmGbeRxPortn_Type()
)
pm1004vdcAlmGbeRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmGbeRxPortn.setStatus("current")
_Pm1004vdcAlmLine_ObjectIdentity = ObjectIdentity
pm1004vdcAlmLine = _Pm1004vdcAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3)
)
_Pm1004vdcAlmLineNurg_ObjectIdentity = ObjectIdentity
pm1004vdcAlmLineNurg = _Pm1004vdcAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1)
)
_Pm1004vdcAlmlineXfp1WarningsTable_Object = MibTable
pm1004vdcAlmlineXfp1WarningsTable = _Pm1004vdcAlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1WarningsTable.setStatus("current")
_Pm1004vdcAlmlineXfp1WarningsEntry_Object = MibTableRow
pm1004vdcAlmlineXfp1WarningsEntry = _Pm1004vdcAlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1)
)
pm1004vdcAlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1WarningsEntry.setStatus("current")


class _Pm1004vdcAlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pm1004vdcAlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmlineXfp1WarningsIndex_Object = MibTableColumn
pm1004vdcAlmlineXfp1WarningsIndex = _Pm1004vdcAlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1, 1),
    _Pm1004vdcAlmlineXfp1WarningsIndex_Type()
)
pm1004vdcAlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1WarningsIndex.setStatus("current")
_Pm1004vdcAlmTxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPowerLowWarningPortn_Object = MibTableColumn
pm1004vdcAlmTxPowerLowWarningPortn = _Pm1004vdcAlmTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1, 2),
    _Pm1004vdcAlmTxPowerLowWarningPortn_Type()
)
pm1004vdcAlmTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPowerLowWarningPortn.setStatus("current")
_Pm1004vdcAlmTxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPowerHighWarningPortn_Object = MibTableColumn
pm1004vdcAlmTxPowerHighWarningPortn = _Pm1004vdcAlmTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1, 3),
    _Pm1004vdcAlmTxPowerHighWarningPortn_Type()
)
pm1004vdcAlmTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPowerHighWarningPortn.setStatus("current")
_Pm1004vdcAlmTxBiasLowWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmTxBiasLowWarningPortn_Object = MibTableColumn
pm1004vdcAlmTxBiasLowWarningPortn = _Pm1004vdcAlmTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1, 4),
    _Pm1004vdcAlmTxBiasLowWarningPortn_Type()
)
pm1004vdcAlmTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxBiasLowWarningPortn.setStatus("current")
_Pm1004vdcAlmTxBiasHighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmTxBiasHighWarningPortn_Object = MibTableColumn
pm1004vdcAlmTxBiasHighWarningPortn = _Pm1004vdcAlmTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1, 5),
    _Pm1004vdcAlmTxBiasHighWarningPortn_Type()
)
pm1004vdcAlmTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxBiasHighWarningPortn.setStatus("current")
_Pm1004vdcAlmTempLowWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmTempLowWarningPortn_Object = MibTableColumn
pm1004vdcAlmTempLowWarningPortn = _Pm1004vdcAlmTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1, 8),
    _Pm1004vdcAlmTempLowWarningPortn_Type()
)
pm1004vdcAlmTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTempLowWarningPortn.setStatus("current")
_Pm1004vdcAlmTempHighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmTempHighWarningPortn_Object = MibTableColumn
pm1004vdcAlmTempHighWarningPortn = _Pm1004vdcAlmTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1, 9),
    _Pm1004vdcAlmTempHighWarningPortn_Type()
)
pm1004vdcAlmTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTempHighWarningPortn.setStatus("current")
_Pm1004vdcAlmRxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPowerLowWarningPortn_Object = MibTableColumn
pm1004vdcAlmRxPowerLowWarningPortn = _Pm1004vdcAlmRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1, 16),
    _Pm1004vdcAlmRxPowerLowWarningPortn_Type()
)
pm1004vdcAlmRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPowerLowWarningPortn.setStatus("current")
_Pm1004vdcAlmRxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPowerHighWarningPortn_Object = MibTableColumn
pm1004vdcAlmRxPowerHighWarningPortn = _Pm1004vdcAlmRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 209, 1, 17),
    _Pm1004vdcAlmRxPowerHighWarningPortn_Type()
)
pm1004vdcAlmRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPowerHighWarningPortn.setStatus("current")
_Pm1004vdcAlmlineOtx1TlhWarningsTable_Object = MibTable
pm1004vdcAlmlineOtx1TlhWarningsTable = _Pm1004vdcAlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineOtx1TlhWarningsTable.setStatus("current")
_Pm1004vdcAlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pm1004vdcAlmlineOtx1TlhWarningsEntry = _Pm1004vdcAlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 225, 1)
)
pm1004vdcAlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pm1004vdcAlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pm1004vdcAlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pm1004vdcAlmlineOtx1TlhWarningsIndex = _Pm1004vdcAlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 225, 1, 1),
    _Pm1004vdcAlmlineOtx1TlhWarningsIndex_Type()
)
pm1004vdcAlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pm1004vdcAlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pm1004vdcAlmLineModulatorAgingHighWarningPortn = _Pm1004vdcAlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 225, 1, 6),
    _Pm1004vdcAlmLineModulatorAgingHighWarningPortn_Type()
)
pm1004vdcAlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pm1004vdcAlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmLineAgingHighWarningPortn_Object = MibTableColumn
pm1004vdcAlmLineAgingHighWarningPortn = _Pm1004vdcAlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 225, 1, 7),
    _Pm1004vdcAlmLineAgingHighWarningPortn_Type()
)
pm1004vdcAlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineAgingHighWarningPortn.setStatus("current")
_Pm1004vdcAlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pm1004vdcAlmLineFreqDevHighWarningPortn = _Pm1004vdcAlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 225, 1, 13),
    _Pm1004vdcAlmLineFreqDevHighWarningPortn_Type()
)
pm1004vdcAlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineFreqDevHighWarningPortn.setStatus("current")
_Pm1004vdcAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm1004vdcAlmLineLaserTempHighWarningPortn = _Pm1004vdcAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 1, 225, 1, 15),
    _Pm1004vdcAlmLineLaserTempHighWarningPortn_Type()
)
pm1004vdcAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm1004vdcAlmLineUrg_ObjectIdentity = ObjectIdentity
pm1004vdcAlmLineUrg = _Pm1004vdcAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2)
)
_Pm1004vdcAlmlineXfp1AlarmTable_Object = MibTable
pm1004vdcAlmlineXfp1AlarmTable = _Pm1004vdcAlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1AlarmTable.setStatus("current")
_Pm1004vdcAlmlineXfp1AlarmEntry_Object = MibTableRow
pm1004vdcAlmlineXfp1AlarmEntry = _Pm1004vdcAlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1)
)
pm1004vdcAlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1AlarmEntry.setStatus("current")


class _Pm1004vdcAlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pm1004vdcAlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmlineXfp1AlarmIndex_Object = MibTableColumn
pm1004vdcAlmlineXfp1AlarmIndex = _Pm1004vdcAlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1, 1),
    _Pm1004vdcAlmlineXfp1AlarmIndex_Type()
)
pm1004vdcAlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1AlarmIndex.setStatus("current")
_Pm1004vdcAlmTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPowerLowAlarmPortn_Object = MibTableColumn
pm1004vdcAlmTxPowerLowAlarmPortn = _Pm1004vdcAlmTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1, 2),
    _Pm1004vdcAlmTxPowerLowAlarmPortn_Type()
)
pm1004vdcAlmTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPowerLowAlarmPortn.setStatus("current")
_Pm1004vdcAlmTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPowerHighAlarmPortn_Object = MibTableColumn
pm1004vdcAlmTxPowerHighAlarmPortn = _Pm1004vdcAlmTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1, 3),
    _Pm1004vdcAlmTxPowerHighAlarmPortn_Type()
)
pm1004vdcAlmTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPowerHighAlarmPortn.setStatus("current")
_Pm1004vdcAlmTxBiasLowAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmTxBiasLowAlarmPortn_Object = MibTableColumn
pm1004vdcAlmTxBiasLowAlarmPortn = _Pm1004vdcAlmTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1, 4),
    _Pm1004vdcAlmTxBiasLowAlarmPortn_Type()
)
pm1004vdcAlmTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxBiasLowAlarmPortn.setStatus("current")
_Pm1004vdcAlmTxBiasHighAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmTxBiasHighAlarmPortn_Object = MibTableColumn
pm1004vdcAlmTxBiasHighAlarmPortn = _Pm1004vdcAlmTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1, 5),
    _Pm1004vdcAlmTxBiasHighAlarmPortn_Type()
)
pm1004vdcAlmTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxBiasHighAlarmPortn.setStatus("current")
_Pm1004vdcAlmTempLowAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmTempLowAlarmPortn_Object = MibTableColumn
pm1004vdcAlmTempLowAlarmPortn = _Pm1004vdcAlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1, 8),
    _Pm1004vdcAlmTempLowAlarmPortn_Type()
)
pm1004vdcAlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTempLowAlarmPortn.setStatus("current")
_Pm1004vdcAlmTempHighAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmTempHighAlarmPortn_Object = MibTableColumn
pm1004vdcAlmTempHighAlarmPortn = _Pm1004vdcAlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1, 9),
    _Pm1004vdcAlmTempHighAlarmPortn_Type()
)
pm1004vdcAlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTempHighAlarmPortn.setStatus("current")
_Pm1004vdcAlmRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPowerLowAlarmPortn_Object = MibTableColumn
pm1004vdcAlmRxPowerLowAlarmPortn = _Pm1004vdcAlmRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1, 16),
    _Pm1004vdcAlmRxPowerLowAlarmPortn_Type()
)
pm1004vdcAlmRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPowerLowAlarmPortn.setStatus("current")
_Pm1004vdcAlmRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPowerHighAlarmPortn_Object = MibTableColumn
pm1004vdcAlmRxPowerHighAlarmPortn = _Pm1004vdcAlmRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 208, 1, 17),
    _Pm1004vdcAlmRxPowerHighAlarmPortn_Type()
)
pm1004vdcAlmRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPowerHighAlarmPortn.setStatus("current")
_Pm1004vdcAlmlineXfp1CritTable_Object = MibTable
pm1004vdcAlmlineXfp1CritTable = _Pm1004vdcAlmlineXfp1CritTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 210)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1CritTable.setStatus("current")
_Pm1004vdcAlmlineXfp1CritEntry_Object = MibTableRow
pm1004vdcAlmlineXfp1CritEntry = _Pm1004vdcAlmlineXfp1CritEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 210, 1)
)
pm1004vdcAlmlineXfp1CritEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmlineXfp1CritIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1CritEntry.setStatus("current")


class _Pm1004vdcAlmlineXfp1CritIndex_Type(Integer32):
    """Custom type pm1004vdcAlmlineXfp1CritIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmlineXfp1CritIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmlineXfp1CritIndex_Object = MibTableColumn
pm1004vdcAlmlineXfp1CritIndex = _Pm1004vdcAlmlineXfp1CritIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 210, 1, 1),
    _Pm1004vdcAlmlineXfp1CritIndex_Type()
)
pm1004vdcAlmlineXfp1CritIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1CritIndex.setStatus("current")
_Pm1004vdcAlmTxPowerLowCritPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPowerLowCritPortn_Object = MibTableColumn
pm1004vdcAlmTxPowerLowCritPortn = _Pm1004vdcAlmTxPowerLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 210, 1, 2),
    _Pm1004vdcAlmTxPowerLowCritPortn_Type()
)
pm1004vdcAlmTxPowerLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPowerLowCritPortn.setStatus("current")
_Pm1004vdcAlmTxPowerHighCritPortn_Type = EkiOnOff
_Pm1004vdcAlmTxPowerHighCritPortn_Object = MibTableColumn
pm1004vdcAlmTxPowerHighCritPortn = _Pm1004vdcAlmTxPowerHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 210, 1, 3),
    _Pm1004vdcAlmTxPowerHighCritPortn_Type()
)
pm1004vdcAlmTxPowerHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxPowerHighCritPortn.setStatus("current")
_Pm1004vdcAlmRxPowerLowCritPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPowerLowCritPortn_Object = MibTableColumn
pm1004vdcAlmRxPowerLowCritPortn = _Pm1004vdcAlmRxPowerLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 210, 1, 16),
    _Pm1004vdcAlmRxPowerLowCritPortn_Type()
)
pm1004vdcAlmRxPowerLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPowerLowCritPortn.setStatus("current")
_Pm1004vdcAlmRxPowerHighCritPortn_Type = EkiOnOff
_Pm1004vdcAlmRxPowerHighCritPortn_Object = MibTableColumn
pm1004vdcAlmRxPowerHighCritPortn = _Pm1004vdcAlmRxPowerHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 210, 1, 17),
    _Pm1004vdcAlmRxPowerHighCritPortn_Type()
)
pm1004vdcAlmRxPowerHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxPowerHighCritPortn.setStatus("current")
_Pm1004vdcAlmlineXfp1SupplyAlarmTable_Object = MibTable
pm1004vdcAlmlineXfp1SupplyAlarmTable = _Pm1004vdcAlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pm1004vdcAlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pm1004vdcAlmlineXfp1SupplyAlarmEntry = _Pm1004vdcAlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1)
)
pm1004vdcAlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pm1004vdcAlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pm1004vdcAlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pm1004vdcAlmlineXfp1SupplyAlarmIndex = _Pm1004vdcAlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 1),
    _Pm1004vdcAlmlineXfp1SupplyAlarmIndex_Type()
)
pm1004vdcAlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pm1004vdcAlmVee5LowAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmVee5LowAlarmPortn_Object = MibTableColumn
pm1004vdcAlmVee5LowAlarmPortn = _Pm1004vdcAlmVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 2),
    _Pm1004vdcAlmVee5LowAlarmPortn_Type()
)
pm1004vdcAlmVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVee5LowAlarmPortn.setStatus("current")
_Pm1004vdcAlmVee5HighAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmVee5HighAlarmPortn_Object = MibTableColumn
pm1004vdcAlmVee5HighAlarmPortn = _Pm1004vdcAlmVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 3),
    _Pm1004vdcAlmVee5HighAlarmPortn_Type()
)
pm1004vdcAlmVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVee5HighAlarmPortn.setStatus("current")
_Pm1004vdcAlmVcc2LowAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc2LowAlarmPortn_Object = MibTableColumn
pm1004vdcAlmVcc2LowAlarmPortn = _Pm1004vdcAlmVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 4),
    _Pm1004vdcAlmVcc2LowAlarmPortn_Type()
)
pm1004vdcAlmVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc2LowAlarmPortn.setStatus("current")
_Pm1004vdcAlmVcc2HighAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc2HighAlarmPortn_Object = MibTableColumn
pm1004vdcAlmVcc2HighAlarmPortn = _Pm1004vdcAlmVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 5),
    _Pm1004vdcAlmVcc2HighAlarmPortn_Type()
)
pm1004vdcAlmVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc2HighAlarmPortn.setStatus("current")
_Pm1004vdcAlmVcc3LowAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc3LowAlarmPortn_Object = MibTableColumn
pm1004vdcAlmVcc3LowAlarmPortn = _Pm1004vdcAlmVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 6),
    _Pm1004vdcAlmVcc3LowAlarmPortn_Type()
)
pm1004vdcAlmVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc3LowAlarmPortn.setStatus("current")
_Pm1004vdcAlmVcc3HighAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc3HighAlarmPortn_Object = MibTableColumn
pm1004vdcAlmVcc3HighAlarmPortn = _Pm1004vdcAlmVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 7),
    _Pm1004vdcAlmVcc3HighAlarmPortn_Type()
)
pm1004vdcAlmVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc3HighAlarmPortn.setStatus("current")
_Pm1004vdcAlmVcc5LowAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc5LowAlarmPortn_Object = MibTableColumn
pm1004vdcAlmVcc5LowAlarmPortn = _Pm1004vdcAlmVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 8),
    _Pm1004vdcAlmVcc5LowAlarmPortn_Type()
)
pm1004vdcAlmVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc5LowAlarmPortn.setStatus("current")
_Pm1004vdcAlmVcc5HighAlarmPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc5HighAlarmPortn_Object = MibTableColumn
pm1004vdcAlmVcc5HighAlarmPortn = _Pm1004vdcAlmVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 9),
    _Pm1004vdcAlmVcc5HighAlarmPortn_Type()
)
pm1004vdcAlmVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc5HighAlarmPortn.setStatus("current")
_Pm1004vdcAlmVee5LowWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmVee5LowWarningPortn_Object = MibTableColumn
pm1004vdcAlmVee5LowWarningPortn = _Pm1004vdcAlmVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 10),
    _Pm1004vdcAlmVee5LowWarningPortn_Type()
)
pm1004vdcAlmVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVee5LowWarningPortn.setStatus("current")
_Pm1004vdcAlmVee5HighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmVee5HighWarningPortn_Object = MibTableColumn
pm1004vdcAlmVee5HighWarningPortn = _Pm1004vdcAlmVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 11),
    _Pm1004vdcAlmVee5HighWarningPortn_Type()
)
pm1004vdcAlmVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVee5HighWarningPortn.setStatus("current")
_Pm1004vdcAlmVcc2LowWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc2LowWarningPortn_Object = MibTableColumn
pm1004vdcAlmVcc2LowWarningPortn = _Pm1004vdcAlmVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 12),
    _Pm1004vdcAlmVcc2LowWarningPortn_Type()
)
pm1004vdcAlmVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc2LowWarningPortn.setStatus("current")
_Pm1004vdcAlmVcc2HighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc2HighWarningPortn_Object = MibTableColumn
pm1004vdcAlmVcc2HighWarningPortn = _Pm1004vdcAlmVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 13),
    _Pm1004vdcAlmVcc2HighWarningPortn_Type()
)
pm1004vdcAlmVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc2HighWarningPortn.setStatus("current")
_Pm1004vdcAlmVcc3LowWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc3LowWarningPortn_Object = MibTableColumn
pm1004vdcAlmVcc3LowWarningPortn = _Pm1004vdcAlmVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 14),
    _Pm1004vdcAlmVcc3LowWarningPortn_Type()
)
pm1004vdcAlmVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc3LowWarningPortn.setStatus("current")
_Pm1004vdcAlmVcc3HighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc3HighWarningPortn_Object = MibTableColumn
pm1004vdcAlmVcc3HighWarningPortn = _Pm1004vdcAlmVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 15),
    _Pm1004vdcAlmVcc3HighWarningPortn_Type()
)
pm1004vdcAlmVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc3HighWarningPortn.setStatus("current")
_Pm1004vdcAlmVcc5LowWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc5LowWarningPortn_Object = MibTableColumn
pm1004vdcAlmVcc5LowWarningPortn = _Pm1004vdcAlmVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 16),
    _Pm1004vdcAlmVcc5LowWarningPortn_Type()
)
pm1004vdcAlmVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc5LowWarningPortn.setStatus("current")
_Pm1004vdcAlmVcc5HighWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmVcc5HighWarningPortn_Object = MibTableColumn
pm1004vdcAlmVcc5HighWarningPortn = _Pm1004vdcAlmVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 212, 1, 17),
    _Pm1004vdcAlmVcc5HighWarningPortn_Type()
)
pm1004vdcAlmVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmVcc5HighWarningPortn.setStatus("current")
_Pm1004vdcAlmlineOtx1TlhAlarmsTable_Object = MibTable
pm1004vdcAlmlineOtx1TlhAlarmsTable = _Pm1004vdcAlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pm1004vdcAlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pm1004vdcAlmlineOtx1TlhAlarmsEntry = _Pm1004vdcAlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 224, 1)
)
pm1004vdcAlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pm1004vdcAlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pm1004vdcAlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pm1004vdcAlmlineOtx1TlhAlarmsIndex = _Pm1004vdcAlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 224, 1, 1),
    _Pm1004vdcAlmlineOtx1TlhAlarmsIndex_Type()
)
pm1004vdcAlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pm1004vdcAlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pm1004vdcAlmLineModulatorAgingHighAlaPortn = _Pm1004vdcAlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 224, 1, 6),
    _Pm1004vdcAlmLineModulatorAgingHighAlaPortn_Type()
)
pm1004vdcAlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pm1004vdcAlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmLineAgingHighAlaPortn_Object = MibTableColumn
pm1004vdcAlmLineAgingHighAlaPortn = _Pm1004vdcAlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 224, 1, 7),
    _Pm1004vdcAlmLineAgingHighAlaPortn_Type()
)
pm1004vdcAlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineAgingHighAlaPortn.setStatus("current")
_Pm1004vdcAlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pm1004vdcAlmLineFreqDevHighAlaPortn = _Pm1004vdcAlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 224, 1, 13),
    _Pm1004vdcAlmLineFreqDevHighAlaPortn_Type()
)
pm1004vdcAlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineFreqDevHighAlaPortn.setStatus("current")
_Pm1004vdcAlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pm1004vdcAlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pm1004vdcAlmLineLaserTempHighAlaPortn = _Pm1004vdcAlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 2, 224, 1, 15),
    _Pm1004vdcAlmLineLaserTempHighAlaPortn_Type()
)
pm1004vdcAlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineLaserTempHighAlaPortn.setStatus("current")
_Pm1004vdcAlmLineCrit_ObjectIdentity = ObjectIdentity
pm1004vdcAlmLineCrit = _Pm1004vdcAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3)
)
_Pm1004vdcAlmsynthAlmLineTable_Object = MibTable
pm1004vdcAlmsynthAlmLineTable = _Pm1004vdcAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsynthAlmLineTable.setStatus("current")
_Pm1004vdcAlmsynthAlmLineEntry_Object = MibTableRow
pm1004vdcAlmsynthAlmLineEntry = _Pm1004vdcAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1)
)
pm1004vdcAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmsynthAlmLineEntry.setStatus("current")


class _Pm1004vdcAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm1004vdcAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmsynthAlmLineIndex_Object = MibTableColumn
pm1004vdcAlmsynthAlmLineIndex = _Pm1004vdcAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 1),
    _Pm1004vdcAlmsynthAlmLineIndex_Type()
)
pm1004vdcAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmsynthAlmLineIndex.setStatus("current")
_Pm1004vdcAlmXfpAbsentPortn_Type = EkiOnOff
_Pm1004vdcAlmXfpAbsentPortn_Object = MibTableColumn
pm1004vdcAlmXfpAbsentPortn = _Pm1004vdcAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 2),
    _Pm1004vdcAlmXfpAbsentPortn_Type()
)
pm1004vdcAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmXfpAbsentPortn.setStatus("current")
_Pm1004vdcAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm1004vdcAlmXfpInitNotComplPortn_Object = MibTableColumn
pm1004vdcAlmXfpInitNotComplPortn = _Pm1004vdcAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 3),
    _Pm1004vdcAlmXfpInitNotComplPortn_Type()
)
pm1004vdcAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmXfpInitNotComplPortn.setStatus("current")
_Pm1004vdcAlmLineHwFailPortn_Type = EkiOnOff
_Pm1004vdcAlmLineHwFailPortn_Object = MibTableColumn
pm1004vdcAlmLineHwFailPortn = _Pm1004vdcAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 5),
    _Pm1004vdcAlmLineHwFailPortn_Type()
)
pm1004vdcAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineHwFailPortn.setStatus("current")
_Pm1004vdcAlmXfpTxOffPortn_Type = EkiOnOff
_Pm1004vdcAlmXfpTxOffPortn_Object = MibTableColumn
pm1004vdcAlmXfpTxOffPortn = _Pm1004vdcAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 6),
    _Pm1004vdcAlmXfpTxOffPortn_Type()
)
pm1004vdcAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmXfpTxOffPortn.setStatus("current")
_Pm1004vdcAlmLineLocalOosPortn_Type = EkiOnOff
_Pm1004vdcAlmLineLocalOosPortn_Object = MibTableColumn
pm1004vdcAlmLineLocalOosPortn = _Pm1004vdcAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 7),
    _Pm1004vdcAlmLineLocalOosPortn_Type()
)
pm1004vdcAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineLocalOosPortn.setStatus("current")
_Pm1004vdcAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm1004vdcAlmLineDdmWarningPortn_Object = MibTableColumn
pm1004vdcAlmLineDdmWarningPortn = _Pm1004vdcAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 10),
    _Pm1004vdcAlmLineDdmWarningPortn_Type()
)
pm1004vdcAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineDdmWarningPortn.setStatus("current")
_Pm1004vdcAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm1004vdcAlmLineDdmAlmPortn_Object = MibTableColumn
pm1004vdcAlmLineDdmAlmPortn = _Pm1004vdcAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 11),
    _Pm1004vdcAlmLineDdmAlmPortn_Type()
)
pm1004vdcAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineDdmAlmPortn.setStatus("current")
_Pm1004vdcAlmLineDdmCritPortn_Type = EkiOnOff
_Pm1004vdcAlmLineDdmCritPortn_Object = MibTableColumn
pm1004vdcAlmLineDdmCritPortn = _Pm1004vdcAlmLineDdmCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 12),
    _Pm1004vdcAlmLineDdmCritPortn_Type()
)
pm1004vdcAlmLineDdmCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineDdmCritPortn.setStatus("current")
_Pm1004vdcAlmLineFailPortn_Type = EkiOnOff
_Pm1004vdcAlmLineFailPortn_Object = MibTableColumn
pm1004vdcAlmLineFailPortn = _Pm1004vdcAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 13),
    _Pm1004vdcAlmLineFailPortn_Type()
)
pm1004vdcAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineFailPortn.setStatus("current")
_Pm1004vdcAlmLineActivePortn_Type = EkiOnOff
_Pm1004vdcAlmLineActivePortn_Object = MibTableColumn
pm1004vdcAlmLineActivePortn = _Pm1004vdcAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 7, 1, 17),
    _Pm1004vdcAlmLineActivePortn_Type()
)
pm1004vdcAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmLineActivePortn.setStatus("current")
_Pm1004vdcAlmdfrmAlmTable_Object = MibTable
pm1004vdcAlmdfrmAlmTable = _Pm1004vdcAlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmdfrmAlmTable.setStatus("current")
_Pm1004vdcAlmdfrmAlmEntry_Object = MibTableRow
pm1004vdcAlmdfrmAlmEntry = _Pm1004vdcAlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 128, 1)
)
pm1004vdcAlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmdfrmAlmEntry.setStatus("current")


class _Pm1004vdcAlmdfrmAlmIndex_Type(Integer32):
    """Custom type pm1004vdcAlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmdfrmAlmIndex_Object = MibTableColumn
pm1004vdcAlmdfrmAlmIndex = _Pm1004vdcAlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 128, 1, 1),
    _Pm1004vdcAlmdfrmAlmIndex_Type()
)
pm1004vdcAlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmdfrmAlmIndex.setStatus("current")
_Pm1004vdcAlmDwLossofsyncPortn_Type = EkiOnOff
_Pm1004vdcAlmDwLossofsyncPortn_Object = MibTableColumn
pm1004vdcAlmDwLossofsyncPortn = _Pm1004vdcAlmDwLossofsyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 128, 1, 5),
    _Pm1004vdcAlmDwLossofsyncPortn_Type()
)
pm1004vdcAlmDwLossofsyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDwLossofsyncPortn.setStatus("current")
_Pm1004vdcAlmlineSyncAlarmsTable_Object = MibTable
pm1004vdcAlmlineSyncAlarmsTable = _Pm1004vdcAlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineSyncAlarmsTable.setStatus("current")
_Pm1004vdcAlmlineSyncAlarmsEntry_Object = MibTableRow
pm1004vdcAlmlineSyncAlarmsEntry = _Pm1004vdcAlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 133, 1)
)
pm1004vdcAlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineSyncAlarmsEntry.setStatus("current")


class _Pm1004vdcAlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pm1004vdcAlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmlineSyncAlarmsIndex_Object = MibTableColumn
pm1004vdcAlmlineSyncAlarmsIndex = _Pm1004vdcAlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 133, 1, 1),
    _Pm1004vdcAlmlineSyncAlarmsIndex_Type()
)
pm1004vdcAlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmlineSyncAlarmsIndex.setStatus("current")
_Pm1004vdcAlmDwLockerrPortn_Type = EkiOnOff
_Pm1004vdcAlmDwLockerrPortn_Object = MibTableColumn
pm1004vdcAlmDwLockerrPortn = _Pm1004vdcAlmDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 133, 1, 13),
    _Pm1004vdcAlmDwLockerrPortn_Type()
)
pm1004vdcAlmDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDwLockerrPortn.setStatus("current")
_Pm1004vdcAlmUpLockerrPortn_Type = EkiOnOff
_Pm1004vdcAlmUpLockerrPortn_Object = MibTableColumn
pm1004vdcAlmUpLockerrPortn = _Pm1004vdcAlmUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 133, 1, 14),
    _Pm1004vdcAlmUpLockerrPortn_Type()
)
pm1004vdcAlmUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmUpLockerrPortn.setStatus("current")
_Pm1004vdcAlmDwLosPortn_Type = EkiOnOff
_Pm1004vdcAlmDwLosPortn_Object = MibTableColumn
pm1004vdcAlmDwLosPortn = _Pm1004vdcAlmDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 133, 1, 17),
    _Pm1004vdcAlmDwLosPortn_Type()
)
pm1004vdcAlmDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmDwLosPortn.setStatus("current")
_Pm1004vdcAlmlineXfp1AlarmsTable_Object = MibTable
pm1004vdcAlmlineXfp1AlarmsTable = _Pm1004vdcAlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1AlarmsTable.setStatus("current")
_Pm1004vdcAlmlineXfp1AlarmsEntry_Object = MibTableRow
pm1004vdcAlmlineXfp1AlarmsEntry = _Pm1004vdcAlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1)
)
pm1004vdcAlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1AlarmsEntry.setStatus("current")


class _Pm1004vdcAlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pm1004vdcAlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcAlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pm1004vdcAlmlineXfp1AlarmsIndex_Object = MibTableColumn
pm1004vdcAlmlineXfp1AlarmsIndex = _Pm1004vdcAlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 1),
    _Pm1004vdcAlmlineXfp1AlarmsIndex_Type()
)
pm1004vdcAlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmlineXfp1AlarmsIndex.setStatus("current")
_Pm1004vdcAlmModNrPortn_Type = EkiOnOff
_Pm1004vdcAlmModNrPortn_Object = MibTableColumn
pm1004vdcAlmModNrPortn = _Pm1004vdcAlmModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 3),
    _Pm1004vdcAlmModNrPortn_Type()
)
pm1004vdcAlmModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmModNrPortn.setStatus("current")
_Pm1004vdcAlmRxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004vdcAlmRxCdrNotLockedPortn_Object = MibTableColumn
pm1004vdcAlmRxCdrNotLockedPortn = _Pm1004vdcAlmRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 4),
    _Pm1004vdcAlmRxCdrNotLockedPortn_Type()
)
pm1004vdcAlmRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxCdrNotLockedPortn.setStatus("current")
_Pm1004vdcAlmRxNrPortn_Type = EkiOnOff
_Pm1004vdcAlmRxNrPortn_Object = MibTableColumn
pm1004vdcAlmRxNrPortn = _Pm1004vdcAlmRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 6),
    _Pm1004vdcAlmRxNrPortn_Type()
)
pm1004vdcAlmRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmRxNrPortn.setStatus("current")
_Pm1004vdcAlmTxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004vdcAlmTxCdrNotLockedPortn_Object = MibTableColumn
pm1004vdcAlmTxCdrNotLockedPortn = _Pm1004vdcAlmTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 7),
    _Pm1004vdcAlmTxCdrNotLockedPortn_Type()
)
pm1004vdcAlmTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxCdrNotLockedPortn.setStatus("current")
_Pm1004vdcAlmTxFaultPortn_Type = EkiOnOff
_Pm1004vdcAlmTxFaultPortn_Object = MibTableColumn
pm1004vdcAlmTxFaultPortn = _Pm1004vdcAlmTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 8),
    _Pm1004vdcAlmTxFaultPortn_Type()
)
pm1004vdcAlmTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxFaultPortn.setStatus("current")
_Pm1004vdcAlmTxNrPortn_Type = EkiOnOff
_Pm1004vdcAlmTxNrPortn_Object = MibTableColumn
pm1004vdcAlmTxNrPortn = _Pm1004vdcAlmTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 9),
    _Pm1004vdcAlmTxNrPortn_Type()
)
pm1004vdcAlmTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTxNrPortn.setStatus("current")
_Pm1004vdcAlmWavelengthUnlockedPortn_Type = EkiOnOff
_Pm1004vdcAlmWavelengthUnlockedPortn_Object = MibTableColumn
pm1004vdcAlmWavelengthUnlockedPortn = _Pm1004vdcAlmWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 15),
    _Pm1004vdcAlmWavelengthUnlockedPortn_Type()
)
pm1004vdcAlmWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmWavelengthUnlockedPortn.setStatus("current")
_Pm1004vdcAlmTecFaultPortn_Type = EkiOnOff
_Pm1004vdcAlmTecFaultPortn_Object = MibTableColumn
pm1004vdcAlmTecFaultPortn = _Pm1004vdcAlmTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 16),
    _Pm1004vdcAlmTecFaultPortn_Type()
)
pm1004vdcAlmTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmTecFaultPortn.setStatus("current")
_Pm1004vdcAlmApdSupplyFaultPortn_Type = EkiOnOff
_Pm1004vdcAlmApdSupplyFaultPortn_Object = MibTableColumn
pm1004vdcAlmApdSupplyFaultPortn = _Pm1004vdcAlmApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 2, 3, 3, 211, 1, 17),
    _Pm1004vdcAlmApdSupplyFaultPortn_Type()
)
pm1004vdcAlmApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcAlmApdSupplyFaultPortn.setStatus("current")
_Pm1004vdcmeasures_ObjectIdentity = ObjectIdentity
pm1004vdcmeasures = _Pm1004vdcmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3)
)
_Pm1004vdcMesrOther_ObjectIdentity = ObjectIdentity
pm1004vdcMesrOther = _Pm1004vdcMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 1)
)
_Pm1004vdcMesrsynth0_Type = EkiMeasureType
_Pm1004vdcMesrsynth0_Object = MibScalar
pm1004vdcMesrsynth0 = _Pm1004vdcMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 1, 0),
    _Pm1004vdcMesrsynth0_Type()
)
pm1004vdcMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrsynth0.setStatus("deprecated")
_Pm1004vdcMesrsynth1_Type = EkiMeasureType
_Pm1004vdcMesrsynth1_Object = MibScalar
pm1004vdcMesrsynth1 = _Pm1004vdcMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 1, 1),
    _Pm1004vdcMesrsynth1_Type()
)
pm1004vdcMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrsynth1.setStatus("deprecated")
_Pm1004vdcMesrClient_ObjectIdentity = ObjectIdentity
pm1004vdcMesrClient = _Pm1004vdcMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2)
)
_Pm1004vdcMesrtempMeasTable_Object = MibTable
pm1004vdcMesrtempMeasTable = _Pm1004vdcMesrtempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrtempMeasTable.setStatus("current")
_Pm1004vdcMesrtempMeasEntry_Object = MibTableRow
pm1004vdcMesrtempMeasEntry = _Pm1004vdcMesrtempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 16, 1)
)
pm1004vdcMesrtempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrtempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrtempMeasEntry.setStatus("current")


class _Pm1004vdcMesrtempMeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrtempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrtempMeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrtempMeasIndex_Object = MibTableColumn
pm1004vdcMesrtempMeasIndex = _Pm1004vdcMesrtempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 16, 1, 1),
    _Pm1004vdcMesrtempMeasIndex_Type()
)
pm1004vdcMesrtempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrtempMeasIndex.setStatus("current")


class _Pm1004vdcMesrtempMeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrtempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrtempMeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrtempMeasPortn_Object = MibTableColumn
pm1004vdcMesrtempMeasPortn = _Pm1004vdcMesrtempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 16, 1, 2),
    _Pm1004vdcMesrtempMeasPortn_Type()
)
pm1004vdcMesrtempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrtempMeasPortn.setStatus("current")
_Pm1004vdcMesrvoltMeasTable_Object = MibTable
pm1004vdcMesrvoltMeasTable = _Pm1004vdcMesrvoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrvoltMeasTable.setStatus("current")
_Pm1004vdcMesrvoltMeasEntry_Object = MibTableRow
pm1004vdcMesrvoltMeasEntry = _Pm1004vdcMesrvoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 24, 1)
)
pm1004vdcMesrvoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrvoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrvoltMeasEntry.setStatus("current")


class _Pm1004vdcMesrvoltMeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrvoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrvoltMeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrvoltMeasIndex_Object = MibTableColumn
pm1004vdcMesrvoltMeasIndex = _Pm1004vdcMesrvoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 24, 1, 1),
    _Pm1004vdcMesrvoltMeasIndex_Type()
)
pm1004vdcMesrvoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrvoltMeasIndex.setStatus("current")


class _Pm1004vdcMesrvoltMeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrvoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrvoltMeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrvoltMeasPortn_Object = MibTableColumn
pm1004vdcMesrvoltMeasPortn = _Pm1004vdcMesrvoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 24, 1, 2),
    _Pm1004vdcMesrvoltMeasPortn_Type()
)
pm1004vdcMesrvoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrvoltMeasPortn.setStatus("current")
_Pm1004vdcMesrbiasMeasTable_Object = MibTable
pm1004vdcMesrbiasMeasTable = _Pm1004vdcMesrbiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrbiasMeasTable.setStatus("current")
_Pm1004vdcMesrbiasMeasEntry_Object = MibTableRow
pm1004vdcMesrbiasMeasEntry = _Pm1004vdcMesrbiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 32, 1)
)
pm1004vdcMesrbiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrbiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrbiasMeasEntry.setStatus("current")


class _Pm1004vdcMesrbiasMeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrbiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrbiasMeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrbiasMeasIndex_Object = MibTableColumn
pm1004vdcMesrbiasMeasIndex = _Pm1004vdcMesrbiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 32, 1, 1),
    _Pm1004vdcMesrbiasMeasIndex_Type()
)
pm1004vdcMesrbiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrbiasMeasIndex.setStatus("current")


class _Pm1004vdcMesrbiasMeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrbiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrbiasMeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrbiasMeasPortn_Object = MibTableColumn
pm1004vdcMesrbiasMeasPortn = _Pm1004vdcMesrbiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 32, 1, 2),
    _Pm1004vdcMesrbiasMeasPortn_Type()
)
pm1004vdcMesrbiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrbiasMeasPortn.setStatus("current")
_Pm1004vdcMesrtxpwrMeasTable_Object = MibTable
pm1004vdcMesrtxpwrMeasTable = _Pm1004vdcMesrtxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrtxpwrMeasTable.setStatus("current")
_Pm1004vdcMesrtxpwrMeasEntry_Object = MibTableRow
pm1004vdcMesrtxpwrMeasEntry = _Pm1004vdcMesrtxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 40, 1)
)
pm1004vdcMesrtxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrtxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrtxpwrMeasEntry.setStatus("current")


class _Pm1004vdcMesrtxpwrMeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrtxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrtxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrtxpwrMeasIndex_Object = MibTableColumn
pm1004vdcMesrtxpwrMeasIndex = _Pm1004vdcMesrtxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 40, 1, 1),
    _Pm1004vdcMesrtxpwrMeasIndex_Type()
)
pm1004vdcMesrtxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrtxpwrMeasIndex.setStatus("current")


class _Pm1004vdcMesrtxpwrMeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrtxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrtxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrtxpwrMeasPortn_Object = MibTableColumn
pm1004vdcMesrtxpwrMeasPortn = _Pm1004vdcMesrtxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 40, 1, 2),
    _Pm1004vdcMesrtxpwrMeasPortn_Type()
)
pm1004vdcMesrtxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrtxpwrMeasPortn.setStatus("current")
_Pm1004vdcMesrrxpwrMeasTable_Object = MibTable
pm1004vdcMesrrxpwrMeasTable = _Pm1004vdcMesrrxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrrxpwrMeasTable.setStatus("current")
_Pm1004vdcMesrrxpwrMeasEntry_Object = MibTableRow
pm1004vdcMesrrxpwrMeasEntry = _Pm1004vdcMesrrxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 48, 1)
)
pm1004vdcMesrrxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrrxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrrxpwrMeasEntry.setStatus("current")


class _Pm1004vdcMesrrxpwrMeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrrxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrrxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrrxpwrMeasIndex_Object = MibTableColumn
pm1004vdcMesrrxpwrMeasIndex = _Pm1004vdcMesrrxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 48, 1, 1),
    _Pm1004vdcMesrrxpwrMeasIndex_Type()
)
pm1004vdcMesrrxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrrxpwrMeasIndex.setStatus("current")


class _Pm1004vdcMesrrxpwrMeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrrxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrrxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrrxpwrMeasPortn_Object = MibTableColumn
pm1004vdcMesrrxpwrMeasPortn = _Pm1004vdcMesrrxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 2, 48, 1, 2),
    _Pm1004vdcMesrrxpwrMeasPortn_Type()
)
pm1004vdcMesrrxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrrxpwrMeasPortn.setStatus("current")
_Pm1004vdcMesrLine_ObjectIdentity = ObjectIdentity
pm1004vdcMesrLine = _Pm1004vdcMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3)
)
_Pm1004vdcMesrxfp1LxModTempMeasTable_Object = MibTable
pm1004vdcMesrxfp1LxModTempMeasTable = _Pm1004vdcMesrxfp1LxModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxModTempMeasTable.setStatus("current")
_Pm1004vdcMesrxfp1LxModTempMeasEntry_Object = MibTableRow
pm1004vdcMesrxfp1LxModTempMeasEntry = _Pm1004vdcMesrxfp1LxModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 208, 1)
)
pm1004vdcMesrxfp1LxModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrxfp1LxModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxModTempMeasEntry.setStatus("current")


class _Pm1004vdcMesrxfp1LxModTempMeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LxModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrxfp1LxModTempMeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LxModTempMeasIndex_Object = MibTableColumn
pm1004vdcMesrxfp1LxModTempMeasIndex = _Pm1004vdcMesrxfp1LxModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 208, 1, 1),
    _Pm1004vdcMesrxfp1LxModTempMeasIndex_Type()
)
pm1004vdcMesrxfp1LxModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxModTempMeasIndex.setStatus("current")


class _Pm1004vdcMesrxfp1LxModTempMeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LxModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrxfp1LxModTempMeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LxModTempMeasPortn_Object = MibTableColumn
pm1004vdcMesrxfp1LxModTempMeasPortn = _Pm1004vdcMesrxfp1LxModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 208, 1, 2),
    _Pm1004vdcMesrxfp1LxModTempMeasPortn_Type()
)
pm1004vdcMesrxfp1LxModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxModTempMeasPortn.setStatus("current")
_Pm1004vdcMesrxfp1ReservedTable_Object = MibTable
pm1004vdcMesrxfp1ReservedTable = _Pm1004vdcMesrxfp1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1ReservedTable.setStatus("deprecated")
_Pm1004vdcMesrxfp1ReservedEntry_Object = MibTableRow
pm1004vdcMesrxfp1ReservedEntry = _Pm1004vdcMesrxfp1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 209, 1)
)
pm1004vdcMesrxfp1ReservedEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrxfp1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1ReservedEntry.setStatus("deprecated")


class _Pm1004vdcMesrxfp1ReservedIndex_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrxfp1ReservedIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1ReservedIndex_Object = MibTableColumn
pm1004vdcMesrxfp1ReservedIndex = _Pm1004vdcMesrxfp1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 209, 1, 1),
    _Pm1004vdcMesrxfp1ReservedIndex_Type()
)
pm1004vdcMesrxfp1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1ReservedIndex.setStatus("deprecated")


class _Pm1004vdcMesrxfp1ReservedPortn_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrxfp1ReservedPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1ReservedPortn_Object = MibTableColumn
pm1004vdcMesrxfp1ReservedPortn = _Pm1004vdcMesrxfp1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 209, 1, 2),
    _Pm1004vdcMesrxfp1ReservedPortn_Type()
)
pm1004vdcMesrxfp1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1ReservedPortn.setStatus("deprecated")
_Pm1004vdcMesrxfp1LoBiasCurrentMeasTable_Object = MibTable
pm1004vdcMesrxfp1LoBiasCurrentMeasTable = _Pm1004vdcMesrxfp1LoBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LoBiasCurrentMeasTable.setStatus("current")
_Pm1004vdcMesrxfp1LoBiasCurrentMeasEntry_Object = MibTableRow
pm1004vdcMesrxfp1LoBiasCurrentMeasEntry = _Pm1004vdcMesrxfp1LoBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 210, 1)
)
pm1004vdcMesrxfp1LoBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrxfp1LoBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LoBiasCurrentMeasEntry.setStatus("current")


class _Pm1004vdcMesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LoBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrxfp1LoBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LoBiasCurrentMeasIndex_Object = MibTableColumn
pm1004vdcMesrxfp1LoBiasCurrentMeasIndex = _Pm1004vdcMesrxfp1LoBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 210, 1, 1),
    _Pm1004vdcMesrxfp1LoBiasCurrentMeasIndex_Type()
)
pm1004vdcMesrxfp1LoBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LoBiasCurrentMeasIndex.setStatus("current")


class _Pm1004vdcMesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LoBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrxfp1LoBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LoBiasCurrentMeasPortn_Object = MibTableColumn
pm1004vdcMesrxfp1LoBiasCurrentMeasPortn = _Pm1004vdcMesrxfp1LoBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 210, 1, 2),
    _Pm1004vdcMesrxfp1LoBiasCurrentMeasPortn_Type()
)
pm1004vdcMesrxfp1LoBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LoBiasCurrentMeasPortn.setStatus("current")
_Pm1004vdcMesrxfp1LoTxPowerMeasTable_Object = MibTable
pm1004vdcMesrxfp1LoTxPowerMeasTable = _Pm1004vdcMesrxfp1LoTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LoTxPowerMeasTable.setStatus("current")
_Pm1004vdcMesrxfp1LoTxPowerMeasEntry_Object = MibTableRow
pm1004vdcMesrxfp1LoTxPowerMeasEntry = _Pm1004vdcMesrxfp1LoTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 211, 1)
)
pm1004vdcMesrxfp1LoTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrxfp1LoTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LoTxPowerMeasEntry.setStatus("current")


class _Pm1004vdcMesrxfp1LoTxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LoTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrxfp1LoTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LoTxPowerMeasIndex_Object = MibTableColumn
pm1004vdcMesrxfp1LoTxPowerMeasIndex = _Pm1004vdcMesrxfp1LoTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 211, 1, 1),
    _Pm1004vdcMesrxfp1LoTxPowerMeasIndex_Type()
)
pm1004vdcMesrxfp1LoTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LoTxPowerMeasIndex.setStatus("current")


class _Pm1004vdcMesrxfp1LoTxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LoTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrxfp1LoTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LoTxPowerMeasPortn_Object = MibTableColumn
pm1004vdcMesrxfp1LoTxPowerMeasPortn = _Pm1004vdcMesrxfp1LoTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 211, 1, 2),
    _Pm1004vdcMesrxfp1LoTxPowerMeasPortn_Type()
)
pm1004vdcMesrxfp1LoTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LoTxPowerMeasPortn.setStatus("current")
_Pm1004vdcMesrxfp1LiRxPowerMeasTable_Object = MibTable
pm1004vdcMesrxfp1LiRxPowerMeasTable = _Pm1004vdcMesrxfp1LiRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LiRxPowerMeasTable.setStatus("current")
_Pm1004vdcMesrxfp1LiRxPowerMeasEntry_Object = MibTableRow
pm1004vdcMesrxfp1LiRxPowerMeasEntry = _Pm1004vdcMesrxfp1LiRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 212, 1)
)
pm1004vdcMesrxfp1LiRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrxfp1LiRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LiRxPowerMeasEntry.setStatus("current")


class _Pm1004vdcMesrxfp1LiRxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LiRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrxfp1LiRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LiRxPowerMeasIndex_Object = MibTableColumn
pm1004vdcMesrxfp1LiRxPowerMeasIndex = _Pm1004vdcMesrxfp1LiRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 212, 1, 1),
    _Pm1004vdcMesrxfp1LiRxPowerMeasIndex_Type()
)
pm1004vdcMesrxfp1LiRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LiRxPowerMeasIndex.setStatus("current")


class _Pm1004vdcMesrxfp1LiRxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LiRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrxfp1LiRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LiRxPowerMeasPortn_Object = MibTableColumn
pm1004vdcMesrxfp1LiRxPowerMeasPortn = _Pm1004vdcMesrxfp1LiRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 212, 1, 2),
    _Pm1004vdcMesrxfp1LiRxPowerMeasPortn_Type()
)
pm1004vdcMesrxfp1LiRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LiRxPowerMeasPortn.setStatus("current")
_Pm1004vdcMesrxfp1LxAux1MeasTable_Object = MibTable
pm1004vdcMesrxfp1LxAux1MeasTable = _Pm1004vdcMesrxfp1LxAux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxAux1MeasTable.setStatus("deprecated")
_Pm1004vdcMesrxfp1LxAux1MeasEntry_Object = MibTableRow
pm1004vdcMesrxfp1LxAux1MeasEntry = _Pm1004vdcMesrxfp1LxAux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 213, 1)
)
pm1004vdcMesrxfp1LxAux1MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrxfp1LxAux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxAux1MeasEntry.setStatus("deprecated")


class _Pm1004vdcMesrxfp1LxAux1MeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LxAux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrxfp1LxAux1MeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LxAux1MeasIndex_Object = MibTableColumn
pm1004vdcMesrxfp1LxAux1MeasIndex = _Pm1004vdcMesrxfp1LxAux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 213, 1, 1),
    _Pm1004vdcMesrxfp1LxAux1MeasIndex_Type()
)
pm1004vdcMesrxfp1LxAux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxAux1MeasIndex.setStatus("deprecated")


class _Pm1004vdcMesrxfp1LxAux1MeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LxAux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrxfp1LxAux1MeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LxAux1MeasPortn_Object = MibTableColumn
pm1004vdcMesrxfp1LxAux1MeasPortn = _Pm1004vdcMesrxfp1LxAux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 213, 1, 2),
    _Pm1004vdcMesrxfp1LxAux1MeasPortn_Type()
)
pm1004vdcMesrxfp1LxAux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxAux1MeasPortn.setStatus("deprecated")
_Pm1004vdcMesrxfp1LxAux2MeasTable_Object = MibTable
pm1004vdcMesrxfp1LxAux2MeasTable = _Pm1004vdcMesrxfp1LxAux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxAux2MeasTable.setStatus("deprecated")
_Pm1004vdcMesrxfp1LxAux2MeasEntry_Object = MibTableRow
pm1004vdcMesrxfp1LxAux2MeasEntry = _Pm1004vdcMesrxfp1LxAux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 214, 1)
)
pm1004vdcMesrxfp1LxAux2MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrxfp1LxAux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxAux2MeasEntry.setStatus("deprecated")


class _Pm1004vdcMesrxfp1LxAux2MeasIndex_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LxAux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrxfp1LxAux2MeasIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LxAux2MeasIndex_Object = MibTableColumn
pm1004vdcMesrxfp1LxAux2MeasIndex = _Pm1004vdcMesrxfp1LxAux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 214, 1, 1),
    _Pm1004vdcMesrxfp1LxAux2MeasIndex_Type()
)
pm1004vdcMesrxfp1LxAux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxAux2MeasIndex.setStatus("deprecated")


class _Pm1004vdcMesrxfp1LxAux2MeasPortn_Type(Integer32):
    """Custom type pm1004vdcMesrxfp1LxAux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrxfp1LxAux2MeasPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrxfp1LxAux2MeasPortn_Object = MibTableColumn
pm1004vdcMesrxfp1LxAux2MeasPortn = _Pm1004vdcMesrxfp1LxAux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 214, 1, 2),
    _Pm1004vdcMesrxfp1LxAux2MeasPortn_Type()
)
pm1004vdcMesrxfp1LxAux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrxfp1LxAux2MeasPortn.setStatus("deprecated")
_Pm1004vdcMesrotx1AgingTable_Object = MibTable
pm1004vdcMesrotx1AgingTable = _Pm1004vdcMesrotx1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1AgingTable.setStatus("current")
_Pm1004vdcMesrotx1AgingEntry_Object = MibTableRow
pm1004vdcMesrotx1AgingEntry = _Pm1004vdcMesrotx1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 224, 1)
)
pm1004vdcMesrotx1AgingEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrotx1AgingIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1AgingEntry.setStatus("current")


class _Pm1004vdcMesrotx1AgingIndex_Type(Integer32):
    """Custom type pm1004vdcMesrotx1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrotx1AgingIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrotx1AgingIndex_Object = MibTableColumn
pm1004vdcMesrotx1AgingIndex = _Pm1004vdcMesrotx1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 224, 1, 1),
    _Pm1004vdcMesrotx1AgingIndex_Type()
)
pm1004vdcMesrotx1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1AgingIndex.setStatus("current")


class _Pm1004vdcMesrotx1AgingPortn_Type(Integer32):
    """Custom type pm1004vdcMesrotx1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrotx1AgingPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrotx1AgingPortn_Object = MibTableColumn
pm1004vdcMesrotx1AgingPortn = _Pm1004vdcMesrotx1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 224, 1, 2),
    _Pm1004vdcMesrotx1AgingPortn_Type()
)
pm1004vdcMesrotx1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1AgingPortn.setStatus("current")
_Pm1004vdcMesrotx1LaserTemperatureTable_Object = MibTable
pm1004vdcMesrotx1LaserTemperatureTable = _Pm1004vdcMesrotx1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1LaserTemperatureTable.setStatus("deprecated")
_Pm1004vdcMesrotx1LaserTemperatureEntry_Object = MibTableRow
pm1004vdcMesrotx1LaserTemperatureEntry = _Pm1004vdcMesrotx1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 225, 1)
)
pm1004vdcMesrotx1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrotx1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1LaserTemperatureEntry.setStatus("deprecated")


class _Pm1004vdcMesrotx1LaserTemperatureIndex_Type(Integer32):
    """Custom type pm1004vdcMesrotx1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrotx1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrotx1LaserTemperatureIndex_Object = MibTableColumn
pm1004vdcMesrotx1LaserTemperatureIndex = _Pm1004vdcMesrotx1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 225, 1, 1),
    _Pm1004vdcMesrotx1LaserTemperatureIndex_Type()
)
pm1004vdcMesrotx1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1LaserTemperatureIndex.setStatus("deprecated")


class _Pm1004vdcMesrotx1LaserTemperaturePortn_Type(Integer32):
    """Custom type pm1004vdcMesrotx1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrotx1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrotx1LaserTemperaturePortn_Object = MibTableColumn
pm1004vdcMesrotx1LaserTemperaturePortn = _Pm1004vdcMesrotx1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 225, 1, 2),
    _Pm1004vdcMesrotx1LaserTemperaturePortn_Type()
)
pm1004vdcMesrotx1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1LaserTemperaturePortn.setStatus("deprecated")
_Pm1004vdcMesrotx1FreqDeviationTable_Object = MibTable
pm1004vdcMesrotx1FreqDeviationTable = _Pm1004vdcMesrotx1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1FreqDeviationTable.setStatus("current")
_Pm1004vdcMesrotx1FreqDeviationEntry_Object = MibTableRow
pm1004vdcMesrotx1FreqDeviationEntry = _Pm1004vdcMesrotx1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 226, 1)
)
pm1004vdcMesrotx1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrotx1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1FreqDeviationEntry.setStatus("current")


class _Pm1004vdcMesrotx1FreqDeviationIndex_Type(Integer32):
    """Custom type pm1004vdcMesrotx1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrotx1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrotx1FreqDeviationIndex_Object = MibTableColumn
pm1004vdcMesrotx1FreqDeviationIndex = _Pm1004vdcMesrotx1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 226, 1, 1),
    _Pm1004vdcMesrotx1FreqDeviationIndex_Type()
)
pm1004vdcMesrotx1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1FreqDeviationIndex.setStatus("current")


class _Pm1004vdcMesrotx1FreqDeviationPortn_Type(Integer32):
    """Custom type pm1004vdcMesrotx1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrotx1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrotx1FreqDeviationPortn_Object = MibTableColumn
pm1004vdcMesrotx1FreqDeviationPortn = _Pm1004vdcMesrotx1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 226, 1, 2),
    _Pm1004vdcMesrotx1FreqDeviationPortn_Type()
)
pm1004vdcMesrotx1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1FreqDeviationPortn.setStatus("current")
_Pm1004vdcMesrotx1LaserWvlengthTable_Object = MibTable
pm1004vdcMesrotx1LaserWvlengthTable = _Pm1004vdcMesrotx1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1LaserWvlengthTable.setStatus("current")
_Pm1004vdcMesrotx1LaserWvlengthEntry_Object = MibTableRow
pm1004vdcMesrotx1LaserWvlengthEntry = _Pm1004vdcMesrotx1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 227, 1)
)
pm1004vdcMesrotx1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMesrotx1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1LaserWvlengthEntry.setStatus("current")


class _Pm1004vdcMesrotx1LaserWvlengthIndex_Type(Integer32):
    """Custom type pm1004vdcMesrotx1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMesrotx1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pm1004vdcMesrotx1LaserWvlengthIndex_Object = MibTableColumn
pm1004vdcMesrotx1LaserWvlengthIndex = _Pm1004vdcMesrotx1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 227, 1, 1),
    _Pm1004vdcMesrotx1LaserWvlengthIndex_Type()
)
pm1004vdcMesrotx1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1LaserWvlengthIndex.setStatus("current")


class _Pm1004vdcMesrotx1LaserWvlengthPortn_Type(Integer32):
    """Custom type pm1004vdcMesrotx1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vdcMesrotx1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pm1004vdcMesrotx1LaserWvlengthPortn_Object = MibTableColumn
pm1004vdcMesrotx1LaserWvlengthPortn = _Pm1004vdcMesrotx1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 3, 3, 227, 1, 2),
    _Pm1004vdcMesrotx1LaserWvlengthPortn_Type()
)
pm1004vdcMesrotx1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMesrotx1LaserWvlengthPortn.setStatus("current")
_Pm1004vdccounters_ObjectIdentity = ObjectIdentity
pm1004vdccounters = _Pm1004vdccounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4)
)
_Pm1004vdcCntOther_ObjectIdentity = ObjectIdentity
pm1004vdcCntOther = _Pm1004vdcCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 1)
)
_Pm1004vdcCntClient_ObjectIdentity = ObjectIdentity
pm1004vdcCntClient = _Pm1004vdcCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 2)
)
_Pm1004vdcCntLine_ObjectIdentity = ObjectIdentity
pm1004vdcCntLine = _Pm1004vdcCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3)
)
_Pm1004vdcCntdfrmB1ErrCntTable_Object = MibTable
pm1004vdcCntdfrmB1ErrCntTable = _Pm1004vdcCntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmB1ErrCntTable.setStatus("current")
_Pm1004vdcCntdfrmB1ErrCntEntry_Object = MibTableRow
pm1004vdcCntdfrmB1ErrCntEntry = _Pm1004vdcCntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 152, 1)
)
pm1004vdcCntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmB1ErrCntEntry.setStatus("current")


class _Pm1004vdcCntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm1004vdcCntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcCntdfrmB1ErrCntIndex_Object = MibTableColumn
pm1004vdcCntdfrmB1ErrCntIndex = _Pm1004vdcCntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 152, 1, 1),
    _Pm1004vdcCntdfrmB1ErrCntIndex_Type()
)
pm1004vdcCntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmB1ErrCntIndex.setStatus("current")
_Pm1004vdcCntdfrmB1ErrCntValuePortn_Type = Counter32
_Pm1004vdcCntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pm1004vdcCntdfrmB1ErrCntValuePortn = _Pm1004vdcCntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 152, 1, 2),
    _Pm1004vdcCntdfrmB1ErrCntValuePortn_Type()
)
pm1004vdcCntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmB1ErrCntValuePortn.setStatus("current")
_Pm1004vdcCntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm1004vdcCntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm1004vdcCntdfrmB1ErrCntErrorPortn = _Pm1004vdcCntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 152, 1, 3),
    _Pm1004vdcCntdfrmB1ErrCntErrorPortn_Type()
)
pm1004vdcCntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pm1004vdcCntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcCntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm1004vdcCntdfrmB1ErrCntOverloadPortn = _Pm1004vdcCntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 152, 1, 4),
    _Pm1004vdcCntdfrmB1ErrCntOverloadPortn_Type()
)
pm1004vdcCntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm1004vdcCntdfrmTimCntTable_Object = MibTable
pm1004vdcCntdfrmTimCntTable = _Pm1004vdcCntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmTimCntTable.setStatus("current")
_Pm1004vdcCntdfrmTimCntEntry_Object = MibTableRow
pm1004vdcCntdfrmTimCntEntry = _Pm1004vdcCntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 153, 1)
)
pm1004vdcCntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmTimCntEntry.setStatus("current")


class _Pm1004vdcCntdfrmTimCntIndex_Type(Integer32):
    """Custom type pm1004vdcCntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcCntdfrmTimCntIndex_Object = MibTableColumn
pm1004vdcCntdfrmTimCntIndex = _Pm1004vdcCntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 153, 1, 1),
    _Pm1004vdcCntdfrmTimCntIndex_Type()
)
pm1004vdcCntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmTimCntIndex.setStatus("current")
_Pm1004vdcCntdfrmTimCntValuePortn_Type = Counter32
_Pm1004vdcCntdfrmTimCntValuePortn_Object = MibTableColumn
pm1004vdcCntdfrmTimCntValuePortn = _Pm1004vdcCntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 153, 1, 2),
    _Pm1004vdcCntdfrmTimCntValuePortn_Type()
)
pm1004vdcCntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmTimCntValuePortn.setStatus("current")
_Pm1004vdcCntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pm1004vdcCntdfrmTimCntErrorPortn_Object = MibTableColumn
pm1004vdcCntdfrmTimCntErrorPortn = _Pm1004vdcCntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 153, 1, 3),
    _Pm1004vdcCntdfrmTimCntErrorPortn_Type()
)
pm1004vdcCntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmTimCntErrorPortn.setStatus("current")
_Pm1004vdcCntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcCntdfrmTimCntOverloadPortn_Object = MibTableColumn
pm1004vdcCntdfrmTimCntOverloadPortn = _Pm1004vdcCntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 3, 153, 1, 4),
    _Pm1004vdcCntdfrmTimCntOverloadPortn_Type()
)
pm1004vdcCntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCntdfrmTimCntOverloadPortn.setStatus("current")
_Pm1004vdcCntCountersReset_Type = EkiOnOff
_Pm1004vdcCntCountersReset_Object = MibScalar
pm1004vdcCntCountersReset = _Pm1004vdcCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 259),
    _Pm1004vdcCntCountersReset_Type()
)
pm1004vdcCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCntCountersReset.setStatus("current")
_Pm1004vdcCntCountersStop_Type = EkiOnOff
_Pm1004vdcCntCountersStop_Object = MibScalar
pm1004vdcCntCountersStop = _Pm1004vdcCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 4, 260),
    _Pm1004vdcCntCountersStop_Type()
)
pm1004vdcCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCntCountersStop.setStatus("current")
_Pm1004vdccontrolsWrite_ObjectIdentity = ObjectIdentity
pm1004vdccontrolsWrite = _Pm1004vdccontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6)
)
_Pm1004vdcCtrlOther_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlOther = _Pm1004vdcCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1)
)
_Pm1004vdcCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlconfMgnt1 = _Pm1004vdcCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 1)
)
_Pm1004vdcCtrlConf1Load1_Type = EkiOnOff
_Pm1004vdcCtrlConf1Load1_Object = MibScalar
pm1004vdcCtrlConf1Load1 = _Pm1004vdcCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 1, 1),
    _Pm1004vdcCtrlConf1Load1_Type()
)
pm1004vdcCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlConf1Load1.setStatus("current")
_Pm1004vdcCtrlConf2Load1_Type = EkiOnOff
_Pm1004vdcCtrlConf2Load1_Object = MibScalar
pm1004vdcCtrlConf2Load1 = _Pm1004vdcCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 1, 2),
    _Pm1004vdcCtrlConf2Load1_Type()
)
pm1004vdcCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlConf2Load1.setStatus("current")
_Pm1004vdcCtrlConf2Flash1_Type = EkiOnOff
_Pm1004vdcCtrlConf2Flash1_Object = MibScalar
pm1004vdcCtrlConf2Flash1 = _Pm1004vdcCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 1, 10),
    _Pm1004vdcCtrlConf2Flash1_Type()
)
pm1004vdcCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlConf2Flash1.setStatus("current")
_Pm1004vdcCtrlConf2Clear1_Type = EkiOnOff
_Pm1004vdcCtrlConf2Clear1_Object = MibScalar
pm1004vdcCtrlConf2Clear1 = _Pm1004vdcCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 1, 14),
    _Pm1004vdcCtrlConf2Clear1_Type()
)
pm1004vdcCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlConf2Clear1.setStatus("current")
_Pm1004vdcCtrlsynth4_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlsynth4 = _Pm1004vdcCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 4)
)
_Pm1004vdcCtrlCorrelatOn_Type = EkiOnOff
_Pm1004vdcCtrlCorrelatOn_Object = MibScalar
pm1004vdcCtrlCorrelatOn = _Pm1004vdcCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 4, 1),
    _Pm1004vdcCtrlCorrelatOn_Type()
)
pm1004vdcCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlCorrelatOn.setStatus("current")
_Pm1004vdcCtrlCorrelatOff_Type = EkiOnOff
_Pm1004vdcCtrlCorrelatOff_Object = MibScalar
pm1004vdcCtrlCorrelatOff = _Pm1004vdcCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 4, 2),
    _Pm1004vdcCtrlCorrelatOff_Type()
)
pm1004vdcCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlCorrelatOff.setStatus("current")
_Pm1004vdcCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlswMgnt = _Pm1004vdcCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 5)
)
_Pm1004vdcCtrlColdReset_Type = EkiOnOff
_Pm1004vdcCtrlColdReset_Object = MibScalar
pm1004vdcCtrlColdReset = _Pm1004vdcCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 5, 2),
    _Pm1004vdcCtrlColdReset_Type()
)
pm1004vdcCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlColdReset.setStatus("current")
_Pm1004vdcCtrlWarmReset_Type = EkiOnOff
_Pm1004vdcCtrlWarmReset_Object = MibScalar
pm1004vdcCtrlWarmReset = _Pm1004vdcCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 5, 3),
    _Pm1004vdcCtrlWarmReset_Type()
)
pm1004vdcCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlWarmReset.setStatus("current")
_Pm1004vdcCtrlLoadSwBank1_Type = EkiOnOff
_Pm1004vdcCtrlLoadSwBank1_Object = MibScalar
pm1004vdcCtrlLoadSwBank1 = _Pm1004vdcCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 5, 5),
    _Pm1004vdcCtrlLoadSwBank1_Type()
)
pm1004vdcCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlLoadSwBank1.setStatus("current")
_Pm1004vdcCtrlLoadSwBank2_Type = EkiOnOff
_Pm1004vdcCtrlLoadSwBank2_Object = MibScalar
pm1004vdcCtrlLoadSwBank2 = _Pm1004vdcCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 5, 6),
    _Pm1004vdcCtrlLoadSwBank2_Type()
)
pm1004vdcCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlLoadSwBank2.setStatus("current")
_Pm1004vdcCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlgwMgnt = _Pm1004vdcCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 6)
)
_Pm1004vdcCtrlCurrentGwReset_Type = EkiOnOff
_Pm1004vdcCtrlCurrentGwReset_Object = MibScalar
pm1004vdcCtrlCurrentGwReset = _Pm1004vdcCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 6, 1),
    _Pm1004vdcCtrlCurrentGwReset_Type()
)
pm1004vdcCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlCurrentGwReset.setStatus("current")
_Pm1004vdcCtrlLoadGwBank1_Type = EkiOnOff
_Pm1004vdcCtrlLoadGwBank1_Object = MibScalar
pm1004vdcCtrlLoadGwBank1 = _Pm1004vdcCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 6, 5),
    _Pm1004vdcCtrlLoadGwBank1_Type()
)
pm1004vdcCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlLoadGwBank1.setStatus("current")
_Pm1004vdcCtrlLoadGwBank2_Type = EkiOnOff
_Pm1004vdcCtrlLoadGwBank2_Object = MibScalar
pm1004vdcCtrlLoadGwBank2 = _Pm1004vdcCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 6, 6),
    _Pm1004vdcCtrlLoadGwBank2_Type()
)
pm1004vdcCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlLoadGwBank2.setStatus("current")
_Pm1004vdcCtrlLoadGwBank3_Type = EkiOnOff
_Pm1004vdcCtrlLoadGwBank3_Object = MibScalar
pm1004vdcCtrlLoadGwBank3 = _Pm1004vdcCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 6, 7),
    _Pm1004vdcCtrlLoadGwBank3_Type()
)
pm1004vdcCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlLoadGwBank3.setStatus("current")
_Pm1004vdcCtrlLoadGwBank4_Type = EkiOnOff
_Pm1004vdcCtrlLoadGwBank4_Object = MibScalar
pm1004vdcCtrlLoadGwBank4 = _Pm1004vdcCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 6, 8),
    _Pm1004vdcCtrlLoadGwBank4_Type()
)
pm1004vdcCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlLoadGwBank4.setStatus("current")
_Pm1004vdcCtrlledTest_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlledTest = _Pm1004vdcCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 192)
)
_Pm1004vdcCtrlGreenLed_Type = EkiOnOff
_Pm1004vdcCtrlGreenLed_Object = MibScalar
pm1004vdcCtrlGreenLed = _Pm1004vdcCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 192, 1),
    _Pm1004vdcCtrlGreenLed_Type()
)
pm1004vdcCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlGreenLed.setStatus("current")
_Pm1004vdcCtrlRedLed_Type = EkiOnOff
_Pm1004vdcCtrlRedLed_Object = MibScalar
pm1004vdcCtrlRedLed = _Pm1004vdcCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 192, 2),
    _Pm1004vdcCtrlRedLed_Type()
)
pm1004vdcCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlRedLed.setStatus("current")
_Pm1004vdcCtrlLedOff_Type = EkiOnOff
_Pm1004vdcCtrlLedOff_Object = MibScalar
pm1004vdcCtrlLedOff = _Pm1004vdcCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 192, 3),
    _Pm1004vdcCtrlLedOff_Type()
)
pm1004vdcCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlLedOff.setStatus("current")
_Pm1004vdcCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlmoduleOosMode = _Pm1004vdcCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 193)
)
_Pm1004vdcCtrlModuleOosMode_Type = EkiOnOff
_Pm1004vdcCtrlModuleOosMode_Object = MibScalar
pm1004vdcCtrlModuleOosMode = _Pm1004vdcCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 193, 1),
    _Pm1004vdcCtrlModuleOosMode_Type()
)
pm1004vdcCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlModuleOosMode.setStatus("current")
_Pm1004vdcCtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlmaintenanceMode = _Pm1004vdcCtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 197)
)
_Pm1004vdcCtrlMaintenanceMode_Type = EkiOnOff
_Pm1004vdcCtrlMaintenanceMode_Object = MibScalar
pm1004vdcCtrlMaintenanceMode = _Pm1004vdcCtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 1, 197, 1),
    _Pm1004vdcCtrlMaintenanceMode_Type()
)
pm1004vdcCtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlMaintenanceMode.setStatus("current")
_Pm1004vdcCtrlClient_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlClient = _Pm1004vdcCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2)
)
_Pm1004vdcCtrlaccessLoopTable_Object = MibTable
pm1004vdcCtrlaccessLoopTable = _Pm1004vdcCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlaccessLoopTable.setStatus("current")
_Pm1004vdcCtrlaccessLoopEntry_Object = MibTableRow
pm1004vdcCtrlaccessLoopEntry = _Pm1004vdcCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 16, 1)
)
pm1004vdcCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlaccessLoopEntry.setStatus("current")


class _Pm1004vdcCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlaccessLoopIndex_Object = MibTableColumn
pm1004vdcCtrlaccessLoopIndex = _Pm1004vdcCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 16, 1, 1),
    _Pm1004vdcCtrlaccessLoopIndex_Type()
)
pm1004vdcCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlaccessLoopIndex.setStatus("current")
_Pm1004vdcCtrlaccessLoopPortn_Type = EkiState
_Pm1004vdcCtrlaccessLoopPortn_Object = MibTableColumn
pm1004vdcCtrlaccessLoopPortn = _Pm1004vdcCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 16, 1, 2),
    _Pm1004vdcCtrlaccessLoopPortn_Type()
)
pm1004vdcCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlaccessLoopPortn.setStatus("current")
_Pm1004vdcCtrlportOosModeTable_Object = MibTable
pm1004vdcCtrlportOosModeTable = _Pm1004vdcCtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlportOosModeTable.setStatus("current")
_Pm1004vdcCtrlportOosModeEntry_Object = MibTableRow
pm1004vdcCtrlportOosModeEntry = _Pm1004vdcCtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 18, 1)
)
pm1004vdcCtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlportOosModeEntry.setStatus("current")


class _Pm1004vdcCtrlportOosModeIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlportOosModeIndex_Object = MibTableColumn
pm1004vdcCtrlportOosModeIndex = _Pm1004vdcCtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 18, 1, 1),
    _Pm1004vdcCtrlportOosModeIndex_Type()
)
pm1004vdcCtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlportOosModeIndex.setStatus("current")
_Pm1004vdcCtrlportOosModePortn_Type = Pm1004vdcClientOosMode
_Pm1004vdcCtrlportOosModePortn_Object = MibTableColumn
pm1004vdcCtrlportOosModePortn = _Pm1004vdcCtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 18, 1, 2),
    _Pm1004vdcCtrlportOosModePortn_Type()
)
pm1004vdcCtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlportOosModePortn.setStatus("current")
_Pm1004vdcCtrlsfpOffCtrlTable_Object = MibTable
pm1004vdcCtrlsfpOffCtrlTable = _Pm1004vdcCtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlsfpOffCtrlTable.setStatus("current")
_Pm1004vdcCtrlsfpOffCtrlEntry_Object = MibTableRow
pm1004vdcCtrlsfpOffCtrlEntry = _Pm1004vdcCtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 20, 1)
)
pm1004vdcCtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlsfpOffCtrlEntry.setStatus("current")


class _Pm1004vdcCtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlsfpOffCtrlIndex_Object = MibTableColumn
pm1004vdcCtrlsfpOffCtrlIndex = _Pm1004vdcCtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 20, 1, 1),
    _Pm1004vdcCtrlsfpOffCtrlIndex_Type()
)
pm1004vdcCtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlsfpOffCtrlIndex.setStatus("current")
_Pm1004vdcCtrlsfpOffCtrlPortn_Type = EkiState
_Pm1004vdcCtrlsfpOffCtrlPortn_Object = MibTableColumn
pm1004vdcCtrlsfpOffCtrlPortn = _Pm1004vdcCtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 20, 1, 2),
    _Pm1004vdcCtrlsfpOffCtrlPortn_Type()
)
pm1004vdcCtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlsfpOffCtrlPortn.setStatus("current")
_Pm1004vdcCtrlcsfUpInsTable_Object = MibTable
pm1004vdcCtrlcsfUpInsTable = _Pm1004vdcCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlcsfUpInsTable.setStatus("current")
_Pm1004vdcCtrlcsfUpInsEntry_Object = MibTableRow
pm1004vdcCtrlcsfUpInsEntry = _Pm1004vdcCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 21, 1)
)
pm1004vdcCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlcsfUpInsEntry.setStatus("current")


class _Pm1004vdcCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlcsfUpInsIndex_Object = MibTableColumn
pm1004vdcCtrlcsfUpInsIndex = _Pm1004vdcCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 21, 1, 1),
    _Pm1004vdcCtrlcsfUpInsIndex_Type()
)
pm1004vdcCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlcsfUpInsIndex.setStatus("current")
_Pm1004vdcCtrlcsfUpInsPortn_Type = EkiState
_Pm1004vdcCtrlcsfUpInsPortn_Object = MibTableColumn
pm1004vdcCtrlcsfUpInsPortn = _Pm1004vdcCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 21, 1, 2),
    _Pm1004vdcCtrlcsfUpInsPortn_Type()
)
pm1004vdcCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlcsfUpInsPortn.setStatus("current")
_Pm1004vdcCtrlcaisDwInsTable_Object = MibTable
pm1004vdcCtrlcaisDwInsTable = _Pm1004vdcCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlcaisDwInsTable.setStatus("current")
_Pm1004vdcCtrlcaisDwInsEntry_Object = MibTableRow
pm1004vdcCtrlcaisDwInsEntry = _Pm1004vdcCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 22, 1)
)
pm1004vdcCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlcaisDwInsEntry.setStatus("current")


class _Pm1004vdcCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlcaisDwInsIndex_Object = MibTableColumn
pm1004vdcCtrlcaisDwInsIndex = _Pm1004vdcCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 22, 1, 1),
    _Pm1004vdcCtrlcaisDwInsIndex_Type()
)
pm1004vdcCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlcaisDwInsIndex.setStatus("current")
_Pm1004vdcCtrlcaisDwInsPortn_Type = EkiState
_Pm1004vdcCtrlcaisDwInsPortn_Object = MibTableColumn
pm1004vdcCtrlcaisDwInsPortn = _Pm1004vdcCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 22, 1, 2),
    _Pm1004vdcCtrlcaisDwInsPortn_Type()
)
pm1004vdcCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlcaisDwInsPortn.setStatus("current")
_Pm1004vdcCtrlclientAccessTermLoopTable_Object = MibTable
pm1004vdcCtrlclientAccessTermLoopTable = _Pm1004vdcCtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlclientAccessTermLoopTable.setStatus("current")
_Pm1004vdcCtrlclientAccessTermLoopEntry_Object = MibTableRow
pm1004vdcCtrlclientAccessTermLoopEntry = _Pm1004vdcCtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 26, 1)
)
pm1004vdcCtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm1004vdcCtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm1004vdcCtrlclientAccessTermLoopIndex = _Pm1004vdcCtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 26, 1, 1),
    _Pm1004vdcCtrlclientAccessTermLoopIndex_Type()
)
pm1004vdcCtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlclientAccessTermLoopIndex.setStatus("current")
_Pm1004vdcCtrlclientAccessTermLoopPortn_Type = EkiState
_Pm1004vdcCtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm1004vdcCtrlclientAccessTermLoopPortn = _Pm1004vdcCtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 26, 1, 2),
    _Pm1004vdcCtrlclientAccessTermLoopPortn_Type()
)
pm1004vdcCtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlclientAccessTermLoopPortn.setStatus("current")
_Pm1004vdcCtrlrxVideoProtocolTable_Object = MibTable
pm1004vdcCtrlrxVideoProtocolTable = _Pm1004vdcCtrlrxVideoProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 43)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlrxVideoProtocolTable.setStatus("current")
_Pm1004vdcCtrlrxVideoProtocolEntry_Object = MibTableRow
pm1004vdcCtrlrxVideoProtocolEntry = _Pm1004vdcCtrlrxVideoProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 43, 1)
)
pm1004vdcCtrlrxVideoProtocolEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlrxVideoProtocolIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlrxVideoProtocolEntry.setStatus("current")


class _Pm1004vdcCtrlrxVideoProtocolIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlrxVideoProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlrxVideoProtocolIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlrxVideoProtocolIndex_Object = MibTableColumn
pm1004vdcCtrlrxVideoProtocolIndex = _Pm1004vdcCtrlrxVideoProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 43, 1, 1),
    _Pm1004vdcCtrlrxVideoProtocolIndex_Type()
)
pm1004vdcCtrlrxVideoProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlrxVideoProtocolIndex.setStatus("current")
_Pm1004vdcCtrlrxVideoProtocolPortn_Type = EkiState
_Pm1004vdcCtrlrxVideoProtocolPortn_Object = MibTableColumn
pm1004vdcCtrlrxVideoProtocolPortn = _Pm1004vdcCtrlrxVideoProtocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 43, 1, 2),
    _Pm1004vdcCtrlrxVideoProtocolPortn_Type()
)
pm1004vdcCtrlrxVideoProtocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlrxVideoProtocolPortn.setStatus("current")
_Pm1004vdcCtrladddropClientRxProtectTable_Object = MibTable
pm1004vdcCtrladddropClientRxProtectTable = _Pm1004vdcCtrladddropClientRxProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 128)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrladddropClientRxProtectTable.setStatus("current")
_Pm1004vdcCtrladddropClientRxProtectEntry_Object = MibTableRow
pm1004vdcCtrladddropClientRxProtectEntry = _Pm1004vdcCtrladddropClientRxProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 128, 1)
)
pm1004vdcCtrladddropClientRxProtectEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrladddropClientRxProtectIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrladddropClientRxProtectEntry.setStatus("current")


class _Pm1004vdcCtrladddropClientRxProtectIndex_Type(Integer32):
    """Custom type pm1004vdcCtrladddropClientRxProtectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrladddropClientRxProtectIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrladddropClientRxProtectIndex_Object = MibTableColumn
pm1004vdcCtrladddropClientRxProtectIndex = _Pm1004vdcCtrladddropClientRxProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 128, 1, 1),
    _Pm1004vdcCtrladddropClientRxProtectIndex_Type()
)
pm1004vdcCtrladddropClientRxProtectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrladddropClientRxProtectIndex.setStatus("current")
_Pm1004vdcCtrladddropClientRxProtectPortn_Type = Pm1004vdcProtectionTimeSlot
_Pm1004vdcCtrladddropClientRxProtectPortn_Object = MibTableColumn
pm1004vdcCtrladddropClientRxProtectPortn = _Pm1004vdcCtrladddropClientRxProtectPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 128, 1, 2),
    _Pm1004vdcCtrladddropClientRxProtectPortn_Type()
)
pm1004vdcCtrladddropClientRxProtectPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrladddropClientRxProtectPortn.setStatus("current")
_Pm1004vdcCtrladddropTsClientModeTable_Object = MibTable
pm1004vdcCtrladddropTsClientModeTable = _Pm1004vdcCtrladddropTsClientModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 136)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrladddropTsClientModeTable.setStatus("current")
_Pm1004vdcCtrladddropTsClientModeEntry_Object = MibTableRow
pm1004vdcCtrladddropTsClientModeEntry = _Pm1004vdcCtrladddropTsClientModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 136, 1)
)
pm1004vdcCtrladddropTsClientModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrladddropTsClientModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrladddropTsClientModeEntry.setStatus("current")


class _Pm1004vdcCtrladddropTsClientModeIndex_Type(Integer32):
    """Custom type pm1004vdcCtrladddropTsClientModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrladddropTsClientModeIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrladddropTsClientModeIndex_Object = MibTableColumn
pm1004vdcCtrladddropTsClientModeIndex = _Pm1004vdcCtrladddropTsClientModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 136, 1, 1),
    _Pm1004vdcCtrladddropTsClientModeIndex_Type()
)
pm1004vdcCtrladddropTsClientModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrladddropTsClientModeIndex.setStatus("current")
_Pm1004vdcCtrladddropTsClientModePortn_Type = Pm1004vdcModeTimeSlot
_Pm1004vdcCtrladddropTsClientModePortn_Object = MibTableColumn
pm1004vdcCtrladddropTsClientModePortn = _Pm1004vdcCtrladddropTsClientModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 2, 136, 1, 2),
    _Pm1004vdcCtrladddropTsClientModePortn_Type()
)
pm1004vdcCtrladddropTsClientModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrladddropTsClientModePortn.setStatus("current")
_Pm1004vdcCtrlLine_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlLine = _Pm1004vdcCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3)
)
_Pm1004vdcCtrlcommAccessLoop_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlcommAccessLoop = _Pm1004vdcCtrlcommAccessLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 64)
)
_Pm1004vdcCtrlCommAccessloop_Type = EkiOnOff
_Pm1004vdcCtrlCommAccessloop_Object = MibScalar
pm1004vdcCtrlCommAccessloop = _Pm1004vdcCtrlCommAccessloop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 64, 1),
    _Pm1004vdcCtrlCommAccessloop_Type()
)
pm1004vdcCtrlCommAccessloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlCommAccessloop.setStatus("deprecated")
_Pm1004vdcCtrllineLoop_ObjectIdentity = ObjectIdentity
pm1004vdcCtrllineLoop = _Pm1004vdcCtrllineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 66)
)
_Pm1004vdcCtrlLineLoop_Type = EkiOnOff
_Pm1004vdcCtrlLineLoop_Object = MibScalar
pm1004vdcCtrlLineLoop = _Pm1004vdcCtrlLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 66, 1),
    _Pm1004vdcCtrlLineLoop_Type()
)
pm1004vdcCtrlLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlLineLoop.setStatus("deprecated")
_Pm1004vdcCtrlProtMgnt_ObjectIdentity = ObjectIdentity
pm1004vdcCtrlProtMgnt = _Pm1004vdcCtrlProtMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 73)
)


class _Pm1004vdcCtrlLineNumber_Type(Unsigned32):
    """Custom type pm1004vdcCtrlLineNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Pm1004vdcCtrlLineNumber_Type.__name__ = "Unsigned32"
_Pm1004vdcCtrlLineNumber_Object = MibScalar
pm1004vdcCtrlLineNumber = _Pm1004vdcCtrlLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 73, 1),
    _Pm1004vdcCtrlLineNumber_Type()
)
pm1004vdcCtrlLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlLineNumber.setStatus("current")
_Pm1004vdcCtrlProtMode_Type = EkiMode
_Pm1004vdcCtrlProtMode_Object = MibScalar
pm1004vdcCtrlProtMode = _Pm1004vdcCtrlProtMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 73, 2),
    _Pm1004vdcCtrlProtMode_Type()
)
pm1004vdcCtrlProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlProtMode.setStatus("current")
_Pm1004vdcCtrllineOosModeTable_Object = MibTable
pm1004vdcCtrllineOosModeTable = _Pm1004vdcCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrllineOosModeTable.setStatus("current")
_Pm1004vdcCtrllineOosModeEntry_Object = MibTableRow
pm1004vdcCtrllineOosModeEntry = _Pm1004vdcCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 74, 1)
)
pm1004vdcCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrllineOosModeEntry.setStatus("current")


class _Pm1004vdcCtrllineOosModeIndex_Type(Integer32):
    """Custom type pm1004vdcCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrllineOosModeIndex_Object = MibTableColumn
pm1004vdcCtrllineOosModeIndex = _Pm1004vdcCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 74, 1, 1),
    _Pm1004vdcCtrllineOosModeIndex_Type()
)
pm1004vdcCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrllineOosModeIndex.setStatus("current")
_Pm1004vdcCtrllineOosModePortn_Type = EkiState
_Pm1004vdcCtrllineOosModePortn_Object = MibTableColumn
pm1004vdcCtrllineOosModePortn = _Pm1004vdcCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 74, 1, 2),
    _Pm1004vdcCtrllineOosModePortn_Type()
)
pm1004vdcCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrllineOosModePortn.setStatus("current")
_Pm1004vdcCtrldccEnableTable_Object = MibTable
pm1004vdcCtrldccEnableTable = _Pm1004vdcCtrldccEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 198)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrldccEnableTable.setStatus("current")
_Pm1004vdcCtrldccEnableEntry_Object = MibTableRow
pm1004vdcCtrldccEnableEntry = _Pm1004vdcCtrldccEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 198, 1)
)
pm1004vdcCtrldccEnableEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrldccEnableIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrldccEnableEntry.setStatus("current")


class _Pm1004vdcCtrldccEnableIndex_Type(Integer32):
    """Custom type pm1004vdcCtrldccEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrldccEnableIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrldccEnableIndex_Object = MibTableColumn
pm1004vdcCtrldccEnableIndex = _Pm1004vdcCtrldccEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 198, 1, 1),
    _Pm1004vdcCtrldccEnableIndex_Type()
)
pm1004vdcCtrldccEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrldccEnableIndex.setStatus("current")
_Pm1004vdcCtrldccEnablePortn_Type = EkiState
_Pm1004vdcCtrldccEnablePortn_Object = MibTableColumn
pm1004vdcCtrldccEnablePortn = _Pm1004vdcCtrldccEnablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 198, 1, 2),
    _Pm1004vdcCtrldccEnablePortn_Type()
)
pm1004vdcCtrldccEnablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrldccEnablePortn.setStatus("current")
_Pm1004vdcCtrlxfpOnoffTable_Object = MibTable
pm1004vdcCtrlxfpOnoffTable = _Pm1004vdcCtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpOnoffTable.setStatus("current")
_Pm1004vdcCtrlxfpOnoffEntry_Object = MibTableRow
pm1004vdcCtrlxfpOnoffEntry = _Pm1004vdcCtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 208, 1)
)
pm1004vdcCtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpOnoffEntry.setStatus("current")


class _Pm1004vdcCtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlxfpOnoffIndex_Object = MibTableColumn
pm1004vdcCtrlxfpOnoffIndex = _Pm1004vdcCtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 208, 1, 1),
    _Pm1004vdcCtrlxfpOnoffIndex_Type()
)
pm1004vdcCtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpOnoffIndex.setStatus("current")
_Pm1004vdcCtrlxfpOnoffPortn_Type = EkiState
_Pm1004vdcCtrlxfpOnoffPortn_Object = MibTableColumn
pm1004vdcCtrlxfpOnoffPortn = _Pm1004vdcCtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 208, 1, 2),
    _Pm1004vdcCtrlxfpOnoffPortn_Type()
)
pm1004vdcCtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpOnoffPortn.setStatus("current")
_Pm1004vdcCtrlxfpLineLoopTable_Object = MibTable
pm1004vdcCtrlxfpLineLoopTable = _Pm1004vdcCtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpLineLoopTable.setStatus("current")
_Pm1004vdcCtrlxfpLineLoopEntry_Object = MibTableRow
pm1004vdcCtrlxfpLineLoopEntry = _Pm1004vdcCtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 209, 1)
)
pm1004vdcCtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpLineLoopEntry.setStatus("current")


class _Pm1004vdcCtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlxfpLineLoopIndex_Object = MibTableColumn
pm1004vdcCtrlxfpLineLoopIndex = _Pm1004vdcCtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 209, 1, 1),
    _Pm1004vdcCtrlxfpLineLoopIndex_Type()
)
pm1004vdcCtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpLineLoopIndex.setStatus("current")
_Pm1004vdcCtrlxfpLineLoopPortn_Type = EkiState
_Pm1004vdcCtrlxfpLineLoopPortn_Object = MibTableColumn
pm1004vdcCtrlxfpLineLoopPortn = _Pm1004vdcCtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 209, 1, 2),
    _Pm1004vdcCtrlxfpLineLoopPortn_Type()
)
pm1004vdcCtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpLineLoopPortn.setStatus("current")
_Pm1004vdcCtrlxfpXfiLoopTable_Object = MibTable
pm1004vdcCtrlxfpXfiLoopTable = _Pm1004vdcCtrlxfpXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpXfiLoopTable.setStatus("current")
_Pm1004vdcCtrlxfpXfiLoopEntry_Object = MibTableRow
pm1004vdcCtrlxfpXfiLoopEntry = _Pm1004vdcCtrlxfpXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 210, 1)
)
pm1004vdcCtrlxfpXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCtrlxfpXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpXfiLoopEntry.setStatus("current")


class _Pm1004vdcCtrlxfpXfiLoopIndex_Type(Integer32):
    """Custom type pm1004vdcCtrlxfpXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCtrlxfpXfiLoopIndex_Type.__name__ = "Integer32"
_Pm1004vdcCtrlxfpXfiLoopIndex_Object = MibTableColumn
pm1004vdcCtrlxfpXfiLoopIndex = _Pm1004vdcCtrlxfpXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 210, 1, 1),
    _Pm1004vdcCtrlxfpXfiLoopIndex_Type()
)
pm1004vdcCtrlxfpXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpXfiLoopIndex.setStatus("current")
_Pm1004vdcCtrlxfpXfiLoopPortn_Type = EkiState
_Pm1004vdcCtrlxfpXfiLoopPortn_Object = MibTableColumn
pm1004vdcCtrlxfpXfiLoopPortn = _Pm1004vdcCtrlxfpXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 6, 3, 210, 1, 2),
    _Pm1004vdcCtrlxfpXfiLoopPortn_Type()
)
pm1004vdcCtrlxfpXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCtrlxfpXfiLoopPortn.setStatus("current")
_Pm1004vdcri_ObjectIdentity = ObjectIdentity
pm1004vdcri = _Pm1004vdcri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7)
)
_Pm1004vdcriTable_ObjectIdentity = ObjectIdentity
pm1004vdcriTable = _Pm1004vdcriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 1)
)
_Pm1004vdcRinvSfpTable_Object = MibTable
pm1004vdcRinvSfpTable = _Pm1004vdcRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcRinvSfpTable.setStatus("current")
_Pm1004vdcRinvSfpEntry_Object = MibTableRow
pm1004vdcRinvSfpEntry = _Pm1004vdcRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 1, 1, 1)
)
pm1004vdcRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcRinvSfpEntry.setStatus("current")


class _Pm1004vdcRinvSfpIndex_Type(Integer32):
    """Custom type pm1004vdcRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004vdcRinvSfpIndex_Type.__name__ = "Integer32"
_Pm1004vdcRinvSfpIndex_Object = MibTableColumn
pm1004vdcRinvSfpIndex = _Pm1004vdcRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 1, 1, 1, 1),
    _Pm1004vdcRinvSfpIndex_Type()
)
pm1004vdcRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcRinvSfpIndex.setStatus("current")
_Pm1004vdcRinvsfp_Type = DisplayString
_Pm1004vdcRinvsfp_Object = MibTableColumn
pm1004vdcRinvsfp = _Pm1004vdcRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 1, 1, 1, 2),
    _Pm1004vdcRinvsfp_Type()
)
pm1004vdcRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcRinvsfp.setStatus("current")
_Pm1004vdcRinvLineTable_Object = MibTable
pm1004vdcRinvLineTable = _Pm1004vdcRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm1004vdcRinvLineTable.setStatus("current")
_Pm1004vdcRinvLineEntry_Object = MibTableRow
pm1004vdcRinvLineEntry = _Pm1004vdcRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 1, 2, 1)
)
pm1004vdcRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcRinvLineEntry.setStatus("current")


class _Pm1004vdcRinvLineIndex_Type(Integer32):
    """Custom type pm1004vdcRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004vdcRinvLineIndex_Type.__name__ = "Integer32"
_Pm1004vdcRinvLineIndex_Object = MibTableColumn
pm1004vdcRinvLineIndex = _Pm1004vdcRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 1, 2, 1, 1),
    _Pm1004vdcRinvLineIndex_Type()
)
pm1004vdcRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcRinvLineIndex.setStatus("current")
_Pm1004vdcRinvxfpLine_Type = DisplayString
_Pm1004vdcRinvxfpLine_Object = MibTableColumn
pm1004vdcRinvxfpLine = _Pm1004vdcRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 1, 2, 1, 2),
    _Pm1004vdcRinvxfpLine_Type()
)
pm1004vdcRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcRinvxfpLine.setStatus("current")
_Pm1004vdcRinvReloadInventory_Type = EkiOnOff
_Pm1004vdcRinvReloadInventory_Object = MibScalar
pm1004vdcRinvReloadInventory = _Pm1004vdcRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 2),
    _Pm1004vdcRinvReloadInventory_Type()
)
pm1004vdcRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcRinvReloadInventory.setStatus("current")
_Pm1004vdcRinvHwPlatform_Type = DisplayString
_Pm1004vdcRinvHwPlatform_Object = MibScalar
pm1004vdcRinvHwPlatform = _Pm1004vdcRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 3),
    _Pm1004vdcRinvHwPlatform_Type()
)
pm1004vdcRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcRinvHwPlatform.setStatus("current")
_Pm1004vdcRinvModulePlatform_Type = DisplayString
_Pm1004vdcRinvModulePlatform_Object = MibScalar
pm1004vdcRinvModulePlatform = _Pm1004vdcRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 4),
    _Pm1004vdcRinvModulePlatform_Type()
)
pm1004vdcRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcRinvModulePlatform.setStatus("current")
_Pm1004vdcRinvSwPlatform_Type = DisplayString
_Pm1004vdcRinvSwPlatform_Object = MibScalar
pm1004vdcRinvSwPlatform = _Pm1004vdcRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 5),
    _Pm1004vdcRinvSwPlatform_Type()
)
pm1004vdcRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcRinvSwPlatform.setStatus("current")
_Pm1004vdcRinvGwPlatform_Type = DisplayString
_Pm1004vdcRinvGwPlatform_Object = MibScalar
pm1004vdcRinvGwPlatform = _Pm1004vdcRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 7, 6),
    _Pm1004vdcRinvGwPlatform_Type()
)
pm1004vdcRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcRinvGwPlatform.setStatus("current")
_Pm1004vdcdownload_ObjectIdentity = ObjectIdentity
pm1004vdcdownload = _Pm1004vdcdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8)
)
_Pm1004vdcDwlOther_ObjectIdentity = ObjectIdentity
pm1004vdcDwlOther = _Pm1004vdcDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1)
)
_Pm1004vdcDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm1004vdcDwlrestartProcess = _Pm1004vdcDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 0)
)
_Pm1004vdcDwlWarmRestartProcessed_Type = EkiOnOff
_Pm1004vdcDwlWarmRestartProcessed_Object = MibScalar
pm1004vdcDwlWarmRestartProcessed = _Pm1004vdcDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 0, 1),
    _Pm1004vdcDwlWarmRestartProcessed_Type()
)
pm1004vdcDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlWarmRestartProcessed.setStatus("current")
_Pm1004vdcDwlColdRestartProcessed_Type = EkiOnOff
_Pm1004vdcDwlColdRestartProcessed_Object = MibScalar
pm1004vdcDwlColdRestartProcessed = _Pm1004vdcDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 0, 2),
    _Pm1004vdcDwlColdRestartProcessed_Type()
)
pm1004vdcDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlColdRestartProcessed.setStatus("current")
_Pm1004vdcDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm1004vdcDwlswBanksUsed = _Pm1004vdcDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 1)
)
_Pm1004vdcDwlSwBank1Used_Type = EkiOnOff
_Pm1004vdcDwlSwBank1Used_Object = MibScalar
pm1004vdcDwlSwBank1Used = _Pm1004vdcDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 1, 1),
    _Pm1004vdcDwlSwBank1Used_Type()
)
pm1004vdcDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlSwBank1Used.setStatus("current")
_Pm1004vdcDwlSwBank2Used_Type = EkiOnOff
_Pm1004vdcDwlSwBank2Used_Object = MibScalar
pm1004vdcDwlSwBank2Used = _Pm1004vdcDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 1, 2),
    _Pm1004vdcDwlSwBank2Used_Type()
)
pm1004vdcDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlSwBank2Used.setStatus("current")
_Pm1004vdcDwlSwBank1Notempty_Type = EkiOnOff
_Pm1004vdcDwlSwBank1Notempty_Object = MibScalar
pm1004vdcDwlSwBank1Notempty = _Pm1004vdcDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 1, 5),
    _Pm1004vdcDwlSwBank1Notempty_Type()
)
pm1004vdcDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlSwBank1Notempty.setStatus("current")
_Pm1004vdcDwlSwBank2Notempty_Type = EkiOnOff
_Pm1004vdcDwlSwBank2Notempty_Object = MibScalar
pm1004vdcDwlSwBank2Notempty = _Pm1004vdcDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 1, 6),
    _Pm1004vdcDwlSwBank2Notempty_Type()
)
pm1004vdcDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlSwBank2Notempty.setStatus("current")
_Pm1004vdcDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm1004vdcDwlgwBanksUsed = _Pm1004vdcDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 2)
)
_Pm1004vdcDwlGwBank1Used_Type = EkiOnOff
_Pm1004vdcDwlGwBank1Used_Object = MibScalar
pm1004vdcDwlGwBank1Used = _Pm1004vdcDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 2, 1),
    _Pm1004vdcDwlGwBank1Used_Type()
)
pm1004vdcDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlGwBank1Used.setStatus("current")
_Pm1004vdcDwlGwBank2Used_Type = EkiOnOff
_Pm1004vdcDwlGwBank2Used_Object = MibScalar
pm1004vdcDwlGwBank2Used = _Pm1004vdcDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 2, 2),
    _Pm1004vdcDwlGwBank2Used_Type()
)
pm1004vdcDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlGwBank2Used.setStatus("current")
_Pm1004vdcDwlGwBank3Used_Type = EkiOnOff
_Pm1004vdcDwlGwBank3Used_Object = MibScalar
pm1004vdcDwlGwBank3Used = _Pm1004vdcDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 2, 3),
    _Pm1004vdcDwlGwBank3Used_Type()
)
pm1004vdcDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlGwBank3Used.setStatus("current")
_Pm1004vdcDwlGwBank4Used_Type = EkiOnOff
_Pm1004vdcDwlGwBank4Used_Object = MibScalar
pm1004vdcDwlGwBank4Used = _Pm1004vdcDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 2, 4),
    _Pm1004vdcDwlGwBank4Used_Type()
)
pm1004vdcDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlGwBank4Used.setStatus("current")
_Pm1004vdcDwlGwBank1Notempty_Type = EkiOnOff
_Pm1004vdcDwlGwBank1Notempty_Object = MibScalar
pm1004vdcDwlGwBank1Notempty = _Pm1004vdcDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 2, 5),
    _Pm1004vdcDwlGwBank1Notempty_Type()
)
pm1004vdcDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlGwBank1Notempty.setStatus("current")
_Pm1004vdcDwlGwBank2Notempty_Type = EkiOnOff
_Pm1004vdcDwlGwBank2Notempty_Object = MibScalar
pm1004vdcDwlGwBank2Notempty = _Pm1004vdcDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 2, 6),
    _Pm1004vdcDwlGwBank2Notempty_Type()
)
pm1004vdcDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlGwBank2Notempty.setStatus("current")
_Pm1004vdcDwlGwBank3Notempty_Type = EkiOnOff
_Pm1004vdcDwlGwBank3Notempty_Object = MibScalar
pm1004vdcDwlGwBank3Notempty = _Pm1004vdcDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 2, 7),
    _Pm1004vdcDwlGwBank3Notempty_Type()
)
pm1004vdcDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlGwBank3Notempty.setStatus("current")
_Pm1004vdcDwlGwBank4Notempty_Type = EkiOnOff
_Pm1004vdcDwlGwBank4Notempty_Object = MibScalar
pm1004vdcDwlGwBank4Notempty = _Pm1004vdcDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 1, 2, 8),
    _Pm1004vdcDwlGwBank4Notempty_Type()
)
pm1004vdcDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcDwlGwBank4Notempty.setStatus("current")
_Pm1004vdcDwlClient_ObjectIdentity = ObjectIdentity
pm1004vdcDwlClient = _Pm1004vdcDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 2)
)
_Pm1004vdcDwlLine_ObjectIdentity = ObjectIdentity
pm1004vdcDwlLine = _Pm1004vdcDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 8, 3)
)
_Pm1004vdcConfig_ObjectIdentity = ObjectIdentity
pm1004vdcConfig = _Pm1004vdcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9)
)
_Pm1004vdcCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm1004vdcCfgAccessCAisCsf = _Pm1004vdcCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1)
)
_Pm1004vdcCfgClientcaiscsfTable_Object = MibTable
pm1004vdcCfgClientcaiscsfTable = _Pm1004vdcCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgClientcaiscsfTable.setStatus("current")
_Pm1004vdcCfgClientcaiscsfEntry_Object = MibTableRow
pm1004vdcCfgClientcaiscsfEntry = _Pm1004vdcCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1, 1)
)
pm1004vdcCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgClientcaiscsfEntry.setStatus("current")


class _Pm1004vdcCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm1004vdcCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm1004vdcCfgClientcaiscsfIndex_Object = MibTableColumn
pm1004vdcCfgClientcaiscsfIndex = _Pm1004vdcCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1, 1, 1),
    _Pm1004vdcCfgClientcaiscsfIndex_Type()
)
pm1004vdcCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgClientcaiscsfIndex.setStatus("current")


class _Pm1004vdcCfgCAisModePortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgCAisModePortn_Object = MibTableColumn
pm1004vdcCfgCAisModePortn = _Pm1004vdcCfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1, 1, 3),
    _Pm1004vdcCfgCAisModePortn_Type()
)
pm1004vdcCfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgCAisModePortn.setStatus("current")


class _Pm1004vdcCfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgUpAccessioAlmPortn_Object = MibTableColumn
pm1004vdcCfgUpAccessioAlmPortn = _Pm1004vdcCfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1, 1, 9),
    _Pm1004vdcCfgUpAccessioAlmPortn_Type()
)
pm1004vdcCfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgUpAccessioAlmPortn.setStatus("current")


class _Pm1004vdcCfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgUpMapperDeAlmPortn_Object = MibTableColumn
pm1004vdcCfgUpMapperDeAlmPortn = _Pm1004vdcCfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1, 1, 10),
    _Pm1004vdcCfgUpMapperDeAlmPortn_Type()
)
pm1004vdcCfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgUpMapperDeAlmPortn.setStatus("current")


class _Pm1004vdcCfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgDownAccessioAlmPortn_Object = MibTableColumn
pm1004vdcCfgDownAccessioAlmPortn = _Pm1004vdcCfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1, 1, 17),
    _Pm1004vdcCfgDownAccessioAlmPortn_Type()
)
pm1004vdcCfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgDownAccessioAlmPortn.setStatus("current")


class _Pm1004vdcCfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgDownMapperDeAlmPortn_Object = MibTableColumn
pm1004vdcCfgDownMapperDeAlmPortn = _Pm1004vdcCfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1, 1, 18),
    _Pm1004vdcCfgDownMapperDeAlmPortn_Type()
)
pm1004vdcCfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgDownMapperDeAlmPortn.setStatus("current")


class _Pm1004vdcCfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgDownDfrmAlmPortn_Object = MibTableColumn
pm1004vdcCfgDownDfrmAlmPortn = _Pm1004vdcCfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1, 1, 19),
    _Pm1004vdcCfgDownDfrmAlmPortn_Type()
)
pm1004vdcCfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgDownDfrmAlmPortn.setStatus("current")


class _Pm1004vdcCfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pm1004vdcCfgDownLineSyncAlarmsPortn = _Pm1004vdcCfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 1, 1, 1, 20),
    _Pm1004vdcCfgDownLineSyncAlarmsPortn_Type()
)
pm1004vdcCfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgDownLineSyncAlarmsPortn.setStatus("deprecated")
_Pm1004vdcCfgStartup_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartup = _Pm1004vdcCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2)
)
_Pm1004vdcCfgClientStartupTable_Object = MibTable
pm1004vdcCfgClientStartupTable = _Pm1004vdcCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgClientStartupTable.setStatus("current")
_Pm1004vdcCfgClientStartupEntry_Object = MibTableRow
pm1004vdcCfgClientStartupEntry = _Pm1004vdcCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 1, 1)
)
pm1004vdcCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgClientStartupEntry.setStatus("current")


class _Pm1004vdcCfgClientStartupIndex_Type(Integer32):
    """Custom type pm1004vdcCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm1004vdcCfgClientStartupIndex_Object = MibTableColumn
pm1004vdcCfgClientStartupIndex = _Pm1004vdcCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 1, 1, 1),
    _Pm1004vdcCfgClientStartupIndex_Type()
)
pm1004vdcCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgClientStartupIndex.setStatus("current")


class _Pm1004vdcCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgSystConfPortPortn_Object = MibTableColumn
pm1004vdcCfgSystConfPortPortn = _Pm1004vdcCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 1, 1, 3),
    _Pm1004vdcCfgSystConfPortPortn_Type()
)
pm1004vdcCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgSystConfPortPortn.setStatus("current")


class _Pm1004vdcCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgNetConfPortPortn_Object = MibTableColumn
pm1004vdcCfgNetConfPortPortn = _Pm1004vdcCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 1, 1, 4),
    _Pm1004vdcCfgNetConfPortPortn_Type()
)
pm1004vdcCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgNetConfPortPortn.setStatus("current")


class _Pm1004vdcCfgAdddropConfPortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgAdddropConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgAdddropConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgAdddropConfPortPortn_Object = MibTableColumn
pm1004vdcCfgAdddropConfPortPortn = _Pm1004vdcCfgAdddropConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 1, 1, 5),
    _Pm1004vdcCfgAdddropConfPortPortn_Type()
)
pm1004vdcCfgAdddropConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgAdddropConfPortPortn.setStatus("deprecated")
_Pm1004vdctablelineStartup_ObjectIdentity = ObjectIdentity
pm1004vdctablelineStartup = _Pm1004vdctablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 2)
)


class _Pm1004vdcCfgsystConfLine1_Type(Unsigned32):
    """Custom type pm1004vdcCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgsystConfLine1_Object = MibScalar
pm1004vdcCfgsystConfLine1 = _Pm1004vdcCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 2, 2),
    _Pm1004vdcCfgsystConfLine1_Type()
)
pm1004vdcCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgsystConfLine1.setStatus("current")


class _Pm1004vdcCfglineOptions1_Type(Unsigned32):
    """Custom type pm1004vdcCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfglineOptions1_Type.__name__ = "Unsigned32"
_Pm1004vdcCfglineOptions1_Object = MibScalar
pm1004vdcCfglineOptions1 = _Pm1004vdcCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 2, 5),
    _Pm1004vdcCfglineOptions1_Type()
)
pm1004vdcCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfglineOptions1.setStatus("current")


class _Pm1004vdcCfgsystConfLine2_Type(Unsigned32):
    """Custom type pm1004vdcCfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgsystConfLine2_Object = MibScalar
pm1004vdcCfgsystConfLine2 = _Pm1004vdcCfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 2, 6),
    _Pm1004vdcCfgsystConfLine2_Type()
)
pm1004vdcCfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgsystConfLine2.setStatus("current")


class _Pm1004vdcCfglineSelection_Type(Unsigned32):
    """Custom type pm1004vdcCfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfglineSelection_Type.__name__ = "Unsigned32"
_Pm1004vdcCfglineSelection_Object = MibScalar
pm1004vdcCfglineSelection = _Pm1004vdcCfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 2, 7),
    _Pm1004vdcCfglineSelection_Type()
)
pm1004vdcCfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfglineSelection.setStatus("current")


class _Pm1004vdcCfglineOptions2_Type(Unsigned32):
    """Custom type pm1004vdcCfglineOptions2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfglineOptions2_Type.__name__ = "Unsigned32"
_Pm1004vdcCfglineOptions2_Object = MibScalar
pm1004vdcCfglineOptions2 = _Pm1004vdcCfglineOptions2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 2, 9),
    _Pm1004vdcCfglineOptions2_Type()
)
pm1004vdcCfglineOptions2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfglineOptions2.setStatus("current")
_Pm1004vdcCfgXfpTable_Object = MibTable
pm1004vdcCfgXfpTable = _Pm1004vdcCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgXfpTable.setStatus("current")
_Pm1004vdcCfgXfpEntry_Object = MibTableRow
pm1004vdcCfgXfpEntry = _Pm1004vdcCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 3, 1)
)
pm1004vdcCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgXfpEntry.setStatus("current")


class _Pm1004vdcCfgXfpIndex_Type(Integer32):
    """Custom type pm1004vdcCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgXfpIndex_Type.__name__ = "Integer32"
_Pm1004vdcCfgXfpIndex_Object = MibTableColumn
pm1004vdcCfgXfpIndex = _Pm1004vdcCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 3, 1, 1),
    _Pm1004vdcCfgXfpIndex_Type()
)
pm1004vdcCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgXfpIndex.setStatus("current")


class _Pm1004vdcCfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgSystConfXfpPortn_Object = MibTableColumn
pm1004vdcCfgSystConfXfpPortn = _Pm1004vdcCfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 3, 1, 3),
    _Pm1004vdcCfgSystConfXfpPortn_Type()
)
pm1004vdcCfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgSystConfXfpPortn.setStatus("current")


class _Pm1004vdcCfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgDataRateConfXfpPortn_Object = MibTableColumn
pm1004vdcCfgDataRateConfXfpPortn = _Pm1004vdcCfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 2, 3, 1, 4),
    _Pm1004vdcCfgDataRateConfXfpPortn_Type()
)
pm1004vdcCfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgDataRateConfXfpPortn.setStatus("deprecated")
_Pm1004vdcCfgLabels_ObjectIdentity = ObjectIdentity
pm1004vdcCfgLabels = _Pm1004vdcCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 3)
)
_Pm1004vdcCfgLabelclientTable_Object = MibTable
pm1004vdcCfgLabelclientTable = _Pm1004vdcCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgLabelclientTable.setStatus("current")
_Pm1004vdcCfgLabelclientEntry_Object = MibTableRow
pm1004vdcCfgLabelclientEntry = _Pm1004vdcCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 3, 1, 1)
)
pm1004vdcCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgLabelclientEntry.setStatus("current")


class _Pm1004vdcCfgLabelclientIndex_Type(Integer32):
    """Custom type pm1004vdcCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1004vdcCfgLabelclientIndex_Object = MibTableColumn
pm1004vdcCfgLabelclientIndex = _Pm1004vdcCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 3, 1, 1, 1),
    _Pm1004vdcCfgLabelclientIndex_Type()
)
pm1004vdcCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgLabelclientIndex.setStatus("current")


class _Pm1004vdcCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1004vdcCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004vdcCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1004vdcCfgLabelclientPortn_Object = MibTableColumn
pm1004vdcCfgLabelclientPortn = _Pm1004vdcCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 3, 1, 1, 3),
    _Pm1004vdcCfgLabelclientPortn_Type()
)
pm1004vdcCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLabelclientPortn.setStatus("current")
_Pm1004vdcCfgLabellineTable_Object = MibTable
pm1004vdcCfgLabellineTable = _Pm1004vdcCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgLabellineTable.setStatus("current")
_Pm1004vdcCfgLabellineEntry_Object = MibTableRow
pm1004vdcCfgLabellineEntry = _Pm1004vdcCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 3, 2, 1)
)
pm1004vdcCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgLabellineEntry.setStatus("current")


class _Pm1004vdcCfgLabellineIndex_Type(Integer32):
    """Custom type pm1004vdcCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1004vdcCfgLabellineIndex_Object = MibTableColumn
pm1004vdcCfgLabellineIndex = _Pm1004vdcCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 3, 2, 1, 1),
    _Pm1004vdcCfgLabellineIndex_Type()
)
pm1004vdcCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgLabellineIndex.setStatus("current")


class _Pm1004vdcCfgLabellinePortn_Type(DisplayString):
    """Custom type pm1004vdcCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004vdcCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1004vdcCfgLabellinePortn_Object = MibTableColumn
pm1004vdcCfgLabellinePortn = _Pm1004vdcCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 3, 2, 1, 3),
    _Pm1004vdcCfgLabellinePortn_Type()
)
pm1004vdcCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLabellinePortn.setStatus("current")
_Pm1004vdcCfgStartupthresholds_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartupthresholds = _Pm1004vdcCfgStartupthresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4)
)
_Pm1004vdcCfgClientStartupThreshTable_Object = MibTable
pm1004vdcCfgClientStartupThreshTable = _Pm1004vdcCfgClientStartupThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgClientStartupThreshTable.setStatus("current")
_Pm1004vdcCfgClientStartupThreshEntry_Object = MibTableRow
pm1004vdcCfgClientStartupThreshEntry = _Pm1004vdcCfgClientStartupThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 1, 1)
)
pm1004vdcCfgClientStartupThreshEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgClientStartupThreshIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgClientStartupThreshEntry.setStatus("current")


class _Pm1004vdcCfgClientStartupThreshIndex_Type(Integer32):
    """Custom type pm1004vdcCfgClientStartupThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgClientStartupThreshIndex_Type.__name__ = "Integer32"
_Pm1004vdcCfgClientStartupThreshIndex_Object = MibTableColumn
pm1004vdcCfgClientStartupThreshIndex = _Pm1004vdcCfgClientStartupThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 1, 1, 1),
    _Pm1004vdcCfgClientStartupThreshIndex_Type()
)
pm1004vdcCfgClientStartupThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgClientStartupThreshIndex.setStatus("current")


class _Pm1004vdcCfgClientThreshtxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgClientThreshtxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgClientThreshtxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgClientThreshtxpowhighPortn_Object = MibTableColumn
pm1004vdcCfgClientThreshtxpowhighPortn = _Pm1004vdcCfgClientThreshtxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 1, 1, 15),
    _Pm1004vdcCfgClientThreshtxpowhighPortn_Type()
)
pm1004vdcCfgClientThreshtxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgClientThreshtxpowhighPortn.setStatus("current")


class _Pm1004vdcCfgClientThreshtxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgClientThreshtxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgClientThreshtxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgClientThreshtxpowlowPortn_Object = MibTableColumn
pm1004vdcCfgClientThreshtxpowlowPortn = _Pm1004vdcCfgClientThreshtxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 1, 1, 16),
    _Pm1004vdcCfgClientThreshtxpowlowPortn_Type()
)
pm1004vdcCfgClientThreshtxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgClientThreshtxpowlowPortn.setStatus("current")


class _Pm1004vdcCfgClientThreshrxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgClientThreshrxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgClientThreshrxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgClientThreshrxpowhighPortn_Object = MibTableColumn
pm1004vdcCfgClientThreshrxpowhighPortn = _Pm1004vdcCfgClientThreshrxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 1, 1, 19),
    _Pm1004vdcCfgClientThreshrxpowhighPortn_Type()
)
pm1004vdcCfgClientThreshrxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgClientThreshrxpowhighPortn.setStatus("current")


class _Pm1004vdcCfgClientThreshrxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgClientThreshrxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgClientThreshrxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgClientThreshrxpowlowPortn_Object = MibTableColumn
pm1004vdcCfgClientThreshrxpowlowPortn = _Pm1004vdcCfgClientThreshrxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 1, 1, 20),
    _Pm1004vdcCfgClientThreshrxpowlowPortn_Type()
)
pm1004vdcCfgClientThreshrxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgClientThreshrxpowlowPortn.setStatus("current")
_Pm1004vdcCfgLineStartupThreshTable_Object = MibTable
pm1004vdcCfgLineStartupThreshTable = _Pm1004vdcCfgLineStartupThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgLineStartupThreshTable.setStatus("current")
_Pm1004vdcCfgLineStartupThreshEntry_Object = MibTableRow
pm1004vdcCfgLineStartupThreshEntry = _Pm1004vdcCfgLineStartupThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 2, 1)
)
pm1004vdcCfgLineStartupThreshEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgLineStartupThreshIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgLineStartupThreshEntry.setStatus("current")


class _Pm1004vdcCfgLineStartupThreshIndex_Type(Integer32):
    """Custom type pm1004vdcCfgLineStartupThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgLineStartupThreshIndex_Type.__name__ = "Integer32"
_Pm1004vdcCfgLineStartupThreshIndex_Object = MibTableColumn
pm1004vdcCfgLineStartupThreshIndex = _Pm1004vdcCfgLineStartupThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 2, 1, 1),
    _Pm1004vdcCfgLineStartupThreshIndex_Type()
)
pm1004vdcCfgLineStartupThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgLineStartupThreshIndex.setStatus("current")


class _Pm1004vdcCfgLineThreshtxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLineThreshtxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLineThreshtxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLineThreshtxpowhighPortn_Object = MibTableColumn
pm1004vdcCfgLineThreshtxpowhighPortn = _Pm1004vdcCfgLineThreshtxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 2, 1, 15),
    _Pm1004vdcCfgLineThreshtxpowhighPortn_Type()
)
pm1004vdcCfgLineThreshtxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLineThreshtxpowhighPortn.setStatus("current")


class _Pm1004vdcCfgLineThreshtxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLineThreshtxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLineThreshtxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLineThreshtxpowlowPortn_Object = MibTableColumn
pm1004vdcCfgLineThreshtxpowlowPortn = _Pm1004vdcCfgLineThreshtxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 2, 1, 16),
    _Pm1004vdcCfgLineThreshtxpowlowPortn_Type()
)
pm1004vdcCfgLineThreshtxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLineThreshtxpowlowPortn.setStatus("current")


class _Pm1004vdcCfgLineThreshrxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLineThreshrxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLineThreshrxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLineThreshrxpowhighPortn_Object = MibTableColumn
pm1004vdcCfgLineThreshrxpowhighPortn = _Pm1004vdcCfgLineThreshrxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 2, 1, 19),
    _Pm1004vdcCfgLineThreshrxpowhighPortn_Type()
)
pm1004vdcCfgLineThreshrxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLineThreshrxpowhighPortn.setStatus("current")


class _Pm1004vdcCfgLineThreshrxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLineThreshrxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLineThreshrxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLineThreshrxpowlowPortn_Object = MibTableColumn
pm1004vdcCfgLineThreshrxpowlowPortn = _Pm1004vdcCfgLineThreshrxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 4, 2, 1, 20),
    _Pm1004vdcCfgLineThreshrxpowlowPortn_Type()
)
pm1004vdcCfgLineThreshrxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLineThreshrxpowlowPortn.setStatus("current")
_Pm1004vdcCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartuptlh = _Pm1004vdcCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5)
)
_Pm1004vdcCfgOtxtlhTable_Object = MibTable
pm1004vdcCfgOtxtlhTable = _Pm1004vdcCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgOtxtlhTable.setStatus("current")
_Pm1004vdcCfgOtxtlhEntry_Object = MibTableRow
pm1004vdcCfgOtxtlhEntry = _Pm1004vdcCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1)
)
pm1004vdcCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgOtxtlhEntry.setStatus("current")


class _Pm1004vdcCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm1004vdcCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm1004vdcCfgOtxtlhIndex_Object = MibTableColumn
pm1004vdcCfgOtxtlhIndex = _Pm1004vdcCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 1),
    _Pm1004vdcCfgOtxtlhIndex_Type()
)
pm1004vdcCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgOtxtlhIndex.setStatus("current")


class _Pm1004vdcCfgNuPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgNuPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgNuPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgNuPortn_Object = MibTableColumn
pm1004vdcCfgNuPortn = _Pm1004vdcCfgNuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 3),
    _Pm1004vdcCfgNuPortn_Type()
)
pm1004vdcCfgNuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgNuPortn.setStatus("deprecated")


class _Pm1004vdcCfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLineDitherRatePortn_Object = MibTableColumn
pm1004vdcCfgLineDitherRatePortn = _Pm1004vdcCfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 4),
    _Pm1004vdcCfgLineDitherRatePortn_Type()
)
pm1004vdcCfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLineDitherRatePortn.setStatus("current")


class _Pm1004vdcCfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLineDitherFhzPortn_Object = MibTableColumn
pm1004vdcCfgLineDitherFhzPortn = _Pm1004vdcCfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 5),
    _Pm1004vdcCfgLineDitherFhzPortn_Type()
)
pm1004vdcCfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLineDitherFhzPortn.setStatus("current")


class _Pm1004vdcCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLinePwrLaserPortn_Object = MibTableColumn
pm1004vdcCfgLinePwrLaserPortn = _Pm1004vdcCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 6),
    _Pm1004vdcCfgLinePwrLaserPortn_Type()
)
pm1004vdcCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLinePwrLaserPortn.setStatus("current")


class _Pm1004vdcCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLineFCurrentPortn_Object = MibTableColumn
pm1004vdcCfgLineFCurrentPortn = _Pm1004vdcCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 7),
    _Pm1004vdcCfgLineFCurrentPortn_Type()
)
pm1004vdcCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLineFCurrentPortn.setStatus("current")


class _Pm1004vdcCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLineGridCurrentPortn_Object = MibTableColumn
pm1004vdcCfgLineGridCurrentPortn = _Pm1004vdcCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 8),
    _Pm1004vdcCfgLineGridCurrentPortn_Type()
)
pm1004vdcCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLineGridCurrentPortn.setStatus("current")


class _Pm1004vdcCfgFPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgFPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgFPortn_Object = MibTableColumn
pm1004vdcCfgFPortn = _Pm1004vdcCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 9),
    _Pm1004vdcCfgFPortn_Type()
)
pm1004vdcCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgFPortn.setStatus("current")


class _Pm1004vdcCfgReservedPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgReservedPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgReservedPortn_Object = MibTableColumn
pm1004vdcCfgReservedPortn = _Pm1004vdcCfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 10),
    _Pm1004vdcCfgReservedPortn_Type()
)
pm1004vdcCfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgReservedPortn.setStatus("deprecated")


class _Pm1004vdcCfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLinePhotodiodeModePortn_Object = MibTableColumn
pm1004vdcCfgLinePhotodiodeModePortn = _Pm1004vdcCfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 11),
    _Pm1004vdcCfgLinePhotodiodeModePortn_Type()
)
pm1004vdcCfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLinePhotodiodeModePortn.setStatus("current")


class _Pm1004vdcCfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLinePhotodiodeValuePortn_Object = MibTableColumn
pm1004vdcCfgLinePhotodiodeValuePortn = _Pm1004vdcCfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 5, 1, 1, 12),
    _Pm1004vdcCfgLinePhotodiodeValuePortn_Type()
)
pm1004vdcCfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLinePhotodiodeValuePortn.setStatus("current")
_Pm1004vdcCfgStartupslotslineaddtx1_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartupslotslineaddtx1 = _Pm1004vdcCfgStartupslotslineaddtx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 6)
)
_Pm1004vdcCfgSlotslineaddtx1Table_Object = MibTable
pm1004vdcCfgSlotslineaddtx1Table = _Pm1004vdcCfgSlotslineaddtx1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslineaddtx1Table.setStatus("current")
_Pm1004vdcCfgSlotslineaddtx1Entry_Object = MibTableRow
pm1004vdcCfgSlotslineaddtx1Entry = _Pm1004vdcCfgSlotslineaddtx1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 6, 1, 1)
)
pm1004vdcCfgSlotslineaddtx1Entry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgSlotslineaddtx1Index"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslineaddtx1Entry.setStatus("current")


class _Pm1004vdcCfgSlotslineaddtx1Index_Type(Integer32):
    """Custom type pm1004vdcCfgSlotslineaddtx1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgSlotslineaddtx1Index_Type.__name__ = "Integer32"
_Pm1004vdcCfgSlotslineaddtx1Index_Object = MibTableColumn
pm1004vdcCfgSlotslineaddtx1Index = _Pm1004vdcCfgSlotslineaddtx1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 6, 1, 1, 1),
    _Pm1004vdcCfgSlotslineaddtx1Index_Type()
)
pm1004vdcCfgSlotslineaddtx1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslineaddtx1Index.setStatus("current")


class _Pm1004vdcCfgLine1Addslotb2PortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine1Addslotb2PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine1Addslotb2PortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine1Addslotb2PortPortn_Object = MibTableColumn
pm1004vdcCfgLine1Addslotb2PortPortn = _Pm1004vdcCfgLine1Addslotb2PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 6, 1, 1, 3),
    _Pm1004vdcCfgLine1Addslotb2PortPortn_Type()
)
pm1004vdcCfgLine1Addslotb2PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine1Addslotb2PortPortn.setStatus("current")


class _Pm1004vdcCfgLine1Addslotb1PortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine1Addslotb1PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine1Addslotb1PortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine1Addslotb1PortPortn_Object = MibTableColumn
pm1004vdcCfgLine1Addslotb1PortPortn = _Pm1004vdcCfgLine1Addslotb1PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 6, 1, 1, 4),
    _Pm1004vdcCfgLine1Addslotb1PortPortn_Type()
)
pm1004vdcCfgLine1Addslotb1PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine1Addslotb1PortPortn.setStatus("current")


class _Pm1004vdcCfgLine1AddprotocolPortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine1AddprotocolPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine1AddprotocolPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine1AddprotocolPortPortn_Object = MibTableColumn
pm1004vdcCfgLine1AddprotocolPortPortn = _Pm1004vdcCfgLine1AddprotocolPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 6, 1, 1, 5),
    _Pm1004vdcCfgLine1AddprotocolPortPortn_Type()
)
pm1004vdcCfgLine1AddprotocolPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine1AddprotocolPortPortn.setStatus("current")
_Pm1004vdcCfgStartupslotslineaddtx2_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartupslotslineaddtx2 = _Pm1004vdcCfgStartupslotslineaddtx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 7)
)
_Pm1004vdcCfgSlotslineaddtx2Table_Object = MibTable
pm1004vdcCfgSlotslineaddtx2Table = _Pm1004vdcCfgSlotslineaddtx2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 7, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslineaddtx2Table.setStatus("current")
_Pm1004vdcCfgSlotslineaddtx2Entry_Object = MibTableRow
pm1004vdcCfgSlotslineaddtx2Entry = _Pm1004vdcCfgSlotslineaddtx2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 7, 1, 1)
)
pm1004vdcCfgSlotslineaddtx2Entry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgSlotslineaddtx2Index"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslineaddtx2Entry.setStatus("current")


class _Pm1004vdcCfgSlotslineaddtx2Index_Type(Integer32):
    """Custom type pm1004vdcCfgSlotslineaddtx2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgSlotslineaddtx2Index_Type.__name__ = "Integer32"
_Pm1004vdcCfgSlotslineaddtx2Index_Object = MibTableColumn
pm1004vdcCfgSlotslineaddtx2Index = _Pm1004vdcCfgSlotslineaddtx2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 7, 1, 1, 1),
    _Pm1004vdcCfgSlotslineaddtx2Index_Type()
)
pm1004vdcCfgSlotslineaddtx2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslineaddtx2Index.setStatus("current")


class _Pm1004vdcCfgLine2Addslotb2PortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine2Addslotb2PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine2Addslotb2PortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine2Addslotb2PortPortn_Object = MibTableColumn
pm1004vdcCfgLine2Addslotb2PortPortn = _Pm1004vdcCfgLine2Addslotb2PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 7, 1, 1, 3),
    _Pm1004vdcCfgLine2Addslotb2PortPortn_Type()
)
pm1004vdcCfgLine2Addslotb2PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine2Addslotb2PortPortn.setStatus("current")


class _Pm1004vdcCfgLine2Addslotb1PortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine2Addslotb1PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine2Addslotb1PortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine2Addslotb1PortPortn_Object = MibTableColumn
pm1004vdcCfgLine2Addslotb1PortPortn = _Pm1004vdcCfgLine2Addslotb1PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 7, 1, 1, 4),
    _Pm1004vdcCfgLine2Addslotb1PortPortn_Type()
)
pm1004vdcCfgLine2Addslotb1PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine2Addslotb1PortPortn.setStatus("current")


class _Pm1004vdcCfgLine2AddprotocolPortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine2AddprotocolPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine2AddprotocolPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine2AddprotocolPortPortn_Object = MibTableColumn
pm1004vdcCfgLine2AddprotocolPortPortn = _Pm1004vdcCfgLine2AddprotocolPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 7, 1, 1, 5),
    _Pm1004vdcCfgLine2AddprotocolPortPortn_Type()
)
pm1004vdcCfgLine2AddprotocolPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine2AddprotocolPortPortn.setStatus("current")
_Pm1004vdcCfgStartupslotslinepassthroughtx1_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartupslotslinepassthroughtx1 = _Pm1004vdcCfgStartupslotslinepassthroughtx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 8)
)
_Pm1004vdcCfgSlotslinepassthroughtx1Table_Object = MibTable
pm1004vdcCfgSlotslinepassthroughtx1Table = _Pm1004vdcCfgSlotslinepassthroughtx1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 8, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinepassthroughtx1Table.setStatus("current")
_Pm1004vdcCfgSlotslinepassthroughtx1Entry_Object = MibTableRow
pm1004vdcCfgSlotslinepassthroughtx1Entry = _Pm1004vdcCfgSlotslinepassthroughtx1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 8, 1, 1)
)
pm1004vdcCfgSlotslinepassthroughtx1Entry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgSlotslinepassthroughtx1Index"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinepassthroughtx1Entry.setStatus("current")


class _Pm1004vdcCfgSlotslinepassthroughtx1Index_Type(Integer32):
    """Custom type pm1004vdcCfgSlotslinepassthroughtx1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgSlotslinepassthroughtx1Index_Type.__name__ = "Integer32"
_Pm1004vdcCfgSlotslinepassthroughtx1Index_Object = MibTableColumn
pm1004vdcCfgSlotslinepassthroughtx1Index = _Pm1004vdcCfgSlotslinepassthroughtx1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 8, 1, 1, 1),
    _Pm1004vdcCfgSlotslinepassthroughtx1Index_Type()
)
pm1004vdcCfgSlotslinepassthroughtx1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinepassthroughtx1Index.setStatus("current")


class _Pm1004vdcCfgLine1Slotb2PassthroughPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine1Slotb2PassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine1Slotb2PassthroughPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine1Slotb2PassthroughPortn_Object = MibTableColumn
pm1004vdcCfgLine1Slotb2PassthroughPortn = _Pm1004vdcCfgLine1Slotb2PassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 8, 1, 1, 3),
    _Pm1004vdcCfgLine1Slotb2PassthroughPortn_Type()
)
pm1004vdcCfgLine1Slotb2PassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine1Slotb2PassthroughPortn.setStatus("current")


class _Pm1004vdcCfgLine1Slotb1PassthroughPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine1Slotb1PassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine1Slotb1PassthroughPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine1Slotb1PassthroughPortn_Object = MibTableColumn
pm1004vdcCfgLine1Slotb1PassthroughPortn = _Pm1004vdcCfgLine1Slotb1PassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 8, 1, 1, 4),
    _Pm1004vdcCfgLine1Slotb1PassthroughPortn_Type()
)
pm1004vdcCfgLine1Slotb1PassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine1Slotb1PassthroughPortn.setStatus("current")


class _Pm1004vdcCfgLine1ProtocolPassthroughPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine1ProtocolPassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine1ProtocolPassthroughPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine1ProtocolPassthroughPortn_Object = MibTableColumn
pm1004vdcCfgLine1ProtocolPassthroughPortn = _Pm1004vdcCfgLine1ProtocolPassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 8, 1, 1, 5),
    _Pm1004vdcCfgLine1ProtocolPassthroughPortn_Type()
)
pm1004vdcCfgLine1ProtocolPassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine1ProtocolPassthroughPortn.setStatus("current")
_Pm1004vdcCfgStartupslotslinepassthroughtx2_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartupslotslinepassthroughtx2 = _Pm1004vdcCfgStartupslotslinepassthroughtx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 9)
)
_Pm1004vdcCfgSlotslinepassthroughtx2Table_Object = MibTable
pm1004vdcCfgSlotslinepassthroughtx2Table = _Pm1004vdcCfgSlotslinepassthroughtx2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 9, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinepassthroughtx2Table.setStatus("current")
_Pm1004vdcCfgSlotslinepassthroughtx2Entry_Object = MibTableRow
pm1004vdcCfgSlotslinepassthroughtx2Entry = _Pm1004vdcCfgSlotslinepassthroughtx2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 9, 1, 1)
)
pm1004vdcCfgSlotslinepassthroughtx2Entry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgSlotslinepassthroughtx2Index"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinepassthroughtx2Entry.setStatus("current")


class _Pm1004vdcCfgSlotslinepassthroughtx2Index_Type(Integer32):
    """Custom type pm1004vdcCfgSlotslinepassthroughtx2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgSlotslinepassthroughtx2Index_Type.__name__ = "Integer32"
_Pm1004vdcCfgSlotslinepassthroughtx2Index_Object = MibTableColumn
pm1004vdcCfgSlotslinepassthroughtx2Index = _Pm1004vdcCfgSlotslinepassthroughtx2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 9, 1, 1, 1),
    _Pm1004vdcCfgSlotslinepassthroughtx2Index_Type()
)
pm1004vdcCfgSlotslinepassthroughtx2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinepassthroughtx2Index.setStatus("current")


class _Pm1004vdcCfgLine2Slotb2PassthroughPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine2Slotb2PassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine2Slotb2PassthroughPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine2Slotb2PassthroughPortn_Object = MibTableColumn
pm1004vdcCfgLine2Slotb2PassthroughPortn = _Pm1004vdcCfgLine2Slotb2PassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 9, 1, 1, 3),
    _Pm1004vdcCfgLine2Slotb2PassthroughPortn_Type()
)
pm1004vdcCfgLine2Slotb2PassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine2Slotb2PassthroughPortn.setStatus("current")


class _Pm1004vdcCfgLine2Slotb1PassthroughPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine2Slotb1PassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine2Slotb1PassthroughPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine2Slotb1PassthroughPortn_Object = MibTableColumn
pm1004vdcCfgLine2Slotb1PassthroughPortn = _Pm1004vdcCfgLine2Slotb1PassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 9, 1, 1, 4),
    _Pm1004vdcCfgLine2Slotb1PassthroughPortn_Type()
)
pm1004vdcCfgLine2Slotb1PassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine2Slotb1PassthroughPortn.setStatus("current")


class _Pm1004vdcCfgLine2ProtocolPassthroughPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine2ProtocolPassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine2ProtocolPassthroughPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine2ProtocolPassthroughPortn_Object = MibTableColumn
pm1004vdcCfgLine2ProtocolPassthroughPortn = _Pm1004vdcCfgLine2ProtocolPassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 9, 1, 1, 5),
    _Pm1004vdcCfgLine2ProtocolPassthroughPortn_Type()
)
pm1004vdcCfgLine2ProtocolPassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine2ProtocolPassthroughPortn.setStatus("current")
_Pm1004vdcCfgStartupslotslinedroprx1_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartupslotslinedroprx1 = _Pm1004vdcCfgStartupslotslinedroprx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 10)
)
_Pm1004vdcCfgSlotslinedroprx1Table_Object = MibTable
pm1004vdcCfgSlotslinedroprx1Table = _Pm1004vdcCfgSlotslinedroprx1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 10, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinedroprx1Table.setStatus("current")
_Pm1004vdcCfgSlotslinedroprx1Entry_Object = MibTableRow
pm1004vdcCfgSlotslinedroprx1Entry = _Pm1004vdcCfgSlotslinedroprx1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 10, 1, 1)
)
pm1004vdcCfgSlotslinedroprx1Entry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgSlotslinedroprx1Index"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinedroprx1Entry.setStatus("current")


class _Pm1004vdcCfgSlotslinedroprx1Index_Type(Integer32):
    """Custom type pm1004vdcCfgSlotslinedroprx1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgSlotslinedroprx1Index_Type.__name__ = "Integer32"
_Pm1004vdcCfgSlotslinedroprx1Index_Object = MibTableColumn
pm1004vdcCfgSlotslinedroprx1Index = _Pm1004vdcCfgSlotslinedroprx1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 10, 1, 1, 1),
    _Pm1004vdcCfgSlotslinedroprx1Index_Type()
)
pm1004vdcCfgSlotslinedroprx1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinedroprx1Index.setStatus("current")


class _Pm1004vdcCfgLine1Dropslotb2PortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine1Dropslotb2PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine1Dropslotb2PortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine1Dropslotb2PortPortn_Object = MibTableColumn
pm1004vdcCfgLine1Dropslotb2PortPortn = _Pm1004vdcCfgLine1Dropslotb2PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 10, 1, 1, 3),
    _Pm1004vdcCfgLine1Dropslotb2PortPortn_Type()
)
pm1004vdcCfgLine1Dropslotb2PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine1Dropslotb2PortPortn.setStatus("current")


class _Pm1004vdcCfgLine1Dropslotb1PortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine1Dropslotb1PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine1Dropslotb1PortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine1Dropslotb1PortPortn_Object = MibTableColumn
pm1004vdcCfgLine1Dropslotb1PortPortn = _Pm1004vdcCfgLine1Dropslotb1PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 10, 1, 1, 4),
    _Pm1004vdcCfgLine1Dropslotb1PortPortn_Type()
)
pm1004vdcCfgLine1Dropslotb1PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine1Dropslotb1PortPortn.setStatus("current")


class _Pm1004vdcCfgLine1DropprotocolPortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine1DropprotocolPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine1DropprotocolPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine1DropprotocolPortPortn_Object = MibTableColumn
pm1004vdcCfgLine1DropprotocolPortPortn = _Pm1004vdcCfgLine1DropprotocolPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 10, 1, 1, 5),
    _Pm1004vdcCfgLine1DropprotocolPortPortn_Type()
)
pm1004vdcCfgLine1DropprotocolPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine1DropprotocolPortPortn.setStatus("current")
_Pm1004vdcCfgStartupslotslineaddrx2_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartupslotslineaddrx2 = _Pm1004vdcCfgStartupslotslineaddrx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 11)
)
_Pm1004vdcCfgSlotslinedroprx2Table_Object = MibTable
pm1004vdcCfgSlotslinedroprx2Table = _Pm1004vdcCfgSlotslinedroprx2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 11, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinedroprx2Table.setStatus("current")
_Pm1004vdcCfgSlotslinedroprx2Entry_Object = MibTableRow
pm1004vdcCfgSlotslinedroprx2Entry = _Pm1004vdcCfgSlotslinedroprx2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 11, 1, 1)
)
pm1004vdcCfgSlotslinedroprx2Entry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgSlotslinedroprx2Index"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinedroprx2Entry.setStatus("current")


class _Pm1004vdcCfgSlotslinedroprx2Index_Type(Integer32):
    """Custom type pm1004vdcCfgSlotslinedroprx2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgSlotslinedroprx2Index_Type.__name__ = "Integer32"
_Pm1004vdcCfgSlotslinedroprx2Index_Object = MibTableColumn
pm1004vdcCfgSlotslinedroprx2Index = _Pm1004vdcCfgSlotslinedroprx2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 11, 1, 1, 1),
    _Pm1004vdcCfgSlotslinedroprx2Index_Type()
)
pm1004vdcCfgSlotslinedroprx2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgSlotslinedroprx2Index.setStatus("current")


class _Pm1004vdcCfgLine2Dropslotb2PortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine2Dropslotb2PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine2Dropslotb2PortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine2Dropslotb2PortPortn_Object = MibTableColumn
pm1004vdcCfgLine2Dropslotb2PortPortn = _Pm1004vdcCfgLine2Dropslotb2PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 11, 1, 1, 3),
    _Pm1004vdcCfgLine2Dropslotb2PortPortn_Type()
)
pm1004vdcCfgLine2Dropslotb2PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine2Dropslotb2PortPortn.setStatus("current")


class _Pm1004vdcCfgLine2Dropslotb1PortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine2Dropslotb1PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine2Dropslotb1PortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine2Dropslotb1PortPortn_Object = MibTableColumn
pm1004vdcCfgLine2Dropslotb1PortPortn = _Pm1004vdcCfgLine2Dropslotb1PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 11, 1, 1, 4),
    _Pm1004vdcCfgLine2Dropslotb1PortPortn_Type()
)
pm1004vdcCfgLine2Dropslotb1PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine2Dropslotb1PortPortn.setStatus("current")


class _Pm1004vdcCfgLine2DropprotocolPortPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLine2DropprotocolPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLine2DropprotocolPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLine2DropprotocolPortPortn_Object = MibTableColumn
pm1004vdcCfgLine2DropprotocolPortPortn = _Pm1004vdcCfgLine2DropprotocolPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 11, 1, 1, 5),
    _Pm1004vdcCfgLine2DropprotocolPortPortn_Type()
)
pm1004vdcCfgLine2DropprotocolPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgLine2DropprotocolPortPortn.setStatus("current")
_Pm1004vdcCfgOther_ObjectIdentity = ObjectIdentity
pm1004vdcCfgOther = _Pm1004vdcCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 12)
)
_Pm1004vdctablemoduleOther_ObjectIdentity = ObjectIdentity
pm1004vdctablemoduleOther = _Pm1004vdctablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 12, 1)
)


class _Pm1004vdcCfgmode_Type(Unsigned32):
    """Custom type pm1004vdcCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgmode_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgmode_Object = MibScalar
pm1004vdcCfgmode = _Pm1004vdcCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 12, 1, 2),
    _Pm1004vdcCfgmode_Type()
)
pm1004vdcCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgmode.setStatus("current")
_Pm1004vdcCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm1004vdcCfgStartuptablefive = _Pm1004vdcCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 13)
)
_Pm1004vdcCfgOtxtlhcapabilitiesTable_Object = MibTable
pm1004vdcCfgOtxtlhcapabilitiesTable = _Pm1004vdcCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 13, 1)
)
if mibBuilder.loadTexts:
    pm1004vdcCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm1004vdcCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm1004vdcCfgOtxtlhcapabilitiesEntry = _Pm1004vdcCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 13, 1, 1)
)
pm1004vdcCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm1004vdcCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm1004vdcCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm1004vdcCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm1004vdcCfgOtxtlhcapabilitiesIndex = _Pm1004vdcCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 13, 1, 1, 1),
    _Pm1004vdcCfgOtxtlhcapabilitiesIndex_Type()
)
pm1004vdcCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm1004vdcCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgComponentTypePortn_Object = MibTableColumn
pm1004vdcCfgComponentTypePortn = _Pm1004vdcCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 13, 1, 1, 3),
    _Pm1004vdcCfgComponentTypePortn_Type()
)
pm1004vdcCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgComponentTypePortn.setStatus("current")


class _Pm1004vdcCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgMiscellaneousPortn_Object = MibTableColumn
pm1004vdcCfgMiscellaneousPortn = _Pm1004vdcCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 13, 1, 1, 4),
    _Pm1004vdcCfgMiscellaneousPortn_Type()
)
pm1004vdcCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgMiscellaneousPortn.setStatus("current")


class _Pm1004vdcCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgFirstChannelPortn_Object = MibTableColumn
pm1004vdcCfgFirstChannelPortn = _Pm1004vdcCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 13, 1, 1, 5),
    _Pm1004vdcCfgFirstChannelPortn_Type()
)
pm1004vdcCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgFirstChannelPortn.setStatus("current")


class _Pm1004vdcCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgLastChannelPortn_Object = MibTableColumn
pm1004vdcCfgLastChannelPortn = _Pm1004vdcCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 13, 1, 1, 6),
    _Pm1004vdcCfgLastChannelPortn_Type()
)
pm1004vdcCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgLastChannelPortn.setStatus("current")


class _Pm1004vdcCfgGridPortn_Type(Unsigned32):
    """Custom type pm1004vdcCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vdcCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm1004vdcCfgGridPortn_Object = MibTableColumn
pm1004vdcCfgGridPortn = _Pm1004vdcCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 13, 1, 1, 7),
    _Pm1004vdcCfgGridPortn_Type()
)
pm1004vdcCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcCfgGridPortn.setStatus("current")
_Pm1004vdcCfgWriteConfiguration_Type = EkiOnOff
_Pm1004vdcCfgWriteConfiguration_Object = MibScalar
pm1004vdcCfgWriteConfiguration = _Pm1004vdcCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 9, 257),
    _Pm1004vdcCfgWriteConfiguration_Type()
)
pm1004vdcCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcCfgWriteConfiguration.setStatus("current")
_Pm1004vdctraps_ObjectIdentity = ObjectIdentity
pm1004vdctraps = _Pm1004vdctraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10)
)


class _Pm1004vdctrapPortNumber_Type(Integer32):
    """Custom type pm1004vdctrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004vdctrapPortNumber_Type.__name__ = "Integer32"
_Pm1004vdctrapPortNumber_Object = MibScalar
pm1004vdctrapPortNumber = _Pm1004vdctrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 2),
    _Pm1004vdctrapPortNumber_Type()
)
pm1004vdctrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdctrapPortNumber.setStatus("current")


class _Pm1004vdctrapLineNumber_Type(Integer32):
    """Custom type pm1004vdctrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004vdctrapLineNumber_Type.__name__ = "Integer32"
_Pm1004vdctrapLineNumber_Object = MibScalar
pm1004vdctrapLineNumber = _Pm1004vdctrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 3),
    _Pm1004vdctrapLineNumber_Type()
)
pm1004vdctrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdctrapLineNumber.setStatus("current")


class _Pm1004vdctrapBoardNumber_Type(Integer32):
    """Custom type pm1004vdctrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004vdctrapBoardNumber_Type.__name__ = "Integer32"
_Pm1004vdctrapBoardNumber_Object = MibScalar
pm1004vdctrapBoardNumber = _Pm1004vdctrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 4),
    _Pm1004vdctrapBoardNumber_Type()
)
pm1004vdctrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdctrapBoardNumber.setStatus("current")
_Pm1004vdcMonitoring_ObjectIdentity = ObjectIdentity
pm1004vdcMonitoring = _Pm1004vdcMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11)
)
_Pm1004vdcMonOther_ObjectIdentity = ObjectIdentity
pm1004vdcMonOther = _Pm1004vdcMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 1)
)
_Pm1004vdcMonRmon_ObjectIdentity = ObjectIdentity
pm1004vdcMonRmon = _Pm1004vdcMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 1, 3)
)
_Pm1004vdcMonCountersReset_Type = EkiOnOff
_Pm1004vdcMonCountersReset_Object = MibScalar
pm1004vdcMonCountersReset = _Pm1004vdcMonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 1, 3, 359),
    _Pm1004vdcMonCountersReset_Type()
)
pm1004vdcMonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcMonCountersReset.setStatus("current")
_Pm1004vdcMonCountersStop_Type = EkiOnOff
_Pm1004vdcMonCountersStop_Object = MibScalar
pm1004vdcMonCountersStop = _Pm1004vdcMonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 1, 3, 360),
    _Pm1004vdcMonCountersStop_Type()
)
pm1004vdcMonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vdcMonCountersStop.setStatus("current")
_Pm1004vdcMonClient_ObjectIdentity = ObjectIdentity
pm1004vdcMonClient = _Pm1004vdcMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2)
)
_Pm1004vdcMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm1004vdcMonClientRmonCounter = _Pm1004vdcMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4)
)
_Pm1004vdcMonupRmonByteCntTable_Object = MibTable
pm1004vdcMonupRmonByteCntTable = _Pm1004vdcMonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonByteCntTable.setStatus("current")
_Pm1004vdcMonupRmonByteCntEntry_Object = MibTableRow
pm1004vdcMonupRmonByteCntEntry = _Pm1004vdcMonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 16, 1)
)
pm1004vdcMonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonByteCntEntry.setStatus("current")


class _Pm1004vdcMonupRmonByteCntIndex_Type(Integer32):
    """Custom type pm1004vdcMonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcMonupRmonByteCntIndex_Object = MibTableColumn
pm1004vdcMonupRmonByteCntIndex = _Pm1004vdcMonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 16, 1, 1),
    _Pm1004vdcMonupRmonByteCntIndex_Type()
)
pm1004vdcMonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonByteCntIndex.setStatus("current")
_Pm1004vdcMonupRmonByteCntValuePortn_Type = Counter64
_Pm1004vdcMonupRmonByteCntValuePortn_Object = MibTableColumn
pm1004vdcMonupRmonByteCntValuePortn = _Pm1004vdcMonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 16, 1, 2),
    _Pm1004vdcMonupRmonByteCntValuePortn_Type()
)
pm1004vdcMonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonByteCntValuePortn.setStatus("current")
_Pm1004vdcMonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonByteCntErrorPortn_Object = MibTableColumn
pm1004vdcMonupRmonByteCntErrorPortn = _Pm1004vdcMonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 16, 1, 3),
    _Pm1004vdcMonupRmonByteCntErrorPortn_Type()
)
pm1004vdcMonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonByteCntErrorPortn.setStatus("current")
_Pm1004vdcMonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonByteCntOverloadPortn_Object = MibTableColumn
pm1004vdcMonupRmonByteCntOverloadPortn = _Pm1004vdcMonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 16, 1, 4),
    _Pm1004vdcMonupRmonByteCntOverloadPortn_Type()
)
pm1004vdcMonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonByteCntOverloadPortn.setStatus("current")
_Pm1004vdcMonupRmonCrcErrorCntTable_Object = MibTable
pm1004vdcMonupRmonCrcErrorCntTable = _Pm1004vdcMonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 24)
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonCrcErrorCntTable.setStatus("current")
_Pm1004vdcMonupRmonCrcErrorCntEntry_Object = MibTableRow
pm1004vdcMonupRmonCrcErrorCntEntry = _Pm1004vdcMonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 24, 1)
)
pm1004vdcMonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonCrcErrorCntEntry.setStatus("current")


class _Pm1004vdcMonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1004vdcMonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcMonupRmonCrcErrorCntIndex_Object = MibTableColumn
pm1004vdcMonupRmonCrcErrorCntIndex = _Pm1004vdcMonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 24, 1, 1),
    _Pm1004vdcMonupRmonCrcErrorCntIndex_Type()
)
pm1004vdcMonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonCrcErrorCntIndex.setStatus("current")
_Pm1004vdcMonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1004vdcMonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1004vdcMonupRmonCrcErrorCntValuePortn = _Pm1004vdcMonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 24, 1, 2),
    _Pm1004vdcMonupRmonCrcErrorCntValuePortn_Type()
)
pm1004vdcMonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1004vdcMonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1004vdcMonupRmonCrcErrorCntErrorPortn = _Pm1004vdcMonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 24, 1, 3),
    _Pm1004vdcMonupRmonCrcErrorCntErrorPortn_Type()
)
pm1004vdcMonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1004vdcMonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1004vdcMonupRmonCrcErrorCntOverloadPortn = _Pm1004vdcMonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 24, 1, 4),
    _Pm1004vdcMonupRmonCrcErrorCntOverloadPortn_Type()
)
pm1004vdcMonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1004vdcMonupRmonPacketsCntTable_Object = MibTable
pm1004vdcMonupRmonPacketsCntTable = _Pm1004vdcMonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonPacketsCntTable.setStatus("current")
_Pm1004vdcMonupRmonPacketsCntEntry_Object = MibTableRow
pm1004vdcMonupRmonPacketsCntEntry = _Pm1004vdcMonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 32, 1)
)
pm1004vdcMonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonPacketsCntEntry.setStatus("current")


class _Pm1004vdcMonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1004vdcMonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcMonupRmonPacketsCntIndex_Object = MibTableColumn
pm1004vdcMonupRmonPacketsCntIndex = _Pm1004vdcMonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 32, 1, 1),
    _Pm1004vdcMonupRmonPacketsCntIndex_Type()
)
pm1004vdcMonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonPacketsCntIndex.setStatus("current")
_Pm1004vdcMonupRmonPacketsCntValuePortn_Type = Counter64
_Pm1004vdcMonupRmonPacketsCntValuePortn_Object = MibTableColumn
pm1004vdcMonupRmonPacketsCntValuePortn = _Pm1004vdcMonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 32, 1, 2),
    _Pm1004vdcMonupRmonPacketsCntValuePortn_Type()
)
pm1004vdcMonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonPacketsCntValuePortn.setStatus("current")
_Pm1004vdcMonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1004vdcMonupRmonPacketsCntErrorPortn = _Pm1004vdcMonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 32, 1, 3),
    _Pm1004vdcMonupRmonPacketsCntErrorPortn_Type()
)
pm1004vdcMonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonPacketsCntErrorPortn.setStatus("current")
_Pm1004vdcMonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1004vdcMonupRmonPacketsCntOverloadPortn = _Pm1004vdcMonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 32, 1, 4),
    _Pm1004vdcMonupRmonPacketsCntOverloadPortn_Type()
)
pm1004vdcMonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1004vdcMonupRmonBroadcastCntTable_Object = MibTable
pm1004vdcMonupRmonBroadcastCntTable = _Pm1004vdcMonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 40)
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonBroadcastCntTable.setStatus("current")
_Pm1004vdcMonupRmonBroadcastCntEntry_Object = MibTableRow
pm1004vdcMonupRmonBroadcastCntEntry = _Pm1004vdcMonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 40, 1)
)
pm1004vdcMonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonBroadcastCntEntry.setStatus("current")


class _Pm1004vdcMonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pm1004vdcMonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcMonupRmonBroadcastCntIndex_Object = MibTableColumn
pm1004vdcMonupRmonBroadcastCntIndex = _Pm1004vdcMonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 40, 1, 1),
    _Pm1004vdcMonupRmonBroadcastCntIndex_Type()
)
pm1004vdcMonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonBroadcastCntIndex.setStatus("current")
_Pm1004vdcMonupRmonBroadcastCntValuePortn_Type = Counter64
_Pm1004vdcMonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pm1004vdcMonupRmonBroadcastCntValuePortn = _Pm1004vdcMonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 40, 1, 2),
    _Pm1004vdcMonupRmonBroadcastCntValuePortn_Type()
)
pm1004vdcMonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonBroadcastCntValuePortn.setStatus("current")
_Pm1004vdcMonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pm1004vdcMonupRmonBroadcastCntErrorPortn = _Pm1004vdcMonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 40, 1, 3),
    _Pm1004vdcMonupRmonBroadcastCntErrorPortn_Type()
)
pm1004vdcMonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pm1004vdcMonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pm1004vdcMonupRmonBroadcastCntOverloadPortn = _Pm1004vdcMonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 40, 1, 4),
    _Pm1004vdcMonupRmonBroadcastCntOverloadPortn_Type()
)
pm1004vdcMonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pm1004vdcMonupRmonMulticastCntTable_Object = MibTable
pm1004vdcMonupRmonMulticastCntTable = _Pm1004vdcMonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonMulticastCntTable.setStatus("current")
_Pm1004vdcMonupRmonMulticastCntEntry_Object = MibTableRow
pm1004vdcMonupRmonMulticastCntEntry = _Pm1004vdcMonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 48, 1)
)
pm1004vdcMonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonMulticastCntEntry.setStatus("current")


class _Pm1004vdcMonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pm1004vdcMonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcMonupRmonMulticastCntIndex_Object = MibTableColumn
pm1004vdcMonupRmonMulticastCntIndex = _Pm1004vdcMonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 48, 1, 1),
    _Pm1004vdcMonupRmonMulticastCntIndex_Type()
)
pm1004vdcMonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonMulticastCntIndex.setStatus("current")
_Pm1004vdcMonupRmonMulticastCntValuePortn_Type = Counter64
_Pm1004vdcMonupRmonMulticastCntValuePortn_Object = MibTableColumn
pm1004vdcMonupRmonMulticastCntValuePortn = _Pm1004vdcMonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 48, 1, 2),
    _Pm1004vdcMonupRmonMulticastCntValuePortn_Type()
)
pm1004vdcMonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonMulticastCntValuePortn.setStatus("current")
_Pm1004vdcMonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pm1004vdcMonupRmonMulticastCntErrorPortn = _Pm1004vdcMonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 48, 1, 3),
    _Pm1004vdcMonupRmonMulticastCntErrorPortn_Type()
)
pm1004vdcMonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonMulticastCntErrorPortn.setStatus("current")
_Pm1004vdcMonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcMonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pm1004vdcMonupRmonMulticastCntOverloadPortn = _Pm1004vdcMonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 48, 1, 4),
    _Pm1004vdcMonupRmonMulticastCntOverloadPortn_Type()
)
pm1004vdcMonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupRmonMulticastCntOverloadPortn.setStatus("current")
_Pm1004vdcMonupLineRmonByteCntTable_Object = MibTable
pm1004vdcMonupLineRmonByteCntTable = _Pm1004vdcMonupLineRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 208)
)
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonByteCntTable.setStatus("current")
_Pm1004vdcMonupLineRmonByteCntEntry_Object = MibTableRow
pm1004vdcMonupLineRmonByteCntEntry = _Pm1004vdcMonupLineRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 208, 1)
)
pm1004vdcMonupLineRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMonupLineRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonByteCntEntry.setStatus("current")


class _Pm1004vdcMonupLineRmonByteCntIndex_Type(Integer32):
    """Custom type pm1004vdcMonupLineRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMonupLineRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcMonupLineRmonByteCntIndex_Object = MibTableColumn
pm1004vdcMonupLineRmonByteCntIndex = _Pm1004vdcMonupLineRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 208, 1, 1),
    _Pm1004vdcMonupLineRmonByteCntIndex_Type()
)
pm1004vdcMonupLineRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonByteCntIndex.setStatus("current")
_Pm1004vdcMonupLineRmonByteCntValuePortn_Type = Counter64
_Pm1004vdcMonupLineRmonByteCntValuePortn_Object = MibTableColumn
pm1004vdcMonupLineRmonByteCntValuePortn = _Pm1004vdcMonupLineRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 208, 1, 2),
    _Pm1004vdcMonupLineRmonByteCntValuePortn_Type()
)
pm1004vdcMonupLineRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonByteCntValuePortn.setStatus("current")
_Pm1004vdcMonupLineRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1004vdcMonupLineRmonByteCntErrorPortn_Object = MibTableColumn
pm1004vdcMonupLineRmonByteCntErrorPortn = _Pm1004vdcMonupLineRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 208, 1, 3),
    _Pm1004vdcMonupLineRmonByteCntErrorPortn_Type()
)
pm1004vdcMonupLineRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonByteCntErrorPortn.setStatus("current")
_Pm1004vdcMonupLineRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcMonupLineRmonByteCntOverloadPortn_Object = MibTableColumn
pm1004vdcMonupLineRmonByteCntOverloadPortn = _Pm1004vdcMonupLineRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 208, 1, 4),
    _Pm1004vdcMonupLineRmonByteCntOverloadPortn_Type()
)
pm1004vdcMonupLineRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonByteCntOverloadPortn.setStatus("current")
_Pm1004vdcMonupLineRmonCrcErrorCntTable_Object = MibTable
pm1004vdcMonupLineRmonCrcErrorCntTable = _Pm1004vdcMonupLineRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 209)
)
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonCrcErrorCntTable.setStatus("current")
_Pm1004vdcMonupLineRmonCrcErrorCntEntry_Object = MibTableRow
pm1004vdcMonupLineRmonCrcErrorCntEntry = _Pm1004vdcMonupLineRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 209, 1)
)
pm1004vdcMonupLineRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMonupLineRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonCrcErrorCntEntry.setStatus("current")


class _Pm1004vdcMonupLineRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1004vdcMonupLineRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMonupLineRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcMonupLineRmonCrcErrorCntIndex_Object = MibTableColumn
pm1004vdcMonupLineRmonCrcErrorCntIndex = _Pm1004vdcMonupLineRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 209, 1, 1),
    _Pm1004vdcMonupLineRmonCrcErrorCntIndex_Type()
)
pm1004vdcMonupLineRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonCrcErrorCntIndex.setStatus("current")
_Pm1004vdcMonupLineRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1004vdcMonupLineRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1004vdcMonupLineRmonCrcErrorCntValuePortn = _Pm1004vdcMonupLineRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 209, 1, 2),
    _Pm1004vdcMonupLineRmonCrcErrorCntValuePortn_Type()
)
pm1004vdcMonupLineRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1004vdcMonupLineRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1004vdcMonupLineRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1004vdcMonupLineRmonCrcErrorCntErrorPortn = _Pm1004vdcMonupLineRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 209, 1, 3),
    _Pm1004vdcMonupLineRmonCrcErrorCntErrorPortn_Type()
)
pm1004vdcMonupLineRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1004vdcMonupLineRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcMonupLineRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1004vdcMonupLineRmonCrcErrorCntOverloadPortn = _Pm1004vdcMonupLineRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 209, 1, 4),
    _Pm1004vdcMonupLineRmonCrcErrorCntOverloadPortn_Type()
)
pm1004vdcMonupLineRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1004vdcMonupLineRmonPacketsCntTable_Object = MibTable
pm1004vdcMonupLineRmonPacketsCntTable = _Pm1004vdcMonupLineRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 210)
)
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonPacketsCntTable.setStatus("current")
_Pm1004vdcMonupLineRmonPacketsCntEntry_Object = MibTableRow
pm1004vdcMonupLineRmonPacketsCntEntry = _Pm1004vdcMonupLineRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 210, 1)
)
pm1004vdcMonupLineRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004VDC-MIB", "pm1004vdcMonupLineRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonPacketsCntEntry.setStatus("current")


class _Pm1004vdcMonupLineRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1004vdcMonupLineRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vdcMonupLineRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1004vdcMonupLineRmonPacketsCntIndex_Object = MibTableColumn
pm1004vdcMonupLineRmonPacketsCntIndex = _Pm1004vdcMonupLineRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 210, 1, 1),
    _Pm1004vdcMonupLineRmonPacketsCntIndex_Type()
)
pm1004vdcMonupLineRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonPacketsCntIndex.setStatus("current")
_Pm1004vdcMonupLineRmonPacketsCntValuePortn_Type = Counter64
_Pm1004vdcMonupLineRmonPacketsCntValuePortn_Object = MibTableColumn
pm1004vdcMonupLineRmonPacketsCntValuePortn = _Pm1004vdcMonupLineRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 210, 1, 2),
    _Pm1004vdcMonupLineRmonPacketsCntValuePortn_Type()
)
pm1004vdcMonupLineRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonPacketsCntValuePortn.setStatus("current")
_Pm1004vdcMonupLineRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1004vdcMonupLineRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1004vdcMonupLineRmonPacketsCntErrorPortn = _Pm1004vdcMonupLineRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 210, 1, 3),
    _Pm1004vdcMonupLineRmonPacketsCntErrorPortn_Type()
)
pm1004vdcMonupLineRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonPacketsCntErrorPortn.setStatus("current")
_Pm1004vdcMonupLineRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1004vdcMonupLineRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1004vdcMonupLineRmonPacketsCntOverloadPortn = _Pm1004vdcMonupLineRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 2, 4, 210, 1, 4),
    _Pm1004vdcMonupLineRmonPacketsCntOverloadPortn_Type()
)
pm1004vdcMonupLineRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vdcMonupLineRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1004vdcMonLine_ObjectIdentity = ObjectIdentity
pm1004vdcMonLine = _Pm1004vdcMonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 3)
)
_Pm1004vdcMonLineRmonCounter_ObjectIdentity = ObjectIdentity
pm1004vdcMonLineRmonCounter = _Pm1004vdcMonLineRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 38, 11, 3, 4)
)

# Managed Objects groups


# Notification objects

pm1004vdcLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 30)
)
pm1004vdcLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapLineNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1004vdcLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 31)
)
pm1004vdcLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapLineNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1004vdcLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 32)
)
pm1004vdcLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapLineNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004vdcLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 33)
)
pm1004vdcLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapLineNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1004vdcLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 34)
)
pm1004vdcLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmLineFailPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapLineNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcLineTrapCritGoesOn.setStatus(
        "current"
    )

pm1004vdcLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 35)
)
pm1004vdcLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmLineFailPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapLineNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcLineTrapCritGoesOff.setStatus(
        "current"
    )

pm1004vdcClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 40)
)
pm1004vdcClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapPortNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1004vdcClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 41)
)
pm1004vdcClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapPortNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1004vdcClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 42)
)
pm1004vdcClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapPortNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004vdcClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 43)
)
pm1004vdcClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapPortNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1004vdcClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 44)
)
pm1004vdcClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmFailAccPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapPortNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcClientTrapCritGoesOn.setStatus(
        "current"
    )

pm1004vdcClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 45)
)
pm1004vdcClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmFailAccPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapPortNumber"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcClientTrapCritGoesOff.setStatus(
        "current"
    )

pm1004vdcPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 50)
)
pm1004vdcPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmDefFuseB"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmDefFuseA"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004vdcPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 38, 10, 51)
)
pm1004vdcPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmDefFuseB"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdcAlmDefFuseA"),
        ("EKINOPS-Pm1004VDC-MIB", "pm1004vdctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vdcPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1004VDC-MIB",
    **{"Pm1004vdcModeTimeSlot": Pm1004vdcModeTimeSlot,
       "Pm1004vdcModeAddDrop": Pm1004vdcModeAddDrop,
       "Pm1004vdcProtectionTimeSlot": Pm1004vdcProtectionTimeSlot,
       "Pm1004vdcProtectionStartUp": Pm1004vdcProtectionStartUp,
       "Pm1004vdcDccMode": Pm1004vdcDccMode,
       "Pm1004vdcClientOosMode": Pm1004vdcClientOosMode,
       "Pm1004vdcOtxMode": Pm1004vdcOtxMode,
       "Pm1004vdcOtxGrid": Pm1004vdcOtxGrid,
       "Pm1004vdcAdjustValue": Pm1004vdcAdjustValue,
       "Pm1004vdcOtxChannel": Pm1004vdcOtxChannel,
       "modulePm1004vdc": modulePm1004vdc,
       "pm1004vdcalarms": pm1004vdcalarms,
       "pm1004vdcAlmOther": pm1004vdcAlmOther,
       "pm1004vdcAlmOtherNurg": pm1004vdcAlmOtherNurg,
       "pm1004vdcAlmsynthAlm2": pm1004vdcAlmsynthAlm2,
       "pm1004vdcAlmConfTableSave": pm1004vdcAlmConfTableSave,
       "pm1004vdcAlmInvUpload": pm1004vdcAlmInvUpload,
       "pm1004vdcAlmConfTableLoad": pm1004vdcAlmConfTableLoad,
       "pm1004vdcAlmCorrelatOff": pm1004vdcAlmCorrelatOff,
       "pm1004vdcAlmMaintenanceOn": pm1004vdcAlmMaintenanceOn,
       "pm1004vdcAlmOtherUrg": pm1004vdcAlmOtherUrg,
       "pm1004vdcAlmmodInitFailLevel2": pm1004vdcAlmmodInitFailLevel2,
       "pm1004vdcAlmLedFail": pm1004vdcAlmLedFail,
       "pm1004vdcAlmNextColdBootForced": pm1004vdcAlmNextColdBootForced,
       "pm1004vdcAlmBootUndone": pm1004vdcAlmBootUndone,
       "pm1004vdcAlmResetHwInitFail": pm1004vdcAlmResetHwInitFail,
       "pm1004vdcAlmSwInitFail": pm1004vdcAlmSwInitFail,
       "pm1004vdcAlmmodInitFailLevel3": pm1004vdcAlmmodInitFailLevel3,
       "pm1004vdcAlmGwIdentFail": pm1004vdcAlmGwIdentFail,
       "pm1004vdcAlmObmTypeReadFail": pm1004vdcAlmObmTypeReadFail,
       "pm1004vdcAlmInitModuleFail": pm1004vdcAlmInitModuleFail,
       "pm1004vdcAlmXfp1InitFail": pm1004vdcAlmXfp1InitFail,
       "pm1004vdcAlmXfp2InitFail": pm1004vdcAlmXfp2InitFail,
       "pm1004vdcAlmLine1InitFail": pm1004vdcAlmLine1InitFail,
       "pm1004vdcAlmLine2InitFail": pm1004vdcAlmLine2InitFail,
       "pm1004vdcAlmClient1InitFail": pm1004vdcAlmClient1InitFail,
       "pm1004vdcAlmClient2InitFail": pm1004vdcAlmClient2InitFail,
       "pm1004vdcAlmClient3InitFail": pm1004vdcAlmClient3InitFail,
       "pm1004vdcAlmClient4InitFail": pm1004vdcAlmClient4InitFail,
       "pm1004vdcAlmClient5InitFail": pm1004vdcAlmClient5InitFail,
       "pm1004vdcAlmClient6InitFail": pm1004vdcAlmClient6InitFail,
       "pm1004vdcAlmclientRxProt": pm1004vdcAlmclientRxProt,
       "pm1004vdcAlmAdddropClient1West": pm1004vdcAlmAdddropClient1West,
       "pm1004vdcAlmAdddropClient2West": pm1004vdcAlmAdddropClient2West,
       "pm1004vdcAlmAdddropClient3West": pm1004vdcAlmAdddropClient3West,
       "pm1004vdcAlmAdddropClient4West": pm1004vdcAlmAdddropClient4West,
       "pm1004vdcAlmAdddropClient5West": pm1004vdcAlmAdddropClient5West,
       "pm1004vdcAlmAdddropClient6West": pm1004vdcAlmAdddropClient6West,
       "pm1004vdcAlmAdddropClient1East": pm1004vdcAlmAdddropClient1East,
       "pm1004vdcAlmAdddropClient2East": pm1004vdcAlmAdddropClient2East,
       "pm1004vdcAlmAdddropClient3East": pm1004vdcAlmAdddropClient3East,
       "pm1004vdcAlmAdddropClient4East": pm1004vdcAlmAdddropClient4East,
       "pm1004vdcAlmAdddropClient5East": pm1004vdcAlmAdddropClient5East,
       "pm1004vdcAlmAdddropClient6East": pm1004vdcAlmAdddropClient6East,
       "pm1004vdcAlmOtherCrit": pm1004vdcAlmOtherCrit,
       "pm1004vdcAlmsynthAlm0": pm1004vdcAlmsynthAlm0,
       "pm1004vdcAlmModGlobFail": pm1004vdcAlmModGlobFail,
       "pm1004vdcAlmDefFuseA": pm1004vdcAlmDefFuseA,
       "pm1004vdcAlmDefFuseB": pm1004vdcAlmDefFuseB,
       "pm1004vdcAlmClient": pm1004vdcAlmClient,
       "pm1004vdcAlmClientNurg": pm1004vdcAlmClientNurg,
       "pm1004vdcAlmsfpWarnDdmTable": pm1004vdcAlmsfpWarnDdmTable,
       "pm1004vdcAlmsfpWarnDdmEntry": pm1004vdcAlmsfpWarnDdmEntry,
       "pm1004vdcAlmsfpWarnDdmIndex": pm1004vdcAlmsfpWarnDdmIndex,
       "pm1004vdcAlmTxPwLowWngPortn": pm1004vdcAlmTxPwLowWngPortn,
       "pm1004vdcAlmTxPwrHighWngPortn": pm1004vdcAlmTxPwrHighWngPortn,
       "pm1004vdcAlmTxBiasLowWngPortn": pm1004vdcAlmTxBiasLowWngPortn,
       "pm1004vdcAlmTxBiasHighWngPortn": pm1004vdcAlmTxBiasHighWngPortn,
       "pm1004vdcAlmVccLowWngPortn": pm1004vdcAlmVccLowWngPortn,
       "pm1004vdcAlmVccHighWngPortn": pm1004vdcAlmVccHighWngPortn,
       "pm1004vdcAlmTempLowWngPortn": pm1004vdcAlmTempLowWngPortn,
       "pm1004vdcAlmTempHighWngPortn": pm1004vdcAlmTempHighWngPortn,
       "pm1004vdcAlmRxPwrLowWngPortn": pm1004vdcAlmRxPwrLowWngPortn,
       "pm1004vdcAlmRxPwrHighWngPortn": pm1004vdcAlmRxPwrHighWngPortn,
       "pm1004vdcAlmsfpCritDdmTable": pm1004vdcAlmsfpCritDdmTable,
       "pm1004vdcAlmsfpCritDdmEntry": pm1004vdcAlmsfpCritDdmEntry,
       "pm1004vdcAlmsfpCritDdmIndex": pm1004vdcAlmsfpCritDdmIndex,
       "pm1004vdcAlmTxPwrLowCritPortn": pm1004vdcAlmTxPwrLowCritPortn,
       "pm1004vdcAlmTxPwrHighCritPortn": pm1004vdcAlmTxPwrHighCritPortn,
       "pm1004vdcAlmRxPwrLowCritPortn": pm1004vdcAlmRxPwrLowCritPortn,
       "pm1004vdcAlmRxPwrHighCritPortn": pm1004vdcAlmRxPwrHighCritPortn,
       "pm1004vdcAlmClientUrg": pm1004vdcAlmClientUrg,
       "pm1004vdcAlmsfpAlmDdmTable": pm1004vdcAlmsfpAlmDdmTable,
       "pm1004vdcAlmsfpAlmDdmEntry": pm1004vdcAlmsfpAlmDdmEntry,
       "pm1004vdcAlmsfpAlmDdmIndex": pm1004vdcAlmsfpAlmDdmIndex,
       "pm1004vdcAlmTxPwrLowAlaPortn": pm1004vdcAlmTxPwrLowAlaPortn,
       "pm1004vdcAlmTxPwrHighAlaPortn": pm1004vdcAlmTxPwrHighAlaPortn,
       "pm1004vdcAlmTxBiasLowAlaPortn": pm1004vdcAlmTxBiasLowAlaPortn,
       "pm1004vdcAlmTxBiasHighAlaPortn": pm1004vdcAlmTxBiasHighAlaPortn,
       "pm1004vdcAlmVccLowAlaPortn": pm1004vdcAlmVccLowAlaPortn,
       "pm1004vdcAlmVccHighAlaPortn": pm1004vdcAlmVccHighAlaPortn,
       "pm1004vdcAlmTempLowAlaPortn": pm1004vdcAlmTempLowAlaPortn,
       "pm1004vdcAlmTempHighAlaPortn": pm1004vdcAlmTempHighAlaPortn,
       "pm1004vdcAlmRxPwrLowAlaPortn": pm1004vdcAlmRxPwrLowAlaPortn,
       "pm1004vdcAlmRxPwrHighAlaPortn": pm1004vdcAlmRxPwrHighAlaPortn,
       "pm1004vdcAlmClientCrit": pm1004vdcAlmClientCrit,
       "pm1004vdcAlmsynthAlmPortTable": pm1004vdcAlmsynthAlmPortTable,
       "pm1004vdcAlmsynthAlmPortEntry": pm1004vdcAlmsynthAlmPortEntry,
       "pm1004vdcAlmsynthAlmPortIndex": pm1004vdcAlmsynthAlmPortIndex,
       "pm1004vdcAlmSfpAbsentPortn": pm1004vdcAlmSfpAbsentPortn,
       "pm1004vdcAlmDdmAbsentPortn": pm1004vdcAlmDdmAbsentPortn,
       "pm1004vdcAlmHwFailAccPortn": pm1004vdcAlmHwFailAccPortn,
       "pm1004vdcAlmDwLsdPortn": pm1004vdcAlmDwLsdPortn,
       "pm1004vdcAlmClientLocalOosTxPortn": pm1004vdcAlmClientLocalOosTxPortn,
       "pm1004vdcAlmClientLocalOosRxPortn": pm1004vdcAlmClientLocalOosRxPortn,
       "pm1004vdcAlmDwCaisPortn": pm1004vdcAlmDwCaisPortn,
       "pm1004vdcAlmSfpDdmWarningPortn": pm1004vdcAlmSfpDdmWarningPortn,
       "pm1004vdcAlmSfpDdmAlmPortn": pm1004vdcAlmSfpDdmAlmPortn,
       "pm1004vdcAlmSfpDdmCritPortn": pm1004vdcAlmSfpDdmCritPortn,
       "pm1004vdcAlmFailAccPortn": pm1004vdcAlmFailAccPortn,
       "pm1004vdcAlmClientActivePortn": pm1004vdcAlmClientActivePortn,
       "pm1004vdcAlmUpCsfPortn": pm1004vdcAlmUpCsfPortn,
       "pm1004vdcAlmaccessioAlmTable": pm1004vdcAlmaccessioAlmTable,
       "pm1004vdcAlmaccessioAlmEntry": pm1004vdcAlmaccessioAlmEntry,
       "pm1004vdcAlmaccessioAlmIndex": pm1004vdcAlmaccessioAlmIndex,
       "pm1004vdcAlmDwLasFailPortn": pm1004vdcAlmDwLasFailPortn,
       "pm1004vdcAlmUpLosPortn": pm1004vdcAlmUpLosPortn,
       "pm1004vdcAlmmapperDeAlmTable": pm1004vdcAlmmapperDeAlmTable,
       "pm1004vdcAlmmapperDeAlmEntry": pm1004vdcAlmmapperDeAlmEntry,
       "pm1004vdcAlmmapperDeAlmIndex": pm1004vdcAlmmapperDeAlmIndex,
       "pm1004vdcAlmUpAccOosPortn": pm1004vdcAlmUpAccOosPortn,
       "pm1004vdcAlmUpBufferOvlPortn": pm1004vdcAlmUpBufferOvlPortn,
       "pm1004vdcAlmDwCsfDetPortn": pm1004vdcAlmDwCsfDetPortn,
       "pm1004vdcAlmDwBufferOvlPortn": pm1004vdcAlmDwBufferOvlPortn,
       "pm1004vdcAlmvideoProtocolStatusTable": pm1004vdcAlmvideoProtocolStatusTable,
       "pm1004vdcAlmvideoProtocolStatusEntry": pm1004vdcAlmvideoProtocolStatusEntry,
       "pm1004vdcAlmvideoProtocolStatusIndex": pm1004vdcAlmvideoProtocolStatusIndex,
       "pm1004vdcAlmSdiTxPortn": pm1004vdcAlmSdiTxPortn,
       "pm1004vdcAlmHdSdiPalTxPortn": pm1004vdcAlmHdSdiPalTxPortn,
       "pm1004vdcAlmHdSdiNtscTxPortn": pm1004vdcAlmHdSdiNtscTxPortn,
       "pm1004vdcAlmDvbAsiTxPortn": pm1004vdcAlmDvbAsiTxPortn,
       "pm1004vdcAlmFastEtherTxPortn": pm1004vdcAlmFastEtherTxPortn,
       "pm1004vdcAlmGbeTxPortn": pm1004vdcAlmGbeTxPortn,
       "pm1004vdcAlmSdiRxPortn": pm1004vdcAlmSdiRxPortn,
       "pm1004vdcAlmHdSdiPalRxPortn": pm1004vdcAlmHdSdiPalRxPortn,
       "pm1004vdcAlmHdSdiNtscRxPortn": pm1004vdcAlmHdSdiNtscRxPortn,
       "pm1004vdcAlmDvbAsiRxPortn": pm1004vdcAlmDvbAsiRxPortn,
       "pm1004vdcAlmFastEtherRxPortn": pm1004vdcAlmFastEtherRxPortn,
       "pm1004vdcAlmGbeRxPortn": pm1004vdcAlmGbeRxPortn,
       "pm1004vdcAlmLine": pm1004vdcAlmLine,
       "pm1004vdcAlmLineNurg": pm1004vdcAlmLineNurg,
       "pm1004vdcAlmlineXfp1WarningsTable": pm1004vdcAlmlineXfp1WarningsTable,
       "pm1004vdcAlmlineXfp1WarningsEntry": pm1004vdcAlmlineXfp1WarningsEntry,
       "pm1004vdcAlmlineXfp1WarningsIndex": pm1004vdcAlmlineXfp1WarningsIndex,
       "pm1004vdcAlmTxPowerLowWarningPortn": pm1004vdcAlmTxPowerLowWarningPortn,
       "pm1004vdcAlmTxPowerHighWarningPortn": pm1004vdcAlmTxPowerHighWarningPortn,
       "pm1004vdcAlmTxBiasLowWarningPortn": pm1004vdcAlmTxBiasLowWarningPortn,
       "pm1004vdcAlmTxBiasHighWarningPortn": pm1004vdcAlmTxBiasHighWarningPortn,
       "pm1004vdcAlmTempLowWarningPortn": pm1004vdcAlmTempLowWarningPortn,
       "pm1004vdcAlmTempHighWarningPortn": pm1004vdcAlmTempHighWarningPortn,
       "pm1004vdcAlmRxPowerLowWarningPortn": pm1004vdcAlmRxPowerLowWarningPortn,
       "pm1004vdcAlmRxPowerHighWarningPortn": pm1004vdcAlmRxPowerHighWarningPortn,
       "pm1004vdcAlmlineOtx1TlhWarningsTable": pm1004vdcAlmlineOtx1TlhWarningsTable,
       "pm1004vdcAlmlineOtx1TlhWarningsEntry": pm1004vdcAlmlineOtx1TlhWarningsEntry,
       "pm1004vdcAlmlineOtx1TlhWarningsIndex": pm1004vdcAlmlineOtx1TlhWarningsIndex,
       "pm1004vdcAlmLineModulatorAgingHighWarningPortn": pm1004vdcAlmLineModulatorAgingHighWarningPortn,
       "pm1004vdcAlmLineAgingHighWarningPortn": pm1004vdcAlmLineAgingHighWarningPortn,
       "pm1004vdcAlmLineFreqDevHighWarningPortn": pm1004vdcAlmLineFreqDevHighWarningPortn,
       "pm1004vdcAlmLineLaserTempHighWarningPortn": pm1004vdcAlmLineLaserTempHighWarningPortn,
       "pm1004vdcAlmLineUrg": pm1004vdcAlmLineUrg,
       "pm1004vdcAlmlineXfp1AlarmTable": pm1004vdcAlmlineXfp1AlarmTable,
       "pm1004vdcAlmlineXfp1AlarmEntry": pm1004vdcAlmlineXfp1AlarmEntry,
       "pm1004vdcAlmlineXfp1AlarmIndex": pm1004vdcAlmlineXfp1AlarmIndex,
       "pm1004vdcAlmTxPowerLowAlarmPortn": pm1004vdcAlmTxPowerLowAlarmPortn,
       "pm1004vdcAlmTxPowerHighAlarmPortn": pm1004vdcAlmTxPowerHighAlarmPortn,
       "pm1004vdcAlmTxBiasLowAlarmPortn": pm1004vdcAlmTxBiasLowAlarmPortn,
       "pm1004vdcAlmTxBiasHighAlarmPortn": pm1004vdcAlmTxBiasHighAlarmPortn,
       "pm1004vdcAlmTempLowAlarmPortn": pm1004vdcAlmTempLowAlarmPortn,
       "pm1004vdcAlmTempHighAlarmPortn": pm1004vdcAlmTempHighAlarmPortn,
       "pm1004vdcAlmRxPowerLowAlarmPortn": pm1004vdcAlmRxPowerLowAlarmPortn,
       "pm1004vdcAlmRxPowerHighAlarmPortn": pm1004vdcAlmRxPowerHighAlarmPortn,
       "pm1004vdcAlmlineXfp1CritTable": pm1004vdcAlmlineXfp1CritTable,
       "pm1004vdcAlmlineXfp1CritEntry": pm1004vdcAlmlineXfp1CritEntry,
       "pm1004vdcAlmlineXfp1CritIndex": pm1004vdcAlmlineXfp1CritIndex,
       "pm1004vdcAlmTxPowerLowCritPortn": pm1004vdcAlmTxPowerLowCritPortn,
       "pm1004vdcAlmTxPowerHighCritPortn": pm1004vdcAlmTxPowerHighCritPortn,
       "pm1004vdcAlmRxPowerLowCritPortn": pm1004vdcAlmRxPowerLowCritPortn,
       "pm1004vdcAlmRxPowerHighCritPortn": pm1004vdcAlmRxPowerHighCritPortn,
       "pm1004vdcAlmlineXfp1SupplyAlarmTable": pm1004vdcAlmlineXfp1SupplyAlarmTable,
       "pm1004vdcAlmlineXfp1SupplyAlarmEntry": pm1004vdcAlmlineXfp1SupplyAlarmEntry,
       "pm1004vdcAlmlineXfp1SupplyAlarmIndex": pm1004vdcAlmlineXfp1SupplyAlarmIndex,
       "pm1004vdcAlmVee5LowAlarmPortn": pm1004vdcAlmVee5LowAlarmPortn,
       "pm1004vdcAlmVee5HighAlarmPortn": pm1004vdcAlmVee5HighAlarmPortn,
       "pm1004vdcAlmVcc2LowAlarmPortn": pm1004vdcAlmVcc2LowAlarmPortn,
       "pm1004vdcAlmVcc2HighAlarmPortn": pm1004vdcAlmVcc2HighAlarmPortn,
       "pm1004vdcAlmVcc3LowAlarmPortn": pm1004vdcAlmVcc3LowAlarmPortn,
       "pm1004vdcAlmVcc3HighAlarmPortn": pm1004vdcAlmVcc3HighAlarmPortn,
       "pm1004vdcAlmVcc5LowAlarmPortn": pm1004vdcAlmVcc5LowAlarmPortn,
       "pm1004vdcAlmVcc5HighAlarmPortn": pm1004vdcAlmVcc5HighAlarmPortn,
       "pm1004vdcAlmVee5LowWarningPortn": pm1004vdcAlmVee5LowWarningPortn,
       "pm1004vdcAlmVee5HighWarningPortn": pm1004vdcAlmVee5HighWarningPortn,
       "pm1004vdcAlmVcc2LowWarningPortn": pm1004vdcAlmVcc2LowWarningPortn,
       "pm1004vdcAlmVcc2HighWarningPortn": pm1004vdcAlmVcc2HighWarningPortn,
       "pm1004vdcAlmVcc3LowWarningPortn": pm1004vdcAlmVcc3LowWarningPortn,
       "pm1004vdcAlmVcc3HighWarningPortn": pm1004vdcAlmVcc3HighWarningPortn,
       "pm1004vdcAlmVcc5LowWarningPortn": pm1004vdcAlmVcc5LowWarningPortn,
       "pm1004vdcAlmVcc5HighWarningPortn": pm1004vdcAlmVcc5HighWarningPortn,
       "pm1004vdcAlmlineOtx1TlhAlarmsTable": pm1004vdcAlmlineOtx1TlhAlarmsTable,
       "pm1004vdcAlmlineOtx1TlhAlarmsEntry": pm1004vdcAlmlineOtx1TlhAlarmsEntry,
       "pm1004vdcAlmlineOtx1TlhAlarmsIndex": pm1004vdcAlmlineOtx1TlhAlarmsIndex,
       "pm1004vdcAlmLineModulatorAgingHighAlaPortn": pm1004vdcAlmLineModulatorAgingHighAlaPortn,
       "pm1004vdcAlmLineAgingHighAlaPortn": pm1004vdcAlmLineAgingHighAlaPortn,
       "pm1004vdcAlmLineFreqDevHighAlaPortn": pm1004vdcAlmLineFreqDevHighAlaPortn,
       "pm1004vdcAlmLineLaserTempHighAlaPortn": pm1004vdcAlmLineLaserTempHighAlaPortn,
       "pm1004vdcAlmLineCrit": pm1004vdcAlmLineCrit,
       "pm1004vdcAlmsynthAlmLineTable": pm1004vdcAlmsynthAlmLineTable,
       "pm1004vdcAlmsynthAlmLineEntry": pm1004vdcAlmsynthAlmLineEntry,
       "pm1004vdcAlmsynthAlmLineIndex": pm1004vdcAlmsynthAlmLineIndex,
       "pm1004vdcAlmXfpAbsentPortn": pm1004vdcAlmXfpAbsentPortn,
       "pm1004vdcAlmXfpInitNotComplPortn": pm1004vdcAlmXfpInitNotComplPortn,
       "pm1004vdcAlmLineHwFailPortn": pm1004vdcAlmLineHwFailPortn,
       "pm1004vdcAlmXfpTxOffPortn": pm1004vdcAlmXfpTxOffPortn,
       "pm1004vdcAlmLineLocalOosPortn": pm1004vdcAlmLineLocalOosPortn,
       "pm1004vdcAlmLineDdmWarningPortn": pm1004vdcAlmLineDdmWarningPortn,
       "pm1004vdcAlmLineDdmAlmPortn": pm1004vdcAlmLineDdmAlmPortn,
       "pm1004vdcAlmLineDdmCritPortn": pm1004vdcAlmLineDdmCritPortn,
       "pm1004vdcAlmLineFailPortn": pm1004vdcAlmLineFailPortn,
       "pm1004vdcAlmLineActivePortn": pm1004vdcAlmLineActivePortn,
       "pm1004vdcAlmdfrmAlmTable": pm1004vdcAlmdfrmAlmTable,
       "pm1004vdcAlmdfrmAlmEntry": pm1004vdcAlmdfrmAlmEntry,
       "pm1004vdcAlmdfrmAlmIndex": pm1004vdcAlmdfrmAlmIndex,
       "pm1004vdcAlmDwLossofsyncPortn": pm1004vdcAlmDwLossofsyncPortn,
       "pm1004vdcAlmlineSyncAlarmsTable": pm1004vdcAlmlineSyncAlarmsTable,
       "pm1004vdcAlmlineSyncAlarmsEntry": pm1004vdcAlmlineSyncAlarmsEntry,
       "pm1004vdcAlmlineSyncAlarmsIndex": pm1004vdcAlmlineSyncAlarmsIndex,
       "pm1004vdcAlmDwLockerrPortn": pm1004vdcAlmDwLockerrPortn,
       "pm1004vdcAlmUpLockerrPortn": pm1004vdcAlmUpLockerrPortn,
       "pm1004vdcAlmDwLosPortn": pm1004vdcAlmDwLosPortn,
       "pm1004vdcAlmlineXfp1AlarmsTable": pm1004vdcAlmlineXfp1AlarmsTable,
       "pm1004vdcAlmlineXfp1AlarmsEntry": pm1004vdcAlmlineXfp1AlarmsEntry,
       "pm1004vdcAlmlineXfp1AlarmsIndex": pm1004vdcAlmlineXfp1AlarmsIndex,
       "pm1004vdcAlmModNrPortn": pm1004vdcAlmModNrPortn,
       "pm1004vdcAlmRxCdrNotLockedPortn": pm1004vdcAlmRxCdrNotLockedPortn,
       "pm1004vdcAlmRxNrPortn": pm1004vdcAlmRxNrPortn,
       "pm1004vdcAlmTxCdrNotLockedPortn": pm1004vdcAlmTxCdrNotLockedPortn,
       "pm1004vdcAlmTxFaultPortn": pm1004vdcAlmTxFaultPortn,
       "pm1004vdcAlmTxNrPortn": pm1004vdcAlmTxNrPortn,
       "pm1004vdcAlmWavelengthUnlockedPortn": pm1004vdcAlmWavelengthUnlockedPortn,
       "pm1004vdcAlmTecFaultPortn": pm1004vdcAlmTecFaultPortn,
       "pm1004vdcAlmApdSupplyFaultPortn": pm1004vdcAlmApdSupplyFaultPortn,
       "pm1004vdcmeasures": pm1004vdcmeasures,
       "pm1004vdcMesrOther": pm1004vdcMesrOther,
       "pm1004vdcMesrsynth0": pm1004vdcMesrsynth0,
       "pm1004vdcMesrsynth1": pm1004vdcMesrsynth1,
       "pm1004vdcMesrClient": pm1004vdcMesrClient,
       "pm1004vdcMesrtempMeasTable": pm1004vdcMesrtempMeasTable,
       "pm1004vdcMesrtempMeasEntry": pm1004vdcMesrtempMeasEntry,
       "pm1004vdcMesrtempMeasIndex": pm1004vdcMesrtempMeasIndex,
       "pm1004vdcMesrtempMeasPortn": pm1004vdcMesrtempMeasPortn,
       "pm1004vdcMesrvoltMeasTable": pm1004vdcMesrvoltMeasTable,
       "pm1004vdcMesrvoltMeasEntry": pm1004vdcMesrvoltMeasEntry,
       "pm1004vdcMesrvoltMeasIndex": pm1004vdcMesrvoltMeasIndex,
       "pm1004vdcMesrvoltMeasPortn": pm1004vdcMesrvoltMeasPortn,
       "pm1004vdcMesrbiasMeasTable": pm1004vdcMesrbiasMeasTable,
       "pm1004vdcMesrbiasMeasEntry": pm1004vdcMesrbiasMeasEntry,
       "pm1004vdcMesrbiasMeasIndex": pm1004vdcMesrbiasMeasIndex,
       "pm1004vdcMesrbiasMeasPortn": pm1004vdcMesrbiasMeasPortn,
       "pm1004vdcMesrtxpwrMeasTable": pm1004vdcMesrtxpwrMeasTable,
       "pm1004vdcMesrtxpwrMeasEntry": pm1004vdcMesrtxpwrMeasEntry,
       "pm1004vdcMesrtxpwrMeasIndex": pm1004vdcMesrtxpwrMeasIndex,
       "pm1004vdcMesrtxpwrMeasPortn": pm1004vdcMesrtxpwrMeasPortn,
       "pm1004vdcMesrrxpwrMeasTable": pm1004vdcMesrrxpwrMeasTable,
       "pm1004vdcMesrrxpwrMeasEntry": pm1004vdcMesrrxpwrMeasEntry,
       "pm1004vdcMesrrxpwrMeasIndex": pm1004vdcMesrrxpwrMeasIndex,
       "pm1004vdcMesrrxpwrMeasPortn": pm1004vdcMesrrxpwrMeasPortn,
       "pm1004vdcMesrLine": pm1004vdcMesrLine,
       "pm1004vdcMesrxfp1LxModTempMeasTable": pm1004vdcMesrxfp1LxModTempMeasTable,
       "pm1004vdcMesrxfp1LxModTempMeasEntry": pm1004vdcMesrxfp1LxModTempMeasEntry,
       "pm1004vdcMesrxfp1LxModTempMeasIndex": pm1004vdcMesrxfp1LxModTempMeasIndex,
       "pm1004vdcMesrxfp1LxModTempMeasPortn": pm1004vdcMesrxfp1LxModTempMeasPortn,
       "pm1004vdcMesrxfp1ReservedTable": pm1004vdcMesrxfp1ReservedTable,
       "pm1004vdcMesrxfp1ReservedEntry": pm1004vdcMesrxfp1ReservedEntry,
       "pm1004vdcMesrxfp1ReservedIndex": pm1004vdcMesrxfp1ReservedIndex,
       "pm1004vdcMesrxfp1ReservedPortn": pm1004vdcMesrxfp1ReservedPortn,
       "pm1004vdcMesrxfp1LoBiasCurrentMeasTable": pm1004vdcMesrxfp1LoBiasCurrentMeasTable,
       "pm1004vdcMesrxfp1LoBiasCurrentMeasEntry": pm1004vdcMesrxfp1LoBiasCurrentMeasEntry,
       "pm1004vdcMesrxfp1LoBiasCurrentMeasIndex": pm1004vdcMesrxfp1LoBiasCurrentMeasIndex,
       "pm1004vdcMesrxfp1LoBiasCurrentMeasPortn": pm1004vdcMesrxfp1LoBiasCurrentMeasPortn,
       "pm1004vdcMesrxfp1LoTxPowerMeasTable": pm1004vdcMesrxfp1LoTxPowerMeasTable,
       "pm1004vdcMesrxfp1LoTxPowerMeasEntry": pm1004vdcMesrxfp1LoTxPowerMeasEntry,
       "pm1004vdcMesrxfp1LoTxPowerMeasIndex": pm1004vdcMesrxfp1LoTxPowerMeasIndex,
       "pm1004vdcMesrxfp1LoTxPowerMeasPortn": pm1004vdcMesrxfp1LoTxPowerMeasPortn,
       "pm1004vdcMesrxfp1LiRxPowerMeasTable": pm1004vdcMesrxfp1LiRxPowerMeasTable,
       "pm1004vdcMesrxfp1LiRxPowerMeasEntry": pm1004vdcMesrxfp1LiRxPowerMeasEntry,
       "pm1004vdcMesrxfp1LiRxPowerMeasIndex": pm1004vdcMesrxfp1LiRxPowerMeasIndex,
       "pm1004vdcMesrxfp1LiRxPowerMeasPortn": pm1004vdcMesrxfp1LiRxPowerMeasPortn,
       "pm1004vdcMesrxfp1LxAux1MeasTable": pm1004vdcMesrxfp1LxAux1MeasTable,
       "pm1004vdcMesrxfp1LxAux1MeasEntry": pm1004vdcMesrxfp1LxAux1MeasEntry,
       "pm1004vdcMesrxfp1LxAux1MeasIndex": pm1004vdcMesrxfp1LxAux1MeasIndex,
       "pm1004vdcMesrxfp1LxAux1MeasPortn": pm1004vdcMesrxfp1LxAux1MeasPortn,
       "pm1004vdcMesrxfp1LxAux2MeasTable": pm1004vdcMesrxfp1LxAux2MeasTable,
       "pm1004vdcMesrxfp1LxAux2MeasEntry": pm1004vdcMesrxfp1LxAux2MeasEntry,
       "pm1004vdcMesrxfp1LxAux2MeasIndex": pm1004vdcMesrxfp1LxAux2MeasIndex,
       "pm1004vdcMesrxfp1LxAux2MeasPortn": pm1004vdcMesrxfp1LxAux2MeasPortn,
       "pm1004vdcMesrotx1AgingTable": pm1004vdcMesrotx1AgingTable,
       "pm1004vdcMesrotx1AgingEntry": pm1004vdcMesrotx1AgingEntry,
       "pm1004vdcMesrotx1AgingIndex": pm1004vdcMesrotx1AgingIndex,
       "pm1004vdcMesrotx1AgingPortn": pm1004vdcMesrotx1AgingPortn,
       "pm1004vdcMesrotx1LaserTemperatureTable": pm1004vdcMesrotx1LaserTemperatureTable,
       "pm1004vdcMesrotx1LaserTemperatureEntry": pm1004vdcMesrotx1LaserTemperatureEntry,
       "pm1004vdcMesrotx1LaserTemperatureIndex": pm1004vdcMesrotx1LaserTemperatureIndex,
       "pm1004vdcMesrotx1LaserTemperaturePortn": pm1004vdcMesrotx1LaserTemperaturePortn,
       "pm1004vdcMesrotx1FreqDeviationTable": pm1004vdcMesrotx1FreqDeviationTable,
       "pm1004vdcMesrotx1FreqDeviationEntry": pm1004vdcMesrotx1FreqDeviationEntry,
       "pm1004vdcMesrotx1FreqDeviationIndex": pm1004vdcMesrotx1FreqDeviationIndex,
       "pm1004vdcMesrotx1FreqDeviationPortn": pm1004vdcMesrotx1FreqDeviationPortn,
       "pm1004vdcMesrotx1LaserWvlengthTable": pm1004vdcMesrotx1LaserWvlengthTable,
       "pm1004vdcMesrotx1LaserWvlengthEntry": pm1004vdcMesrotx1LaserWvlengthEntry,
       "pm1004vdcMesrotx1LaserWvlengthIndex": pm1004vdcMesrotx1LaserWvlengthIndex,
       "pm1004vdcMesrotx1LaserWvlengthPortn": pm1004vdcMesrotx1LaserWvlengthPortn,
       "pm1004vdccounters": pm1004vdccounters,
       "pm1004vdcCntOther": pm1004vdcCntOther,
       "pm1004vdcCntClient": pm1004vdcCntClient,
       "pm1004vdcCntLine": pm1004vdcCntLine,
       "pm1004vdcCntdfrmB1ErrCntTable": pm1004vdcCntdfrmB1ErrCntTable,
       "pm1004vdcCntdfrmB1ErrCntEntry": pm1004vdcCntdfrmB1ErrCntEntry,
       "pm1004vdcCntdfrmB1ErrCntIndex": pm1004vdcCntdfrmB1ErrCntIndex,
       "pm1004vdcCntdfrmB1ErrCntValuePortn": pm1004vdcCntdfrmB1ErrCntValuePortn,
       "pm1004vdcCntdfrmB1ErrCntErrorPortn": pm1004vdcCntdfrmB1ErrCntErrorPortn,
       "pm1004vdcCntdfrmB1ErrCntOverloadPortn": pm1004vdcCntdfrmB1ErrCntOverloadPortn,
       "pm1004vdcCntdfrmTimCntTable": pm1004vdcCntdfrmTimCntTable,
       "pm1004vdcCntdfrmTimCntEntry": pm1004vdcCntdfrmTimCntEntry,
       "pm1004vdcCntdfrmTimCntIndex": pm1004vdcCntdfrmTimCntIndex,
       "pm1004vdcCntdfrmTimCntValuePortn": pm1004vdcCntdfrmTimCntValuePortn,
       "pm1004vdcCntdfrmTimCntErrorPortn": pm1004vdcCntdfrmTimCntErrorPortn,
       "pm1004vdcCntdfrmTimCntOverloadPortn": pm1004vdcCntdfrmTimCntOverloadPortn,
       "pm1004vdcCntCountersReset": pm1004vdcCntCountersReset,
       "pm1004vdcCntCountersStop": pm1004vdcCntCountersStop,
       "pm1004vdccontrolsWrite": pm1004vdccontrolsWrite,
       "pm1004vdcCtrlOther": pm1004vdcCtrlOther,
       "pm1004vdcCtrlconfMgnt1": pm1004vdcCtrlconfMgnt1,
       "pm1004vdcCtrlConf1Load1": pm1004vdcCtrlConf1Load1,
       "pm1004vdcCtrlConf2Load1": pm1004vdcCtrlConf2Load1,
       "pm1004vdcCtrlConf2Flash1": pm1004vdcCtrlConf2Flash1,
       "pm1004vdcCtrlConf2Clear1": pm1004vdcCtrlConf2Clear1,
       "pm1004vdcCtrlsynth4": pm1004vdcCtrlsynth4,
       "pm1004vdcCtrlCorrelatOn": pm1004vdcCtrlCorrelatOn,
       "pm1004vdcCtrlCorrelatOff": pm1004vdcCtrlCorrelatOff,
       "pm1004vdcCtrlswMgnt": pm1004vdcCtrlswMgnt,
       "pm1004vdcCtrlColdReset": pm1004vdcCtrlColdReset,
       "pm1004vdcCtrlWarmReset": pm1004vdcCtrlWarmReset,
       "pm1004vdcCtrlLoadSwBank1": pm1004vdcCtrlLoadSwBank1,
       "pm1004vdcCtrlLoadSwBank2": pm1004vdcCtrlLoadSwBank2,
       "pm1004vdcCtrlgwMgnt": pm1004vdcCtrlgwMgnt,
       "pm1004vdcCtrlCurrentGwReset": pm1004vdcCtrlCurrentGwReset,
       "pm1004vdcCtrlLoadGwBank1": pm1004vdcCtrlLoadGwBank1,
       "pm1004vdcCtrlLoadGwBank2": pm1004vdcCtrlLoadGwBank2,
       "pm1004vdcCtrlLoadGwBank3": pm1004vdcCtrlLoadGwBank3,
       "pm1004vdcCtrlLoadGwBank4": pm1004vdcCtrlLoadGwBank4,
       "pm1004vdcCtrlledTest": pm1004vdcCtrlledTest,
       "pm1004vdcCtrlGreenLed": pm1004vdcCtrlGreenLed,
       "pm1004vdcCtrlRedLed": pm1004vdcCtrlRedLed,
       "pm1004vdcCtrlLedOff": pm1004vdcCtrlLedOff,
       "pm1004vdcCtrlmoduleOosMode": pm1004vdcCtrlmoduleOosMode,
       "pm1004vdcCtrlModuleOosMode": pm1004vdcCtrlModuleOosMode,
       "pm1004vdcCtrlmaintenanceMode": pm1004vdcCtrlmaintenanceMode,
       "pm1004vdcCtrlMaintenanceMode": pm1004vdcCtrlMaintenanceMode,
       "pm1004vdcCtrlClient": pm1004vdcCtrlClient,
       "pm1004vdcCtrlaccessLoopTable": pm1004vdcCtrlaccessLoopTable,
       "pm1004vdcCtrlaccessLoopEntry": pm1004vdcCtrlaccessLoopEntry,
       "pm1004vdcCtrlaccessLoopIndex": pm1004vdcCtrlaccessLoopIndex,
       "pm1004vdcCtrlaccessLoopPortn": pm1004vdcCtrlaccessLoopPortn,
       "pm1004vdcCtrlportOosModeTable": pm1004vdcCtrlportOosModeTable,
       "pm1004vdcCtrlportOosModeEntry": pm1004vdcCtrlportOosModeEntry,
       "pm1004vdcCtrlportOosModeIndex": pm1004vdcCtrlportOosModeIndex,
       "pm1004vdcCtrlportOosModePortn": pm1004vdcCtrlportOosModePortn,
       "pm1004vdcCtrlsfpOffCtrlTable": pm1004vdcCtrlsfpOffCtrlTable,
       "pm1004vdcCtrlsfpOffCtrlEntry": pm1004vdcCtrlsfpOffCtrlEntry,
       "pm1004vdcCtrlsfpOffCtrlIndex": pm1004vdcCtrlsfpOffCtrlIndex,
       "pm1004vdcCtrlsfpOffCtrlPortn": pm1004vdcCtrlsfpOffCtrlPortn,
       "pm1004vdcCtrlcsfUpInsTable": pm1004vdcCtrlcsfUpInsTable,
       "pm1004vdcCtrlcsfUpInsEntry": pm1004vdcCtrlcsfUpInsEntry,
       "pm1004vdcCtrlcsfUpInsIndex": pm1004vdcCtrlcsfUpInsIndex,
       "pm1004vdcCtrlcsfUpInsPortn": pm1004vdcCtrlcsfUpInsPortn,
       "pm1004vdcCtrlcaisDwInsTable": pm1004vdcCtrlcaisDwInsTable,
       "pm1004vdcCtrlcaisDwInsEntry": pm1004vdcCtrlcaisDwInsEntry,
       "pm1004vdcCtrlcaisDwInsIndex": pm1004vdcCtrlcaisDwInsIndex,
       "pm1004vdcCtrlcaisDwInsPortn": pm1004vdcCtrlcaisDwInsPortn,
       "pm1004vdcCtrlclientAccessTermLoopTable": pm1004vdcCtrlclientAccessTermLoopTable,
       "pm1004vdcCtrlclientAccessTermLoopEntry": pm1004vdcCtrlclientAccessTermLoopEntry,
       "pm1004vdcCtrlclientAccessTermLoopIndex": pm1004vdcCtrlclientAccessTermLoopIndex,
       "pm1004vdcCtrlclientAccessTermLoopPortn": pm1004vdcCtrlclientAccessTermLoopPortn,
       "pm1004vdcCtrlrxVideoProtocolTable": pm1004vdcCtrlrxVideoProtocolTable,
       "pm1004vdcCtrlrxVideoProtocolEntry": pm1004vdcCtrlrxVideoProtocolEntry,
       "pm1004vdcCtrlrxVideoProtocolIndex": pm1004vdcCtrlrxVideoProtocolIndex,
       "pm1004vdcCtrlrxVideoProtocolPortn": pm1004vdcCtrlrxVideoProtocolPortn,
       "pm1004vdcCtrladddropClientRxProtectTable": pm1004vdcCtrladddropClientRxProtectTable,
       "pm1004vdcCtrladddropClientRxProtectEntry": pm1004vdcCtrladddropClientRxProtectEntry,
       "pm1004vdcCtrladddropClientRxProtectIndex": pm1004vdcCtrladddropClientRxProtectIndex,
       "pm1004vdcCtrladddropClientRxProtectPortn": pm1004vdcCtrladddropClientRxProtectPortn,
       "pm1004vdcCtrladddropTsClientModeTable": pm1004vdcCtrladddropTsClientModeTable,
       "pm1004vdcCtrladddropTsClientModeEntry": pm1004vdcCtrladddropTsClientModeEntry,
       "pm1004vdcCtrladddropTsClientModeIndex": pm1004vdcCtrladddropTsClientModeIndex,
       "pm1004vdcCtrladddropTsClientModePortn": pm1004vdcCtrladddropTsClientModePortn,
       "pm1004vdcCtrlLine": pm1004vdcCtrlLine,
       "pm1004vdcCtrlcommAccessLoop": pm1004vdcCtrlcommAccessLoop,
       "pm1004vdcCtrlCommAccessloop": pm1004vdcCtrlCommAccessloop,
       "pm1004vdcCtrllineLoop": pm1004vdcCtrllineLoop,
       "pm1004vdcCtrlLineLoop": pm1004vdcCtrlLineLoop,
       "pm1004vdcCtrlProtMgnt": pm1004vdcCtrlProtMgnt,
       "pm1004vdcCtrlLineNumber": pm1004vdcCtrlLineNumber,
       "pm1004vdcCtrlProtMode": pm1004vdcCtrlProtMode,
       "pm1004vdcCtrllineOosModeTable": pm1004vdcCtrllineOosModeTable,
       "pm1004vdcCtrllineOosModeEntry": pm1004vdcCtrllineOosModeEntry,
       "pm1004vdcCtrllineOosModeIndex": pm1004vdcCtrllineOosModeIndex,
       "pm1004vdcCtrllineOosModePortn": pm1004vdcCtrllineOosModePortn,
       "pm1004vdcCtrldccEnableTable": pm1004vdcCtrldccEnableTable,
       "pm1004vdcCtrldccEnableEntry": pm1004vdcCtrldccEnableEntry,
       "pm1004vdcCtrldccEnableIndex": pm1004vdcCtrldccEnableIndex,
       "pm1004vdcCtrldccEnablePortn": pm1004vdcCtrldccEnablePortn,
       "pm1004vdcCtrlxfpOnoffTable": pm1004vdcCtrlxfpOnoffTable,
       "pm1004vdcCtrlxfpOnoffEntry": pm1004vdcCtrlxfpOnoffEntry,
       "pm1004vdcCtrlxfpOnoffIndex": pm1004vdcCtrlxfpOnoffIndex,
       "pm1004vdcCtrlxfpOnoffPortn": pm1004vdcCtrlxfpOnoffPortn,
       "pm1004vdcCtrlxfpLineLoopTable": pm1004vdcCtrlxfpLineLoopTable,
       "pm1004vdcCtrlxfpLineLoopEntry": pm1004vdcCtrlxfpLineLoopEntry,
       "pm1004vdcCtrlxfpLineLoopIndex": pm1004vdcCtrlxfpLineLoopIndex,
       "pm1004vdcCtrlxfpLineLoopPortn": pm1004vdcCtrlxfpLineLoopPortn,
       "pm1004vdcCtrlxfpXfiLoopTable": pm1004vdcCtrlxfpXfiLoopTable,
       "pm1004vdcCtrlxfpXfiLoopEntry": pm1004vdcCtrlxfpXfiLoopEntry,
       "pm1004vdcCtrlxfpXfiLoopIndex": pm1004vdcCtrlxfpXfiLoopIndex,
       "pm1004vdcCtrlxfpXfiLoopPortn": pm1004vdcCtrlxfpXfiLoopPortn,
       "pm1004vdcri": pm1004vdcri,
       "pm1004vdcriTable": pm1004vdcriTable,
       "pm1004vdcRinvSfpTable": pm1004vdcRinvSfpTable,
       "pm1004vdcRinvSfpEntry": pm1004vdcRinvSfpEntry,
       "pm1004vdcRinvSfpIndex": pm1004vdcRinvSfpIndex,
       "pm1004vdcRinvsfp": pm1004vdcRinvsfp,
       "pm1004vdcRinvLineTable": pm1004vdcRinvLineTable,
       "pm1004vdcRinvLineEntry": pm1004vdcRinvLineEntry,
       "pm1004vdcRinvLineIndex": pm1004vdcRinvLineIndex,
       "pm1004vdcRinvxfpLine": pm1004vdcRinvxfpLine,
       "pm1004vdcRinvReloadInventory": pm1004vdcRinvReloadInventory,
       "pm1004vdcRinvHwPlatform": pm1004vdcRinvHwPlatform,
       "pm1004vdcRinvModulePlatform": pm1004vdcRinvModulePlatform,
       "pm1004vdcRinvSwPlatform": pm1004vdcRinvSwPlatform,
       "pm1004vdcRinvGwPlatform": pm1004vdcRinvGwPlatform,
       "pm1004vdcdownload": pm1004vdcdownload,
       "pm1004vdcDwlOther": pm1004vdcDwlOther,
       "pm1004vdcDwlrestartProcess": pm1004vdcDwlrestartProcess,
       "pm1004vdcDwlWarmRestartProcessed": pm1004vdcDwlWarmRestartProcessed,
       "pm1004vdcDwlColdRestartProcessed": pm1004vdcDwlColdRestartProcessed,
       "pm1004vdcDwlswBanksUsed": pm1004vdcDwlswBanksUsed,
       "pm1004vdcDwlSwBank1Used": pm1004vdcDwlSwBank1Used,
       "pm1004vdcDwlSwBank2Used": pm1004vdcDwlSwBank2Used,
       "pm1004vdcDwlSwBank1Notempty": pm1004vdcDwlSwBank1Notempty,
       "pm1004vdcDwlSwBank2Notempty": pm1004vdcDwlSwBank2Notempty,
       "pm1004vdcDwlgwBanksUsed": pm1004vdcDwlgwBanksUsed,
       "pm1004vdcDwlGwBank1Used": pm1004vdcDwlGwBank1Used,
       "pm1004vdcDwlGwBank2Used": pm1004vdcDwlGwBank2Used,
       "pm1004vdcDwlGwBank3Used": pm1004vdcDwlGwBank3Used,
       "pm1004vdcDwlGwBank4Used": pm1004vdcDwlGwBank4Used,
       "pm1004vdcDwlGwBank1Notempty": pm1004vdcDwlGwBank1Notempty,
       "pm1004vdcDwlGwBank2Notempty": pm1004vdcDwlGwBank2Notempty,
       "pm1004vdcDwlGwBank3Notempty": pm1004vdcDwlGwBank3Notempty,
       "pm1004vdcDwlGwBank4Notempty": pm1004vdcDwlGwBank4Notempty,
       "pm1004vdcDwlClient": pm1004vdcDwlClient,
       "pm1004vdcDwlLine": pm1004vdcDwlLine,
       "pm1004vdcConfig": pm1004vdcConfig,
       "pm1004vdcCfgAccessCAisCsf": pm1004vdcCfgAccessCAisCsf,
       "pm1004vdcCfgClientcaiscsfTable": pm1004vdcCfgClientcaiscsfTable,
       "pm1004vdcCfgClientcaiscsfEntry": pm1004vdcCfgClientcaiscsfEntry,
       "pm1004vdcCfgClientcaiscsfIndex": pm1004vdcCfgClientcaiscsfIndex,
       "pm1004vdcCfgCAisModePortn": pm1004vdcCfgCAisModePortn,
       "pm1004vdcCfgUpAccessioAlmPortn": pm1004vdcCfgUpAccessioAlmPortn,
       "pm1004vdcCfgUpMapperDeAlmPortn": pm1004vdcCfgUpMapperDeAlmPortn,
       "pm1004vdcCfgDownAccessioAlmPortn": pm1004vdcCfgDownAccessioAlmPortn,
       "pm1004vdcCfgDownMapperDeAlmPortn": pm1004vdcCfgDownMapperDeAlmPortn,
       "pm1004vdcCfgDownDfrmAlmPortn": pm1004vdcCfgDownDfrmAlmPortn,
       "pm1004vdcCfgDownLineSyncAlarmsPortn": pm1004vdcCfgDownLineSyncAlarmsPortn,
       "pm1004vdcCfgStartup": pm1004vdcCfgStartup,
       "pm1004vdcCfgClientStartupTable": pm1004vdcCfgClientStartupTable,
       "pm1004vdcCfgClientStartupEntry": pm1004vdcCfgClientStartupEntry,
       "pm1004vdcCfgClientStartupIndex": pm1004vdcCfgClientStartupIndex,
       "pm1004vdcCfgSystConfPortPortn": pm1004vdcCfgSystConfPortPortn,
       "pm1004vdcCfgNetConfPortPortn": pm1004vdcCfgNetConfPortPortn,
       "pm1004vdcCfgAdddropConfPortPortn": pm1004vdcCfgAdddropConfPortPortn,
       "pm1004vdctablelineStartup": pm1004vdctablelineStartup,
       "pm1004vdcCfgsystConfLine1": pm1004vdcCfgsystConfLine1,
       "pm1004vdcCfglineOptions1": pm1004vdcCfglineOptions1,
       "pm1004vdcCfgsystConfLine2": pm1004vdcCfgsystConfLine2,
       "pm1004vdcCfglineSelection": pm1004vdcCfglineSelection,
       "pm1004vdcCfglineOptions2": pm1004vdcCfglineOptions2,
       "pm1004vdcCfgXfpTable": pm1004vdcCfgXfpTable,
       "pm1004vdcCfgXfpEntry": pm1004vdcCfgXfpEntry,
       "pm1004vdcCfgXfpIndex": pm1004vdcCfgXfpIndex,
       "pm1004vdcCfgSystConfXfpPortn": pm1004vdcCfgSystConfXfpPortn,
       "pm1004vdcCfgDataRateConfXfpPortn": pm1004vdcCfgDataRateConfXfpPortn,
       "pm1004vdcCfgLabels": pm1004vdcCfgLabels,
       "pm1004vdcCfgLabelclientTable": pm1004vdcCfgLabelclientTable,
       "pm1004vdcCfgLabelclientEntry": pm1004vdcCfgLabelclientEntry,
       "pm1004vdcCfgLabelclientIndex": pm1004vdcCfgLabelclientIndex,
       "pm1004vdcCfgLabelclientPortn": pm1004vdcCfgLabelclientPortn,
       "pm1004vdcCfgLabellineTable": pm1004vdcCfgLabellineTable,
       "pm1004vdcCfgLabellineEntry": pm1004vdcCfgLabellineEntry,
       "pm1004vdcCfgLabellineIndex": pm1004vdcCfgLabellineIndex,
       "pm1004vdcCfgLabellinePortn": pm1004vdcCfgLabellinePortn,
       "pm1004vdcCfgStartupthresholds": pm1004vdcCfgStartupthresholds,
       "pm1004vdcCfgClientStartupThreshTable": pm1004vdcCfgClientStartupThreshTable,
       "pm1004vdcCfgClientStartupThreshEntry": pm1004vdcCfgClientStartupThreshEntry,
       "pm1004vdcCfgClientStartupThreshIndex": pm1004vdcCfgClientStartupThreshIndex,
       "pm1004vdcCfgClientThreshtxpowhighPortn": pm1004vdcCfgClientThreshtxpowhighPortn,
       "pm1004vdcCfgClientThreshtxpowlowPortn": pm1004vdcCfgClientThreshtxpowlowPortn,
       "pm1004vdcCfgClientThreshrxpowhighPortn": pm1004vdcCfgClientThreshrxpowhighPortn,
       "pm1004vdcCfgClientThreshrxpowlowPortn": pm1004vdcCfgClientThreshrxpowlowPortn,
       "pm1004vdcCfgLineStartupThreshTable": pm1004vdcCfgLineStartupThreshTable,
       "pm1004vdcCfgLineStartupThreshEntry": pm1004vdcCfgLineStartupThreshEntry,
       "pm1004vdcCfgLineStartupThreshIndex": pm1004vdcCfgLineStartupThreshIndex,
       "pm1004vdcCfgLineThreshtxpowhighPortn": pm1004vdcCfgLineThreshtxpowhighPortn,
       "pm1004vdcCfgLineThreshtxpowlowPortn": pm1004vdcCfgLineThreshtxpowlowPortn,
       "pm1004vdcCfgLineThreshrxpowhighPortn": pm1004vdcCfgLineThreshrxpowhighPortn,
       "pm1004vdcCfgLineThreshrxpowlowPortn": pm1004vdcCfgLineThreshrxpowlowPortn,
       "pm1004vdcCfgStartuptlh": pm1004vdcCfgStartuptlh,
       "pm1004vdcCfgOtxtlhTable": pm1004vdcCfgOtxtlhTable,
       "pm1004vdcCfgOtxtlhEntry": pm1004vdcCfgOtxtlhEntry,
       "pm1004vdcCfgOtxtlhIndex": pm1004vdcCfgOtxtlhIndex,
       "pm1004vdcCfgNuPortn": pm1004vdcCfgNuPortn,
       "pm1004vdcCfgLineDitherRatePortn": pm1004vdcCfgLineDitherRatePortn,
       "pm1004vdcCfgLineDitherFhzPortn": pm1004vdcCfgLineDitherFhzPortn,
       "pm1004vdcCfgLinePwrLaserPortn": pm1004vdcCfgLinePwrLaserPortn,
       "pm1004vdcCfgLineFCurrentPortn": pm1004vdcCfgLineFCurrentPortn,
       "pm1004vdcCfgLineGridCurrentPortn": pm1004vdcCfgLineGridCurrentPortn,
       "pm1004vdcCfgFPortn": pm1004vdcCfgFPortn,
       "pm1004vdcCfgReservedPortn": pm1004vdcCfgReservedPortn,
       "pm1004vdcCfgLinePhotodiodeModePortn": pm1004vdcCfgLinePhotodiodeModePortn,
       "pm1004vdcCfgLinePhotodiodeValuePortn": pm1004vdcCfgLinePhotodiodeValuePortn,
       "pm1004vdcCfgStartupslotslineaddtx1": pm1004vdcCfgStartupslotslineaddtx1,
       "pm1004vdcCfgSlotslineaddtx1Table": pm1004vdcCfgSlotslineaddtx1Table,
       "pm1004vdcCfgSlotslineaddtx1Entry": pm1004vdcCfgSlotslineaddtx1Entry,
       "pm1004vdcCfgSlotslineaddtx1Index": pm1004vdcCfgSlotslineaddtx1Index,
       "pm1004vdcCfgLine1Addslotb2PortPortn": pm1004vdcCfgLine1Addslotb2PortPortn,
       "pm1004vdcCfgLine1Addslotb1PortPortn": pm1004vdcCfgLine1Addslotb1PortPortn,
       "pm1004vdcCfgLine1AddprotocolPortPortn": pm1004vdcCfgLine1AddprotocolPortPortn,
       "pm1004vdcCfgStartupslotslineaddtx2": pm1004vdcCfgStartupslotslineaddtx2,
       "pm1004vdcCfgSlotslineaddtx2Table": pm1004vdcCfgSlotslineaddtx2Table,
       "pm1004vdcCfgSlotslineaddtx2Entry": pm1004vdcCfgSlotslineaddtx2Entry,
       "pm1004vdcCfgSlotslineaddtx2Index": pm1004vdcCfgSlotslineaddtx2Index,
       "pm1004vdcCfgLine2Addslotb2PortPortn": pm1004vdcCfgLine2Addslotb2PortPortn,
       "pm1004vdcCfgLine2Addslotb1PortPortn": pm1004vdcCfgLine2Addslotb1PortPortn,
       "pm1004vdcCfgLine2AddprotocolPortPortn": pm1004vdcCfgLine2AddprotocolPortPortn,
       "pm1004vdcCfgStartupslotslinepassthroughtx1": pm1004vdcCfgStartupslotslinepassthroughtx1,
       "pm1004vdcCfgSlotslinepassthroughtx1Table": pm1004vdcCfgSlotslinepassthroughtx1Table,
       "pm1004vdcCfgSlotslinepassthroughtx1Entry": pm1004vdcCfgSlotslinepassthroughtx1Entry,
       "pm1004vdcCfgSlotslinepassthroughtx1Index": pm1004vdcCfgSlotslinepassthroughtx1Index,
       "pm1004vdcCfgLine1Slotb2PassthroughPortn": pm1004vdcCfgLine1Slotb2PassthroughPortn,
       "pm1004vdcCfgLine1Slotb1PassthroughPortn": pm1004vdcCfgLine1Slotb1PassthroughPortn,
       "pm1004vdcCfgLine1ProtocolPassthroughPortn": pm1004vdcCfgLine1ProtocolPassthroughPortn,
       "pm1004vdcCfgStartupslotslinepassthroughtx2": pm1004vdcCfgStartupslotslinepassthroughtx2,
       "pm1004vdcCfgSlotslinepassthroughtx2Table": pm1004vdcCfgSlotslinepassthroughtx2Table,
       "pm1004vdcCfgSlotslinepassthroughtx2Entry": pm1004vdcCfgSlotslinepassthroughtx2Entry,
       "pm1004vdcCfgSlotslinepassthroughtx2Index": pm1004vdcCfgSlotslinepassthroughtx2Index,
       "pm1004vdcCfgLine2Slotb2PassthroughPortn": pm1004vdcCfgLine2Slotb2PassthroughPortn,
       "pm1004vdcCfgLine2Slotb1PassthroughPortn": pm1004vdcCfgLine2Slotb1PassthroughPortn,
       "pm1004vdcCfgLine2ProtocolPassthroughPortn": pm1004vdcCfgLine2ProtocolPassthroughPortn,
       "pm1004vdcCfgStartupslotslinedroprx1": pm1004vdcCfgStartupslotslinedroprx1,
       "pm1004vdcCfgSlotslinedroprx1Table": pm1004vdcCfgSlotslinedroprx1Table,
       "pm1004vdcCfgSlotslinedroprx1Entry": pm1004vdcCfgSlotslinedroprx1Entry,
       "pm1004vdcCfgSlotslinedroprx1Index": pm1004vdcCfgSlotslinedroprx1Index,
       "pm1004vdcCfgLine1Dropslotb2PortPortn": pm1004vdcCfgLine1Dropslotb2PortPortn,
       "pm1004vdcCfgLine1Dropslotb1PortPortn": pm1004vdcCfgLine1Dropslotb1PortPortn,
       "pm1004vdcCfgLine1DropprotocolPortPortn": pm1004vdcCfgLine1DropprotocolPortPortn,
       "pm1004vdcCfgStartupslotslineaddrx2": pm1004vdcCfgStartupslotslineaddrx2,
       "pm1004vdcCfgSlotslinedroprx2Table": pm1004vdcCfgSlotslinedroprx2Table,
       "pm1004vdcCfgSlotslinedroprx2Entry": pm1004vdcCfgSlotslinedroprx2Entry,
       "pm1004vdcCfgSlotslinedroprx2Index": pm1004vdcCfgSlotslinedroprx2Index,
       "pm1004vdcCfgLine2Dropslotb2PortPortn": pm1004vdcCfgLine2Dropslotb2PortPortn,
       "pm1004vdcCfgLine2Dropslotb1PortPortn": pm1004vdcCfgLine2Dropslotb1PortPortn,
       "pm1004vdcCfgLine2DropprotocolPortPortn": pm1004vdcCfgLine2DropprotocolPortPortn,
       "pm1004vdcCfgOther": pm1004vdcCfgOther,
       "pm1004vdctablemoduleOther": pm1004vdctablemoduleOther,
       "pm1004vdcCfgmode": pm1004vdcCfgmode,
       "pm1004vdcCfgStartuptablefive": pm1004vdcCfgStartuptablefive,
       "pm1004vdcCfgOtxtlhcapabilitiesTable": pm1004vdcCfgOtxtlhcapabilitiesTable,
       "pm1004vdcCfgOtxtlhcapabilitiesEntry": pm1004vdcCfgOtxtlhcapabilitiesEntry,
       "pm1004vdcCfgOtxtlhcapabilitiesIndex": pm1004vdcCfgOtxtlhcapabilitiesIndex,
       "pm1004vdcCfgComponentTypePortn": pm1004vdcCfgComponentTypePortn,
       "pm1004vdcCfgMiscellaneousPortn": pm1004vdcCfgMiscellaneousPortn,
       "pm1004vdcCfgFirstChannelPortn": pm1004vdcCfgFirstChannelPortn,
       "pm1004vdcCfgLastChannelPortn": pm1004vdcCfgLastChannelPortn,
       "pm1004vdcCfgGridPortn": pm1004vdcCfgGridPortn,
       "pm1004vdcCfgWriteConfiguration": pm1004vdcCfgWriteConfiguration,
       "pm1004vdctraps": pm1004vdctraps,
       "pm1004vdctrapPortNumber": pm1004vdctrapPortNumber,
       "pm1004vdctrapLineNumber": pm1004vdctrapLineNumber,
       "pm1004vdctrapBoardNumber": pm1004vdctrapBoardNumber,
       "pm1004vdcLineTrapNotUrgentGoesOn": pm1004vdcLineTrapNotUrgentGoesOn,
       "pm1004vdcLineTrapNotUrgentGoesOff": pm1004vdcLineTrapNotUrgentGoesOff,
       "pm1004vdcLineTrapUrgentGoesOn": pm1004vdcLineTrapUrgentGoesOn,
       "pm1004vdcLineTrapUrgentGoesOff": pm1004vdcLineTrapUrgentGoesOff,
       "pm1004vdcLineTrapCritGoesOn": pm1004vdcLineTrapCritGoesOn,
       "pm1004vdcLineTrapCritGoesOff": pm1004vdcLineTrapCritGoesOff,
       "pm1004vdcClientTrapNotUrgentGoesOn": pm1004vdcClientTrapNotUrgentGoesOn,
       "pm1004vdcClientTrapNotUrgentGoesOff": pm1004vdcClientTrapNotUrgentGoesOff,
       "pm1004vdcClientTrapUrgentGoesOn": pm1004vdcClientTrapUrgentGoesOn,
       "pm1004vdcClientTrapUrgentGoesOff": pm1004vdcClientTrapUrgentGoesOff,
       "pm1004vdcClientTrapCritGoesOn": pm1004vdcClientTrapCritGoesOn,
       "pm1004vdcClientTrapCritGoesOff": pm1004vdcClientTrapCritGoesOff,
       "pm1004vdcPowerTrapUrgentGoesOn": pm1004vdcPowerTrapUrgentGoesOn,
       "pm1004vdcPowerTrapUrgentGoesOff": pm1004vdcPowerTrapUrgentGoesOff,
       "pm1004vdcMonitoring": pm1004vdcMonitoring,
       "pm1004vdcMonOther": pm1004vdcMonOther,
       "pm1004vdcMonRmon": pm1004vdcMonRmon,
       "pm1004vdcMonCountersReset": pm1004vdcMonCountersReset,
       "pm1004vdcMonCountersStop": pm1004vdcMonCountersStop,
       "pm1004vdcMonClient": pm1004vdcMonClient,
       "pm1004vdcMonClientRmonCounter": pm1004vdcMonClientRmonCounter,
       "pm1004vdcMonupRmonByteCntTable": pm1004vdcMonupRmonByteCntTable,
       "pm1004vdcMonupRmonByteCntEntry": pm1004vdcMonupRmonByteCntEntry,
       "pm1004vdcMonupRmonByteCntIndex": pm1004vdcMonupRmonByteCntIndex,
       "pm1004vdcMonupRmonByteCntValuePortn": pm1004vdcMonupRmonByteCntValuePortn,
       "pm1004vdcMonupRmonByteCntErrorPortn": pm1004vdcMonupRmonByteCntErrorPortn,
       "pm1004vdcMonupRmonByteCntOverloadPortn": pm1004vdcMonupRmonByteCntOverloadPortn,
       "pm1004vdcMonupRmonCrcErrorCntTable": pm1004vdcMonupRmonCrcErrorCntTable,
       "pm1004vdcMonupRmonCrcErrorCntEntry": pm1004vdcMonupRmonCrcErrorCntEntry,
       "pm1004vdcMonupRmonCrcErrorCntIndex": pm1004vdcMonupRmonCrcErrorCntIndex,
       "pm1004vdcMonupRmonCrcErrorCntValuePortn": pm1004vdcMonupRmonCrcErrorCntValuePortn,
       "pm1004vdcMonupRmonCrcErrorCntErrorPortn": pm1004vdcMonupRmonCrcErrorCntErrorPortn,
       "pm1004vdcMonupRmonCrcErrorCntOverloadPortn": pm1004vdcMonupRmonCrcErrorCntOverloadPortn,
       "pm1004vdcMonupRmonPacketsCntTable": pm1004vdcMonupRmonPacketsCntTable,
       "pm1004vdcMonupRmonPacketsCntEntry": pm1004vdcMonupRmonPacketsCntEntry,
       "pm1004vdcMonupRmonPacketsCntIndex": pm1004vdcMonupRmonPacketsCntIndex,
       "pm1004vdcMonupRmonPacketsCntValuePortn": pm1004vdcMonupRmonPacketsCntValuePortn,
       "pm1004vdcMonupRmonPacketsCntErrorPortn": pm1004vdcMonupRmonPacketsCntErrorPortn,
       "pm1004vdcMonupRmonPacketsCntOverloadPortn": pm1004vdcMonupRmonPacketsCntOverloadPortn,
       "pm1004vdcMonupRmonBroadcastCntTable": pm1004vdcMonupRmonBroadcastCntTable,
       "pm1004vdcMonupRmonBroadcastCntEntry": pm1004vdcMonupRmonBroadcastCntEntry,
       "pm1004vdcMonupRmonBroadcastCntIndex": pm1004vdcMonupRmonBroadcastCntIndex,
       "pm1004vdcMonupRmonBroadcastCntValuePortn": pm1004vdcMonupRmonBroadcastCntValuePortn,
       "pm1004vdcMonupRmonBroadcastCntErrorPortn": pm1004vdcMonupRmonBroadcastCntErrorPortn,
       "pm1004vdcMonupRmonBroadcastCntOverloadPortn": pm1004vdcMonupRmonBroadcastCntOverloadPortn,
       "pm1004vdcMonupRmonMulticastCntTable": pm1004vdcMonupRmonMulticastCntTable,
       "pm1004vdcMonupRmonMulticastCntEntry": pm1004vdcMonupRmonMulticastCntEntry,
       "pm1004vdcMonupRmonMulticastCntIndex": pm1004vdcMonupRmonMulticastCntIndex,
       "pm1004vdcMonupRmonMulticastCntValuePortn": pm1004vdcMonupRmonMulticastCntValuePortn,
       "pm1004vdcMonupRmonMulticastCntErrorPortn": pm1004vdcMonupRmonMulticastCntErrorPortn,
       "pm1004vdcMonupRmonMulticastCntOverloadPortn": pm1004vdcMonupRmonMulticastCntOverloadPortn,
       "pm1004vdcMonupLineRmonByteCntTable": pm1004vdcMonupLineRmonByteCntTable,
       "pm1004vdcMonupLineRmonByteCntEntry": pm1004vdcMonupLineRmonByteCntEntry,
       "pm1004vdcMonupLineRmonByteCntIndex": pm1004vdcMonupLineRmonByteCntIndex,
       "pm1004vdcMonupLineRmonByteCntValuePortn": pm1004vdcMonupLineRmonByteCntValuePortn,
       "pm1004vdcMonupLineRmonByteCntErrorPortn": pm1004vdcMonupLineRmonByteCntErrorPortn,
       "pm1004vdcMonupLineRmonByteCntOverloadPortn": pm1004vdcMonupLineRmonByteCntOverloadPortn,
       "pm1004vdcMonupLineRmonCrcErrorCntTable": pm1004vdcMonupLineRmonCrcErrorCntTable,
       "pm1004vdcMonupLineRmonCrcErrorCntEntry": pm1004vdcMonupLineRmonCrcErrorCntEntry,
       "pm1004vdcMonupLineRmonCrcErrorCntIndex": pm1004vdcMonupLineRmonCrcErrorCntIndex,
       "pm1004vdcMonupLineRmonCrcErrorCntValuePortn": pm1004vdcMonupLineRmonCrcErrorCntValuePortn,
       "pm1004vdcMonupLineRmonCrcErrorCntErrorPortn": pm1004vdcMonupLineRmonCrcErrorCntErrorPortn,
       "pm1004vdcMonupLineRmonCrcErrorCntOverloadPortn": pm1004vdcMonupLineRmonCrcErrorCntOverloadPortn,
       "pm1004vdcMonupLineRmonPacketsCntTable": pm1004vdcMonupLineRmonPacketsCntTable,
       "pm1004vdcMonupLineRmonPacketsCntEntry": pm1004vdcMonupLineRmonPacketsCntEntry,
       "pm1004vdcMonupLineRmonPacketsCntIndex": pm1004vdcMonupLineRmonPacketsCntIndex,
       "pm1004vdcMonupLineRmonPacketsCntValuePortn": pm1004vdcMonupLineRmonPacketsCntValuePortn,
       "pm1004vdcMonupLineRmonPacketsCntErrorPortn": pm1004vdcMonupLineRmonPacketsCntErrorPortn,
       "pm1004vdcMonupLineRmonPacketsCntOverloadPortn": pm1004vdcMonupLineRmonPacketsCntOverloadPortn,
       "pm1004vdcMonLine": pm1004vdcMonLine,
       "pm1004vdcMonLineRmonCounter": pm1004vdcMonLineRmonCounter}
)
