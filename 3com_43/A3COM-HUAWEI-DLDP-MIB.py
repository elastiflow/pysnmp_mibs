# SNMP MIB module (A3COM-HUAWEI-DLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-DLDP-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:56 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cDldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43)
)
if mibBuilder.loadTexts:
    h3cDldp.setRevisions(
        ("2004-12-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class DLDPStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("inactive", 2),
          ("active", 3),
          ("advertisement", 4),
          ("probe", 5),
          ("disable", 6))
    )



class DLDPNeighborStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unidirection", 1),
          ("bidirection", 2),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_H3cDLDPMibObject_ObjectIdentity = ObjectIdentity
h3cDLDPMibObject = _H3cDLDPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1)
)
_H3cDLDPConfigGroup_ObjectIdentity = ObjectIdentity
h3cDLDPConfigGroup = _H3cDLDPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 1)
)


class _H3cDLDPWorkMode_Type(Integer32):
    """Custom type h3cDLDPWorkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("enhance", 2))
    )


_H3cDLDPWorkMode_Type.__name__ = "Integer32"
_H3cDLDPWorkMode_Object = MibScalar
h3cDLDPWorkMode = _H3cDLDPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 1, 1),
    _H3cDLDPWorkMode_Type()
)
h3cDLDPWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDLDPWorkMode.setStatus("current")
_H3cDLDPSystemEnable_Type = TruthValue
_H3cDLDPSystemEnable_Object = MibScalar
h3cDLDPSystemEnable = _H3cDLDPSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 1, 2),
    _H3cDLDPSystemEnable_Type()
)
h3cDLDPSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDLDPSystemEnable.setStatus("current")
_H3cDLDPSystemReset_Type = TruthValue
_H3cDLDPSystemReset_Object = MibScalar
h3cDLDPSystemReset = _H3cDLDPSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 1, 3),
    _H3cDLDPSystemReset_Type()
)
h3cDLDPSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDLDPSystemReset.setStatus("current")


class _H3cDLDPInterval_Type(Integer32):
    """Custom type h3cDLDPInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cDLDPInterval_Type.__name__ = "Integer32"
_H3cDLDPInterval_Object = MibScalar
h3cDLDPInterval = _H3cDLDPInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 1, 4),
    _H3cDLDPInterval_Type()
)
h3cDLDPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDLDPInterval.setStatus("current")


class _H3cDLDPAuthenticationMode_Type(Integer32):
    """Custom type h3cDLDPAuthenticationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple", 2),
          ("md5", 3))
    )


_H3cDLDPAuthenticationMode_Type.__name__ = "Integer32"
_H3cDLDPAuthenticationMode_Object = MibScalar
h3cDLDPAuthenticationMode = _H3cDLDPAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 1, 5),
    _H3cDLDPAuthenticationMode_Type()
)
h3cDLDPAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDLDPAuthenticationMode.setStatus("current")


class _H3cDLDPAuthenticationPassword_Type(OctetString):
    """Custom type h3cDLDPAuthenticationPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 53),
    )


_H3cDLDPAuthenticationPassword_Type.__name__ = "OctetString"
_H3cDLDPAuthenticationPassword_Object = MibScalar
h3cDLDPAuthenticationPassword = _H3cDLDPAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 1, 6),
    _H3cDLDPAuthenticationPassword_Type()
)
h3cDLDPAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDLDPAuthenticationPassword.setStatus("current")


class _H3cDLDPUnidirectionalShutdown_Type(Integer32):
    """Custom type h3cDLDPUnidirectionalShutdown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_H3cDLDPUnidirectionalShutdown_Type.__name__ = "Integer32"
_H3cDLDPUnidirectionalShutdown_Object = MibScalar
h3cDLDPUnidirectionalShutdown = _H3cDLDPUnidirectionalShutdown_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 1, 7),
    _H3cDLDPUnidirectionalShutdown_Type()
)
h3cDLDPUnidirectionalShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDLDPUnidirectionalShutdown.setStatus("current")
_H3cDLDPPortStateTable_Object = MibTable
h3cDLDPPortStateTable = _H3cDLDPPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDLDPPortStateTable.setStatus("current")
_H3cDLDPPortStateEntry_Object = MibTableRow
h3cDLDPPortStateEntry = _H3cDLDPPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 2, 1)
)
h3cDLDPPortStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDLDPPortStateEntry.setStatus("current")


class _H3cDLDPPortState_Type(EnabledStatus):
    """Custom type h3cDLDPPortState based on EnabledStatus"""
    defaultValue = 2


_H3cDLDPPortState_Type.__name__ = "EnabledStatus"
_H3cDLDPPortState_Object = MibTableColumn
h3cDLDPPortState = _H3cDLDPPortState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 2, 1, 1),
    _H3cDLDPPortState_Type()
)
h3cDLDPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDLDPPortState.setStatus("current")
_H3cDLDPPortDLDPTable_Object = MibTable
h3cDLDPPortDLDPTable = _H3cDLDPPortDLDPTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDLDPPortDLDPTable.setStatus("current")
_H3cDLDPPortDLDPEntry_Object = MibTableRow
h3cDLDPPortDLDPEntry = _H3cDLDPPortDLDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 3, 1)
)
h3cDLDPPortDLDPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDLDPPortDLDPEntry.setStatus("current")
_H3cDLDPPortDLDPState_Type = DLDPStatus
_H3cDLDPPortDLDPState_Object = MibTableColumn
h3cDLDPPortDLDPState = _H3cDLDPPortDLDPState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 3, 1, 1),
    _H3cDLDPPortDLDPState_Type()
)
h3cDLDPPortDLDPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDLDPPortDLDPState.setStatus("current")


class _H3cDLDPLinkState_Type(Integer32):
    """Custom type h3cDLDPLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("unknown", 3))
    )


