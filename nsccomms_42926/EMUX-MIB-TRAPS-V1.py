# SNMP MIB module (EMUX-MIB-TRAPS-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nsccomms_42926/EMUX-MIB-TRAPS-V1.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:13:34 2025
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

(e1ChIndex,
 e1RecvStatus,
 e1SendStatus,
 tdmAdminStatus,
 tdmChIndex,
 tdmLinkStatus) = mibBuilder.importSymbols(
    "EMUX-MIB",
    "e1ChIndex",
    "e1RecvStatus",
    "e1SendStatus",
    "tdmAdminStatus",
    "tdmChIndex",
    "tdmLinkStatus")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nsc_ObjectIdentity = ObjectIdentity
nsc = _Nsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926)
)
_Emux_ObjectIdentity = ObjectIdentity
emux = _Emux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2)
)

# Managed Objects groups


# Notification objects

e1LinkChangeV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42926, 2, 0, 1)
)
e1LinkChangeV1.setObjects(
      *(("EMUX-MIB", "e1ChIndex"),
        ("EMUX-MIB", "e1RecvStatus"),
        ("EMUX-MIB", "e1SendStatus"))
)
if mibBuilder.loadTexts:
    e1LinkChangeV1.setStatus(
        ""
    )

tdmLinkDownV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42926, 2, 0, 2)
)
tdmLinkDownV1.setObjects(
      *(("EMUX-MIB", "tdmChIndex"),
        ("EMUX-MIB", "tdmAdminStatus"),
        ("EMUX-MIB", "tdmLinkStatus"))
)
if mibBuilder.loadTexts:
    tdmLinkDownV1.setStatus(
        ""
    )

tdmLinkUpV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42926, 2, 0, 3)
)
tdmLinkUpV1.setObjects(
      *(("EMUX-MIB", "tdmChIndex"),
        ("EMUX-MIB", "tdmAdminStatus"),
        ("EMUX-MIB", "tdmLinkStatus"))
)
if mibBuilder.loadTexts:
    tdmLinkUpV1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMUX-MIB-TRAPS-V1",
    **{"nsc": nsc,
       "emux": emux,
       "e1LinkChangeV1": e1LinkChangeV1,
       "tdmLinkDownV1": tdmLinkDownV1,
       "tdmLinkUpV1": tdmLinkUpV1}
)
