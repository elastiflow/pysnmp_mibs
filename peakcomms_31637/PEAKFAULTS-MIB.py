# SNMP MIB module (PEAKFAULTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKFAULTS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(FaultType,
 confStat) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "FaultType",
    "confStat")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

peakFaultsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10)
)
if mibBuilder.loadTexts:
    peakFaultsModule.setRevisions(
        ("2016-09-15 09:00",
         "2016-08-22 09:00",
         "2016-08-11 09:00",
         "2016-05-12 09:00",
         "2015-09-15 09:00",
         "2015-04-21 12:00",
         "2014-09-12 12:00",
         "2014-07-29 12:00",
         "2014-01-10 12:00",
         "2013-09-30 12:00",
         "2013-07-12 12:00",
         "2013-04-25 12:00",
         "2013-04-04 12:00",
         "2012-12-17 12:00",
         "2012-10-29 12:00",
         "2012-01-06 12:00",
         "2011-12-20 12:00",
         "2011-11-29 12:00",
         "2011-08-19 12:00",
         "2011-07-11 09:00",
         "2011-06-08 09:00",
         "2011-04-11 09:00",
         "2011-03-04 09:00",
         "2010-11-16 09:00",
         "2010-11-10 09:00",
         "2010-05-27 09:00",
         "2010-04-30 09:00",
         "2010-04-09 09:00",
         "2008-12-03 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FaultsEnumType(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("primaryDCV", 0),
          ("p5V", 1),
          ("p15V", 2),
          ("m15V", 3),
          ("temperature", 4),
          ("humidity", 5),
          ("externalReference", 6),
          ("crystal", 7),
          ("coaxSwitch", 8),
          ("externalFault1", 9),
          ("externalFault2", 10),
          ("plo1", 11),
          ("plo2", 12),
          ("lo", 13),
          ("ethernet", 14),
          ("blockV", 15),
          ("p3V", 16),
          ("dcfeedV", 17),
          ("lo1", 18),
          ("lo2", 19),
          ("mhz815", 20),
          ("blockC", 21),
          ("shf", 22),
          ("externalAlarm", 23),
          ("psu1", 24),
          ("psu2", 25),
          ("unit1", 26),
          ("unit2", 27),
          ("unit1NotPresent", 28),
          ("unit2NotPresent", 29),
          ("lo3", 30),
          ("bandSwitch", 31),
          ("outOfLock", 32),
          ("clearSkyTooLow", 33),
          ("compRangeExcess", 34),
          ("missingExtChannel", 35),
          ("channelByPassFault", 36),
          ("alarm", 37),
          ("hiCurrent", 38),
          ("loCurrent", 39),
          ("waveGuideSwitch", 40),
          ("muteFault", 41),
          ("inputPower", 42),
          ("outputPower", 43),
          ("externalMute", 44),
          ("plo3", 45),
          ("inputHigh", 46),
          ("inputLow", 47),
          ("compression", 48),
          ("p12V", 49),
          ("channelCommunications", 50),
          ("channelPowerSupply", 51),
          ("channelBypass", 52),
          ("channelRF", 53),
          ("psuVoltage", 54),
          ("combinedDCV", 55),
          ("lo4", 56),
          ("bandCoax", 57),
          ("inputSwitch", 58),
          ("outputSwitch", 59),
          ("internalComms", 60),
          ("missing", 61),
          ("amplifier", 62),
          ("attenuator", 63),
          ("plo4", 64),
          ("coax1", 65),
          ("coax2", 66),
          ("amp1", 67),
          ("amp2", 68),
          ("if", 69),
          ("ifCompression", 70),
          ("coax3", 71),
          ("unitStandby", 72),
          ("missingExternalSwitch", 73),
          ("refenceSignalLoss", 74),
          ("lockDetect", 75))
    )



# MIB Managed Objects in the order of their OIDs

_FaultsTrap_ObjectIdentity = ObjectIdentity
faultsTrap = _FaultsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 0)
)
_SummaryFault_Type = FaultType
_SummaryFault_Object = MibScalar
summaryFault = _SummaryFault_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 1),
    _SummaryFault_Type()
)
summaryFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryFault.setStatus("current")
_FaultsTable_Object = MibTable
faultsTable = _FaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 2)
)
if mibBuilder.loadTexts:
    faultsTable.setStatus("current")