_H3cDLDPLinkState_Type.__name__ = "Integer32"
_H3cDLDPLinkState_Object = MibTableColumn
h3cDLDPLinkState = _H3cDLDPLinkState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 3, 1, 2),
    _H3cDLDPLinkState_Type()
)
h3cDLDPLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDLDPLinkState.setStatus("current")
_H3cDLDPPortDLDPReset_Type = TruthValue
_H3cDLDPPortDLDPReset_Object = MibTableColumn
h3cDLDPPortDLDPReset = _H3cDLDPPortDLDPReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 3, 1, 3),
    _H3cDLDPPortDLDPReset_Type()
)
h3cDLDPPortDLDPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDLDPPortDLDPReset.setStatus("current")
_H3cDLDPNeighborTable_Object = MibTable
h3cDLDPNeighborTable = _H3cDLDPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDLDPNeighborTable.setStatus("current")
_H3cDLDPNeighborEntry_Object = MibTableRow
h3cDLDPNeighborEntry = _H3cDLDPNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 4, 1)
)
h3cDLDPNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-DLDP-MIB", "h3cDLDPNeighborBridgeMac"),
    (0, "A3COM-HUAWEI-DLDP-MIB", "h3cDLDPNeighborPortIndex"),
)
if mibBuilder.loadTexts:
    h3cDLDPNeighborEntry.setStatus("current")
_H3cDLDPNeighborBridgeMac_Type = MacAddress
_H3cDLDPNeighborBridgeMac_Object = MibTableColumn
h3cDLDPNeighborBridgeMac = _H3cDLDPNeighborBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 4, 1, 1),
    _H3cDLDPNeighborBridgeMac_Type()
)
h3cDLDPNeighborBridgeMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDLDPNeighborBridgeMac.setStatus("current")
_H3cDLDPNeighborPortIndex_Type = Integer32
_H3cDLDPNeighborPortIndex_Object = MibTableColumn
h3cDLDPNeighborPortIndex = _H3cDLDPNeighborPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 4, 1, 2),
    _H3cDLDPNeighborPortIndex_Type()
)
h3cDLDPNeighborPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDLDPNeighborPortIndex.setStatus("current")
_H3cDLDPNeighborState_Type = DLDPNeighborStatus
_H3cDLDPNeighborState_Object = MibTableColumn
h3cDLDPNeighborState = _H3cDLDPNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 4, 1, 3),
    _H3cDLDPNeighborState_Type()
)
h3cDLDPNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDLDPNeighborState.setStatus("current")
_H3cDLDPNeighborAgingTime_Type = Integer32
_H3cDLDPNeighborAgingTime_Object = MibTableColumn
h3cDLDPNeighborAgingTime = _H3cDLDPNeighborAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 1, 4, 1, 4),
    _H3cDLDPNeighborAgingTime_Type()
)
h3cDLDPNeighborAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDLDPNeighborAgingTime.setStatus("current")
_H3cDLDPTrapObject_ObjectIdentity = ObjectIdentity
h3cDLDPTrapObject = _H3cDLDPTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 2)
)
_H3cDLDPNotification_ObjectIdentity = ObjectIdentity
h3cDLDPNotification = _H3cDLDPNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 2, 1)
)

# Managed Objects groups


# Notification objects

h3cDLDPUnidirectionalPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43, 2, 1, 1)
)
h3cDLDPUnidirectionalPort.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cDLDPUnidirectionalPort.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DLDP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "DLDPStatus": DLDPStatus,
       "DLDPNeighborStatus": DLDPNeighborStatus,
       "h3cDldp": h3cDldp,
       "h3cDLDPMibObject": h3cDLDPMibObject,
       "h3cDLDPConfigGroup": h3cDLDPConfigGroup,
       "h3cDLDPWorkMode": h3cDLDPWorkMode,
       "h3cDLDPSystemEnable": h3cDLDPSystemEnable,
       "h3cDLDPSystemReset": h3cDLDPSystemReset,
       "h3cDLDPInterval": h3cDLDPInterval,
       "h3cDLDPAuthenticationMode": h3cDLDPAuthenticationMode,
       "h3cDLDPAuthenticationPassword": h3cDLDPAuthenticationPassword,
       "h3cDLDPUnidirectionalShutdown": h3cDLDPUnidirectionalShutdown,
       "h3cDLDPPortStateTable": h3cDLDPPortStateTable,
       "h3cDLDPPortStateEntry": h3cDLDPPortStateEntry,
       "h3cDLDPPortState": h3cDLDPPortState,
       "h3cDLDPPortDLDPTable": h3cDLDPPortDLDPTable,
       "h3cDLDPPortDLDPEntry": h3cDLDPPortDLDPEntry,
       "h3cDLDPPortDLDPState": h3cDLDPPortDLDPState,
       "h3cDLDPLinkState": h3cDLDPLinkState,
       "h3cDLDPPortDLDPReset": h3cDLDPPortDLDPReset,
       "h3cDLDPNeighborTable": h3cDLDPNeighborTable,
       "h3cDLDPNeighborEntry": h3cDLDPNeighborEntry,
       "h3cDLDPNeighborBridgeMac": h3cDLDPNeighborBridgeMac,
       "h3cDLDPNeighborPortIndex": h3cDLDPNeighborPortIndex,
       "h3cDLDPNeighborState": h3cDLDPNeighborState,
       "h3cDLDPNeighborAgingTime": h3cDLDPNeighborAgingTime,
       "h3cDLDPTrapObject": h3cDLDPTrapObject,
       "h3cDLDPNotification": h3cDLDPNotification,
       "h3cDLDPUnidirectionalPort": h3cDLDPUnidirectionalPort}
)
