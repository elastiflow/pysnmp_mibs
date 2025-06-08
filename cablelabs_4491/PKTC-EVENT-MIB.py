# SNMP MIB module (PKTC-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/PKTC-EVENT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:41:44 2025
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

(clabProjPacketCable,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjPacketCable")

(ifPhysAddress,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifPhysAddress")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

pktcEventMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcDevEventControl_ObjectIdentity = ObjectIdentity
pktcDevEventControl = _PktcDevEventControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 1)
)


class _PktcDevEvControl_Type(Bits):
    """Custom type pktcDevEvControl based on Bits"""
    namedValues = NamedValues(
        *(("resetEventLogTable", 0),
          ("resetEventDescrTable", 1))
    )

_PktcDevEvControl_Type.__name__ = "Bits"
_PktcDevEvControl_Object = MibScalar
pktcDevEvControl = _PktcDevEvControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 1, 1),
    _PktcDevEvControl_Type()
)
pktcDevEvControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEvControl.setStatus("current")
_PktcDevEvSyslogAddressType_Type = InetAddressType
_PktcDevEvSyslogAddressType_Object = MibScalar
pktcDevEvSyslogAddressType = _PktcDevEvSyslogAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 1, 2),
    _PktcDevEvSyslogAddressType_Type()
)
pktcDevEvSyslogAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEvSyslogAddressType.setStatus("current")
_PktcDevEvSyslogAddress_Type = InetAddress
_PktcDevEvSyslogAddress_Object = MibScalar
pktcDevEvSyslogAddress = _PktcDevEvSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 1, 3),
    _PktcDevEvSyslogAddress_Type()
)
pktcDevEvSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEvSyslogAddress.setStatus("current")


class _PktcDevEvSyslogUdpPort_Type(InetPortNumber):
    """Custom type pktcDevEvSyslogUdpPort based on InetPortNumber"""
    defaultValue = 514


_PktcDevEvSyslogUdpPort_Type.__name__ = "InetPortNumber"
_PktcDevEvSyslogUdpPort_Object = MibScalar
pktcDevEvSyslogUdpPort = _PktcDevEvSyslogUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 1, 4),
    _PktcDevEvSyslogUdpPort_Type()
)
pktcDevEvSyslogUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEvSyslogUdpPort.setStatus("current")
_PktcDevEventThrottle_ObjectIdentity = ObjectIdentity
pktcDevEventThrottle = _PktcDevEventThrottle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 2)
)


