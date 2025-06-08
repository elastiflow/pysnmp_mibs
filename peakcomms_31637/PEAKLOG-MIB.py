# SNMP MIB module (PEAKLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKLOG-MIB.mib
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

(YesNoType,
 confStat) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "YesNoType",
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

peakLogModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11)
)
if mibBuilder.loadTexts:
    peakLogModule.setRevisions(
        ("2015-09-15 10:00",
         "2013-04-04 12:00",
         "2011-08-19 12:00",
         "2011-06-03 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LogEnumType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("powerOn", 1),
          ("ethernetUp", 2),
          ("autoSwitchOver", 3),
          ("manualSwitchOver", 4),
          ("logCleared", 5))
    )



# MIB Managed Objects in the order of their OIDs

_LogTrap_ObjectIdentity = ObjectIdentity
logTrap = _LogTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 0)
)
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 1)
)
if mibBuilder.loadTexts:
    logTable.setStatus("current")
_LogTableEntry_Object = MibTableRow
logTableEntry = _LogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 1, 1)
)
logTableEntry.setIndexNames(
    (0, "PEAKLOG-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logTableEntry.setStatus("current")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 1, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")
_LogModuleType_Type = OctetString
_LogModuleType_Object = MibTableColumn
logModuleType = _LogModuleType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 1, 1, 2),
    _LogModuleType_Type()
)
logModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logModuleType.setStatus("current")


class _LogModuleInstance_Type(Integer32):
    """Custom type logModuleInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_LogModuleInstance_Type.__name__ = "Integer32"
_LogModuleInstance_Object = MibTableColumn
logModuleInstance = _LogModuleInstance_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 1, 1, 3),
    _LogModuleInstance_Type()
)
logModuleInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logModuleInstance.setStatus("current")
_LogType_Type = LogEnumType
_LogType_Object = MibTableColumn
logType = _LogType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 1, 1, 4),
    _LogType_Type()
)
logType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logType.setStatus("current")
_LogExtra_Type = OctetString
_LogExtra_Object = MibTableColumn
logExtra = _LogExtra_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 1, 1, 5),
    _LogExtra_Type()
)
logExtra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExtra.setStatus("current")
_LogDateTimeStamp_Type = OctetString
_LogDateTimeStamp_Object = MibTableColumn
logDateTimeStamp = _LogDateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 1, 1, 6),
    _LogDateTimeStamp_Type()
)
logDateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDateTimeStamp.setStatus("current")


class _LogSNTPServerAddress_Type(OctetString):
    """Custom type logSNTPServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_LogSNTPServerAddress_Type.__name__ = "OctetString"
_LogSNTPServerAddress_Object = MibScalar
logSNTPServerAddress = _LogSNTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 2),
    _LogSNTPServerAddress_Type()
)
logSNTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logSNTPServerAddress.setStatus("current")
_LogCurrentDateTime_Type = OctetString
_LogCurrentDateTime_Object = MibScalar
logCurrentDateTime = _LogCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 3),
    _LogCurrentDateTime_Type()
)
logCurrentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentDateTime.setStatus("current")
_LogClear_Type = YesNoType
_LogClear_Object = MibScalar
logClear = _LogClear_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 4),
    _LogClear_Type()
)
logClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logClear.setStatus("current")
_LogConvGroups_ObjectIdentity = ObjectIdentity
logConvGroups = _LogConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 10)
)
_LogConvConformance_ObjectIdentity = ObjectIdentity
logConvConformance = _LogConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 11)
)

# Managed Objects groups

logCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 10, 1)
)
logCNFReqGrp.setObjects(
      *(("PEAKLOG-MIB", "logModuleType"),
        ("PEAKLOG-MIB", "logModuleInstance"),
        ("PEAKLOG-MIB", "logType"),
        ("PEAKLOG-MIB", "logExtra"),
        ("PEAKLOG-MIB", "logDateTimeStamp"),
        ("PEAKLOG-MIB", "logSNTPServerAddress"),
        ("PEAKLOG-MIB", "logCurrentDateTime"),
        ("PEAKLOG-MIB", "logClear"))
)
if mibBuilder.loadTexts:
    logCNFReqGrp.setStatus("current")


# Notification objects

generalLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 0, 5)
)
generalLogTrap.setObjects(
      *(("PEAKLOG-MIB", "logModuleType"),
        ("PEAKLOG-MIB", "logModuleInstance"),
        ("PEAKLOG-MIB", "logType"),
        ("PEAKLOG-MIB", "logExtra"),
        ("PEAKLOG-MIB", "logDateTimeStamp"))
)
if mibBuilder.loadTexts:
    generalLogTrap.setStatus(
        "current"
    )


# Notifications groups

logTrapNotifyGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 10, 2)
)
logTrapNotifyGrp.setObjects(
    ("PEAKLOG-MIB", "generalLogTrap")
)
if mibBuilder.loadTexts:
    logTrapNotifyGrp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

logCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 11, 11, 1)
)
logCNFCompliance.setObjects(
      *(("PEAKLOG-MIB", "logCNFReqGrp"),
        ("PEAKLOG-MIB", "logTrapNotifyGrp"))
)
if mibBuilder.loadTexts:
    logCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKLOG-MIB",
    **{"LogEnumType": LogEnumType,
       "peakLogModule": peakLogModule,
       "logTrap": logTrap,
       "generalLogTrap": generalLogTrap,
       "logTable": logTable,
       "logTableEntry": logTableEntry,
       "logIndex": logIndex,
       "logModuleType": logModuleType,
       "logModuleInstance": logModuleInstance,
       "logType": logType,
       "logExtra": logExtra,
       "logDateTimeStamp": logDateTimeStamp,
       "logSNTPServerAddress": logSNTPServerAddress,
       "logCurrentDateTime": logCurrentDateTime,
       "logClear": logClear,
       "logConvGroups": logConvGroups,
       "logCNFReqGrp": logCNFReqGrp,
       "logTrapNotifyGrp": logTrapNotifyGrp,
       "logConvConformance": logConvConformance,
       "logCNFCompliance": logCNFCompliance}
)
