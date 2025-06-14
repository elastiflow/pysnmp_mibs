# SNMP MIB module (WWP-SYSLOG-COLLECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wwp_6141/WWP-SYSLOG-COLLECTOR-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:31:32 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpSyslogCollectorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46)
)
if mibBuilder.loadTexts:
    wwpSyslogCollectorMIB.setRevisions(
        ("2003-01-21 10:12",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogFacility(TextualConvention, Integer32):
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              99)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 0),
          ("user", 1),
          ("mail", 2),
          ("daemon", 3),
          ("auth", 4),
          ("syslog", 5),
          ("lpr", 6),
          ("news", 7),
          ("uucp", 8),
          ("cron", 9),
          ("authPriv", 10),
          ("ftp", 11),
          ("ntp", 12),
          ("security", 13),
          ("console", 14),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("noMap", 99))
    )



class SyslogSeverity(TextualConvention, Integer32):
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7),
          ("other", 99))
    )



# MIB Managed Objects in the order of their OIDs

_WwpSyslogCollMIBObjects_ObjectIdentity = ObjectIdentity
wwpSyslogCollMIBObjects = _WwpSyslogCollMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1)
)
_WwpSyslogSystem_ObjectIdentity = ObjectIdentity
wwpSyslogSystem = _WwpSyslogSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 1)
)


class _WwpSyslogEnable_Type(TruthValue):
    """Custom type wwpSyslogEnable based on TruthValue"""
    defaultValue = 1


_WwpSyslogEnable_Type.__name__ = "TruthValue"
_WwpSyslogEnable_Object = MibScalar
wwpSyslogEnable = _WwpSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 1, 1),
    _WwpSyslogEnable_Type()
)
wwpSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSyslogEnable.setStatus("current")
_WwpSyslogColl_ObjectIdentity = ObjectIdentity
wwpSyslogColl = _WwpSyslogColl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2)
)
_WwpSyslogCollectorTable_Object = MibTable
wwpSyslogCollectorTable = _WwpSyslogCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpSyslogCollectorTable.setStatus("current")
_WwpSyslogCollectorEntry_Object = MibTableRow
wwpSyslogCollectorEntry = _WwpSyslogCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1)
)
wwpSyslogCollectorEntry.setIndexNames(
    (0, "WWP-SYSLOG-COLLECTOR-MIB", "wwpSyslogCollectorAddr"),
)
if mibBuilder.loadTexts:
    wwpSyslogCollectorEntry.setStatus("current")
_WwpSyslogCollectorAddr_Type = IpAddress
_WwpSyslogCollectorAddr_Object = MibTableColumn
wwpSyslogCollectorAddr = _WwpSyslogCollectorAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 1),
    _WwpSyslogCollectorAddr_Type()
)
wwpSyslogCollectorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpSyslogCollectorAddr.setStatus("current")