class _PktcDevEvThrottleAdminStatus_Type(Integer32):
    """Custom type pktcDevEvThrottleAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unconstrained", 1),
          ("maintainBelowThreshold", 2),
          ("stopAtThreshold", 3),
          ("inhibited", 4))
    )


_PktcDevEvThrottleAdminStatus_Type.__name__ = "Integer32"
_PktcDevEvThrottleAdminStatus_Object = MibScalar
pktcDevEvThrottleAdminStatus = _PktcDevEvThrottleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 2, 1),
    _PktcDevEvThrottleAdminStatus_Type()
)
pktcDevEvThrottleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEvThrottleAdminStatus.setStatus("current")


class _PktcDevEvThrottleThreshold_Type(Unsigned32):
    """Custom type pktcDevEvThrottleThreshold based on Unsigned32"""
    defaultValue = 2


_PktcDevEvThrottleThreshold_Type.__name__ = "Unsigned32"
_PktcDevEvThrottleThreshold_Object = MibScalar
pktcDevEvThrottleThreshold = _PktcDevEvThrottleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 2, 2),
    _PktcDevEvThrottleThreshold_Type()
)
pktcDevEvThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEvThrottleThreshold.setStatus("current")


class _PktcDevEvThrottleInterval_Type(Unsigned32):
    """Custom type pktcDevEvThrottleInterval based on Unsigned32"""
    defaultValue = 1


_PktcDevEvThrottleInterval_Type.__name__ = "Unsigned32"
_PktcDevEvThrottleInterval_Object = MibScalar
pktcDevEvThrottleInterval = _PktcDevEvThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 2, 3),
    _PktcDevEvThrottleInterval_Type()
)
pktcDevEvThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEvThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    pktcDevEvThrottleInterval.setUnits("seconds")
_PktcDevEventStatus_ObjectIdentity = ObjectIdentity
pktcDevEventStatus = _PktcDevEventStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 3)
)


class _PktcDevEvTransmissionStatus_Type(Bits):
    """Custom type pktcDevEvTransmissionStatus based on Bits"""
    namedValues = NamedValues(
        *(("syslogThrottled", 0),
          ("snmpThrottled", 1),
          ("validSyslogServerAbsent", 2),
          ("validSnmpManagerAbsent", 3),
          ("syslogTransmitError", 4),
          ("snmpTransmitError", 5))
    )

_PktcDevEvTransmissionStatus_Type.__name__ = "Bits"
_PktcDevEvTransmissionStatus_Object = MibScalar
pktcDevEvTransmissionStatus = _PktcDevEvTransmissionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 3, 1),
    _PktcDevEvTransmissionStatus_Type()
)
pktcDevEvTransmissionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvTransmissionStatus.setStatus("current")
_PktcDevEventDescr_ObjectIdentity = ObjectIdentity
pktcDevEventDescr = _PktcDevEventDescr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 4)
)
_PktcDevEventDescrTable_Object = MibTable
pktcDevEventDescrTable = _PktcDevEventDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    pktcDevEventDescrTable.setStatus("current")
_PktcDevEventDescrEntry_Object = MibTableRow
pktcDevEventDescrEntry = _PktcDevEventDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 4, 1, 1)
)
pktcDevEventDescrEntry.setIndexNames(
    (0, "PKTC-EVENT-MIB", "pktcDevEventDescrId"),
    (0, "PKTC-EVENT-MIB", "pktcDevEventDescrEnterprise"),
)
if mibBuilder.loadTexts:
    pktcDevEventDescrEntry.setStatus("current")
_PktcDevEventDescrId_Type = Unsigned32
_PktcDevEventDescrId_Object = MibTableColumn
pktcDevEventDescrId = _PktcDevEventDescrId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 4, 1, 1, 1),
    _PktcDevEventDescrId_Type()
)
pktcDevEventDescrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcDevEventDescrId.setStatus("current")
_PktcDevEventDescrEnterprise_Type = Unsigned32
_PktcDevEventDescrEnterprise_Object = MibTableColumn
pktcDevEventDescrEnterprise = _PktcDevEventDescrEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 4, 1, 1, 2),
    _PktcDevEventDescrEnterprise_Type()
)
pktcDevEventDescrEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEventDescrEnterprise.setStatus("current")


class _PktcDevEventDescrFacility_Type(Integer32):
    """Custom type pktcDevEventDescrFacility based on Integer32"""
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
              23)
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
          ("clockDaemon", 15),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )


_PktcDevEventDescrFacility_Type.__name__ = "Integer32"
_PktcDevEventDescrFacility_Object = MibTableColumn
pktcDevEventDescrFacility = _PktcDevEventDescrFacility_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 4, 1, 1, 3),
    _PktcDevEventDescrFacility_Type()
)
pktcDevEventDescrFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEventDescrFacility.setStatus("current")


class _PktcDevEventDescrLevel_Type(Integer32):
    """Custom type pktcDevEventDescrLevel based on Integer32"""
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
              7)
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
          ("debug", 7))
    )


_PktcDevEventDescrLevel_Type.__name__ = "Integer32"
_PktcDevEventDescrLevel_Object = MibTableColumn
pktcDevEventDescrLevel = _PktcDevEventDescrLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 4, 1, 1, 4),
    _PktcDevEventDescrLevel_Type()
)
pktcDevEventDescrLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEventDescrLevel.setStatus("current")


class _PktcDevEventDescrReporting_Type(Bits):
    """Custom type pktcDevEventDescrReporting based on Bits"""
    namedValues = NamedValues(
        *(("local", 0),
          ("syslog", 1),
          ("snmpTrap", 2),
          ("snmpInform", 3))
    )

_PktcDevEventDescrReporting_Type.__name__ = "Bits"
_PktcDevEventDescrReporting_Object = MibTableColumn
pktcDevEventDescrReporting = _PktcDevEventDescrReporting_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 4, 1, 1, 5),
    _PktcDevEventDescrReporting_Type()
)
pktcDevEventDescrReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEventDescrReporting.setStatus("current")


class _PktcDevEventDescrText_Type(SnmpAdminString):
    """Custom type pktcDevEventDescrText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PktcDevEventDescrText_Type.__name__ = "SnmpAdminString"
