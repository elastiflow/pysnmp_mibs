# SNMP MIB module (CISCO-SNMP-USM-OIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SNMP-USM-OIDS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:59 2025
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

(ciscoModules,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoModules")

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

ciscoSnmpUsmOidsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 6)
)
if mibBuilder.loadTexts:
    ciscoSnmpUsmOidsMIB.setRevisions(
        ("2006-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSnmpPrivProtocols_ObjectIdentity = ObjectIdentity
ciscoSnmpPrivProtocols = _CiscoSnmpPrivProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 6, 1)
)
_CusmAESCfb192PrivProtocol_ObjectIdentity = ObjectIdentity
cusmAESCfb192PrivProtocol = _CusmAESCfb192PrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 1)
)
_CusmAESCfb256PrivProtocol_ObjectIdentity = ObjectIdentity
cusmAESCfb256PrivProtocol = _CusmAESCfb256PrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 2)
)
_Cusm3DES168PrivProtocol_ObjectIdentity = ObjectIdentity
cusm3DES168PrivProtocol = _Cusm3DES168PrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNMP-USM-OIDS-MIB",
    **{"ciscoSnmpUsmOidsMIB": ciscoSnmpUsmOidsMIB,
       "ciscoSnmpPrivProtocols": ciscoSnmpPrivProtocols,
       "cusmAESCfb192PrivProtocol": cusmAESCfb192PrivProtocol,
       "cusmAESCfb256PrivProtocol": cusmAESCfb256PrivProtocol,
       "cusm3DES168PrivProtocol": cusm3DES168PrivProtocol}
)
