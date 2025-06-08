# SNMP MIB module (HH3C-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-L2TP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:38:10 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cL2tp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139)
)
if mibBuilder.loadTexts:
    hh3cL2tp.setRevisions(
        ("2013-07-05 15:18",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cL2tpObjects_ObjectIdentity = ObjectIdentity
hh3cL2tpObjects = _Hh3cL2tpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1)
)
_Hh3cL2tpScalar_ObjectIdentity = ObjectIdentity
hh3cL2tpScalar = _Hh3cL2tpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1)
)
_Hh3cL2tpStats_ObjectIdentity = ObjectIdentity
hh3cL2tpStats = _Hh3cL2tpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1)
)
_Hh3cL2tpStatsTotalTunnels_Type = Counter32
_Hh3cL2tpStatsTotalTunnels_Object = MibScalar
hh3cL2tpStatsTotalTunnels = _Hh3cL2tpStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 1),
    _Hh3cL2tpStatsTotalTunnels_Type()
)
hh3cL2tpStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpStatsTotalTunnels.setStatus("current")
_Hh3cL2tpStatsTotalSessions_Type = Counter32
_Hh3cL2tpStatsTotalSessions_Object = MibScalar
hh3cL2tpStatsTotalSessions = _Hh3cL2tpStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 2),
    _Hh3cL2tpStatsTotalSessions_Type()
)
hh3cL2tpStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpStatsTotalSessions.setStatus("current")
_Hh3cL2tpSessionRate_Type = Integer32
_Hh3cL2tpSessionRate_Object = MibScalar
hh3cL2tpSessionRate = _Hh3cL2tpSessionRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 3),
    _Hh3cL2tpSessionRate_Type()
)
hh3cL2tpSessionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpSessionRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-L2TP-MIB",
    **{"hh3cL2tp": hh3cL2tp,
       "hh3cL2tpObjects": hh3cL2tpObjects,
       "hh3cL2tpScalar": hh3cL2tpScalar,
       "hh3cL2tpStats": hh3cL2tpStats,
       "hh3cL2tpStatsTotalTunnels": hh3cL2tpStatsTotalTunnels,
       "hh3cL2tpStatsTotalSessions": hh3cL2tpStatsTotalSessions,
       "hh3cL2tpSessionRate": hh3cL2tpSessionRate}
)