_PktcDevEventDescrText_Object = MibTableColumn
pktcDevEventDescrText = _PktcDevEventDescrText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 4, 1, 1, 6),
    _PktcDevEventDescrText_Type()
)
pktcDevEventDescrText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDevEventDescrText.setStatus("current")
_PktcDevEventLog_ObjectIdentity = ObjectIdentity
pktcDevEventLog = _PktcDevEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5)
)
_PktcDevEventLogTable_Object = MibTable
pktcDevEventLogTable = _PktcDevEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    pktcDevEventLogTable.setStatus("current")
_PktcDevEventLogEntry_Object = MibTableRow
pktcDevEventLogEntry = _PktcDevEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1)
)
pktcDevEventLogEntry.setIndexNames(
    (0, "PKTC-EVENT-MIB", "pktcDevEvLogIndex"),
)
if mibBuilder.loadTexts:
    pktcDevEventLogEntry.setStatus("current")
_PktcDevEvLogIndex_Type = Unsigned32
_PktcDevEvLogIndex_Object = MibTableColumn
pktcDevEvLogIndex = _PktcDevEvLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 1),
    _PktcDevEvLogIndex_Type()
)
pktcDevEvLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogIndex.setStatus("current")
_PktcDevEvLogTime_Type = DateAndTime
_PktcDevEvLogTime_Object = MibTableColumn
pktcDevEvLogTime = _PktcDevEvLogTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 2),
    _PktcDevEvLogTime_Type()
)
pktcDevEvLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogTime.setStatus("current")
_PktcDevEvLogEnterprise_Type = Unsigned32
_PktcDevEvLogEnterprise_Object = MibTableColumn
pktcDevEvLogEnterprise = _PktcDevEvLogEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 3),
    _PktcDevEvLogEnterprise_Type()
)
pktcDevEvLogEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogEnterprise.setStatus("current")
_PktcDevEvLogId_Type = Unsigned32
_PktcDevEvLogId_Object = MibTableColumn
pktcDevEvLogId = _PktcDevEvLogId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 4),
    _PktcDevEvLogId_Type()
)
pktcDevEvLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogId.setStatus("current")
_PktcDevEvLogText_Type = SnmpAdminString
_PktcDevEvLogText_Object = MibTableColumn
pktcDevEvLogText = _PktcDevEvLogText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 5),
    _PktcDevEvLogText_Type()
)
pktcDevEvLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogText.setStatus("current")
_PktcDevEvLogEndpointName_Type = SnmpAdminString
_PktcDevEvLogEndpointName_Object = MibTableColumn
pktcDevEvLogEndpointName = _PktcDevEvLogEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 6),
    _PktcDevEvLogEndpointName_Type()
)
pktcDevEvLogEndpointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogEndpointName.setStatus("current")


class _PktcDevEvLogType_Type(Bits):
    """Custom type pktcDevEvLogType based on Bits"""
    namedValues = NamedValues(
        *(("local", 0),
          ("syslog", 1),
          ("trap", 2),
          ("inform", 3))
    )

