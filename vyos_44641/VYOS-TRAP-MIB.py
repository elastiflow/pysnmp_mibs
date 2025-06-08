# SNMP MIB module (VYOS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vyos_44641/VYOS-TRAP-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 21:56:32 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vyos,) = mibBuilder.importSymbols(
    "VYOS-SMI",
    "vyos")


# MODULE-IDENTITY

vyosTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44641, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MgmtTrap_ObjectIdentity = ObjectIdentity
mgmtTrap = _MgmtTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44641, 1, 1)
)
_MgmtEventObjects_ObjectIdentity = ObjectIdentity
mgmtEventObjects = _MgmtEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44641, 1, 1, 1)
)
_MgmtEventUser_Type = OctetString
_MgmtEventUser_Object = MibScalar
mgmtEventUser = _MgmtEventUser_Object(
    (1, 3, 6, 1, 4, 1, 44641, 1, 1, 1, 1),
    _MgmtEventUser_Type()
)
mgmtEventUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmtEventUser.setStatus("current")


class _MgmtEventSource_Type(Integer32):
    """Custom type mgmtEventSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("firewall", 1))
    )


_MgmtEventSource_Type.__name__ = "Integer32"
_MgmtEventSource_Object = MibScalar
mgmtEventSource = _MgmtEventSource_Object(
    (1, 3, 6, 1, 4, 1, 44641, 1, 1, 1, 2),
    _MgmtEventSource_Type()
)
mgmtEventSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmtEventSource.setStatus("current")


class _MgmtEventType_Type(Integer32):
    """Custom type mgmtEventType based on Integer32"""
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
        *(("unknown", 0),
          ("added", 1),
          ("deleted", 2),
          ("changed", 3))
    )


_MgmtEventType_Type.__name__ = "Integer32"
_MgmtEventType_Object = MibScalar
mgmtEventType = _MgmtEventType_Object(
    (1, 3, 6, 1, 4, 1, 44641, 1, 1, 1, 3),
    _MgmtEventType_Type()
)
mgmtEventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmtEventType.setStatus("current")
_MgmtEventPrevCfg_Type = OctetString
_MgmtEventPrevCfg_Object = MibScalar
mgmtEventPrevCfg = _MgmtEventPrevCfg_Object(
    (1, 3, 6, 1, 4, 1, 44641, 1, 1, 1, 4),
    _MgmtEventPrevCfg_Type()
)
mgmtEventPrevCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmtEventPrevCfg.setStatus("current")
_MgmtEventCurrCfg_Type = OctetString
_MgmtEventCurrCfg_Object = MibScalar
mgmtEventCurrCfg = _MgmtEventCurrCfg_Object(
    (1, 3, 6, 1, 4, 1, 44641, 1, 1, 1, 5),
    _MgmtEventCurrCfg_Type()
)
mgmtEventCurrCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmtEventCurrCfg.setStatus("current")
_MgmtEvent_ObjectIdentity = ObjectIdentity
mgmtEvent = _MgmtEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44641, 1, 1, 2)
)

# Managed Objects groups


# Notification objects

mgmtEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 44641, 1, 1, 2, 1)
)
mgmtEventTrap.setObjects(
      *(("VYOS-TRAP-MIB", "mgmtEventUser"),
        ("VYOS-TRAP-MIB", "mgmtEventSource"),
        ("VYOS-TRAP-MIB", "mgmtEventType"),
        ("VYOS-TRAP-MIB", "mgmtEventPrevCfg"),
        ("VYOS-TRAP-MIB", "mgmtEventCurrCfg"))
)
if mibBuilder.loadTexts:
    mgmtEventTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VYOS-TRAP-MIB",
    **{"vyosTrap": vyosTrap,
       "mgmtTrap": mgmtTrap,
       "mgmtEventObjects": mgmtEventObjects,
       "mgmtEventUser": mgmtEventUser,
       "mgmtEventSource": mgmtEventSource,
       "mgmtEventType": mgmtEventType,
       "mgmtEventPrevCfg": mgmtEventPrevCfg,
       "mgmtEventCurrCfg": mgmtEventCurrCfg,
       "mgmtEvent": mgmtEvent,
       "mgmtEventTrap": mgmtEventTrap}
)
