# SNMP MIB module (ZYXEL-ACCESS-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ACCESS-CONTROL-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:30:51 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelAccessControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelAccessControlSetup_ObjectIdentity = ObjectIdentity
zyxelAccessControlSetup = _ZyxelAccessControlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1)
)
_ZyxelAccessControlTable_Object = MibTable
zyxelAccessControlTable = _ZyxelAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelAccessControlTable.setStatus("current")
_ZyxelAccessControlEntry_Object = MibTableRow
zyxelAccessControlEntry = _ZyxelAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1)
)
zyxelAccessControlEntry.setIndexNames(
    (0, "ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlService"),
)
if mibBuilder.loadTexts:
    zyxelAccessControlEntry.setStatus("current")


class _ZyAccessControlService_Type(Integer32):
    """Custom type zyAccessControlService based on Integer32"""
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
        *(("telnet", 1),
          ("ssh", 2),
          ("ftp", 3),
          ("http", 4),
          ("https", 5),
          ("icmp", 6),
          ("snmp", 7),
          ("console", 8))
    )


_ZyAccessControlService_Type.__name__ = "Integer32"
_ZyAccessControlService_Object = MibTableColumn
zyAccessControlService = _ZyAccessControlService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1, 1),
    _ZyAccessControlService_Type()
)
zyAccessControlService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAccessControlService.setStatus("current")
_ZyAccessControlState_Type = EnabledStatus
_ZyAccessControlState_Object = MibTableColumn
zyAccessControlState = _ZyAccessControlState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1, 2),
    _ZyAccessControlState_Type()
)
zyAccessControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAccessControlState.setStatus("current")
_ZyAccessControlServicePort_Type = Integer32
_ZyAccessControlServicePort_Object = MibTableColumn
zyAccessControlServicePort = _ZyAccessControlServicePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1, 3),
    _ZyAccessControlServicePort_Type()
)
zyAccessControlServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAccessControlServicePort.setStatus("current")
_ZyAccessControlTimeout_Type = Integer32
_ZyAccessControlTimeout_Object = MibTableColumn
zyAccessControlTimeout = _ZyAccessControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1, 4),
    _ZyAccessControlTimeout_Type()
)
zyAccessControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAccessControlTimeout.setStatus("current")
_ZyAccessControlLoginTimeout_Type = Integer32
_ZyAccessControlLoginTimeout_Object = MibTableColumn
zyAccessControlLoginTimeout = _ZyAccessControlLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1, 5),
    _ZyAccessControlLoginTimeout_Type()
)
zyAccessControlLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAccessControlLoginTimeout.setStatus("current")
_ZyxelSecuredClientTable_Object = MibTable
zyxelSecuredClientTable = _ZyxelSecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelSecuredClientTable.setStatus("current")
_ZyxelSecuredClientEntry_Object = MibTableRow
zyxelSecuredClientEntry = _ZyxelSecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1)
)
zyxelSecuredClientEntry.setIndexNames(
    (0, "ZYXEL-ACCESS-CONTROL-MIB", "zySecuredClientIndex"),
)
if mibBuilder.loadTexts:
    zyxelSecuredClientEntry.setStatus("current")
_ZySecuredClientIndex_Type = Integer32
_ZySecuredClientIndex_Object = MibTableColumn
zySecuredClientIndex = _ZySecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 1),
    _ZySecuredClientIndex_Type()
)
zySecuredClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySecuredClientIndex.setStatus("current")
_ZySecuredClientState_Type = EnabledStatus
_ZySecuredClientState_Object = MibTableColumn
zySecuredClientState = _ZySecuredClientState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 2),
    _ZySecuredClientState_Type()
)
zySecuredClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySecuredClientState.setStatus("current")
_ZySecuredClientStartIpAddress_Type = IpAddress
_ZySecuredClientStartIpAddress_Object = MibTableColumn
zySecuredClientStartIpAddress = _ZySecuredClientStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 3),
    _ZySecuredClientStartIpAddress_Type()
)
zySecuredClientStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySecuredClientStartIpAddress.setStatus("current")
_ZySecuredClientEndIpAddress_Type = IpAddress
_ZySecuredClientEndIpAddress_Object = MibTableColumn
zySecuredClientEndIpAddress = _ZySecuredClientEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 4),
    _ZySecuredClientEndIpAddress_Type()
)
zySecuredClientEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySecuredClientEndIpAddress.setStatus("current")


class _ZySecuredClientService_Type(Bits):
    """Custom type zySecuredClientService based on Bits"""
    namedValues = NamedValues(
        *(("telnet", 0),
          ("ftp", 1),
          ("http", 2),
          ("icmp", 3),
          ("snmp", 4),
          ("ssh", 5),
          ("https", 6))
    )

