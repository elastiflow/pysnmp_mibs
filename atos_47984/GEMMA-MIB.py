# SNMP MIB module (GEMMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atos_47984/GEMMA-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:39:57 2025
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


# MODULE-IDENTITY

gemma = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6)
)
if mibBuilder.loadTexts:
    gemma.setRevisions(
        ("2021-06-16 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Atos_ObjectIdentity = ObjectIdentity
atos = _Atos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47984)
)
if mibBuilder.loadTexts:
    atos.setStatus("current")
_Ng911_ObjectIdentity = ObjectIdentity
ng911 = _Ng911_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47984, 10)
)
if mibBuilder.loadTexts:
    ng911.setStatus("current")
_NgFaultMgmt_ObjectIdentity = ObjectIdentity
ngFaultMgmt = _NgFaultMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47984, 10, 2)
)
if mibBuilder.loadTexts:
    ngFaultMgmt.setStatus("current")
_NgEventMgmt_ObjectIdentity = ObjectIdentity
ngEventMgmt = _NgEventMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47984, 10, 2, 1)
)
if mibBuilder.loadTexts:
    ngEventMgmt.setStatus("current")


class _NgEvtSeverity_Type(Integer32):
    """Custom type ngEvtSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("information", 5),
          ("clear", 6),
          ("unknown", 7))
    )


_NgEvtSeverity_Type.__name__ = "Integer32"
_NgEvtSeverity_Object = MibScalar
ngEvtSeverity = _NgEvtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 47984, 10, 2, 1, 1),
    _NgEvtSeverity_Type()
)
ngEvtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngEvtSeverity.setStatus("current")
_ReverseMappingTrapPrefix_ObjectIdentity = ObjectIdentity
reverseMappingTrapPrefix = _ReverseMappingTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6, 0)
)

# Managed Objects groups


# Notification objects

gemmaDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6, 0, 1)
)
gemmaDownTrap.setObjects(
    ("GEMMA-MIB", "ngEvtSeverity")
)
if mibBuilder.loadTexts:
    gemmaDownTrap.setStatus(
        "current"
    )

dbDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6, 0, 2)
)
dbDownTrap.setObjects(
    ("GEMMA-MIB", "ngEvtSeverity")
)
if mibBuilder.loadTexts:
    dbDownTrap.setStatus(
        "current"
    )

telephonyDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6, 0, 3)
)
telephonyDownTrap.setObjects(
    ("GEMMA-MIB", "ngEvtSeverity")
)
if mibBuilder.loadTexts:
    telephonyDownTrap.setStatus(
        "current"
    )

mediaServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6, 0, 4)
)
mediaServerDownTrap.setObjects(
    ("GEMMA-MIB", "ngEvtSeverity")
)
if mibBuilder.loadTexts:
    mediaServerDownTrap.setStatus(
        "current"
    )

webrtcServiceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6, 0, 5)
)
webrtcServiceDownTrap.setObjects(
    ("GEMMA-MIB", "ngEvtSeverity")
)
if mibBuilder.loadTexts:
    webrtcServiceDownTrap.setStatus(
        "current"
    )

layoutServiceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6, 0, 6)
)
layoutServiceDownTrap.setObjects(
    ("GEMMA-MIB", "ngEvtSeverity")
)
if mibBuilder.loadTexts:
    layoutServiceDownTrap.setStatus(
        "current"
    )

keycloakServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6, 0, 7)
)
keycloakServerDownTrap.setObjects(
    ("GEMMA-MIB", "ngEvtSeverity")
)
if mibBuilder.loadTexts:
    keycloakServerDownTrap.setStatus(
        "current"
    )

restToSnmpDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47984, 10, 6, 0, 8)
)
restToSnmpDownTrap.setObjects(
    ("GEMMA-MIB", "ngEvtSeverity")
)
if mibBuilder.loadTexts:
    restToSnmpDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GEMMA-MIB",
    **{"atos": atos,
       "ng911": ng911,
       "ngFaultMgmt": ngFaultMgmt,
       "ngEventMgmt": ngEventMgmt,
       "ngEvtSeverity": ngEvtSeverity,
       "gemma": gemma,
       "reverseMappingTrapPrefix": reverseMappingTrapPrefix,
       "gemmaDownTrap": gemmaDownTrap,
       "dbDownTrap": dbDownTrap,
       "telephonyDownTrap": telephonyDownTrap,
       "mediaServerDownTrap": mediaServerDownTrap,
       "webrtcServiceDownTrap": webrtcServiceDownTrap,
       "layoutServiceDownTrap": layoutServiceDownTrap,
       "keycloakServerDownTrap": keycloakServerDownTrap,
       "restToSnmpDownTrap": restToSnmpDownTrap}
)