_FaultsTableEntry_Object = MibTableRow
faultsTableEntry = _FaultsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 2, 1)
)
faultsTableEntry.setIndexNames(
    (0, "PEAKFAULTS-MIB", "faultsIndex"),
)
if mibBuilder.loadTexts:
    faultsTableEntry.setStatus("current")


class _FaultsIndex_Type(Integer32):
    """Custom type faultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FaultsIndex_Type.__name__ = "Integer32"
_FaultsIndex_Object = MibTableColumn
faultsIndex = _FaultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 2, 1, 1),
    _FaultsIndex_Type()
)
faultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    faultsIndex.setStatus("current")
_FaultsModuleType_Type = OctetString
_FaultsModuleType_Object = MibTableColumn
faultsModuleType = _FaultsModuleType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 2, 1, 2),
    _FaultsModuleType_Type()
)
faultsModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultsModuleType.setStatus("current")


class _FaultsModuleInstance_Type(Integer32):
    """Custom type faultsModuleInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_FaultsModuleInstance_Type.__name__ = "Integer32"
_FaultsModuleInstance_Object = MibTableColumn
faultsModuleInstance = _FaultsModuleInstance_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 2, 1, 3),
    _FaultsModuleInstance_Type()
)
faultsModuleInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultsModuleInstance.setStatus("current")
_FaultsType_Type = FaultsEnumType
_FaultsType_Object = MibTableColumn
faultsType = _FaultsType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 2, 1, 4),
    _FaultsType_Type()
)
faultsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultsType.setStatus("current")
_FaultsConvGroups_ObjectIdentity = ObjectIdentity
faultsConvGroups = _FaultsConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 10)
)
_FaultsConvConformance_ObjectIdentity = ObjectIdentity
faultsConvConformance = _FaultsConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 11)
)

# Managed Objects groups

faultsCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 10, 1)
)
faultsCNFReqGrp.setObjects(
      *(("PEAKFAULTS-MIB", "summaryFault"),
        ("PEAKFAULTS-MIB", "faultsModuleType"),
        ("PEAKFAULTS-MIB", "faultsModuleInstance"),
        ("PEAKFAULTS-MIB", "faultsType"))
)
if mibBuilder.loadTexts:
    faultsCNFReqGrp.setStatus("current")


# Notification objects

generalFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 0, 5)
)
generalFaultTrap.setObjects(
      *(("PEAKFAULTS-MIB", "faultsModuleType"),
        ("PEAKFAULTS-MIB", "faultsModuleInstance"),
        ("PEAKFAULTS-MIB", "faultsType"))
)
if mibBuilder.loadTexts:
    generalFaultTrap.setStatus(
        "current"
    )


# Notifications groups

faultsTrapNotifyGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 10, 2)
)
faultsTrapNotifyGrp.setObjects(
    ("PEAKFAULTS-MIB", "generalFaultTrap")
)
if mibBuilder.loadTexts:
    faultsTrapNotifyGrp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

faultsCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 10, 11, 1)
)
faultsCNFCompliance.setObjects(
      *(("PEAKFAULTS-MIB", "faultsCNFReqGrp"),
        ("PEAKFAULTS-MIB", "faultsTrapNotifyGrp"))
)
if mibBuilder.loadTexts:
    faultsCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKFAULTS-MIB",
    **{"FaultsEnumType": FaultsEnumType,
       "peakFaultsModule": peakFaultsModule,
       "faultsTrap": faultsTrap,
       "generalFaultTrap": generalFaultTrap,
       "summaryFault": summaryFault,
       "faultsTable": faultsTable,
       "faultsTableEntry": faultsTableEntry,
       "faultsIndex": faultsIndex,
       "faultsModuleType": faultsModuleType,
       "faultsModuleInstance": faultsModuleInstance,
       "faultsType": faultsType,
       "faultsConvGroups": faultsConvGroups,
       "faultsCNFReqGrp": faultsCNFReqGrp,
       "faultsTrapNotifyGrp": faultsTrapNotifyGrp,
       "faultsConvConformance": faultsConvConformance,
       "faultsCNFCompliance": faultsCNFCompliance}
)