_PktcDevEvLogType_Type.__name__ = "Bits"
_PktcDevEvLogType_Object = MibTableColumn
pktcDevEvLogType = _PktcDevEvLogType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 7),
    _PktcDevEvLogType_Type()
)
pktcDevEvLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogType.setStatus("current")
_PktcDevEvLogTargetInfo_Type = SnmpAdminString
_PktcDevEvLogTargetInfo_Object = MibTableColumn
pktcDevEvLogTargetInfo = _PktcDevEvLogTargetInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 8),
    _PktcDevEvLogTargetInfo_Type()
)
pktcDevEvLogTargetInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogTargetInfo.setStatus("current")
_PktcDevEvLogCorrelationId_Type = Unsigned32
_PktcDevEvLogCorrelationId_Object = MibTableColumn
pktcDevEvLogCorrelationId = _PktcDevEvLogCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 9),
    _PktcDevEvLogCorrelationId_Type()
)
pktcDevEvLogCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogCorrelationId.setStatus("current")
_PktcDevEvLogAdditionalInfo_Type = SnmpAdminString
_PktcDevEvLogAdditionalInfo_Object = MibTableColumn
pktcDevEvLogAdditionalInfo = _PktcDevEvLogAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 5, 1, 1, 10),
    _PktcDevEvLogAdditionalInfo_Type()
)
pktcDevEvLogAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDevEvLogAdditionalInfo.setStatus("current")
_PktcDevEvNotification_ObjectIdentity = ObjectIdentity
pktcDevEvNotification = _PktcDevEvNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 6)
)
_PktcDevEvNotificationIndex_ObjectIdentity = ObjectIdentity
pktcDevEvNotificationIndex = _PktcDevEvNotificationIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 6, 0)
)
_PktcEventConformance_ObjectIdentity = ObjectIdentity
pktcEventConformance = _PktcEventConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 7)
)
_PktcEventCompliances_ObjectIdentity = ObjectIdentity
pktcEventCompliances = _PktcEventCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 7, 1)
)
_PktcEventGroups_ObjectIdentity = ObjectIdentity
pktcEventGroups = _PktcEventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 7, 2)
)

# Managed Objects groups

pktcEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 7, 2, 1)
)
pktcEventGroup.setObjects(
      *(("PKTC-EVENT-MIB", "pktcDevEvControl"),
        ("PKTC-EVENT-MIB", "pktcDevEvSyslogAddressType"),
        ("PKTC-EVENT-MIB", "pktcDevEvSyslogAddress"),
        ("PKTC-EVENT-MIB", "pktcDevEvSyslogUdpPort"),
        ("PKTC-EVENT-MIB", "pktcDevEvThrottleAdminStatus"),
        ("PKTC-EVENT-MIB", "pktcDevEvThrottleThreshold"),
        ("PKTC-EVENT-MIB", "pktcDevEvThrottleInterval"),
        ("PKTC-EVENT-MIB", "pktcDevEvTransmissionStatus"),
        ("PKTC-EVENT-MIB", "pktcDevEventDescrEnterprise"),
        ("PKTC-EVENT-MIB", "pktcDevEventDescrFacility"),
        ("PKTC-EVENT-MIB", "pktcDevEventDescrLevel"),
        ("PKTC-EVENT-MIB", "pktcDevEventDescrReporting"),
        ("PKTC-EVENT-MIB", "pktcDevEventDescrText"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogIndex"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogTime"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogEnterprise"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogId"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogText"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogEndpointName"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogType"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogTargetInfo"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogCorrelationId"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogAdditionalInfo"))
)
if mibBuilder.loadTexts:
    pktcEventGroup.setStatus("current")


# Notification objects

pktcDevEvInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 6, 0, 1)
)
pktcDevEvInform.setObjects(
      *(("PKTC-EVENT-MIB", "pktcDevEvLogIndex"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogTime"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogEnterprise"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogId"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogEndpointName"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogCorrelationId"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    pktcDevEvInform.setStatus(
        "current"
    )

pktcDevEvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 6, 0, 2)
)
pktcDevEvTrap.setObjects(
      *(("PKTC-EVENT-MIB", "pktcDevEvLogIndex"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogTime"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogEnterprise"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogId"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogEndpointName"),
        ("PKTC-EVENT-MIB", "pktcDevEvLogCorrelationId"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    pktcDevEvTrap.setStatus(
        "current"
    )


# Notifications groups

pktcEventNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 7, 2, 2)
)
pktcEventNotificationGroup.setObjects(
      *(("PKTC-EVENT-MIB", "pktcDevEvInform"),
        ("PKTC-EVENT-MIB", "pktcDevEvTrap"))
)
if mibBuilder.loadTexts:
    pktcEventNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pktcEventBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 3, 7, 1, 3)
)
pktcEventBasicCompliance.setObjects(
      *(("PKTC-EVENT-MIB", "pktcEventGroup"),
        ("PKTC-EVENT-MIB", "pktcEventNotificationGroup"))
)
if mibBuilder.loadTexts:
    pktcEventBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-EVENT-MIB",
    **{"pktcEventMib": pktcEventMib,
       "pktcDevEventControl": pktcDevEventControl,
       "pktcDevEvControl": pktcDevEvControl,
       "pktcDevEvSyslogAddressType": pktcDevEvSyslogAddressType,
       "pktcDevEvSyslogAddress": pktcDevEvSyslogAddress,
       "pktcDevEvSyslogUdpPort": pktcDevEvSyslogUdpPort,
       "pktcDevEventThrottle": pktcDevEventThrottle,
       "pktcDevEvThrottleAdminStatus": pktcDevEvThrottleAdminStatus,
       "pktcDevEvThrottleThreshold": pktcDevEvThrottleThreshold,
       "pktcDevEvThrottleInterval": pktcDevEvThrottleInterval,
       "pktcDevEventStatus": pktcDevEventStatus,
       "pktcDevEvTransmissionStatus": pktcDevEvTransmissionStatus,
       "pktcDevEventDescr": pktcDevEventDescr,
       "pktcDevEventDescrTable": pktcDevEventDescrTable,
       "pktcDevEventDescrEntry": pktcDevEventDescrEntry,
       "pktcDevEventDescrId": pktcDevEventDescrId,
       "pktcDevEventDescrEnterprise": pktcDevEventDescrEnterprise,
       "pktcDevEventDescrFacility": pktcDevEventDescrFacility,
       "pktcDevEventDescrLevel": pktcDevEventDescrLevel,
       "pktcDevEventDescrReporting": pktcDevEventDescrReporting,
       "pktcDevEventDescrText": pktcDevEventDescrText,
       "pktcDevEventLog": pktcDevEventLog,
       "pktcDevEventLogTable": pktcDevEventLogTable,
       "pktcDevEventLogEntry": pktcDevEventLogEntry,
       "pktcDevEvLogIndex": pktcDevEvLogIndex,
       "pktcDevEvLogTime": pktcDevEvLogTime,
       "pktcDevEvLogEnterprise": pktcDevEvLogEnterprise,
       "pktcDevEvLogId": pktcDevEvLogId,
       "pktcDevEvLogText": pktcDevEvLogText,
       "pktcDevEvLogEndpointName": pktcDevEvLogEndpointName,
       "pktcDevEvLogType": pktcDevEvLogType,
       "pktcDevEvLogTargetInfo": pktcDevEvLogTargetInfo,
       "pktcDevEvLogCorrelationId": pktcDevEvLogCorrelationId,
       "pktcDevEvLogAdditionalInfo": pktcDevEvLogAdditionalInfo,
       "pktcDevEvNotification": pktcDevEvNotification,
       "pktcDevEvNotificationIndex": pktcDevEvNotificationIndex,
       "pktcDevEvInform": pktcDevEvInform,
       "pktcDevEvTrap": pktcDevEvTrap,
       "pktcEventConformance": pktcEventConformance,
       "pktcEventCompliances": pktcEventCompliances,
       "pktcEventBasicCompliance": pktcEventBasicCompliance,
       "pktcEventGroups": pktcEventGroups,
       "pktcEventGroup": pktcEventGroup,
       "pktcEventNotificationGroup": pktcEventNotificationGroup}
)
