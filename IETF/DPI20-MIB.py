# SNMP MIB module (DPI20-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/DPI20-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:30:43 2025
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmDPI_ObjectIdentity = ObjectIdentity
ibmDPI = _IbmDPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2)
)
_Dpi20MIB_ObjectIdentity = ObjectIdentity
dpi20MIB = _Dpi20MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2, 1)
)
_DpiPort_ObjectIdentity = ObjectIdentity
dpiPort = _DpiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 1)
)


class _DpiPortForTCP_Type(Integer32):
    """Custom type dpiPortForTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpiPortForTCP_Type.__name__ = "Integer32"
_DpiPortForTCP_Object = MibScalar
dpiPortForTCP = _DpiPortForTCP_Object(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 1),
    _DpiPortForTCP_Type()
)
dpiPortForTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiPortForTCP.setStatus("mandatory")


class _DpiPortForUDP_Type(Integer32):
    """Custom type dpiPortForUDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpiPortForUDP_Type.__name__ = "Integer32"
_DpiPortForUDP_Object = MibScalar
dpiPortForUDP = _DpiPortForUDP_Object(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 2),
    _DpiPortForUDP_Type()
)
dpiPortForUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiPortForUDP.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPI20-MIB",
    **{"ibm": ibm,
       "ibmDPI": ibmDPI,
       "dpi20MIB": dpi20MIB,
       "dpiPort": dpiPort,
       "dpiPortForTCP": dpiPortForTCP,
       "dpiPortForUDP": dpiPortForUDP}
)
