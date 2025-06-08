# SNMP MIB module (FDRY-IPV6-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FDRY-IPV6-IP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:53 2025
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

(RtrStatus,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-IP-MIB",
    "RtrStatus")

(fdryIpv6,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "fdryIpv6")

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

fdryIpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    fdryIpv6MIB.setRevisions(
        ("2010-07-26 00:00",
         "2010-05-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdryIpv6GlobalObjects_ObjectIdentity = ObjectIdentity
fdryIpv6GlobalObjects = _FdryIpv6GlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1)
)
_FdryIpv6LoadShare_Type = RtrStatus
_FdryIpv6LoadShare_Object = MibScalar
fdryIpv6LoadShare = _FdryIpv6LoadShare_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 1),
    _FdryIpv6LoadShare_Type()
)
fdryIpv6LoadShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryIpv6LoadShare.setStatus("current")
_FdryIpv6LoadShareNumOfPaths_Type = Unsigned32
_FdryIpv6LoadShareNumOfPaths_Object = MibScalar
fdryIpv6LoadShareNumOfPaths = _FdryIpv6LoadShareNumOfPaths_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 2),
    _FdryIpv6LoadShareNumOfPaths_Type()
)
fdryIpv6LoadShareNumOfPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryIpv6LoadShareNumOfPaths.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-IPV6-IP-MIB",
    **{"fdryIpv6MIB": fdryIpv6MIB,
       "fdryIpv6GlobalObjects": fdryIpv6GlobalObjects,
       "fdryIpv6LoadShare": fdryIpv6LoadShare,
       "fdryIpv6LoadShareNumOfPaths": fdryIpv6LoadShareNumOfPaths}
)