_ZySecuredClientService_Type.__name__ = "Bits"
_ZySecuredClientService_Object = MibTableColumn
zySecuredClientService = _ZySecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 5),
    _ZySecuredClientService_Type()
)
zySecuredClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySecuredClientService.setStatus("current")
_ZyxelAccessControlTrapInfoObject_ObjectIdentity = ObjectIdentity
zyxelAccessControlTrapInfoObject = _ZyxelAccessControlTrapInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 3)
)


class _ZyAccessControlLoginService_Type(Integer32):
    """Custom type zyAccessControlLoginService based on Integer32"""
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
        *(("console", 0),
          ("telnet", 1),
          ("ssh", 2),
          ("ftp", 3),
          ("http", 4),
          ("https", 5))
    )


_ZyAccessControlLoginService_Type.__name__ = "Integer32"
_ZyAccessControlLoginService_Object = MibScalar
zyAccessControlLoginService = _ZyAccessControlLoginService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 3, 1),
    _ZyAccessControlLoginService_Type()
)
zyAccessControlLoginService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAccessControlLoginService.setStatus("current")
_ZyAccessControlLoginUsername_Type = DisplayString
_ZyAccessControlLoginUsername_Object = MibScalar
zyAccessControlLoginUsername = _ZyAccessControlLoginUsername_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 3, 2),
    _ZyAccessControlLoginUsername_Type()
)
zyAccessControlLoginUsername.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAccessControlLoginUsername.setStatus("current")
_ZyAccessControlLoginIpAddress_Type = DisplayString
_ZyAccessControlLoginIpAddress_Object = MibScalar
zyAccessControlLoginIpAddress = _ZyAccessControlLoginIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 3, 3),
    _ZyAccessControlLoginIpAddress_Type()
)
zyAccessControlLoginIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAccessControlLoginIpAddress.setStatus("current")
_ZyxelAccessControlNotifications_ObjectIdentity = ObjectIdentity
zyxelAccessControlNotifications = _ZyxelAccessControlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 4)
)

# Managed Objects groups


# Notification objects

zyAccessControlLoginRecord = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 4, 1)
)
zyAccessControlLoginRecord.setObjects(
      *(("ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlLoginService"),
        ("ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlLoginUsername"),
        ("ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlLoginIpAddress"))
)
if mibBuilder.loadTexts:
    zyAccessControlLoginRecord.setStatus(
        "current"
    )

zyAccessControlLogoutRecord = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 4, 2)
)
zyAccessControlLogoutRecord.setObjects(
      *(("ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlLoginService"),
        ("ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlLoginUsername"),
        ("ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlLoginIpAddress"))
)
if mibBuilder.loadTexts:
    zyAccessControlLogoutRecord.setStatus(
        "current"
    )

zyAccessControlLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 4, 3)
)
zyAccessControlLoginFail.setObjects(
      *(("ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlLoginService"),
        ("ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlLoginUsername"),
        ("ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlLoginIpAddress"))
)
if mibBuilder.loadTexts:
    zyAccessControlLoginFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ACCESS-CONTROL-MIB",
    **{"zyxelAccessControl": zyxelAccessControl,
       "zyxelAccessControlSetup": zyxelAccessControlSetup,
       "zyxelAccessControlTable": zyxelAccessControlTable,
       "zyxelAccessControlEntry": zyxelAccessControlEntry,
       "zyAccessControlService": zyAccessControlService,
       "zyAccessControlState": zyAccessControlState,
       "zyAccessControlServicePort": zyAccessControlServicePort,
       "zyAccessControlTimeout": zyAccessControlTimeout,
       "zyAccessControlLoginTimeout": zyAccessControlLoginTimeout,
       "zyxelSecuredClientTable": zyxelSecuredClientTable,
       "zyxelSecuredClientEntry": zyxelSecuredClientEntry,
       "zySecuredClientIndex": zySecuredClientIndex,
       "zySecuredClientState": zySecuredClientState,
       "zySecuredClientStartIpAddress": zySecuredClientStartIpAddress,
       "zySecuredClientEndIpAddress": zySecuredClientEndIpAddress,
       "zySecuredClientService": zySecuredClientService,
       "zyxelAccessControlTrapInfoObject": zyxelAccessControlTrapInfoObject,
       "zyAccessControlLoginService": zyAccessControlLoginService,
       "zyAccessControlLoginUsername": zyAccessControlLoginUsername,
       "zyAccessControlLoginIpAddress": zyAccessControlLoginIpAddress,
       "zyxelAccessControlNotifications": zyxelAccessControlNotifications,
       "zyAccessControlLoginRecord": zyAccessControlLoginRecord,
       "zyAccessControlLogoutRecord": zyAccessControlLogoutRecord,
       "zyAccessControlLoginFail": zyAccessControlLoginFail}
)