class _WwpSyslogCollectorUDPPort_Type(Integer32):
    """Custom type wwpSyslogCollectorUDPPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpSyslogCollectorUDPPort_Type.__name__ = "Integer32"
_WwpSyslogCollectorUDPPort_Object = MibTableColumn
wwpSyslogCollectorUDPPort = _WwpSyslogCollectorUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 2),
    _WwpSyslogCollectorUDPPort_Type()
)
wwpSyslogCollectorUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpSyslogCollectorUDPPort.setStatus("current")


class _WwpSyslogCollectorFacility_Type(SyslogFacility):
    """Custom type wwpSyslogCollectorFacility based on SyslogFacility"""
    defaultValue = 3


_WwpSyslogCollectorFacility_Type.__name__ = "SyslogFacility"
_WwpSyslogCollectorFacility_Object = MibTableColumn
wwpSyslogCollectorFacility = _WwpSyslogCollectorFacility_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 3),
    _WwpSyslogCollectorFacility_Type()
)
wwpSyslogCollectorFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpSyslogCollectorFacility.setStatus("current")


class _WwpSyslogCollectorMinSeverity_Type(SyslogSeverity):
    """Custom type wwpSyslogCollectorMinSeverity based on SyslogSeverity"""
    defaultValue = 3


_WwpSyslogCollectorMinSeverity_Type.__name__ = "SyslogSeverity"
_WwpSyslogCollectorMinSeverity_Object = MibTableColumn
wwpSyslogCollectorMinSeverity = _WwpSyslogCollectorMinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 4),
    _WwpSyslogCollectorMinSeverity_Type()
)
wwpSyslogCollectorMinSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpSyslogCollectorMinSeverity.setStatus("current")


class _WwpSyslogCollectorMaxSeverity_Type(SyslogSeverity):
    """Custom type wwpSyslogCollectorMaxSeverity based on SyslogSeverity"""
    defaultValue = 0


_WwpSyslogCollectorMaxSeverity_Type.__name__ = "SyslogSeverity"
_WwpSyslogCollectorMaxSeverity_Object = MibTableColumn
wwpSyslogCollectorMaxSeverity = _WwpSyslogCollectorMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 5),
    _WwpSyslogCollectorMaxSeverity_Type()
)
wwpSyslogCollectorMaxSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpSyslogCollectorMaxSeverity.setStatus("current")
_WwpSyslogCollectorStatus_Type = RowStatus
_WwpSyslogCollectorStatus_Object = MibTableColumn
wwpSyslogCollectorStatus = _WwpSyslogCollectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 6),
    _WwpSyslogCollectorStatus_Type()
)
wwpSyslogCollectorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpSyslogCollectorStatus.setStatus("current")
_WwpSyslogCollMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpSyslogCollMIBNotificationPrefix = _WwpSyslogCollMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 2)
)
_WwpSyslogCollMIBNotifications_ObjectIdentity = ObjectIdentity
wwpSyslogCollMIBNotifications = _WwpSyslogCollMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 2, 0)
)
_WwpSyslogCollMIBConformance_ObjectIdentity = ObjectIdentity
wwpSyslogCollMIBConformance = _WwpSyslogCollMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 3)
)
_WwpSyslogCollMIBCompliances_ObjectIdentity = ObjectIdentity
wwpSyslogCollMIBCompliances = _WwpSyslogCollMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 3, 1)
)
_WwpSyslogCollMIBGroups_ObjectIdentity = ObjectIdentity
wwpSyslogCollMIBGroups = _WwpSyslogCollMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 46, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-SYSLOG-COLLECTOR-MIB",
    **{"SyslogFacility": SyslogFacility,
       "SyslogSeverity": SyslogSeverity,
       "wwpSyslogCollectorMIB": wwpSyslogCollectorMIB,
       "wwpSyslogCollMIBObjects": wwpSyslogCollMIBObjects,
       "wwpSyslogSystem": wwpSyslogSystem,
       "wwpSyslogEnable": wwpSyslogEnable,
       "wwpSyslogColl": wwpSyslogColl,
       "wwpSyslogCollectorTable": wwpSyslogCollectorTable,
       "wwpSyslogCollectorEntry": wwpSyslogCollectorEntry,
       "wwpSyslogCollectorAddr": wwpSyslogCollectorAddr,
       "wwpSyslogCollectorUDPPort": wwpSyslogCollectorUDPPort,
       "wwpSyslogCollectorFacility": wwpSyslogCollectorFacility,
       "wwpSyslogCollectorMinSeverity": wwpSyslogCollectorMinSeverity,
       "wwpSyslogCollectorMaxSeverity": wwpSyslogCollectorMaxSeverity,
       "wwpSyslogCollectorStatus": wwpSyslogCollectorStatus,
       "wwpSyslogCollMIBNotificationPrefix": wwpSyslogCollMIBNotificationPrefix,
       "wwpSyslogCollMIBNotifications": wwpSyslogCollMIBNotifications,
       "wwpSyslogCollMIBConformance": wwpSyslogCollMIBConformance,
       "wwpSyslogCollMIBCompliances": wwpSyslogCollMIBCompliances,
       "wwpSyslogCollMIBGroups": wwpSyslogCollMIBGroups}
)
