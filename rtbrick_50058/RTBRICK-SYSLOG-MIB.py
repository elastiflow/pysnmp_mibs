# SNMP MIB module (RTBRICK-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/rtbrick_50058/RTBRICK-SYSLOG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:56:03 2025
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

(rtbrickModules,
 rtbrickSyslogNotifications,
 rtbrickTraps) = mibBuilder.importSymbols(
    "RTBRICK-MIB",
    "rtbrickModules",
    "rtbrickSyslogNotifications",
    "rtbrickTraps")

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

rtBrickSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2)
)
if mibBuilder.loadTexts:
    rtBrickSyslogMIB.setRevisions(
        ("2019-01-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )



# MIB Managed Objects in the order of their OIDs

_RtbrickSyslogNotificationPrefix_ObjectIdentity = ObjectIdentity
rtbrickSyslogNotificationPrefix = _RtbrickSyslogNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 103, 1, 0)
)
if mibBuilder.loadTexts:
    rtbrickSyslogNotificationPrefix.setStatus("current")
_SyslogMessage_ObjectIdentity = ObjectIdentity
syslogMessage = _SyslogMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1)
)
_SyslogMsgNumber_Type = Unsigned32
_SyslogMsgNumber_Object = MibScalar
syslogMsgNumber = _SyslogMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 1),
    _SyslogMsgNumber_Type()
)
syslogMsgNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgNumber.setStatus("current")
_SyslogMsgFacility_Type = DisplayString
_SyslogMsgFacility_Object = MibScalar
syslogMsgFacility = _SyslogMsgFacility_Object(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 2),
    _SyslogMsgFacility_Type()
)
syslogMsgFacility.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgFacility.setStatus("current")
_SyslogMsgSeverity_Type = SyslogSeverity
_SyslogMsgSeverity_Object = MibScalar
syslogMsgSeverity = _SyslogMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 3),
    _SyslogMsgSeverity_Type()
)
syslogMsgSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgSeverity.setStatus("current")
_SyslogMsgText_Type = DisplayString
_SyslogMsgText_Object = MibScalar
syslogMsgText = _SyslogMsgText_Object(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 4),
    _SyslogMsgText_Type()
)
syslogMsgText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgText.setStatus("current")

# Managed Objects groups


# Notification objects

rtbrickSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 50058, 103, 1, 0, 1)
)
if mibBuilder.loadTexts:
    rtbrickSyslogTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RTBRICK-SYSLOG-MIB",
    **{"SyslogSeverity": SyslogSeverity,
       "rtbrickSyslogNotificationPrefix": rtbrickSyslogNotificationPrefix,
       "rtbrickSyslogTrap": rtbrickSyslogTrap,
       "rtBrickSyslogMIB": rtBrickSyslogMIB,
       "syslogMessage": syslogMessage,
       "syslogMsgNumber": syslogMsgNumber,
       "syslogMsgFacility": syslogMsgFacility,
       "syslogMsgSeverity": syslogMsgSeverity,
       "syslogMsgText": syslogMsgText}
)
