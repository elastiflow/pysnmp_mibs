# SNMP MIB module (BROADHOP-QNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/broadhop_26878/BROADHOP-QNS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:03 2025
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

(broadhopProducts,) = mibBuilder.importSymbols(
    "BROADHOP-MIB",
    "broadhopProducts")

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

broadhopProductsQNS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2)
)
if mibBuilder.loadTexts:
    broadhopProductsQNS.setRevisions(
        ("2012-03-12 00:00",
         "2012-02-14 00:00",
         "2012-02-10 00:00",
         "2012-01-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BroadhopProductsQNSComponents_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents = _BroadhopProductsQNSComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2)
)
_BroadhopProductsQNSComponents53_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53 = _BroadhopProductsQNSComponents53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53)
)
_BroadhopProductsQNSComponents53LB01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53LB01 = _BroadhopProductsQNSComponents53LB01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11)
)
_Component53LB01CpuUser_Type = Integer32
_Component53LB01CpuUser_Object = MibScalar
component53LB01CpuUser = _Component53LB01CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 1),
    _Component53LB01CpuUser_Type()
)
component53LB01CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01CpuUser.setStatus("current")
_Component53LB01CpuSystem_Type = Integer32
_Component53LB01CpuSystem_Object = MibScalar
component53LB01CpuSystem = _Component53LB01CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 2),
    _Component53LB01CpuSystem_Type()
)
component53LB01CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01CpuSystem.setStatus("current")
_Component53LB01CpuIdle_Type = Integer32
_Component53LB01CpuIdle_Object = MibScalar
component53LB01CpuIdle = _Component53LB01CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 3),
    _Component53LB01CpuIdle_Type()
)
component53LB01CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01CpuIdle.setStatus("current")
_Component53LB01LoadAverage1_Type = Integer32
_Component53LB01LoadAverage1_Object = MibScalar
component53LB01LoadAverage1 = _Component53LB01LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 4),
    _Component53LB01LoadAverage1_Type()
)
component53LB01LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01LoadAverage1.setStatus("current")
_Component53LB01LoadAverage5_Type = Integer32
_Component53LB01LoadAverage5_Object = MibScalar
component53LB01LoadAverage5 = _Component53LB01LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 5),
    _Component53LB01LoadAverage5_Type()
)
component53LB01LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01LoadAverage5.setStatus("current")
_Component53LB01LoadAverage15_Type = Integer32
_Component53LB01LoadAverage15_Object = MibScalar
component53LB01LoadAverage15 = _Component53LB01LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 6),
    _Component53LB01LoadAverage15_Type()
)
component53LB01LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01LoadAverage15.setStatus("current")
_Component53LB01MemoryTotal_Type = Integer32
_Component53LB01MemoryTotal_Object = MibScalar
component53LB01MemoryTotal = _Component53LB01MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 7),
    _Component53LB01MemoryTotal_Type()
)
component53LB01MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01MemoryTotal.setStatus("current")
_Component53LB01MemoryAvailable_Type = Integer32
_Component53LB01MemoryAvailable_Object = MibScalar
component53LB01MemoryAvailable = _Component53LB01MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 8),
    _Component53LB01MemoryAvailable_Type()
)
component53LB01MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01MemoryAvailable.setStatus("current")
_Component53LB01SwapTotal_Type = Integer32
_Component53LB01SwapTotal_Object = MibScalar
component53LB01SwapTotal = _Component53LB01SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 9),
    _Component53LB01SwapTotal_Type()
)
component53LB01SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01SwapTotal.setStatus("current")
_Component53LB01SwapAvailable_Type = Integer32
_Component53LB01SwapAvailable_Object = MibScalar
component53LB01SwapAvailable = _Component53LB01SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 10),
    _Component53LB01SwapAvailable_Type()
)
component53LB01SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01SwapAvailable.setStatus("current")
_Component53LB01Eth0InOctets_Type = Counter32
_Component53LB01Eth0InOctets_Object = MibScalar
component53LB01Eth0InOctets = _Component53LB01Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 11),
    _Component53LB01Eth0InOctets_Type()
)
component53LB01Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01Eth0InOctets.setStatus("current")
_Component53LB01Eth0OutOctets_Type = Counter32
_Component53LB01Eth0OutOctets_Object = MibScalar
component53LB01Eth0OutOctets = _Component53LB01Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 12),
    _Component53LB01Eth0OutOctets_Type()
)
component53LB01Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01Eth0OutOctets.setStatus("current")
_Component53LB01Eth1InOctets_Type = Counter32
_Component53LB01Eth1InOctets_Object = MibScalar
component53LB01Eth1InOctets = _Component53LB01Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 13),
    _Component53LB01Eth1InOctets_Type()
)
component53LB01Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01Eth1InOctets.setStatus("current")
_Component53LB01Eth1OutOctets_Type = Counter32
_Component53LB01Eth1OutOctets_Object = MibScalar
component53LB01Eth1OutOctets = _Component53LB01Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 11, 14),
    _Component53LB01Eth1OutOctets_Type()
)
component53LB01Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB01Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53LB02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53LB02 = _BroadhopProductsQNSComponents53LB02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12)
)
_Component53LB02CpuUser_Type = Integer32
_Component53LB02CpuUser_Object = MibScalar
component53LB02CpuUser = _Component53LB02CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 1),
    _Component53LB02CpuUser_Type()
)
component53LB02CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02CpuUser.setStatus("current")
_Component53LB02CpuSystem_Type = Integer32
_Component53LB02CpuSystem_Object = MibScalar
component53LB02CpuSystem = _Component53LB02CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 2),
    _Component53LB02CpuSystem_Type()
)
component53LB02CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02CpuSystem.setStatus("current")
_Component53LB02CpuIdle_Type = Integer32
_Component53LB02CpuIdle_Object = MibScalar
component53LB02CpuIdle = _Component53LB02CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 3),
    _Component53LB02CpuIdle_Type()
)
component53LB02CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02CpuIdle.setStatus("current")
_Component53LB02LoadAverage1_Type = Integer32
_Component53LB02LoadAverage1_Object = MibScalar
component53LB02LoadAverage1 = _Component53LB02LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 4),
    _Component53LB02LoadAverage1_Type()
)
component53LB02LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02LoadAverage1.setStatus("current")
_Component53LB02LoadAverage5_Type = Integer32
_Component53LB02LoadAverage5_Object = MibScalar
component53LB02LoadAverage5 = _Component53LB02LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 5),
    _Component53LB02LoadAverage5_Type()
)
component53LB02LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02LoadAverage5.setStatus("current")
_Component53LB02LoadAverage15_Type = Integer32
_Component53LB02LoadAverage15_Object = MibScalar
component53LB02LoadAverage15 = _Component53LB02LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 6),
    _Component53LB02LoadAverage15_Type()
)
component53LB02LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02LoadAverage15.setStatus("current")
_Component53LB02MemoryTotal_Type = Integer32
_Component53LB02MemoryTotal_Object = MibScalar
component53LB02MemoryTotal = _Component53LB02MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 7),
    _Component53LB02MemoryTotal_Type()
)
component53LB02MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02MemoryTotal.setStatus("current")
_Component53LB02MemoryAvailable_Type = Integer32
_Component53LB02MemoryAvailable_Object = MibScalar
component53LB02MemoryAvailable = _Component53LB02MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 8),
    _Component53LB02MemoryAvailable_Type()
)
component53LB02MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02MemoryAvailable.setStatus("current")
_Component53LB02SwapTotal_Type = Integer32
_Component53LB02SwapTotal_Object = MibScalar
component53LB02SwapTotal = _Component53LB02SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 9),
    _Component53LB02SwapTotal_Type()
)
component53LB02SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02SwapTotal.setStatus("current")
_Component53LB02SwapAvailable_Type = Integer32
_Component53LB02SwapAvailable_Object = MibScalar
component53LB02SwapAvailable = _Component53LB02SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 10),
    _Component53LB02SwapAvailable_Type()
)
component53LB02SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02SwapAvailable.setStatus("current")
_Component53LB02Eth0InOctets_Type = Counter32
_Component53LB02Eth0InOctets_Object = MibScalar
component53LB02Eth0InOctets = _Component53LB02Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 11),
    _Component53LB02Eth0InOctets_Type()
)
component53LB02Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02Eth0InOctets.setStatus("current")
_Component53LB02Eth0OutOctets_Type = Counter32
_Component53LB02Eth0OutOctets_Object = MibScalar
component53LB02Eth0OutOctets = _Component53LB02Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 12),
    _Component53LB02Eth0OutOctets_Type()
)
component53LB02Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02Eth0OutOctets.setStatus("current")
_Component53LB02Eth1InOctets_Type = Counter32
_Component53LB02Eth1InOctets_Object = MibScalar
component53LB02Eth1InOctets = _Component53LB02Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 13),
    _Component53LB02Eth1InOctets_Type()
)
component53LB02Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02Eth1InOctets.setStatus("current")
_Component53LB02Eth1OutOctets_Type = Counter32
_Component53LB02Eth1OutOctets_Object = MibScalar
component53LB02Eth1OutOctets = _Component53LB02Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 12, 14),
    _Component53LB02Eth1OutOctets_Type()
)
component53LB02Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53LB02Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53PortalLB01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53PortalLB01 = _BroadhopProductsQNSComponents53PortalLB01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13)
)
_Component53PortalLB01CpuUser_Type = Integer32
_Component53PortalLB01CpuUser_Object = MibScalar
component53PortalLB01CpuUser = _Component53PortalLB01CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 1),
    _Component53PortalLB01CpuUser_Type()
)
component53PortalLB01CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01CpuUser.setStatus("current")
_Component53PortalLB01CpuSystem_Type = Integer32
_Component53PortalLB01CpuSystem_Object = MibScalar
component53PortalLB01CpuSystem = _Component53PortalLB01CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 2),
    _Component53PortalLB01CpuSystem_Type()
)
component53PortalLB01CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01CpuSystem.setStatus("current")
_Component53PortalLB01CpuIdle_Type = Integer32
_Component53PortalLB01CpuIdle_Object = MibScalar
component53PortalLB01CpuIdle = _Component53PortalLB01CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 3),
    _Component53PortalLB01CpuIdle_Type()
)
component53PortalLB01CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01CpuIdle.setStatus("current")
_Component53PortalLB01LoadAverage1_Type = Integer32
_Component53PortalLB01LoadAverage1_Object = MibScalar
component53PortalLB01LoadAverage1 = _Component53PortalLB01LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 4),
    _Component53PortalLB01LoadAverage1_Type()
)
component53PortalLB01LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01LoadAverage1.setStatus("current")
_Component53PortalLB01LoadAverage5_Type = Integer32
_Component53PortalLB01LoadAverage5_Object = MibScalar
component53PortalLB01LoadAverage5 = _Component53PortalLB01LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 5),
    _Component53PortalLB01LoadAverage5_Type()
)
component53PortalLB01LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01LoadAverage5.setStatus("current")
_Component53PortalLB01LoadAverage15_Type = Integer32
_Component53PortalLB01LoadAverage15_Object = MibScalar
component53PortalLB01LoadAverage15 = _Component53PortalLB01LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 6),
    _Component53PortalLB01LoadAverage15_Type()
)
component53PortalLB01LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01LoadAverage15.setStatus("current")
_Component53PortalLB01MemoryTotal_Type = Integer32
_Component53PortalLB01MemoryTotal_Object = MibScalar
component53PortalLB01MemoryTotal = _Component53PortalLB01MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 7),
    _Component53PortalLB01MemoryTotal_Type()
)
component53PortalLB01MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01MemoryTotal.setStatus("current")
_Component53PortalLB01MemoryAvailable_Type = Integer32
_Component53PortalLB01MemoryAvailable_Object = MibScalar
component53PortalLB01MemoryAvailable = _Component53PortalLB01MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 8),
    _Component53PortalLB01MemoryAvailable_Type()
)
component53PortalLB01MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01MemoryAvailable.setStatus("current")
_Component53PortalLB01SwapTotal_Type = Integer32
_Component53PortalLB01SwapTotal_Object = MibScalar
component53PortalLB01SwapTotal = _Component53PortalLB01SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 9),
    _Component53PortalLB01SwapTotal_Type()
)
component53PortalLB01SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01SwapTotal.setStatus("current")
_Component53PortalLB01SwapAvailable_Type = Integer32
_Component53PortalLB01SwapAvailable_Object = MibScalar
component53PortalLB01SwapAvailable = _Component53PortalLB01SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 10),
    _Component53PortalLB01SwapAvailable_Type()
)
component53PortalLB01SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01SwapAvailable.setStatus("current")
_Component53PortalLB01Eth0InOctets_Type = Counter32
_Component53PortalLB01Eth0InOctets_Object = MibScalar
component53PortalLB01Eth0InOctets = _Component53PortalLB01Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 11),
    _Component53PortalLB01Eth0InOctets_Type()
)
component53PortalLB01Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01Eth0InOctets.setStatus("current")
_Component53PortalLB01Eth0OutOctets_Type = Counter32
_Component53PortalLB01Eth0OutOctets_Object = MibScalar
component53PortalLB01Eth0OutOctets = _Component53PortalLB01Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 12),
    _Component53PortalLB01Eth0OutOctets_Type()
)
component53PortalLB01Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01Eth0OutOctets.setStatus("current")
_Component53PortalLB01Eth1InOctets_Type = Counter32
_Component53PortalLB01Eth1InOctets_Object = MibScalar
component53PortalLB01Eth1InOctets = _Component53PortalLB01Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 13),
    _Component53PortalLB01Eth1InOctets_Type()
)
component53PortalLB01Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01Eth1InOctets.setStatus("current")
_Component53PortalLB01Eth1OutOctets_Type = Counter32
_Component53PortalLB01Eth1OutOctets_Object = MibScalar
component53PortalLB01Eth1OutOctets = _Component53PortalLB01Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 13, 14),
    _Component53PortalLB01Eth1OutOctets_Type()
)
component53PortalLB01Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB01Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53PortalLB02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53PortalLB02 = _BroadhopProductsQNSComponents53PortalLB02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14)
)
_Component53PortalLB02CpuUser_Type = Integer32
_Component53PortalLB02CpuUser_Object = MibScalar
component53PortalLB02CpuUser = _Component53PortalLB02CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 1),
    _Component53PortalLB02CpuUser_Type()
)
component53PortalLB02CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02CpuUser.setStatus("current")
_Component53PortalLB02CpuSystem_Type = Integer32
_Component53PortalLB02CpuSystem_Object = MibScalar
component53PortalLB02CpuSystem = _Component53PortalLB02CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 2),
    _Component53PortalLB02CpuSystem_Type()
)
component53PortalLB02CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02CpuSystem.setStatus("current")
_Component53PortalLB02CpuIdle_Type = Integer32
_Component53PortalLB02CpuIdle_Object = MibScalar
component53PortalLB02CpuIdle = _Component53PortalLB02CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 3),
    _Component53PortalLB02CpuIdle_Type()
)
component53PortalLB02CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02CpuIdle.setStatus("current")
_Component53PortalLB02LoadAverage1_Type = Integer32
_Component53PortalLB02LoadAverage1_Object = MibScalar
component53PortalLB02LoadAverage1 = _Component53PortalLB02LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 4),
    _Component53PortalLB02LoadAverage1_Type()
)
component53PortalLB02LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02LoadAverage1.setStatus("current")
_Component53PortalLB02LoadAverage5_Type = Integer32
_Component53PortalLB02LoadAverage5_Object = MibScalar
component53PortalLB02LoadAverage5 = _Component53PortalLB02LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 5),
    _Component53PortalLB02LoadAverage5_Type()
)
component53PortalLB02LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02LoadAverage5.setStatus("current")
_Component53PortalLB02LoadAverage15_Type = Integer32
_Component53PortalLB02LoadAverage15_Object = MibScalar
component53PortalLB02LoadAverage15 = _Component53PortalLB02LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 6),
    _Component53PortalLB02LoadAverage15_Type()
)
component53PortalLB02LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02LoadAverage15.setStatus("current")
_Component53PortalLB02MemoryTotal_Type = Integer32
_Component53PortalLB02MemoryTotal_Object = MibScalar
component53PortalLB02MemoryTotal = _Component53PortalLB02MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 7),
    _Component53PortalLB02MemoryTotal_Type()
)
component53PortalLB02MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02MemoryTotal.setStatus("current")
_Component53PortalLB02MemoryAvailable_Type = Integer32
_Component53PortalLB02MemoryAvailable_Object = MibScalar
component53PortalLB02MemoryAvailable = _Component53PortalLB02MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 8),
    _Component53PortalLB02MemoryAvailable_Type()
)
component53PortalLB02MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02MemoryAvailable.setStatus("current")
_Component53PortalLB02SwapTotal_Type = Integer32
_Component53PortalLB02SwapTotal_Object = MibScalar
component53PortalLB02SwapTotal = _Component53PortalLB02SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 9),
    _Component53PortalLB02SwapTotal_Type()
)
component53PortalLB02SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02SwapTotal.setStatus("current")
_Component53PortalLB02SwapAvailable_Type = Integer32
_Component53PortalLB02SwapAvailable_Object = MibScalar
component53PortalLB02SwapAvailable = _Component53PortalLB02SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 10),
    _Component53PortalLB02SwapAvailable_Type()
)
component53PortalLB02SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02SwapAvailable.setStatus("current")
_Component53PortalLB02Eth0InOctets_Type = Counter32
_Component53PortalLB02Eth0InOctets_Object = MibScalar
component53PortalLB02Eth0InOctets = _Component53PortalLB02Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 11),
    _Component53PortalLB02Eth0InOctets_Type()
)
component53PortalLB02Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02Eth0InOctets.setStatus("current")
_Component53PortalLB02Eth0OutOctets_Type = Counter32
_Component53PortalLB02Eth0OutOctets_Object = MibScalar
component53PortalLB02Eth0OutOctets = _Component53PortalLB02Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 12),
    _Component53PortalLB02Eth0OutOctets_Type()
)
component53PortalLB02Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02Eth0OutOctets.setStatus("current")
_Component53PortalLB02Eth1InOctets_Type = Counter32
_Component53PortalLB02Eth1InOctets_Object = MibScalar
component53PortalLB02Eth1InOctets = _Component53PortalLB02Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 13),
    _Component53PortalLB02Eth1InOctets_Type()
)
component53PortalLB02Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02Eth1InOctets.setStatus("current")
_Component53PortalLB02Eth1OutOctets_Type = Counter32
_Component53PortalLB02Eth1OutOctets_Object = MibScalar
component53PortalLB02Eth1OutOctets = _Component53PortalLB02Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 14, 14),
    _Component53PortalLB02Eth1OutOctets_Type()
)
component53PortalLB02Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PortalLB02Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53PCRFClient01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53PCRFClient01 = _BroadhopProductsQNSComponents53PCRFClient01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21)
)
_Component53PCRFClient01CpuUser_Type = Integer32
_Component53PCRFClient01CpuUser_Object = MibScalar
component53PCRFClient01CpuUser = _Component53PCRFClient01CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 1),
    _Component53PCRFClient01CpuUser_Type()
)
component53PCRFClient01CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01CpuUser.setStatus("current")
_Component53PCRFClient01CpuSystem_Type = Integer32
_Component53PCRFClient01CpuSystem_Object = MibScalar
component53PCRFClient01CpuSystem = _Component53PCRFClient01CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 2),
    _Component53PCRFClient01CpuSystem_Type()
)
component53PCRFClient01CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01CpuSystem.setStatus("current")
_Component53PCRFClient01CpuIdle_Type = Integer32
_Component53PCRFClient01CpuIdle_Object = MibScalar
component53PCRFClient01CpuIdle = _Component53PCRFClient01CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 3),
    _Component53PCRFClient01CpuIdle_Type()
)
component53PCRFClient01CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01CpuIdle.setStatus("current")
_Component53PCRFClient01LoadAverage1_Type = Integer32
_Component53PCRFClient01LoadAverage1_Object = MibScalar
component53PCRFClient01LoadAverage1 = _Component53PCRFClient01LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 4),
    _Component53PCRFClient01LoadAverage1_Type()
)
component53PCRFClient01LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01LoadAverage1.setStatus("current")
_Component53PCRFClient01LoadAverage5_Type = Integer32
_Component53PCRFClient01LoadAverage5_Object = MibScalar
component53PCRFClient01LoadAverage5 = _Component53PCRFClient01LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 5),
    _Component53PCRFClient01LoadAverage5_Type()
)
component53PCRFClient01LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01LoadAverage5.setStatus("current")
_Component53PCRFClient01LoadAverage15_Type = Integer32
_Component53PCRFClient01LoadAverage15_Object = MibScalar
component53PCRFClient01LoadAverage15 = _Component53PCRFClient01LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 6),
    _Component53PCRFClient01LoadAverage15_Type()
)
component53PCRFClient01LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01LoadAverage15.setStatus("current")
_Component53PCRFClient01MemoryTotal_Type = Integer32
_Component53PCRFClient01MemoryTotal_Object = MibScalar
component53PCRFClient01MemoryTotal = _Component53PCRFClient01MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 7),
    _Component53PCRFClient01MemoryTotal_Type()
)
component53PCRFClient01MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01MemoryTotal.setStatus("current")
_Component53PCRFClient01MemoryAvailable_Type = Integer32
_Component53PCRFClient01MemoryAvailable_Object = MibScalar
component53PCRFClient01MemoryAvailable = _Component53PCRFClient01MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 8),
    _Component53PCRFClient01MemoryAvailable_Type()
)
component53PCRFClient01MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01MemoryAvailable.setStatus("current")
_Component53PCRFClient01SwapTotal_Type = Integer32
_Component53PCRFClient01SwapTotal_Object = MibScalar
component53PCRFClient01SwapTotal = _Component53PCRFClient01SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 9),
    _Component53PCRFClient01SwapTotal_Type()
)
component53PCRFClient01SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01SwapTotal.setStatus("current")
_Component53PCRFClient01SwapAvailable_Type = Integer32
_Component53PCRFClient01SwapAvailable_Object = MibScalar
component53PCRFClient01SwapAvailable = _Component53PCRFClient01SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 10),
    _Component53PCRFClient01SwapAvailable_Type()
)
component53PCRFClient01SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01SwapAvailable.setStatus("current")
_Component53PCRFClient01Eth0InOctets_Type = Counter32
_Component53PCRFClient01Eth0InOctets_Object = MibScalar
component53PCRFClient01Eth0InOctets = _Component53PCRFClient01Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 11),
    _Component53PCRFClient01Eth0InOctets_Type()
)
component53PCRFClient01Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01Eth0InOctets.setStatus("current")
_Component53PCRFClient01Eth0OutOctets_Type = Counter32
_Component53PCRFClient01Eth0OutOctets_Object = MibScalar
component53PCRFClient01Eth0OutOctets = _Component53PCRFClient01Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 12),
    _Component53PCRFClient01Eth0OutOctets_Type()
)
component53PCRFClient01Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01Eth0OutOctets.setStatus("current")
_Component53PCRFClient01Eth1InOctets_Type = Counter32
_Component53PCRFClient01Eth1InOctets_Object = MibScalar
component53PCRFClient01Eth1InOctets = _Component53PCRFClient01Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 13),
    _Component53PCRFClient01Eth1InOctets_Type()
)
component53PCRFClient01Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01Eth1InOctets.setStatus("current")
_Component53PCRFClient01Eth1OutOctets_Type = Counter32
_Component53PCRFClient01Eth1OutOctets_Object = MibScalar
component53PCRFClient01Eth1OutOctets = _Component53PCRFClient01Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 21, 14),
    _Component53PCRFClient01Eth1OutOctets_Type()
)
component53PCRFClient01Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient01Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53PCRFClient02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53PCRFClient02 = _BroadhopProductsQNSComponents53PCRFClient02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22)
)
_Component53PCRFClient02CpuUser_Type = Integer32
_Component53PCRFClient02CpuUser_Object = MibScalar
component53PCRFClient02CpuUser = _Component53PCRFClient02CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 1),
    _Component53PCRFClient02CpuUser_Type()
)
component53PCRFClient02CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02CpuUser.setStatus("current")
_Component53PCRFClient02CpuSystem_Type = Integer32
_Component53PCRFClient02CpuSystem_Object = MibScalar
component53PCRFClient02CpuSystem = _Component53PCRFClient02CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 2),
    _Component53PCRFClient02CpuSystem_Type()
)
component53PCRFClient02CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02CpuSystem.setStatus("current")
_Component53PCRFClient02CpuIdle_Type = Integer32
_Component53PCRFClient02CpuIdle_Object = MibScalar
component53PCRFClient02CpuIdle = _Component53PCRFClient02CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 3),
    _Component53PCRFClient02CpuIdle_Type()
)
component53PCRFClient02CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02CpuIdle.setStatus("current")
_Component53PCRFClient02LoadAverage1_Type = Integer32
_Component53PCRFClient02LoadAverage1_Object = MibScalar
component53PCRFClient02LoadAverage1 = _Component53PCRFClient02LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 4),
    _Component53PCRFClient02LoadAverage1_Type()
)
component53PCRFClient02LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02LoadAverage1.setStatus("current")
_Component53PCRFClient02LoadAverage5_Type = Integer32
_Component53PCRFClient02LoadAverage5_Object = MibScalar
component53PCRFClient02LoadAverage5 = _Component53PCRFClient02LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 5),
    _Component53PCRFClient02LoadAverage5_Type()
)
component53PCRFClient02LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02LoadAverage5.setStatus("current")
_Component53PCRFClient02LoadAverage15_Type = Integer32
_Component53PCRFClient02LoadAverage15_Object = MibScalar
component53PCRFClient02LoadAverage15 = _Component53PCRFClient02LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 6),
    _Component53PCRFClient02LoadAverage15_Type()
)
component53PCRFClient02LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02LoadAverage15.setStatus("current")
_Component53PCRFClient02MemoryTotal_Type = Integer32
_Component53PCRFClient02MemoryTotal_Object = MibScalar
component53PCRFClient02MemoryTotal = _Component53PCRFClient02MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 7),
    _Component53PCRFClient02MemoryTotal_Type()
)
component53PCRFClient02MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02MemoryTotal.setStatus("current")
_Component53PCRFClient02MemoryAvailable_Type = Integer32
_Component53PCRFClient02MemoryAvailable_Object = MibScalar
component53PCRFClient02MemoryAvailable = _Component53PCRFClient02MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 8),
    _Component53PCRFClient02MemoryAvailable_Type()
)
component53PCRFClient02MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02MemoryAvailable.setStatus("current")
_Component53PCRFClient02SwapTotal_Type = Integer32
_Component53PCRFClient02SwapTotal_Object = MibScalar
component53PCRFClient02SwapTotal = _Component53PCRFClient02SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 9),
    _Component53PCRFClient02SwapTotal_Type()
)
component53PCRFClient02SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02SwapTotal.setStatus("current")
_Component53PCRFClient02SwapAvailable_Type = Integer32
_Component53PCRFClient02SwapAvailable_Object = MibScalar
component53PCRFClient02SwapAvailable = _Component53PCRFClient02SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 10),
    _Component53PCRFClient02SwapAvailable_Type()
)
component53PCRFClient02SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02SwapAvailable.setStatus("current")
_Component53PCRFClient02Eth0InOctets_Type = Counter32
_Component53PCRFClient02Eth0InOctets_Object = MibScalar
component53PCRFClient02Eth0InOctets = _Component53PCRFClient02Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 11),
    _Component53PCRFClient02Eth0InOctets_Type()
)
component53PCRFClient02Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02Eth0InOctets.setStatus("current")
_Component53PCRFClient02Eth0OutOctets_Type = Counter32
_Component53PCRFClient02Eth0OutOctets_Object = MibScalar
component53PCRFClient02Eth0OutOctets = _Component53PCRFClient02Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 12),
    _Component53PCRFClient02Eth0OutOctets_Type()
)
component53PCRFClient02Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02Eth0OutOctets.setStatus("current")
_Component53PCRFClient02Eth1InOctets_Type = Counter32
_Component53PCRFClient02Eth1InOctets_Object = MibScalar
component53PCRFClient02Eth1InOctets = _Component53PCRFClient02Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 13),
    _Component53PCRFClient02Eth1InOctets_Type()
)
component53PCRFClient02Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02Eth1InOctets.setStatus("current")
_Component53PCRFClient02Eth1OutOctets_Type = Counter32
_Component53PCRFClient02Eth1OutOctets_Object = MibScalar
component53PCRFClient02Eth1OutOctets = _Component53PCRFClient02Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 22, 14),
    _Component53PCRFClient02Eth1OutOctets_Type()
)
component53PCRFClient02Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53PCRFClient02Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53SessionMgr01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53SessionMgr01 = _BroadhopProductsQNSComponents53SessionMgr01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31)
)
_Component53SessionMgr01CpuUser_Type = Integer32
_Component53SessionMgr01CpuUser_Object = MibScalar
component53SessionMgr01CpuUser = _Component53SessionMgr01CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 1),
    _Component53SessionMgr01CpuUser_Type()
)
component53SessionMgr01CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01CpuUser.setStatus("current")
_Component53SessionMgr01CpuSystem_Type = Integer32
_Component53SessionMgr01CpuSystem_Object = MibScalar
component53SessionMgr01CpuSystem = _Component53SessionMgr01CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 2),
    _Component53SessionMgr01CpuSystem_Type()
)
component53SessionMgr01CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01CpuSystem.setStatus("current")
_Component53SessionMgr01CpuIdle_Type = Integer32
_Component53SessionMgr01CpuIdle_Object = MibScalar
component53SessionMgr01CpuIdle = _Component53SessionMgr01CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 3),
    _Component53SessionMgr01CpuIdle_Type()
)
component53SessionMgr01CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01CpuIdle.setStatus("current")
_Component53SessionMgr01LoadAverage1_Type = Integer32
_Component53SessionMgr01LoadAverage1_Object = MibScalar
component53SessionMgr01LoadAverage1 = _Component53SessionMgr01LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 4),
    _Component53SessionMgr01LoadAverage1_Type()
)
component53SessionMgr01LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01LoadAverage1.setStatus("current")
_Component53SessionMgr01LoadAverage5_Type = Integer32
_Component53SessionMgr01LoadAverage5_Object = MibScalar
component53SessionMgr01LoadAverage5 = _Component53SessionMgr01LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 5),
    _Component53SessionMgr01LoadAverage5_Type()
)
component53SessionMgr01LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01LoadAverage5.setStatus("current")
_Component53SessionMgr01LoadAverage15_Type = Integer32
_Component53SessionMgr01LoadAverage15_Object = MibScalar
component53SessionMgr01LoadAverage15 = _Component53SessionMgr01LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 6),
    _Component53SessionMgr01LoadAverage15_Type()
)
component53SessionMgr01LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01LoadAverage15.setStatus("current")
_Component53SessionMgr01MemoryTotal_Type = Integer32
_Component53SessionMgr01MemoryTotal_Object = MibScalar
component53SessionMgr01MemoryTotal = _Component53SessionMgr01MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 7),
    _Component53SessionMgr01MemoryTotal_Type()
)
component53SessionMgr01MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01MemoryTotal.setStatus("current")
_Component53SessionMgr01MemoryAvailable_Type = Integer32
_Component53SessionMgr01MemoryAvailable_Object = MibScalar
component53SessionMgr01MemoryAvailable = _Component53SessionMgr01MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 8),
    _Component53SessionMgr01MemoryAvailable_Type()
)
component53SessionMgr01MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01MemoryAvailable.setStatus("current")
_Component53SessionMgr01SwapTotal_Type = Integer32
_Component53SessionMgr01SwapTotal_Object = MibScalar
component53SessionMgr01SwapTotal = _Component53SessionMgr01SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 9),
    _Component53SessionMgr01SwapTotal_Type()
)
component53SessionMgr01SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01SwapTotal.setStatus("current")
_Component53SessionMgr01SwapAvailable_Type = Integer32
_Component53SessionMgr01SwapAvailable_Object = MibScalar
component53SessionMgr01SwapAvailable = _Component53SessionMgr01SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 10),
    _Component53SessionMgr01SwapAvailable_Type()
)
component53SessionMgr01SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01SwapAvailable.setStatus("current")
_Component53SessionMgr01Eth0InOctets_Type = Counter32
_Component53SessionMgr01Eth0InOctets_Object = MibScalar
component53SessionMgr01Eth0InOctets = _Component53SessionMgr01Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 11),
    _Component53SessionMgr01Eth0InOctets_Type()
)
component53SessionMgr01Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01Eth0InOctets.setStatus("current")
_Component53SessionMgr01Eth0OutOctets_Type = Counter32
_Component53SessionMgr01Eth0OutOctets_Object = MibScalar
component53SessionMgr01Eth0OutOctets = _Component53SessionMgr01Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 12),
    _Component53SessionMgr01Eth0OutOctets_Type()
)
component53SessionMgr01Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01Eth0OutOctets.setStatus("current")
_Component53SessionMgr01Eth1InOctets_Type = Counter32
_Component53SessionMgr01Eth1InOctets_Object = MibScalar
component53SessionMgr01Eth1InOctets = _Component53SessionMgr01Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 13),
    _Component53SessionMgr01Eth1InOctets_Type()
)
component53SessionMgr01Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01Eth1InOctets.setStatus("current")
_Component53SessionMgr01Eth1OutOctets_Type = Counter32
_Component53SessionMgr01Eth1OutOctets_Object = MibScalar
component53SessionMgr01Eth1OutOctets = _Component53SessionMgr01Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 31, 14),
    _Component53SessionMgr01Eth1OutOctets_Type()
)
component53SessionMgr01Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr01Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53SessionMgr02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53SessionMgr02 = _BroadhopProductsQNSComponents53SessionMgr02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32)
)
_Component53SessionMgr02CpuUser_Type = Integer32
_Component53SessionMgr02CpuUser_Object = MibScalar
component53SessionMgr02CpuUser = _Component53SessionMgr02CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 1),
    _Component53SessionMgr02CpuUser_Type()
)
component53SessionMgr02CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02CpuUser.setStatus("current")
_Component53SessionMgr02CpuSystem_Type = Integer32
_Component53SessionMgr02CpuSystem_Object = MibScalar
component53SessionMgr02CpuSystem = _Component53SessionMgr02CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 2),
    _Component53SessionMgr02CpuSystem_Type()
)
component53SessionMgr02CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02CpuSystem.setStatus("current")
_Component53SessionMgr02CpuIdle_Type = Integer32
_Component53SessionMgr02CpuIdle_Object = MibScalar
component53SessionMgr02CpuIdle = _Component53SessionMgr02CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 3),
    _Component53SessionMgr02CpuIdle_Type()
)
component53SessionMgr02CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02CpuIdle.setStatus("current")
_Component53SessionMgr02LoadAverage1_Type = Integer32
_Component53SessionMgr02LoadAverage1_Object = MibScalar
component53SessionMgr02LoadAverage1 = _Component53SessionMgr02LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 4),
    _Component53SessionMgr02LoadAverage1_Type()
)
component53SessionMgr02LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02LoadAverage1.setStatus("current")
_Component53SessionMgr02LoadAverage5_Type = Integer32
_Component53SessionMgr02LoadAverage5_Object = MibScalar
component53SessionMgr02LoadAverage5 = _Component53SessionMgr02LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 5),
    _Component53SessionMgr02LoadAverage5_Type()
)
component53SessionMgr02LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02LoadAverage5.setStatus("current")
_Component53SessionMgr02LoadAverage15_Type = Integer32
_Component53SessionMgr02LoadAverage15_Object = MibScalar
component53SessionMgr02LoadAverage15 = _Component53SessionMgr02LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 6),
    _Component53SessionMgr02LoadAverage15_Type()
)
component53SessionMgr02LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02LoadAverage15.setStatus("current")
_Component53SessionMgr02MemoryTotal_Type = Integer32
_Component53SessionMgr02MemoryTotal_Object = MibScalar
component53SessionMgr02MemoryTotal = _Component53SessionMgr02MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 7),
    _Component53SessionMgr02MemoryTotal_Type()
)
component53SessionMgr02MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02MemoryTotal.setStatus("current")
_Component53SessionMgr02MemoryAvailable_Type = Integer32
_Component53SessionMgr02MemoryAvailable_Object = MibScalar
component53SessionMgr02MemoryAvailable = _Component53SessionMgr02MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 8),
    _Component53SessionMgr02MemoryAvailable_Type()
)
component53SessionMgr02MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02MemoryAvailable.setStatus("current")
_Component53SessionMgr02SwapTotal_Type = Integer32
_Component53SessionMgr02SwapTotal_Object = MibScalar
component53SessionMgr02SwapTotal = _Component53SessionMgr02SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 9),
    _Component53SessionMgr02SwapTotal_Type()
)
component53SessionMgr02SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02SwapTotal.setStatus("current")
_Component53SessionMgr02SwapAvailable_Type = Integer32
_Component53SessionMgr02SwapAvailable_Object = MibScalar
component53SessionMgr02SwapAvailable = _Component53SessionMgr02SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 10),
    _Component53SessionMgr02SwapAvailable_Type()
)
component53SessionMgr02SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02SwapAvailable.setStatus("current")
_Component53SessionMgr02Eth0InOctets_Type = Counter32
_Component53SessionMgr02Eth0InOctets_Object = MibScalar
component53SessionMgr02Eth0InOctets = _Component53SessionMgr02Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 11),
    _Component53SessionMgr02Eth0InOctets_Type()
)
component53SessionMgr02Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02Eth0InOctets.setStatus("current")
_Component53SessionMgr02Eth0OutOctets_Type = Counter32
_Component53SessionMgr02Eth0OutOctets_Object = MibScalar
component53SessionMgr02Eth0OutOctets = _Component53SessionMgr02Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 12),
    _Component53SessionMgr02Eth0OutOctets_Type()
)
component53SessionMgr02Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02Eth0OutOctets.setStatus("current")
_Component53SessionMgr02Eth1InOctets_Type = Counter32
_Component53SessionMgr02Eth1InOctets_Object = MibScalar
component53SessionMgr02Eth1InOctets = _Component53SessionMgr02Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 13),
    _Component53SessionMgr02Eth1InOctets_Type()
)
component53SessionMgr02Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02Eth1InOctets.setStatus("current")
_Component53SessionMgr02Eth1OutOctets_Type = Counter32
_Component53SessionMgr02Eth1OutOctets_Object = MibScalar
component53SessionMgr02Eth1OutOctets = _Component53SessionMgr02Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 32, 14),
    _Component53SessionMgr02Eth1OutOctets_Type()
)
component53SessionMgr02Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53SessionMgr02Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53QNS01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53QNS01 = _BroadhopProductsQNSComponents53QNS01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41)
)
_Component53QNS01CpuUser_Type = Integer32
_Component53QNS01CpuUser_Object = MibScalar
component53QNS01CpuUser = _Component53QNS01CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 1),
    _Component53QNS01CpuUser_Type()
)
component53QNS01CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01CpuUser.setStatus("current")
_Component53QNS01CpuSystem_Type = Integer32
_Component53QNS01CpuSystem_Object = MibScalar
component53QNS01CpuSystem = _Component53QNS01CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 2),
    _Component53QNS01CpuSystem_Type()
)
component53QNS01CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01CpuSystem.setStatus("current")
_Component53QNS01CpuIdle_Type = Integer32
_Component53QNS01CpuIdle_Object = MibScalar
component53QNS01CpuIdle = _Component53QNS01CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 3),
    _Component53QNS01CpuIdle_Type()
)
component53QNS01CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01CpuIdle.setStatus("current")
_Component53QNS01LoadAverage1_Type = Integer32
_Component53QNS01LoadAverage1_Object = MibScalar
component53QNS01LoadAverage1 = _Component53QNS01LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 4),
    _Component53QNS01LoadAverage1_Type()
)
component53QNS01LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01LoadAverage1.setStatus("current")
_Component53QNS01LoadAverage5_Type = Integer32
_Component53QNS01LoadAverage5_Object = MibScalar
component53QNS01LoadAverage5 = _Component53QNS01LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 5),
    _Component53QNS01LoadAverage5_Type()
)
component53QNS01LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01LoadAverage5.setStatus("current")
_Component53QNS01LoadAverage15_Type = Integer32
_Component53QNS01LoadAverage15_Object = MibScalar
component53QNS01LoadAverage15 = _Component53QNS01LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 6),
    _Component53QNS01LoadAverage15_Type()
)
component53QNS01LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01LoadAverage15.setStatus("current")
_Component53QNS01MemoryTotal_Type = Integer32
_Component53QNS01MemoryTotal_Object = MibScalar
component53QNS01MemoryTotal = _Component53QNS01MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 7),
    _Component53QNS01MemoryTotal_Type()
)
component53QNS01MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01MemoryTotal.setStatus("current")
_Component53QNS01MemoryAvailable_Type = Integer32
_Component53QNS01MemoryAvailable_Object = MibScalar
component53QNS01MemoryAvailable = _Component53QNS01MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 8),
    _Component53QNS01MemoryAvailable_Type()
)
component53QNS01MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01MemoryAvailable.setStatus("current")
_Component53QNS01SwapTotal_Type = Integer32
_Component53QNS01SwapTotal_Object = MibScalar
component53QNS01SwapTotal = _Component53QNS01SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 9),
    _Component53QNS01SwapTotal_Type()
)
component53QNS01SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01SwapTotal.setStatus("current")
_Component53QNS01SwapAvailable_Type = Integer32
_Component53QNS01SwapAvailable_Object = MibScalar
component53QNS01SwapAvailable = _Component53QNS01SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 10),
    _Component53QNS01SwapAvailable_Type()
)
component53QNS01SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01SwapAvailable.setStatus("current")
_Component53QNS01Eth0InOctets_Type = Counter32
_Component53QNS01Eth0InOctets_Object = MibScalar
component53QNS01Eth0InOctets = _Component53QNS01Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 11),
    _Component53QNS01Eth0InOctets_Type()
)
component53QNS01Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01Eth0InOctets.setStatus("current")
_Component53QNS01Eth0OutOctets_Type = Counter32
_Component53QNS01Eth0OutOctets_Object = MibScalar
component53QNS01Eth0OutOctets = _Component53QNS01Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 12),
    _Component53QNS01Eth0OutOctets_Type()
)
component53QNS01Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01Eth0OutOctets.setStatus("current")
_Component53QNS01Eth1InOctets_Type = Counter32
_Component53QNS01Eth1InOctets_Object = MibScalar
component53QNS01Eth1InOctets = _Component53QNS01Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 13),
    _Component53QNS01Eth1InOctets_Type()
)
component53QNS01Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01Eth1InOctets.setStatus("current")
_Component53QNS01Eth1OutOctets_Type = Counter32
_Component53QNS01Eth1OutOctets_Object = MibScalar
component53QNS01Eth1OutOctets = _Component53QNS01Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 41, 14),
    _Component53QNS01Eth1OutOctets_Type()
)
component53QNS01Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS01Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53QNS02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53QNS02 = _BroadhopProductsQNSComponents53QNS02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42)
)
_Component53QNS02CpuUser_Type = Integer32
_Component53QNS02CpuUser_Object = MibScalar
component53QNS02CpuUser = _Component53QNS02CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 1),
    _Component53QNS02CpuUser_Type()
)
component53QNS02CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02CpuUser.setStatus("current")
_Component53QNS02CpuSystem_Type = Integer32
_Component53QNS02CpuSystem_Object = MibScalar
component53QNS02CpuSystem = _Component53QNS02CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 2),
    _Component53QNS02CpuSystem_Type()
)
component53QNS02CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02CpuSystem.setStatus("current")
_Component53QNS02CpuIdle_Type = Integer32
_Component53QNS02CpuIdle_Object = MibScalar
component53QNS02CpuIdle = _Component53QNS02CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 3),
    _Component53QNS02CpuIdle_Type()
)
component53QNS02CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02CpuIdle.setStatus("current")
_Component53QNS02LoadAverage1_Type = Integer32
_Component53QNS02LoadAverage1_Object = MibScalar
component53QNS02LoadAverage1 = _Component53QNS02LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 4),
    _Component53QNS02LoadAverage1_Type()
)
component53QNS02LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02LoadAverage1.setStatus("current")
_Component53QNS02LoadAverage5_Type = Integer32
_Component53QNS02LoadAverage5_Object = MibScalar
component53QNS02LoadAverage5 = _Component53QNS02LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 5),
    _Component53QNS02LoadAverage5_Type()
)
component53QNS02LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02LoadAverage5.setStatus("current")
_Component53QNS02LoadAverage15_Type = Integer32
_Component53QNS02LoadAverage15_Object = MibScalar
component53QNS02LoadAverage15 = _Component53QNS02LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 6),
    _Component53QNS02LoadAverage15_Type()
)
component53QNS02LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02LoadAverage15.setStatus("current")
_Component53QNS02MemoryTotal_Type = Integer32
_Component53QNS02MemoryTotal_Object = MibScalar
component53QNS02MemoryTotal = _Component53QNS02MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 7),
    _Component53QNS02MemoryTotal_Type()
)
component53QNS02MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02MemoryTotal.setStatus("current")
_Component53QNS02MemoryAvailable_Type = Integer32
_Component53QNS02MemoryAvailable_Object = MibScalar
component53QNS02MemoryAvailable = _Component53QNS02MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 8),
    _Component53QNS02MemoryAvailable_Type()
)
component53QNS02MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02MemoryAvailable.setStatus("current")
_Component53QNS02SwapTotal_Type = Integer32
_Component53QNS02SwapTotal_Object = MibScalar
component53QNS02SwapTotal = _Component53QNS02SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 9),
    _Component53QNS02SwapTotal_Type()
)
component53QNS02SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02SwapTotal.setStatus("current")
_Component53QNS02SwapAvailable_Type = Integer32
_Component53QNS02SwapAvailable_Object = MibScalar
component53QNS02SwapAvailable = _Component53QNS02SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 10),
    _Component53QNS02SwapAvailable_Type()
)
component53QNS02SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02SwapAvailable.setStatus("current")
_Component53QNS02Eth0InOctets_Type = Counter32
_Component53QNS02Eth0InOctets_Object = MibScalar
component53QNS02Eth0InOctets = _Component53QNS02Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 11),
    _Component53QNS02Eth0InOctets_Type()
)
component53QNS02Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02Eth0InOctets.setStatus("current")
_Component53QNS02Eth0OutOctets_Type = Counter32
_Component53QNS02Eth0OutOctets_Object = MibScalar
component53QNS02Eth0OutOctets = _Component53QNS02Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 12),
    _Component53QNS02Eth0OutOctets_Type()
)
component53QNS02Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02Eth0OutOctets.setStatus("current")
_Component53QNS02Eth1InOctets_Type = Counter32
_Component53QNS02Eth1InOctets_Object = MibScalar
component53QNS02Eth1InOctets = _Component53QNS02Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 13),
    _Component53QNS02Eth1InOctets_Type()
)
component53QNS02Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02Eth1InOctets.setStatus("current")
_Component53QNS02Eth1OutOctets_Type = Counter32
_Component53QNS02Eth1OutOctets_Object = MibScalar
component53QNS02Eth1OutOctets = _Component53QNS02Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 42, 14),
    _Component53QNS02Eth1OutOctets_Type()
)
component53QNS02Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS02Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53QNS03_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53QNS03 = _BroadhopProductsQNSComponents53QNS03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43)
)
_Component53QNS03CpuUser_Type = Integer32
_Component53QNS03CpuUser_Object = MibScalar
component53QNS03CpuUser = _Component53QNS03CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 1),
    _Component53QNS03CpuUser_Type()
)
component53QNS03CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03CpuUser.setStatus("current")
_Component53QNS03CpuSystem_Type = Integer32
_Component53QNS03CpuSystem_Object = MibScalar
component53QNS03CpuSystem = _Component53QNS03CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 2),
    _Component53QNS03CpuSystem_Type()
)
component53QNS03CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03CpuSystem.setStatus("current")
_Component53QNS03CpuIdle_Type = Integer32
_Component53QNS03CpuIdle_Object = MibScalar
component53QNS03CpuIdle = _Component53QNS03CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 3),
    _Component53QNS03CpuIdle_Type()
)
component53QNS03CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03CpuIdle.setStatus("current")
_Component53QNS03LoadAverage1_Type = Integer32
_Component53QNS03LoadAverage1_Object = MibScalar
component53QNS03LoadAverage1 = _Component53QNS03LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 4),
    _Component53QNS03LoadAverage1_Type()
)
component53QNS03LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03LoadAverage1.setStatus("current")
_Component53QNS03LoadAverage5_Type = Integer32
_Component53QNS03LoadAverage5_Object = MibScalar
component53QNS03LoadAverage5 = _Component53QNS03LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 5),
    _Component53QNS03LoadAverage5_Type()
)
component53QNS03LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03LoadAverage5.setStatus("current")
_Component53QNS03LoadAverage15_Type = Integer32
_Component53QNS03LoadAverage15_Object = MibScalar
component53QNS03LoadAverage15 = _Component53QNS03LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 6),
    _Component53QNS03LoadAverage15_Type()
)
component53QNS03LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03LoadAverage15.setStatus("current")
_Component53QNS03MemoryTotal_Type = Integer32
_Component53QNS03MemoryTotal_Object = MibScalar
component53QNS03MemoryTotal = _Component53QNS03MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 7),
    _Component53QNS03MemoryTotal_Type()
)
component53QNS03MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03MemoryTotal.setStatus("current")
_Component53QNS03MemoryAvailable_Type = Integer32
_Component53QNS03MemoryAvailable_Object = MibScalar
component53QNS03MemoryAvailable = _Component53QNS03MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 8),
    _Component53QNS03MemoryAvailable_Type()
)
component53QNS03MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03MemoryAvailable.setStatus("current")
_Component53QNS03SwapTotal_Type = Integer32
_Component53QNS03SwapTotal_Object = MibScalar
component53QNS03SwapTotal = _Component53QNS03SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 9),
    _Component53QNS03SwapTotal_Type()
)
component53QNS03SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03SwapTotal.setStatus("current")
_Component53QNS03SwapAvailable_Type = Integer32
_Component53QNS03SwapAvailable_Object = MibScalar
component53QNS03SwapAvailable = _Component53QNS03SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 10),
    _Component53QNS03SwapAvailable_Type()
)
component53QNS03SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03SwapAvailable.setStatus("current")
_Component53QNS03Eth0InOctets_Type = Counter32
_Component53QNS03Eth0InOctets_Object = MibScalar
component53QNS03Eth0InOctets = _Component53QNS03Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 11),
    _Component53QNS03Eth0InOctets_Type()
)
component53QNS03Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03Eth0InOctets.setStatus("current")
_Component53QNS03Eth0OutOctets_Type = Counter32
_Component53QNS03Eth0OutOctets_Object = MibScalar
component53QNS03Eth0OutOctets = _Component53QNS03Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 12),
    _Component53QNS03Eth0OutOctets_Type()
)
component53QNS03Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03Eth0OutOctets.setStatus("current")
_Component53QNS03Eth1InOctets_Type = Counter32
_Component53QNS03Eth1InOctets_Object = MibScalar
component53QNS03Eth1InOctets = _Component53QNS03Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 13),
    _Component53QNS03Eth1InOctets_Type()
)
component53QNS03Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03Eth1InOctets.setStatus("current")
_Component53QNS03Eth1OutOctets_Type = Counter32
_Component53QNS03Eth1OutOctets_Object = MibScalar
component53QNS03Eth1OutOctets = _Component53QNS03Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 43, 14),
    _Component53QNS03Eth1OutOctets_Type()
)
component53QNS03Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS03Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53QNS04_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53QNS04 = _BroadhopProductsQNSComponents53QNS04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44)
)
_Component53QNS04CpuUser_Type = Integer32
_Component53QNS04CpuUser_Object = MibScalar
component53QNS04CpuUser = _Component53QNS04CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 1),
    _Component53QNS04CpuUser_Type()
)
component53QNS04CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04CpuUser.setStatus("current")
_Component53QNS04CpuSystem_Type = Integer32
_Component53QNS04CpuSystem_Object = MibScalar
component53QNS04CpuSystem = _Component53QNS04CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 2),
    _Component53QNS04CpuSystem_Type()
)
component53QNS04CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04CpuSystem.setStatus("current")
_Component53QNS04CpuIdle_Type = Integer32
_Component53QNS04CpuIdle_Object = MibScalar
component53QNS04CpuIdle = _Component53QNS04CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 3),
    _Component53QNS04CpuIdle_Type()
)
component53QNS04CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04CpuIdle.setStatus("current")
_Component53QNS04LoadAverage1_Type = Integer32
_Component53QNS04LoadAverage1_Object = MibScalar
component53QNS04LoadAverage1 = _Component53QNS04LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 4),
    _Component53QNS04LoadAverage1_Type()
)
component53QNS04LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04LoadAverage1.setStatus("current")
_Component53QNS04LoadAverage5_Type = Integer32
_Component53QNS04LoadAverage5_Object = MibScalar
component53QNS04LoadAverage5 = _Component53QNS04LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 5),
    _Component53QNS04LoadAverage5_Type()
)
component53QNS04LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04LoadAverage5.setStatus("current")
_Component53QNS04LoadAverage15_Type = Integer32
_Component53QNS04LoadAverage15_Object = MibScalar
component53QNS04LoadAverage15 = _Component53QNS04LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 6),
    _Component53QNS04LoadAverage15_Type()
)
component53QNS04LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04LoadAverage15.setStatus("current")
_Component53QNS04MemoryTotal_Type = Integer32
_Component53QNS04MemoryTotal_Object = MibScalar
component53QNS04MemoryTotal = _Component53QNS04MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 7),
    _Component53QNS04MemoryTotal_Type()
)
component53QNS04MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04MemoryTotal.setStatus("current")
_Component53QNS04MemoryAvailable_Type = Integer32
_Component53QNS04MemoryAvailable_Object = MibScalar
component53QNS04MemoryAvailable = _Component53QNS04MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 8),
    _Component53QNS04MemoryAvailable_Type()
)
component53QNS04MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04MemoryAvailable.setStatus("current")
_Component53QNS04SwapTotal_Type = Integer32
_Component53QNS04SwapTotal_Object = MibScalar
component53QNS04SwapTotal = _Component53QNS04SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 9),
    _Component53QNS04SwapTotal_Type()
)
component53QNS04SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04SwapTotal.setStatus("current")
_Component53QNS04SwapAvailable_Type = Integer32
_Component53QNS04SwapAvailable_Object = MibScalar
component53QNS04SwapAvailable = _Component53QNS04SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 10),
    _Component53QNS04SwapAvailable_Type()
)
component53QNS04SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04SwapAvailable.setStatus("current")
_Component53QNS04Eth0InOctets_Type = Counter32
_Component53QNS04Eth0InOctets_Object = MibScalar
component53QNS04Eth0InOctets = _Component53QNS04Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 11),
    _Component53QNS04Eth0InOctets_Type()
)
component53QNS04Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04Eth0InOctets.setStatus("current")
_Component53QNS04Eth0OutOctets_Type = Counter32
_Component53QNS04Eth0OutOctets_Object = MibScalar
component53QNS04Eth0OutOctets = _Component53QNS04Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 12),
    _Component53QNS04Eth0OutOctets_Type()
)
component53QNS04Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04Eth0OutOctets.setStatus("current")
_Component53QNS04Eth1InOctets_Type = Counter32
_Component53QNS04Eth1InOctets_Object = MibScalar
component53QNS04Eth1InOctets = _Component53QNS04Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 13),
    _Component53QNS04Eth1InOctets_Type()
)
component53QNS04Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04Eth1InOctets.setStatus("current")
_Component53QNS04Eth1OutOctets_Type = Counter32
_Component53QNS04Eth1OutOctets_Object = MibScalar
component53QNS04Eth1OutOctets = _Component53QNS04Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 44, 14),
    _Component53QNS04Eth1OutOctets_Type()
)
component53QNS04Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53QNS04Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53Portal01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53Portal01 = _BroadhopProductsQNSComponents53Portal01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51)
)
_Component53Portal01CpuUser_Type = Integer32
_Component53Portal01CpuUser_Object = MibScalar
component53Portal01CpuUser = _Component53Portal01CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 1),
    _Component53Portal01CpuUser_Type()
)
component53Portal01CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01CpuUser.setStatus("current")
_Component53Portal01CpuSystem_Type = Integer32
_Component53Portal01CpuSystem_Object = MibScalar
component53Portal01CpuSystem = _Component53Portal01CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 2),
    _Component53Portal01CpuSystem_Type()
)
component53Portal01CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01CpuSystem.setStatus("current")
_Component53Portal01CpuIdle_Type = Integer32
_Component53Portal01CpuIdle_Object = MibScalar
component53Portal01CpuIdle = _Component53Portal01CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 3),
    _Component53Portal01CpuIdle_Type()
)
component53Portal01CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01CpuIdle.setStatus("current")
_Component53Portal01LoadAverage1_Type = Integer32
_Component53Portal01LoadAverage1_Object = MibScalar
component53Portal01LoadAverage1 = _Component53Portal01LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 4),
    _Component53Portal01LoadAverage1_Type()
)
component53Portal01LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01LoadAverage1.setStatus("current")
_Component53Portal01LoadAverage5_Type = Integer32
_Component53Portal01LoadAverage5_Object = MibScalar
component53Portal01LoadAverage5 = _Component53Portal01LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 5),
    _Component53Portal01LoadAverage5_Type()
)
component53Portal01LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01LoadAverage5.setStatus("current")
_Component53Portal01LoadAverage15_Type = Integer32
_Component53Portal01LoadAverage15_Object = MibScalar
component53Portal01LoadAverage15 = _Component53Portal01LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 6),
    _Component53Portal01LoadAverage15_Type()
)
component53Portal01LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01LoadAverage15.setStatus("current")
_Component53Portal01MemoryTotal_Type = Integer32
_Component53Portal01MemoryTotal_Object = MibScalar
component53Portal01MemoryTotal = _Component53Portal01MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 7),
    _Component53Portal01MemoryTotal_Type()
)
component53Portal01MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01MemoryTotal.setStatus("current")
_Component53Portal01MemoryAvailable_Type = Integer32
_Component53Portal01MemoryAvailable_Object = MibScalar
component53Portal01MemoryAvailable = _Component53Portal01MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 8),
    _Component53Portal01MemoryAvailable_Type()
)
component53Portal01MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01MemoryAvailable.setStatus("current")
_Component53Portal01SwapTotal_Type = Integer32
_Component53Portal01SwapTotal_Object = MibScalar
component53Portal01SwapTotal = _Component53Portal01SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 9),
    _Component53Portal01SwapTotal_Type()
)
component53Portal01SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01SwapTotal.setStatus("current")
_Component53Portal01SwapAvailable_Type = Integer32
_Component53Portal01SwapAvailable_Object = MibScalar
component53Portal01SwapAvailable = _Component53Portal01SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 10),
    _Component53Portal01SwapAvailable_Type()
)
component53Portal01SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01SwapAvailable.setStatus("current")
_Component53Portal01Eth0InOctets_Type = Counter32
_Component53Portal01Eth0InOctets_Object = MibScalar
component53Portal01Eth0InOctets = _Component53Portal01Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 11),
    _Component53Portal01Eth0InOctets_Type()
)
component53Portal01Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01Eth0InOctets.setStatus("current")
_Component53Portal01Eth0OutOctets_Type = Counter32
_Component53Portal01Eth0OutOctets_Object = MibScalar
component53Portal01Eth0OutOctets = _Component53Portal01Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 12),
    _Component53Portal01Eth0OutOctets_Type()
)
component53Portal01Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01Eth0OutOctets.setStatus("current")
_Component53Portal01Eth1InOctets_Type = Counter32
_Component53Portal01Eth1InOctets_Object = MibScalar
component53Portal01Eth1InOctets = _Component53Portal01Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 13),
    _Component53Portal01Eth1InOctets_Type()
)
component53Portal01Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01Eth1InOctets.setStatus("current")
_Component53Portal01Eth1OutOctets_Type = Counter32
_Component53Portal01Eth1OutOctets_Object = MibScalar
component53Portal01Eth1OutOctets = _Component53Portal01Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 51, 14),
    _Component53Portal01Eth1OutOctets_Type()
)
component53Portal01Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal01Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSComponents53Portal02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSComponents53Portal02 = _BroadhopProductsQNSComponents53Portal02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52)
)
_Component53Portal02CpuUser_Type = Integer32
_Component53Portal02CpuUser_Object = MibScalar
component53Portal02CpuUser = _Component53Portal02CpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 1),
    _Component53Portal02CpuUser_Type()
)
component53Portal02CpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02CpuUser.setStatus("current")
_Component53Portal02CpuSystem_Type = Integer32
_Component53Portal02CpuSystem_Object = MibScalar
component53Portal02CpuSystem = _Component53Portal02CpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 2),
    _Component53Portal02CpuSystem_Type()
)
component53Portal02CpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02CpuSystem.setStatus("current")
_Component53Portal02CpuIdle_Type = Integer32
_Component53Portal02CpuIdle_Object = MibScalar
component53Portal02CpuIdle = _Component53Portal02CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 3),
    _Component53Portal02CpuIdle_Type()
)
component53Portal02CpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02CpuIdle.setStatus("current")
_Component53Portal02LoadAverage1_Type = Integer32
_Component53Portal02LoadAverage1_Object = MibScalar
component53Portal02LoadAverage1 = _Component53Portal02LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 4),
    _Component53Portal02LoadAverage1_Type()
)
component53Portal02LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02LoadAverage1.setStatus("current")
_Component53Portal02LoadAverage5_Type = Integer32
_Component53Portal02LoadAverage5_Object = MibScalar
component53Portal02LoadAverage5 = _Component53Portal02LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 5),
    _Component53Portal02LoadAverage5_Type()
)
component53Portal02LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02LoadAverage5.setStatus("current")
_Component53Portal02LoadAverage15_Type = Integer32
_Component53Portal02LoadAverage15_Object = MibScalar
component53Portal02LoadAverage15 = _Component53Portal02LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 6),
    _Component53Portal02LoadAverage15_Type()
)
component53Portal02LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02LoadAverage15.setStatus("current")
_Component53Portal02MemoryTotal_Type = Integer32
_Component53Portal02MemoryTotal_Object = MibScalar
component53Portal02MemoryTotal = _Component53Portal02MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 7),
    _Component53Portal02MemoryTotal_Type()
)
component53Portal02MemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02MemoryTotal.setStatus("current")
_Component53Portal02MemoryAvailable_Type = Integer32
_Component53Portal02MemoryAvailable_Object = MibScalar
component53Portal02MemoryAvailable = _Component53Portal02MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 8),
    _Component53Portal02MemoryAvailable_Type()
)
component53Portal02MemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02MemoryAvailable.setStatus("current")
_Component53Portal02SwapTotal_Type = Integer32
_Component53Portal02SwapTotal_Object = MibScalar
component53Portal02SwapTotal = _Component53Portal02SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 9),
    _Component53Portal02SwapTotal_Type()
)
component53Portal02SwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02SwapTotal.setStatus("current")
_Component53Portal02SwapAvailable_Type = Integer32
_Component53Portal02SwapAvailable_Object = MibScalar
component53Portal02SwapAvailable = _Component53Portal02SwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 10),
    _Component53Portal02SwapAvailable_Type()
)
component53Portal02SwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02SwapAvailable.setStatus("current")
_Component53Portal02Eth0InOctets_Type = Counter32
_Component53Portal02Eth0InOctets_Object = MibScalar
component53Portal02Eth0InOctets = _Component53Portal02Eth0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 11),
    _Component53Portal02Eth0InOctets_Type()
)
component53Portal02Eth0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02Eth0InOctets.setStatus("current")
_Component53Portal02Eth0OutOctets_Type = Counter32
_Component53Portal02Eth0OutOctets_Object = MibScalar
component53Portal02Eth0OutOctets = _Component53Portal02Eth0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 12),
    _Component53Portal02Eth0OutOctets_Type()
)
component53Portal02Eth0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02Eth0OutOctets.setStatus("current")
_Component53Portal02Eth1InOctets_Type = Counter32
_Component53Portal02Eth1InOctets_Object = MibScalar
component53Portal02Eth1InOctets = _Component53Portal02Eth1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 13),
    _Component53Portal02Eth1InOctets_Type()
)
component53Portal02Eth1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02Eth1InOctets.setStatus("current")
_Component53Portal02Eth1OutOctets_Type = Counter32
_Component53Portal02Eth1OutOctets_Object = MibScalar
component53Portal02Eth1OutOctets = _Component53Portal02Eth1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2, 53, 52, 14),
    _Component53Portal02Eth1OutOctets_Type()
)
component53Portal02Eth1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component53Portal02Eth1OutOctets.setStatus("current")
_BroadhopProductsQNSConsolidatedKPIVersion_ObjectIdentity = ObjectIdentity
broadhopProductsQNSConsolidatedKPIVersion = _BroadhopProductsQNSConsolidatedKPIVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3)
)
_BroadhopProductsQNSConsolidatedKPI52_ObjectIdentity = ObjectIdentity
broadhopProductsQNSConsolidatedKPI52 = _BroadhopProductsQNSConsolidatedKPI52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52)
)
_ConsolidatedKPI52QNS_ObjectIdentity = ObjectIdentity
consolidatedKPI52QNS = _ConsolidatedKPI52QNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1)
)
_ConsolidatedKPI52QNS01_ObjectIdentity = ObjectIdentity
consolidatedKPI52QNS01 = _ConsolidatedKPI52QNS01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1)
)
_Kpi52QNS01RealServerStatus_Type = Gauge32
_Kpi52QNS01RealServerStatus_Object = MibScalar
kpi52QNS01RealServerStatus = _Kpi52QNS01RealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 1),
    _Kpi52QNS01RealServerStatus_Type()
)
kpi52QNS01RealServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01RealServerStatus.setStatus("current")
_Kpi52QNS01CreateEntryAvgTime_Type = DisplayString
_Kpi52QNS01CreateEntryAvgTime_Object = MibScalar
kpi52QNS01CreateEntryAvgTime = _Kpi52QNS01CreateEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 2),
    _Kpi52QNS01CreateEntryAvgTime_Type()
)
kpi52QNS01CreateEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01CreateEntryAvgTime.setStatus("current")
_Kpi52QNS01CreateEntrySuccess_Type = DisplayString
_Kpi52QNS01CreateEntrySuccess_Object = MibScalar
kpi52QNS01CreateEntrySuccess = _Kpi52QNS01CreateEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 3),
    _Kpi52QNS01CreateEntrySuccess_Type()
)
kpi52QNS01CreateEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01CreateEntrySuccess.setStatus("current")
_Kpi52QNS01DeleteEntryAvgTime_Type = DisplayString
_Kpi52QNS01DeleteEntryAvgTime_Object = MibScalar
kpi52QNS01DeleteEntryAvgTime = _Kpi52QNS01DeleteEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 4),
    _Kpi52QNS01DeleteEntryAvgTime_Type()
)
kpi52QNS01DeleteEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01DeleteEntryAvgTime.setStatus("current")
_Kpi52QNS01DeleteEntrySuccess_Type = DisplayString
_Kpi52QNS01DeleteEntrySuccess_Object = MibScalar
kpi52QNS01DeleteEntrySuccess = _Kpi52QNS01DeleteEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 5),
    _Kpi52QNS01DeleteEntrySuccess_Type()
)
kpi52QNS01DeleteEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01DeleteEntrySuccess.setStatus("current")
_Kpi52QNS01GetSessionActionAvgTime_Type = DisplayString
_Kpi52QNS01GetSessionActionAvgTime_Object = MibScalar
kpi52QNS01GetSessionActionAvgTime = _Kpi52QNS01GetSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 6),
    _Kpi52QNS01GetSessionActionAvgTime_Type()
)
kpi52QNS01GetSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01GetSessionActionAvgTime.setStatus("current")
_Kpi52QNS01GetSessionActionSuccess_Type = DisplayString
_Kpi52QNS01GetSessionActionSuccess_Object = MibScalar
kpi52QNS01GetSessionActionSuccess = _Kpi52QNS01GetSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 7),
    _Kpi52QNS01GetSessionActionSuccess_Type()
)
kpi52QNS01GetSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01GetSessionActionSuccess.setStatus("current")
_Kpi52QNS01LockSessionActionAvgTime_Type = DisplayString
_Kpi52QNS01LockSessionActionAvgTime_Object = MibScalar
kpi52QNS01LockSessionActionAvgTime = _Kpi52QNS01LockSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 8),
    _Kpi52QNS01LockSessionActionAvgTime_Type()
)
kpi52QNS01LockSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01LockSessionActionAvgTime.setStatus("current")
_Kpi52QNS01LockSessionActionSuccess_Type = DisplayString
_Kpi52QNS01LockSessionActionSuccess_Object = MibScalar
kpi52QNS01LockSessionActionSuccess = _Kpi52QNS01LockSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 9),
    _Kpi52QNS01LockSessionActionSuccess_Type()
)
kpi52QNS01LockSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01LockSessionActionSuccess.setStatus("current")
_Kpi52QNS01PushQuotaAvgTime_Type = DisplayString
_Kpi52QNS01PushQuotaAvgTime_Object = MibScalar
kpi52QNS01PushQuotaAvgTime = _Kpi52QNS01PushQuotaAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 10),
    _Kpi52QNS01PushQuotaAvgTime_Type()
)
kpi52QNS01PushQuotaAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01PushQuotaAvgTime.setStatus("current")
_Kpi52QNS01PushQuotaSuccess_Type = DisplayString
_Kpi52QNS01PushQuotaSuccess_Object = MibScalar
kpi52QNS01PushQuotaSuccess = _Kpi52QNS01PushQuotaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 11),
    _Kpi52QNS01PushQuotaSuccess_Type()
)
kpi52QNS01PushQuotaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01PushQuotaSuccess.setStatus("current")
_Kpi52QNS01QuotaCalculationAvgTime_Type = DisplayString
_Kpi52QNS01QuotaCalculationAvgTime_Object = MibScalar
kpi52QNS01QuotaCalculationAvgTime = _Kpi52QNS01QuotaCalculationAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 12),
    _Kpi52QNS01QuotaCalculationAvgTime_Type()
)
kpi52QNS01QuotaCalculationAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01QuotaCalculationAvgTime.setStatus("current")
_Kpi52QNS01QuotaCalculationSuccess_Type = DisplayString
_Kpi52QNS01QuotaCalculationSuccess_Object = MibScalar
kpi52QNS01QuotaCalculationSuccess = _Kpi52QNS01QuotaCalculationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 13),
    _Kpi52QNS01QuotaCalculationSuccess_Type()
)
kpi52QNS01QuotaCalculationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01QuotaCalculationSuccess.setStatus("current")
_Kpi52QNS01QuotaDepletedRequestAvgTime_Type = DisplayString
_Kpi52QNS01QuotaDepletedRequestAvgTime_Object = MibScalar
kpi52QNS01QuotaDepletedRequestAvgTime = _Kpi52QNS01QuotaDepletedRequestAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 14),
    _Kpi52QNS01QuotaDepletedRequestAvgTime_Type()
)
kpi52QNS01QuotaDepletedRequestAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01QuotaDepletedRequestAvgTime.setStatus("current")
_Kpi52QNS01QuotaDepletedRequestSucccess_Type = DisplayString
_Kpi52QNS01QuotaDepletedRequestSucccess_Object = MibScalar
kpi52QNS01QuotaDepletedRequestSucccess = _Kpi52QNS01QuotaDepletedRequestSucccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 15),
    _Kpi52QNS01QuotaDepletedRequestSucccess_Type()
)
kpi52QNS01QuotaDepletedRequestSucccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01QuotaDepletedRequestSucccess.setStatus("current")
_Kpi52QNS01RadiusAccountingMessageAvgTime_Type = DisplayString
_Kpi52QNS01RadiusAccountingMessageAvgTime_Object = MibScalar
kpi52QNS01RadiusAccountingMessageAvgTime = _Kpi52QNS01RadiusAccountingMessageAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 16),
    _Kpi52QNS01RadiusAccountingMessageAvgTime_Type()
)
kpi52QNS01RadiusAccountingMessageAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01RadiusAccountingMessageAvgTime.setStatus("current")
_Kpi52QNS01RadiusAccountingMessageSuccess_Type = DisplayString
_Kpi52QNS01RadiusAccountingMessageSuccess_Object = MibScalar
kpi52QNS01RadiusAccountingMessageSuccess = _Kpi52QNS01RadiusAccountingMessageSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 17),
    _Kpi52QNS01RadiusAccountingMessageSuccess_Type()
)
kpi52QNS01RadiusAccountingMessageSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01RadiusAccountingMessageSuccess.setStatus("current")
_Kpi52QNS01RetrieveSumAvPairAvgTime_Type = DisplayString
_Kpi52QNS01RetrieveSumAvPairAvgTime_Object = MibScalar
kpi52QNS01RetrieveSumAvPairAvgTime = _Kpi52QNS01RetrieveSumAvPairAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 18),
    _Kpi52QNS01RetrieveSumAvPairAvgTime_Type()
)
kpi52QNS01RetrieveSumAvPairAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01RetrieveSumAvPairAvgTime.setStatus("current")
_Kpi52QNS01RetrieveSumAvPairSuccess_Type = DisplayString
_Kpi52QNS01RetrieveSumAvPairSuccess_Object = MibScalar
kpi52QNS01RetrieveSumAvPairSuccess = _Kpi52QNS01RetrieveSumAvPairSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 19),
    _Kpi52QNS01RetrieveSumAvPairSuccess_Type()
)
kpi52QNS01RetrieveSumAvPairSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01RetrieveSumAvPairSuccess.setStatus("current")
_Kpi52QNS01PolicyCount_Type = DisplayString
_Kpi52QNS01PolicyCount_Object = MibScalar
kpi52QNS01PolicyCount = _Kpi52QNS01PolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 20),
    _Kpi52QNS01PolicyCount_Type()
)
kpi52QNS01PolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01PolicyCount.setStatus("current")
_Kpi52QNS01QueueSize_Type = DisplayString
_Kpi52QNS01QueueSize_Object = MibScalar
kpi52QNS01QueueSize = _Kpi52QNS01QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 21),
    _Kpi52QNS01QueueSize_Type()
)
kpi52QNS01QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01QueueSize.setStatus("current")
_Kpi52QNS01FailedEnqueueCount_Type = DisplayString
_Kpi52QNS01FailedEnqueueCount_Object = MibScalar
kpi52QNS01FailedEnqueueCount = _Kpi52QNS01FailedEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 22),
    _Kpi52QNS01FailedEnqueueCount_Type()
)
kpi52QNS01FailedEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01FailedEnqueueCount.setStatus("current")
_Kpi52QNS01ErrorCount_Type = DisplayString
_Kpi52QNS01ErrorCount_Object = MibScalar
kpi52QNS01ErrorCount = _Kpi52QNS01ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 23),
    _Kpi52QNS01ErrorCount_Type()
)
kpi52QNS01ErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01ErrorCount.setStatus("current")
_Kpi52QNS01SessionCount_Type = DisplayString
_Kpi52QNS01SessionCount_Object = MibScalar
kpi52QNS01SessionCount = _Kpi52QNS01SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 24),
    _Kpi52QNS01SessionCount_Type()
)
kpi52QNS01SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01SessionCount.setStatus("current")
_Kpi52QNS01FreeMemory_Type = DisplayString
_Kpi52QNS01FreeMemory_Object = MibScalar
kpi52QNS01FreeMemory = _Kpi52QNS01FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 1, 25),
    _Kpi52QNS01FreeMemory_Type()
)
kpi52QNS01FreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS01FreeMemory.setStatus("current")
_ConsolidatedKPI52QNS02_ObjectIdentity = ObjectIdentity
consolidatedKPI52QNS02 = _ConsolidatedKPI52QNS02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2)
)
_Kpi52QNS02RealServerStatus_Type = Gauge32
_Kpi52QNS02RealServerStatus_Object = MibScalar
kpi52QNS02RealServerStatus = _Kpi52QNS02RealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 1),
    _Kpi52QNS02RealServerStatus_Type()
)
kpi52QNS02RealServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02RealServerStatus.setStatus("current")
_Kpi52QNS02CreateEntryAvgTime_Type = DisplayString
_Kpi52QNS02CreateEntryAvgTime_Object = MibScalar
kpi52QNS02CreateEntryAvgTime = _Kpi52QNS02CreateEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 2),
    _Kpi52QNS02CreateEntryAvgTime_Type()
)
kpi52QNS02CreateEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02CreateEntryAvgTime.setStatus("current")
_Kpi52QNS02CreateEntrySuccess_Type = DisplayString
_Kpi52QNS02CreateEntrySuccess_Object = MibScalar
kpi52QNS02CreateEntrySuccess = _Kpi52QNS02CreateEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 3),
    _Kpi52QNS02CreateEntrySuccess_Type()
)
kpi52QNS02CreateEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02CreateEntrySuccess.setStatus("current")
_Kpi52QNS02DeleteEntryAvgTime_Type = DisplayString
_Kpi52QNS02DeleteEntryAvgTime_Object = MibScalar
kpi52QNS02DeleteEntryAvgTime = _Kpi52QNS02DeleteEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 4),
    _Kpi52QNS02DeleteEntryAvgTime_Type()
)
kpi52QNS02DeleteEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02DeleteEntryAvgTime.setStatus("current")
_Kpi52QNS02DeleteEntrySuccess_Type = DisplayString
_Kpi52QNS02DeleteEntrySuccess_Object = MibScalar
kpi52QNS02DeleteEntrySuccess = _Kpi52QNS02DeleteEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 5),
    _Kpi52QNS02DeleteEntrySuccess_Type()
)
kpi52QNS02DeleteEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02DeleteEntrySuccess.setStatus("current")
_Kpi52QNS02GetSessionActionAvgTime_Type = DisplayString
_Kpi52QNS02GetSessionActionAvgTime_Object = MibScalar
kpi52QNS02GetSessionActionAvgTime = _Kpi52QNS02GetSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 6),
    _Kpi52QNS02GetSessionActionAvgTime_Type()
)
kpi52QNS02GetSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02GetSessionActionAvgTime.setStatus("current")
_Kpi52QNS02GetSessionActionSuccess_Type = DisplayString
_Kpi52QNS02GetSessionActionSuccess_Object = MibScalar
kpi52QNS02GetSessionActionSuccess = _Kpi52QNS02GetSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 7),
    _Kpi52QNS02GetSessionActionSuccess_Type()
)
kpi52QNS02GetSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02GetSessionActionSuccess.setStatus("current")
_Kpi52QNS02LockSessionActionAvgTime_Type = DisplayString
_Kpi52QNS02LockSessionActionAvgTime_Object = MibScalar
kpi52QNS02LockSessionActionAvgTime = _Kpi52QNS02LockSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 8),
    _Kpi52QNS02LockSessionActionAvgTime_Type()
)
kpi52QNS02LockSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02LockSessionActionAvgTime.setStatus("current")
_Kpi52QNS02LockSessionActionSuccess_Type = DisplayString
_Kpi52QNS02LockSessionActionSuccess_Object = MibScalar
kpi52QNS02LockSessionActionSuccess = _Kpi52QNS02LockSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 9),
    _Kpi52QNS02LockSessionActionSuccess_Type()
)
kpi52QNS02LockSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02LockSessionActionSuccess.setStatus("current")
_Kpi52QNS02PushQuotaAvgTime_Type = DisplayString
_Kpi52QNS02PushQuotaAvgTime_Object = MibScalar
kpi52QNS02PushQuotaAvgTime = _Kpi52QNS02PushQuotaAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 10),
    _Kpi52QNS02PushQuotaAvgTime_Type()
)
kpi52QNS02PushQuotaAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02PushQuotaAvgTime.setStatus("current")
_Kpi52QNS02PushQuotaSuccess_Type = DisplayString
_Kpi52QNS02PushQuotaSuccess_Object = MibScalar
kpi52QNS02PushQuotaSuccess = _Kpi52QNS02PushQuotaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 11),
    _Kpi52QNS02PushQuotaSuccess_Type()
)
kpi52QNS02PushQuotaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02PushQuotaSuccess.setStatus("current")
_Kpi52QNS02QuotaCalculationAvgTime_Type = DisplayString
_Kpi52QNS02QuotaCalculationAvgTime_Object = MibScalar
kpi52QNS02QuotaCalculationAvgTime = _Kpi52QNS02QuotaCalculationAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 12),
    _Kpi52QNS02QuotaCalculationAvgTime_Type()
)
kpi52QNS02QuotaCalculationAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02QuotaCalculationAvgTime.setStatus("current")
_Kpi52QNS02QuotaCalculationSuccess_Type = DisplayString
_Kpi52QNS02QuotaCalculationSuccess_Object = MibScalar
kpi52QNS02QuotaCalculationSuccess = _Kpi52QNS02QuotaCalculationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 13),
    _Kpi52QNS02QuotaCalculationSuccess_Type()
)
kpi52QNS02QuotaCalculationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02QuotaCalculationSuccess.setStatus("current")
_Kpi52QNS02QuotaDepletedRequestAvgTime_Type = DisplayString
_Kpi52QNS02QuotaDepletedRequestAvgTime_Object = MibScalar
kpi52QNS02QuotaDepletedRequestAvgTime = _Kpi52QNS02QuotaDepletedRequestAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 14),
    _Kpi52QNS02QuotaDepletedRequestAvgTime_Type()
)
kpi52QNS02QuotaDepletedRequestAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02QuotaDepletedRequestAvgTime.setStatus("current")
_Kpi52QNS02QuotaDepletedRequestSucccess_Type = DisplayString
_Kpi52QNS02QuotaDepletedRequestSucccess_Object = MibScalar
kpi52QNS02QuotaDepletedRequestSucccess = _Kpi52QNS02QuotaDepletedRequestSucccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 15),
    _Kpi52QNS02QuotaDepletedRequestSucccess_Type()
)
kpi52QNS02QuotaDepletedRequestSucccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02QuotaDepletedRequestSucccess.setStatus("current")
_Kpi52QNS02RadiusAccountingMessageAvgTime_Type = DisplayString
_Kpi52QNS02RadiusAccountingMessageAvgTime_Object = MibScalar
kpi52QNS02RadiusAccountingMessageAvgTime = _Kpi52QNS02RadiusAccountingMessageAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 16),
    _Kpi52QNS02RadiusAccountingMessageAvgTime_Type()
)
kpi52QNS02RadiusAccountingMessageAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02RadiusAccountingMessageAvgTime.setStatus("current")
_Kpi52QNS02RadiusAccountingMessageSuccess_Type = DisplayString
_Kpi52QNS02RadiusAccountingMessageSuccess_Object = MibScalar
kpi52QNS02RadiusAccountingMessageSuccess = _Kpi52QNS02RadiusAccountingMessageSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 17),
    _Kpi52QNS02RadiusAccountingMessageSuccess_Type()
)
kpi52QNS02RadiusAccountingMessageSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02RadiusAccountingMessageSuccess.setStatus("current")
_Kpi52QNS02RetrieveSumAvPairAvgTime_Type = DisplayString
_Kpi52QNS02RetrieveSumAvPairAvgTime_Object = MibScalar
kpi52QNS02RetrieveSumAvPairAvgTime = _Kpi52QNS02RetrieveSumAvPairAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 18),
    _Kpi52QNS02RetrieveSumAvPairAvgTime_Type()
)
kpi52QNS02RetrieveSumAvPairAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02RetrieveSumAvPairAvgTime.setStatus("current")
_Kpi52QNS02RetrieveSumAvPairSuccess_Type = DisplayString
_Kpi52QNS02RetrieveSumAvPairSuccess_Object = MibScalar
kpi52QNS02RetrieveSumAvPairSuccess = _Kpi52QNS02RetrieveSumAvPairSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 19),
    _Kpi52QNS02RetrieveSumAvPairSuccess_Type()
)
kpi52QNS02RetrieveSumAvPairSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02RetrieveSumAvPairSuccess.setStatus("current")
_Kpi52QNS02PolicyCount_Type = DisplayString
_Kpi52QNS02PolicyCount_Object = MibScalar
kpi52QNS02PolicyCount = _Kpi52QNS02PolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 20),
    _Kpi52QNS02PolicyCount_Type()
)
kpi52QNS02PolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02PolicyCount.setStatus("current")
_Kpi52QNS02QueueSize_Type = DisplayString
_Kpi52QNS02QueueSize_Object = MibScalar
kpi52QNS02QueueSize = _Kpi52QNS02QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 21),
    _Kpi52QNS02QueueSize_Type()
)
kpi52QNS02QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02QueueSize.setStatus("current")
_Kpi52QNS02FailedEnqueueCount_Type = DisplayString
_Kpi52QNS02FailedEnqueueCount_Object = MibScalar
kpi52QNS02FailedEnqueueCount = _Kpi52QNS02FailedEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 22),
    _Kpi52QNS02FailedEnqueueCount_Type()
)
kpi52QNS02FailedEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02FailedEnqueueCount.setStatus("current")
_Kpi52QNS02ErrorCount_Type = DisplayString
_Kpi52QNS02ErrorCount_Object = MibScalar
kpi52QNS02ErrorCount = _Kpi52QNS02ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 23),
    _Kpi52QNS02ErrorCount_Type()
)
kpi52QNS02ErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02ErrorCount.setStatus("current")
_Kpi52QNS02SessionCount_Type = DisplayString
_Kpi52QNS02SessionCount_Object = MibScalar
kpi52QNS02SessionCount = _Kpi52QNS02SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 24),
    _Kpi52QNS02SessionCount_Type()
)
kpi52QNS02SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02SessionCount.setStatus("current")
_Kpi52QNS02FreeMemory_Type = DisplayString
_Kpi52QNS02FreeMemory_Object = MibScalar
kpi52QNS02FreeMemory = _Kpi52QNS02FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 2, 25),
    _Kpi52QNS02FreeMemory_Type()
)
kpi52QNS02FreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS02FreeMemory.setStatus("current")
_ConsolidatedKPI52QNS03_ObjectIdentity = ObjectIdentity
consolidatedKPI52QNS03 = _ConsolidatedKPI52QNS03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3)
)
_Kpi52QNS03RealServerStatus_Type = Gauge32
_Kpi52QNS03RealServerStatus_Object = MibScalar
kpi52QNS03RealServerStatus = _Kpi52QNS03RealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 1),
    _Kpi52QNS03RealServerStatus_Type()
)
kpi52QNS03RealServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03RealServerStatus.setStatus("current")
_Kpi52QNS03CreateEntryAvgTime_Type = DisplayString
_Kpi52QNS03CreateEntryAvgTime_Object = MibScalar
kpi52QNS03CreateEntryAvgTime = _Kpi52QNS03CreateEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 2),
    _Kpi52QNS03CreateEntryAvgTime_Type()
)
kpi52QNS03CreateEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03CreateEntryAvgTime.setStatus("current")
_Kpi52QNS03CreateEntrySuccess_Type = DisplayString
_Kpi52QNS03CreateEntrySuccess_Object = MibScalar
kpi52QNS03CreateEntrySuccess = _Kpi52QNS03CreateEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 3),
    _Kpi52QNS03CreateEntrySuccess_Type()
)
kpi52QNS03CreateEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03CreateEntrySuccess.setStatus("current")
_Kpi52QNS03DeleteEntryAvgTime_Type = DisplayString
_Kpi52QNS03DeleteEntryAvgTime_Object = MibScalar
kpi52QNS03DeleteEntryAvgTime = _Kpi52QNS03DeleteEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 4),
    _Kpi52QNS03DeleteEntryAvgTime_Type()
)
kpi52QNS03DeleteEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03DeleteEntryAvgTime.setStatus("current")
_Kpi52QNS03DeleteEntrySuccess_Type = DisplayString
_Kpi52QNS03DeleteEntrySuccess_Object = MibScalar
kpi52QNS03DeleteEntrySuccess = _Kpi52QNS03DeleteEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 5),
    _Kpi52QNS03DeleteEntrySuccess_Type()
)
kpi52QNS03DeleteEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03DeleteEntrySuccess.setStatus("current")
_Kpi52QNS03GetSessionActionAvgTime_Type = DisplayString
_Kpi52QNS03GetSessionActionAvgTime_Object = MibScalar
kpi52QNS03GetSessionActionAvgTime = _Kpi52QNS03GetSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 6),
    _Kpi52QNS03GetSessionActionAvgTime_Type()
)
kpi52QNS03GetSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03GetSessionActionAvgTime.setStatus("current")
_Kpi52QNS03GetSessionActionSuccess_Type = DisplayString
_Kpi52QNS03GetSessionActionSuccess_Object = MibScalar
kpi52QNS03GetSessionActionSuccess = _Kpi52QNS03GetSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 7),
    _Kpi52QNS03GetSessionActionSuccess_Type()
)
kpi52QNS03GetSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03GetSessionActionSuccess.setStatus("current")
_Kpi52QNS03LockSessionActionAvgTime_Type = DisplayString
_Kpi52QNS03LockSessionActionAvgTime_Object = MibScalar
kpi52QNS03LockSessionActionAvgTime = _Kpi52QNS03LockSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 8),
    _Kpi52QNS03LockSessionActionAvgTime_Type()
)
kpi52QNS03LockSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03LockSessionActionAvgTime.setStatus("current")
_Kpi52QNS03LockSessionActionSuccess_Type = DisplayString
_Kpi52QNS03LockSessionActionSuccess_Object = MibScalar
kpi52QNS03LockSessionActionSuccess = _Kpi52QNS03LockSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 9),
    _Kpi52QNS03LockSessionActionSuccess_Type()
)
kpi52QNS03LockSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03LockSessionActionSuccess.setStatus("current")
_Kpi52QNS03PushQuotaAvgTime_Type = DisplayString
_Kpi52QNS03PushQuotaAvgTime_Object = MibScalar
kpi52QNS03PushQuotaAvgTime = _Kpi52QNS03PushQuotaAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 10),
    _Kpi52QNS03PushQuotaAvgTime_Type()
)
kpi52QNS03PushQuotaAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03PushQuotaAvgTime.setStatus("current")
_Kpi52QNS03PushQuotaSuccess_Type = DisplayString
_Kpi52QNS03PushQuotaSuccess_Object = MibScalar
kpi52QNS03PushQuotaSuccess = _Kpi52QNS03PushQuotaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 11),
    _Kpi52QNS03PushQuotaSuccess_Type()
)
kpi52QNS03PushQuotaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03PushQuotaSuccess.setStatus("current")
_Kpi52QNS03QuotaCalculationAvgTime_Type = DisplayString
_Kpi52QNS03QuotaCalculationAvgTime_Object = MibScalar
kpi52QNS03QuotaCalculationAvgTime = _Kpi52QNS03QuotaCalculationAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 12),
    _Kpi52QNS03QuotaCalculationAvgTime_Type()
)
kpi52QNS03QuotaCalculationAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03QuotaCalculationAvgTime.setStatus("current")
_Kpi52QNS03QuotaCalculationSuccess_Type = DisplayString
_Kpi52QNS03QuotaCalculationSuccess_Object = MibScalar
kpi52QNS03QuotaCalculationSuccess = _Kpi52QNS03QuotaCalculationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 13),
    _Kpi52QNS03QuotaCalculationSuccess_Type()
)
kpi52QNS03QuotaCalculationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03QuotaCalculationSuccess.setStatus("current")
_Kpi52QNS03QuotaDepletedRequestAvgTime_Type = DisplayString
_Kpi52QNS03QuotaDepletedRequestAvgTime_Object = MibScalar
kpi52QNS03QuotaDepletedRequestAvgTime = _Kpi52QNS03QuotaDepletedRequestAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 14),
    _Kpi52QNS03QuotaDepletedRequestAvgTime_Type()
)
kpi52QNS03QuotaDepletedRequestAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03QuotaDepletedRequestAvgTime.setStatus("current")
_Kpi52QNS03QuotaDepletedRequestSucccess_Type = DisplayString
_Kpi52QNS03QuotaDepletedRequestSucccess_Object = MibScalar
kpi52QNS03QuotaDepletedRequestSucccess = _Kpi52QNS03QuotaDepletedRequestSucccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 15),
    _Kpi52QNS03QuotaDepletedRequestSucccess_Type()
)
kpi52QNS03QuotaDepletedRequestSucccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03QuotaDepletedRequestSucccess.setStatus("current")
_Kpi52QNS03RadiusAccountingMessageAvgTime_Type = DisplayString
_Kpi52QNS03RadiusAccountingMessageAvgTime_Object = MibScalar
kpi52QNS03RadiusAccountingMessageAvgTime = _Kpi52QNS03RadiusAccountingMessageAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 16),
    _Kpi52QNS03RadiusAccountingMessageAvgTime_Type()
)
kpi52QNS03RadiusAccountingMessageAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03RadiusAccountingMessageAvgTime.setStatus("current")
_Kpi52QNS03RadiusAccountingMessageSuccess_Type = DisplayString
_Kpi52QNS03RadiusAccountingMessageSuccess_Object = MibScalar
kpi52QNS03RadiusAccountingMessageSuccess = _Kpi52QNS03RadiusAccountingMessageSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 17),
    _Kpi52QNS03RadiusAccountingMessageSuccess_Type()
)
kpi52QNS03RadiusAccountingMessageSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03RadiusAccountingMessageSuccess.setStatus("current")
_Kpi52QNS03RetrieveSumAvPairAvgTime_Type = DisplayString
_Kpi52QNS03RetrieveSumAvPairAvgTime_Object = MibScalar
kpi52QNS03RetrieveSumAvPairAvgTime = _Kpi52QNS03RetrieveSumAvPairAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 18),
    _Kpi52QNS03RetrieveSumAvPairAvgTime_Type()
)
kpi52QNS03RetrieveSumAvPairAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03RetrieveSumAvPairAvgTime.setStatus("current")
_Kpi52QNS03RetrieveSumAvPairSuccess_Type = DisplayString
_Kpi52QNS03RetrieveSumAvPairSuccess_Object = MibScalar
kpi52QNS03RetrieveSumAvPairSuccess = _Kpi52QNS03RetrieveSumAvPairSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 19),
    _Kpi52QNS03RetrieveSumAvPairSuccess_Type()
)
kpi52QNS03RetrieveSumAvPairSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03RetrieveSumAvPairSuccess.setStatus("current")
_Kpi52QNS03PolicyCount_Type = DisplayString
_Kpi52QNS03PolicyCount_Object = MibScalar
kpi52QNS03PolicyCount = _Kpi52QNS03PolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 20),
    _Kpi52QNS03PolicyCount_Type()
)
kpi52QNS03PolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03PolicyCount.setStatus("current")
_Kpi52QNS03QueueSize_Type = DisplayString
_Kpi52QNS03QueueSize_Object = MibScalar
kpi52QNS03QueueSize = _Kpi52QNS03QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 21),
    _Kpi52QNS03QueueSize_Type()
)
kpi52QNS03QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03QueueSize.setStatus("current")
_Kpi52QNS03FailedEnqueueCount_Type = DisplayString
_Kpi52QNS03FailedEnqueueCount_Object = MibScalar
kpi52QNS03FailedEnqueueCount = _Kpi52QNS03FailedEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 22),
    _Kpi52QNS03FailedEnqueueCount_Type()
)
kpi52QNS03FailedEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03FailedEnqueueCount.setStatus("current")
_Kpi52QNS03ErrorCount_Type = DisplayString
_Kpi52QNS03ErrorCount_Object = MibScalar
kpi52QNS03ErrorCount = _Kpi52QNS03ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 23),
    _Kpi52QNS03ErrorCount_Type()
)
kpi52QNS03ErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03ErrorCount.setStatus("current")
_Kpi52QNS03SessionCount_Type = DisplayString
_Kpi52QNS03SessionCount_Object = MibScalar
kpi52QNS03SessionCount = _Kpi52QNS03SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 24),
    _Kpi52QNS03SessionCount_Type()
)
kpi52QNS03SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03SessionCount.setStatus("current")
_Kpi52QNS03FreeMemory_Type = DisplayString
_Kpi52QNS03FreeMemory_Object = MibScalar
kpi52QNS03FreeMemory = _Kpi52QNS03FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 3, 25),
    _Kpi52QNS03FreeMemory_Type()
)
kpi52QNS03FreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS03FreeMemory.setStatus("current")
_ConsolidatedKPI52QNS04_ObjectIdentity = ObjectIdentity
consolidatedKPI52QNS04 = _ConsolidatedKPI52QNS04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4)
)
_Kpi52QNS04RealServerStatus_Type = Gauge32
_Kpi52QNS04RealServerStatus_Object = MibScalar
kpi52QNS04RealServerStatus = _Kpi52QNS04RealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 1),
    _Kpi52QNS04RealServerStatus_Type()
)
kpi52QNS04RealServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04RealServerStatus.setStatus("current")
_Kpi52QNS04CreateEntryAvgTime_Type = DisplayString
_Kpi52QNS04CreateEntryAvgTime_Object = MibScalar
kpi52QNS04CreateEntryAvgTime = _Kpi52QNS04CreateEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 2),
    _Kpi52QNS04CreateEntryAvgTime_Type()
)
kpi52QNS04CreateEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04CreateEntryAvgTime.setStatus("current")
_Kpi52QNS04CreateEntrySuccess_Type = DisplayString
_Kpi52QNS04CreateEntrySuccess_Object = MibScalar
kpi52QNS04CreateEntrySuccess = _Kpi52QNS04CreateEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 3),
    _Kpi52QNS04CreateEntrySuccess_Type()
)
kpi52QNS04CreateEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04CreateEntrySuccess.setStatus("current")
_Kpi52QNS04DeleteEntryAvgTime_Type = DisplayString
_Kpi52QNS04DeleteEntryAvgTime_Object = MibScalar
kpi52QNS04DeleteEntryAvgTime = _Kpi52QNS04DeleteEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 4),
    _Kpi52QNS04DeleteEntryAvgTime_Type()
)
kpi52QNS04DeleteEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04DeleteEntryAvgTime.setStatus("current")
_Kpi52QNS04DeleteEntrySuccess_Type = DisplayString
_Kpi52QNS04DeleteEntrySuccess_Object = MibScalar
kpi52QNS04DeleteEntrySuccess = _Kpi52QNS04DeleteEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 5),
    _Kpi52QNS04DeleteEntrySuccess_Type()
)
kpi52QNS04DeleteEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04DeleteEntrySuccess.setStatus("current")
_Kpi52QNS04GetSessionActionAvgTime_Type = DisplayString
_Kpi52QNS04GetSessionActionAvgTime_Object = MibScalar
kpi52QNS04GetSessionActionAvgTime = _Kpi52QNS04GetSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 6),
    _Kpi52QNS04GetSessionActionAvgTime_Type()
)
kpi52QNS04GetSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04GetSessionActionAvgTime.setStatus("current")
_Kpi52QNS04GetSessionActionSuccess_Type = DisplayString
_Kpi52QNS04GetSessionActionSuccess_Object = MibScalar
kpi52QNS04GetSessionActionSuccess = _Kpi52QNS04GetSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 7),
    _Kpi52QNS04GetSessionActionSuccess_Type()
)
kpi52QNS04GetSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04GetSessionActionSuccess.setStatus("current")
_Kpi52QNS04LockSessionActionAvgTime_Type = DisplayString
_Kpi52QNS04LockSessionActionAvgTime_Object = MibScalar
kpi52QNS04LockSessionActionAvgTime = _Kpi52QNS04LockSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 8),
    _Kpi52QNS04LockSessionActionAvgTime_Type()
)
kpi52QNS04LockSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04LockSessionActionAvgTime.setStatus("current")
_Kpi52QNS04LockSessionActionSuccess_Type = DisplayString
_Kpi52QNS04LockSessionActionSuccess_Object = MibScalar
kpi52QNS04LockSessionActionSuccess = _Kpi52QNS04LockSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 9),
    _Kpi52QNS04LockSessionActionSuccess_Type()
)
kpi52QNS04LockSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04LockSessionActionSuccess.setStatus("current")
_Kpi52QNS04PushQuotaAvgTime_Type = DisplayString
_Kpi52QNS04PushQuotaAvgTime_Object = MibScalar
kpi52QNS04PushQuotaAvgTime = _Kpi52QNS04PushQuotaAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 10),
    _Kpi52QNS04PushQuotaAvgTime_Type()
)
kpi52QNS04PushQuotaAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04PushQuotaAvgTime.setStatus("current")
_Kpi52QNS04PushQuotaSuccess_Type = DisplayString
_Kpi52QNS04PushQuotaSuccess_Object = MibScalar
kpi52QNS04PushQuotaSuccess = _Kpi52QNS04PushQuotaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 11),
    _Kpi52QNS04PushQuotaSuccess_Type()
)
kpi52QNS04PushQuotaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04PushQuotaSuccess.setStatus("current")
_Kpi52QNS04QuotaCalculationAvgTime_Type = DisplayString
_Kpi52QNS04QuotaCalculationAvgTime_Object = MibScalar
kpi52QNS04QuotaCalculationAvgTime = _Kpi52QNS04QuotaCalculationAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 12),
    _Kpi52QNS04QuotaCalculationAvgTime_Type()
)
kpi52QNS04QuotaCalculationAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04QuotaCalculationAvgTime.setStatus("current")
_Kpi52QNS04QuotaCalculationSuccess_Type = DisplayString
_Kpi52QNS04QuotaCalculationSuccess_Object = MibScalar
kpi52QNS04QuotaCalculationSuccess = _Kpi52QNS04QuotaCalculationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 13),
    _Kpi52QNS04QuotaCalculationSuccess_Type()
)
kpi52QNS04QuotaCalculationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04QuotaCalculationSuccess.setStatus("current")
_Kpi52QNS04QuotaDepletedRequestAvgTime_Type = DisplayString
_Kpi52QNS04QuotaDepletedRequestAvgTime_Object = MibScalar
kpi52QNS04QuotaDepletedRequestAvgTime = _Kpi52QNS04QuotaDepletedRequestAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 14),
    _Kpi52QNS04QuotaDepletedRequestAvgTime_Type()
)
kpi52QNS04QuotaDepletedRequestAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04QuotaDepletedRequestAvgTime.setStatus("current")
_Kpi52QNS04QuotaDepletedRequestSucccess_Type = DisplayString
_Kpi52QNS04QuotaDepletedRequestSucccess_Object = MibScalar
kpi52QNS04QuotaDepletedRequestSucccess = _Kpi52QNS04QuotaDepletedRequestSucccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 15),
    _Kpi52QNS04QuotaDepletedRequestSucccess_Type()
)
kpi52QNS04QuotaDepletedRequestSucccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04QuotaDepletedRequestSucccess.setStatus("current")
_Kpi52QNS04RadiusAccountingMessageAvgTime_Type = DisplayString
_Kpi52QNS04RadiusAccountingMessageAvgTime_Object = MibScalar
kpi52QNS04RadiusAccountingMessageAvgTime = _Kpi52QNS04RadiusAccountingMessageAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 16),
    _Kpi52QNS04RadiusAccountingMessageAvgTime_Type()
)
kpi52QNS04RadiusAccountingMessageAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04RadiusAccountingMessageAvgTime.setStatus("current")
_Kpi52QNS04RadiusAccountingMessageSuccess_Type = DisplayString
_Kpi52QNS04RadiusAccountingMessageSuccess_Object = MibScalar
kpi52QNS04RadiusAccountingMessageSuccess = _Kpi52QNS04RadiusAccountingMessageSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 17),
    _Kpi52QNS04RadiusAccountingMessageSuccess_Type()
)
kpi52QNS04RadiusAccountingMessageSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04RadiusAccountingMessageSuccess.setStatus("current")
_Kpi52QNS04RetrieveSumAvPairAvgTime_Type = DisplayString
_Kpi52QNS04RetrieveSumAvPairAvgTime_Object = MibScalar
kpi52QNS04RetrieveSumAvPairAvgTime = _Kpi52QNS04RetrieveSumAvPairAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 18),
    _Kpi52QNS04RetrieveSumAvPairAvgTime_Type()
)
kpi52QNS04RetrieveSumAvPairAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04RetrieveSumAvPairAvgTime.setStatus("current")
_Kpi52QNS04RetrieveSumAvPairSuccess_Type = DisplayString
_Kpi52QNS04RetrieveSumAvPairSuccess_Object = MibScalar
kpi52QNS04RetrieveSumAvPairSuccess = _Kpi52QNS04RetrieveSumAvPairSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 19),
    _Kpi52QNS04RetrieveSumAvPairSuccess_Type()
)
kpi52QNS04RetrieveSumAvPairSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04RetrieveSumAvPairSuccess.setStatus("current")
_Kpi52QNS04PolicyCount_Type = DisplayString
_Kpi52QNS04PolicyCount_Object = MibScalar
kpi52QNS04PolicyCount = _Kpi52QNS04PolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 20),
    _Kpi52QNS04PolicyCount_Type()
)
kpi52QNS04PolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04PolicyCount.setStatus("current")
_Kpi52QNS04QueueSize_Type = DisplayString
_Kpi52QNS04QueueSize_Object = MibScalar
kpi52QNS04QueueSize = _Kpi52QNS04QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 21),
    _Kpi52QNS04QueueSize_Type()
)
kpi52QNS04QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04QueueSize.setStatus("current")
_Kpi52QNS04FailedEnqueueCount_Type = DisplayString
_Kpi52QNS04FailedEnqueueCount_Object = MibScalar
kpi52QNS04FailedEnqueueCount = _Kpi52QNS04FailedEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 22),
    _Kpi52QNS04FailedEnqueueCount_Type()
)
kpi52QNS04FailedEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04FailedEnqueueCount.setStatus("current")
_Kpi52QNS04ErrorCount_Type = DisplayString
_Kpi52QNS04ErrorCount_Object = MibScalar
kpi52QNS04ErrorCount = _Kpi52QNS04ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 23),
    _Kpi52QNS04ErrorCount_Type()
)
kpi52QNS04ErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04ErrorCount.setStatus("current")
_Kpi52QNS04SessionCount_Type = DisplayString
_Kpi52QNS04SessionCount_Object = MibScalar
kpi52QNS04SessionCount = _Kpi52QNS04SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 24),
    _Kpi52QNS04SessionCount_Type()
)
kpi52QNS04SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04SessionCount.setStatus("current")
_Kpi52QNS04FreeMemory_Type = DisplayString
_Kpi52QNS04FreeMemory_Object = MibScalar
kpi52QNS04FreeMemory = _Kpi52QNS04FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 1, 4, 25),
    _Kpi52QNS04FreeMemory_Type()
)
kpi52QNS04FreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52QNS04FreeMemory.setStatus("current")
_ConsolidatedKPI52SUM_ObjectIdentity = ObjectIdentity
consolidatedKPI52SUM = _ConsolidatedKPI52SUM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 2)
)
_ConsolidatedKPI52SUM01_ObjectIdentity = ObjectIdentity
consolidatedKPI52SUM01 = _ConsolidatedKPI52SUM01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 2, 1)
)
_Kpi52Sum01RealServerStatus_Type = Integer32
_Kpi52Sum01RealServerStatus_Object = MibScalar
kpi52Sum01RealServerStatus = _Kpi52Sum01RealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 2, 1, 1),
    _Kpi52Sum01RealServerStatus_Type()
)
kpi52Sum01RealServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Sum01RealServerStatus.setStatus("current")
_ConsolidatedKPI52SUM02_ObjectIdentity = ObjectIdentity
consolidatedKPI52SUM02 = _ConsolidatedKPI52SUM02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 2, 2)
)
_Kpi52Sum02RealServerStatus_Type = Integer32
_Kpi52Sum02RealServerStatus_Object = MibScalar
kpi52Sum02RealServerStatus = _Kpi52Sum02RealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 2, 2, 1),
    _Kpi52Sum02RealServerStatus_Type()
)
kpi52Sum02RealServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Sum02RealServerStatus.setStatus("current")
_ConsolidatedKPI52MYSQL_ObjectIdentity = ObjectIdentity
consolidatedKPI52MYSQL = _ConsolidatedKPI52MYSQL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3)
)
_ConsolidatedKPI52MYSQL01_ObjectIdentity = ObjectIdentity
consolidatedKPI52MYSQL01 = _ConsolidatedKPI52MYSQL01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 1)
)
_Kpi52Mysql01RealServerStatus_Type = Integer32
_Kpi52Mysql01RealServerStatus_Object = MibScalar
kpi52Mysql01RealServerStatus = _Kpi52Mysql01RealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 1, 1),
    _Kpi52Mysql01RealServerStatus_Type()
)
kpi52Mysql01RealServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql01RealServerStatus.setStatus("current")
_Kpi52Mysql01RealServerUptime_Type = Integer32
_Kpi52Mysql01RealServerUptime_Object = MibScalar
kpi52Mysql01RealServerUptime = _Kpi52Mysql01RealServerUptime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 1, 2),
    _Kpi52Mysql01RealServerUptime_Type()
)
kpi52Mysql01RealServerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql01RealServerUptime.setStatus("current")
_Kpi52Mysql01SlowQueries_Type = Integer32
_Kpi52Mysql01SlowQueries_Object = MibScalar
kpi52Mysql01SlowQueries = _Kpi52Mysql01SlowQueries_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 1, 3),
    _Kpi52Mysql01SlowQueries_Type()
)
kpi52Mysql01SlowQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql01SlowQueries.setStatus("current")
_Kpi52Mysql01ThreadCount_Type = Integer32
_Kpi52Mysql01ThreadCount_Object = MibScalar
kpi52Mysql01ThreadCount = _Kpi52Mysql01ThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 1, 4),
    _Kpi52Mysql01ThreadCount_Type()
)
kpi52Mysql01ThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql01ThreadCount.setStatus("current")
_Kpi52Mysql01QueriesPerSecond_Type = Integer32
_Kpi52Mysql01QueriesPerSecond_Object = MibScalar
kpi52Mysql01QueriesPerSecond = _Kpi52Mysql01QueriesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 1, 5),
    _Kpi52Mysql01QueriesPerSecond_Type()
)
kpi52Mysql01QueriesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql01QueriesPerSecond.setStatus("current")
_ConsolidatedKPI52MYSQL02_ObjectIdentity = ObjectIdentity
consolidatedKPI52MYSQL02 = _ConsolidatedKPI52MYSQL02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 2)
)
_Kpi52Mysql02RealServerStatus_Type = Integer32
_Kpi52Mysql02RealServerStatus_Object = MibScalar
kpi52Mysql02RealServerStatus = _Kpi52Mysql02RealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 2, 1),
    _Kpi52Mysql02RealServerStatus_Type()
)
kpi52Mysql02RealServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql02RealServerStatus.setStatus("current")
_Kpi52Mysql02RealServerUptime_Type = Integer32
_Kpi52Mysql02RealServerUptime_Object = MibScalar
kpi52Mysql02RealServerUptime = _Kpi52Mysql02RealServerUptime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 2, 2),
    _Kpi52Mysql02RealServerUptime_Type()
)
kpi52Mysql02RealServerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql02RealServerUptime.setStatus("current")
_Kpi52Mysql02SlowQueries_Type = Integer32
_Kpi52Mysql02SlowQueries_Object = MibScalar
kpi52Mysql02SlowQueries = _Kpi52Mysql02SlowQueries_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 2, 3),
    _Kpi52Mysql02SlowQueries_Type()
)
kpi52Mysql02SlowQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql02SlowQueries.setStatus("current")
_Kpi52Mysql02ThreadCount_Type = Integer32
_Kpi52Mysql02ThreadCount_Object = MibScalar
kpi52Mysql02ThreadCount = _Kpi52Mysql02ThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 2, 4),
    _Kpi52Mysql02ThreadCount_Type()
)
kpi52Mysql02ThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql02ThreadCount.setStatus("current")
_Kpi52Mysql02QueriesPerSecond_Type = Integer32
_Kpi52Mysql02QueriesPerSecond_Object = MibScalar
kpi52Mysql02QueriesPerSecond = _Kpi52Mysql02QueriesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 52, 3, 2, 5),
    _Kpi52Mysql02QueriesPerSecond_Type()
)
kpi52Mysql02QueriesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi52Mysql02QueriesPerSecond.setStatus("current")
_BroadhopProductsQNSKPI53_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53 = _BroadhopProductsQNSKPI53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53)
)
_BroadhopProductsQNSKPI53LB01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53LB01 = _BroadhopProductsQNSKPI53LB01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 11)
)
_Kpi53LB01PCRFProxyExternalCurrentSessions_Type = DisplayString
_Kpi53LB01PCRFProxyExternalCurrentSessions_Object = MibScalar
kpi53LB01PCRFProxyExternalCurrentSessions = _Kpi53LB01PCRFProxyExternalCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 11, 1),
    _Kpi53LB01PCRFProxyExternalCurrentSessions_Type()
)
kpi53LB01PCRFProxyExternalCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53LB01PCRFProxyExternalCurrentSessions.setStatus("current")
_Kpi53LB01PCRFProxyInternalCurrentSessions_Type = DisplayString
_Kpi53LB01PCRFProxyInternalCurrentSessions_Object = MibScalar
kpi53LB01PCRFProxyInternalCurrentSessions = _Kpi53LB01PCRFProxyInternalCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 11, 2),
    _Kpi53LB01PCRFProxyInternalCurrentSessions_Type()
)
kpi53LB01PCRFProxyInternalCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53LB01PCRFProxyInternalCurrentSessions.setStatus("current")
_BroadhopProductsQNSKPI53LB02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53LB02 = _BroadhopProductsQNSKPI53LB02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 12)
)
_Kpi53LB02PCRFProxyExternalCurrentSessions_Type = DisplayString
_Kpi53LB02PCRFProxyExternalCurrentSessions_Object = MibScalar
kpi53LB02PCRFProxyExternalCurrentSessions = _Kpi53LB02PCRFProxyExternalCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 12, 1),
    _Kpi53LB02PCRFProxyExternalCurrentSessions_Type()
)
kpi53LB02PCRFProxyExternalCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53LB02PCRFProxyExternalCurrentSessions.setStatus("current")
_Kpi53LB02PCRFProxyInternalCurrentSessions_Type = DisplayString
_Kpi53LB02PCRFProxyInternalCurrentSessions_Object = MibScalar
kpi53LB02PCRFProxyInternalCurrentSessions = _Kpi53LB02PCRFProxyInternalCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 12, 2),
    _Kpi53LB02PCRFProxyInternalCurrentSessions_Type()
)
kpi53LB02PCRFProxyInternalCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53LB02PCRFProxyInternalCurrentSessions.setStatus("current")
_BroadhopProductsQNSKPI53PortalLB01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53PortalLB01 = _BroadhopProductsQNSKPI53PortalLB01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 13)
)
_Kpi53PortalLB01PortalProxyExternalCurrentSessions_Type = DisplayString
_Kpi53PortalLB01PortalProxyExternalCurrentSessions_Object = MibScalar
kpi53PortalLB01PortalProxyExternalCurrentSessions = _Kpi53PortalLB01PortalProxyExternalCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 13, 1),
    _Kpi53PortalLB01PortalProxyExternalCurrentSessions_Type()
)
kpi53PortalLB01PortalProxyExternalCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53PortalLB01PortalProxyExternalCurrentSessions.setStatus("current")
_BroadhopProductsQNSKPI53PortalLB02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53PortalLB02 = _BroadhopProductsQNSKPI53PortalLB02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 14)
)
_Kpi53PortalLB02PortalProxyExternalCurrentSessions_Type = DisplayString
_Kpi53PortalLB02PortalProxyExternalCurrentSessions_Object = MibScalar
kpi53PortalLB02PortalProxyExternalCurrentSessions = _Kpi53PortalLB02PortalProxyExternalCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 14, 1),
    _Kpi53PortalLB02PortalProxyExternalCurrentSessions_Type()
)
kpi53PortalLB02PortalProxyExternalCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53PortalLB02PortalProxyExternalCurrentSessions.setStatus("current")
_BroadhopProductsQNSKPI53SessionMgr01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53SessionMgr01 = _BroadhopProductsQNSKPI53SessionMgr01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 31)
)
_BroadhopProductsQNSKPI53SessionMgr02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53SessionMgr02 = _BroadhopProductsQNSKPI53SessionMgr02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 32)
)
_BroadhopProductsQNSKPI53QNS01_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53QNS01 = _BroadhopProductsQNSKPI53QNS01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41)
)
_Kpi53QNS01CreateEntryAvgTime_Type = DisplayString
_Kpi53QNS01CreateEntryAvgTime_Object = MibScalar
kpi53QNS01CreateEntryAvgTime = _Kpi53QNS01CreateEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 2),
    _Kpi53QNS01CreateEntryAvgTime_Type()
)
kpi53QNS01CreateEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01CreateEntryAvgTime.setStatus("current")
_Kpi53QNS01CreateEntrySuccess_Type = DisplayString
_Kpi53QNS01CreateEntrySuccess_Object = MibScalar
kpi53QNS01CreateEntrySuccess = _Kpi53QNS01CreateEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 3),
    _Kpi53QNS01CreateEntrySuccess_Type()
)
kpi53QNS01CreateEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01CreateEntrySuccess.setStatus("current")
_Kpi53QNS01DeleteEntryAvgTime_Type = DisplayString
_Kpi53QNS01DeleteEntryAvgTime_Object = MibScalar
kpi53QNS01DeleteEntryAvgTime = _Kpi53QNS01DeleteEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 4),
    _Kpi53QNS01DeleteEntryAvgTime_Type()
)
kpi53QNS01DeleteEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01DeleteEntryAvgTime.setStatus("current")
_Kpi53QNS01DeleteEntrySuccess_Type = DisplayString
_Kpi53QNS01DeleteEntrySuccess_Object = MibScalar
kpi53QNS01DeleteEntrySuccess = _Kpi53QNS01DeleteEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 5),
    _Kpi53QNS01DeleteEntrySuccess_Type()
)
kpi53QNS01DeleteEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01DeleteEntrySuccess.setStatus("current")
_Kpi53QNS01GetSessionActionAvgTime_Type = DisplayString
_Kpi53QNS01GetSessionActionAvgTime_Object = MibScalar
kpi53QNS01GetSessionActionAvgTime = _Kpi53QNS01GetSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 6),
    _Kpi53QNS01GetSessionActionAvgTime_Type()
)
kpi53QNS01GetSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01GetSessionActionAvgTime.setStatus("current")
_Kpi53QNS01GetSessionActionSuccess_Type = DisplayString
_Kpi53QNS01GetSessionActionSuccess_Object = MibScalar
kpi53QNS01GetSessionActionSuccess = _Kpi53QNS01GetSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 7),
    _Kpi53QNS01GetSessionActionSuccess_Type()
)
kpi53QNS01GetSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01GetSessionActionSuccess.setStatus("current")
_Kpi53QNS01LockSessionActionAvgTime_Type = DisplayString
_Kpi53QNS01LockSessionActionAvgTime_Object = MibScalar
kpi53QNS01LockSessionActionAvgTime = _Kpi53QNS01LockSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 8),
    _Kpi53QNS01LockSessionActionAvgTime_Type()
)
kpi53QNS01LockSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01LockSessionActionAvgTime.setStatus("current")
_Kpi53QNS01LockSessionActionSuccess_Type = DisplayString
_Kpi53QNS01LockSessionActionSuccess_Object = MibScalar
kpi53QNS01LockSessionActionSuccess = _Kpi53QNS01LockSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 9),
    _Kpi53QNS01LockSessionActionSuccess_Type()
)
kpi53QNS01LockSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01LockSessionActionSuccess.setStatus("current")
_Kpi53QNS01PushQuotaAvgTime_Type = DisplayString
_Kpi53QNS01PushQuotaAvgTime_Object = MibScalar
kpi53QNS01PushQuotaAvgTime = _Kpi53QNS01PushQuotaAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 10),
    _Kpi53QNS01PushQuotaAvgTime_Type()
)
kpi53QNS01PushQuotaAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01PushQuotaAvgTime.setStatus("current")
_Kpi53QNS01PushQuotaSuccess_Type = DisplayString
_Kpi53QNS01PushQuotaSuccess_Object = MibScalar
kpi53QNS01PushQuotaSuccess = _Kpi53QNS01PushQuotaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 11),
    _Kpi53QNS01PushQuotaSuccess_Type()
)
kpi53QNS01PushQuotaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01PushQuotaSuccess.setStatus("current")
_Kpi53QNS01QuotaCalculationAvgTime_Type = DisplayString
_Kpi53QNS01QuotaCalculationAvgTime_Object = MibScalar
kpi53QNS01QuotaCalculationAvgTime = _Kpi53QNS01QuotaCalculationAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 12),
    _Kpi53QNS01QuotaCalculationAvgTime_Type()
)
kpi53QNS01QuotaCalculationAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01QuotaCalculationAvgTime.setStatus("current")
_Kpi53QNS01QuotaCalculationSuccess_Type = DisplayString
_Kpi53QNS01QuotaCalculationSuccess_Object = MibScalar
kpi53QNS01QuotaCalculationSuccess = _Kpi53QNS01QuotaCalculationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 13),
    _Kpi53QNS01QuotaCalculationSuccess_Type()
)
kpi53QNS01QuotaCalculationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01QuotaCalculationSuccess.setStatus("current")
_Kpi53QNS01QuotaDepletedRequestAvgTime_Type = DisplayString
_Kpi53QNS01QuotaDepletedRequestAvgTime_Object = MibScalar
kpi53QNS01QuotaDepletedRequestAvgTime = _Kpi53QNS01QuotaDepletedRequestAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 14),
    _Kpi53QNS01QuotaDepletedRequestAvgTime_Type()
)
kpi53QNS01QuotaDepletedRequestAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01QuotaDepletedRequestAvgTime.setStatus("current")
_Kpi53QNS01QuotaDepletedRequestSucccess_Type = DisplayString
_Kpi53QNS01QuotaDepletedRequestSucccess_Object = MibScalar
kpi53QNS01QuotaDepletedRequestSucccess = _Kpi53QNS01QuotaDepletedRequestSucccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 15),
    _Kpi53QNS01QuotaDepletedRequestSucccess_Type()
)
kpi53QNS01QuotaDepletedRequestSucccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01QuotaDepletedRequestSucccess.setStatus("current")
_Kpi53QNS01RadiusAccountingMessageAvgTime_Type = DisplayString
_Kpi53QNS01RadiusAccountingMessageAvgTime_Object = MibScalar
kpi53QNS01RadiusAccountingMessageAvgTime = _Kpi53QNS01RadiusAccountingMessageAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 16),
    _Kpi53QNS01RadiusAccountingMessageAvgTime_Type()
)
kpi53QNS01RadiusAccountingMessageAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01RadiusAccountingMessageAvgTime.setStatus("current")
_Kpi53QNS01RadiusAccountingMessageSuccess_Type = DisplayString
_Kpi53QNS01RadiusAccountingMessageSuccess_Object = MibScalar
kpi53QNS01RadiusAccountingMessageSuccess = _Kpi53QNS01RadiusAccountingMessageSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 17),
    _Kpi53QNS01RadiusAccountingMessageSuccess_Type()
)
kpi53QNS01RadiusAccountingMessageSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01RadiusAccountingMessageSuccess.setStatus("current")
_Kpi53QNS01RetrieveSumAvPairAvgTime_Type = DisplayString
_Kpi53QNS01RetrieveSumAvPairAvgTime_Object = MibScalar
kpi53QNS01RetrieveSumAvPairAvgTime = _Kpi53QNS01RetrieveSumAvPairAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 18),
    _Kpi53QNS01RetrieveSumAvPairAvgTime_Type()
)
kpi53QNS01RetrieveSumAvPairAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01RetrieveSumAvPairAvgTime.setStatus("current")
_Kpi53QNS01RetrieveSumAvPairSuccess_Type = DisplayString
_Kpi53QNS01RetrieveSumAvPairSuccess_Object = MibScalar
kpi53QNS01RetrieveSumAvPairSuccess = _Kpi53QNS01RetrieveSumAvPairSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 19),
    _Kpi53QNS01RetrieveSumAvPairSuccess_Type()
)
kpi53QNS01RetrieveSumAvPairSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01RetrieveSumAvPairSuccess.setStatus("current")
_Kpi53QNS01PolicyCount_Type = DisplayString
_Kpi53QNS01PolicyCount_Object = MibScalar
kpi53QNS01PolicyCount = _Kpi53QNS01PolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 20),
    _Kpi53QNS01PolicyCount_Type()
)
kpi53QNS01PolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01PolicyCount.setStatus("current")
_Kpi53QNS01QueueSize_Type = DisplayString
_Kpi53QNS01QueueSize_Object = MibScalar
kpi53QNS01QueueSize = _Kpi53QNS01QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 21),
    _Kpi53QNS01QueueSize_Type()
)
kpi53QNS01QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01QueueSize.setStatus("current")
_Kpi53QNS01FailedEnqueueCount_Type = DisplayString
_Kpi53QNS01FailedEnqueueCount_Object = MibScalar
kpi53QNS01FailedEnqueueCount = _Kpi53QNS01FailedEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 22),
    _Kpi53QNS01FailedEnqueueCount_Type()
)
kpi53QNS01FailedEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01FailedEnqueueCount.setStatus("current")
_Kpi53QNS01ErrorCount_Type = DisplayString
_Kpi53QNS01ErrorCount_Object = MibScalar
kpi53QNS01ErrorCount = _Kpi53QNS01ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 23),
    _Kpi53QNS01ErrorCount_Type()
)
kpi53QNS01ErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01ErrorCount.setStatus("current")
_Kpi53QNS01SessionCount_Type = DisplayString
_Kpi53QNS01SessionCount_Object = MibScalar
kpi53QNS01SessionCount = _Kpi53QNS01SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 24),
    _Kpi53QNS01SessionCount_Type()
)
kpi53QNS01SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01SessionCount.setStatus("current")
_Kpi53QNS01FreeMemory_Type = DisplayString
_Kpi53QNS01FreeMemory_Object = MibScalar
kpi53QNS01FreeMemory = _Kpi53QNS01FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 41, 25),
    _Kpi53QNS01FreeMemory_Type()
)
kpi53QNS01FreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS01FreeMemory.setStatus("current")
_BroadhopProductsQNSKPI53QNS02_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53QNS02 = _BroadhopProductsQNSKPI53QNS02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42)
)
_Kpi53QNS02CreateEntryAvgTime_Type = DisplayString
_Kpi53QNS02CreateEntryAvgTime_Object = MibScalar
kpi53QNS02CreateEntryAvgTime = _Kpi53QNS02CreateEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 2),
    _Kpi53QNS02CreateEntryAvgTime_Type()
)
kpi53QNS02CreateEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02CreateEntryAvgTime.setStatus("current")
_Kpi53QNS02CreateEntrySuccess_Type = DisplayString
_Kpi53QNS02CreateEntrySuccess_Object = MibScalar
kpi53QNS02CreateEntrySuccess = _Kpi53QNS02CreateEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 3),
    _Kpi53QNS02CreateEntrySuccess_Type()
)
kpi53QNS02CreateEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02CreateEntrySuccess.setStatus("current")
_Kpi53QNS02DeleteEntryAvgTime_Type = DisplayString
_Kpi53QNS02DeleteEntryAvgTime_Object = MibScalar
kpi53QNS02DeleteEntryAvgTime = _Kpi53QNS02DeleteEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 4),
    _Kpi53QNS02DeleteEntryAvgTime_Type()
)
kpi53QNS02DeleteEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02DeleteEntryAvgTime.setStatus("current")
_Kpi53QNS02DeleteEntrySuccess_Type = DisplayString
_Kpi53QNS02DeleteEntrySuccess_Object = MibScalar
kpi53QNS02DeleteEntrySuccess = _Kpi53QNS02DeleteEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 5),
    _Kpi53QNS02DeleteEntrySuccess_Type()
)
kpi53QNS02DeleteEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02DeleteEntrySuccess.setStatus("current")
_Kpi53QNS02GetSessionActionAvgTime_Type = DisplayString
_Kpi53QNS02GetSessionActionAvgTime_Object = MibScalar
kpi53QNS02GetSessionActionAvgTime = _Kpi53QNS02GetSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 6),
    _Kpi53QNS02GetSessionActionAvgTime_Type()
)
kpi53QNS02GetSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02GetSessionActionAvgTime.setStatus("current")
_Kpi53QNS02GetSessionActionSuccess_Type = DisplayString
_Kpi53QNS02GetSessionActionSuccess_Object = MibScalar
kpi53QNS02GetSessionActionSuccess = _Kpi53QNS02GetSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 7),
    _Kpi53QNS02GetSessionActionSuccess_Type()
)
kpi53QNS02GetSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02GetSessionActionSuccess.setStatus("current")
_Kpi53QNS02LockSessionActionAvgTime_Type = DisplayString
_Kpi53QNS02LockSessionActionAvgTime_Object = MibScalar
kpi53QNS02LockSessionActionAvgTime = _Kpi53QNS02LockSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 8),
    _Kpi53QNS02LockSessionActionAvgTime_Type()
)
kpi53QNS02LockSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02LockSessionActionAvgTime.setStatus("current")
_Kpi53QNS02LockSessionActionSuccess_Type = DisplayString
_Kpi53QNS02LockSessionActionSuccess_Object = MibScalar
kpi53QNS02LockSessionActionSuccess = _Kpi53QNS02LockSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 9),
    _Kpi53QNS02LockSessionActionSuccess_Type()
)
kpi53QNS02LockSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02LockSessionActionSuccess.setStatus("current")
_Kpi53QNS02PushQuotaAvgTime_Type = DisplayString
_Kpi53QNS02PushQuotaAvgTime_Object = MibScalar
kpi53QNS02PushQuotaAvgTime = _Kpi53QNS02PushQuotaAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 10),
    _Kpi53QNS02PushQuotaAvgTime_Type()
)
kpi53QNS02PushQuotaAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02PushQuotaAvgTime.setStatus("current")
_Kpi53QNS02PushQuotaSuccess_Type = DisplayString
_Kpi53QNS02PushQuotaSuccess_Object = MibScalar
kpi53QNS02PushQuotaSuccess = _Kpi53QNS02PushQuotaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 11),
    _Kpi53QNS02PushQuotaSuccess_Type()
)
kpi53QNS02PushQuotaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02PushQuotaSuccess.setStatus("current")
_Kpi53QNS02QuotaCalculationAvgTime_Type = DisplayString
_Kpi53QNS02QuotaCalculationAvgTime_Object = MibScalar
kpi53QNS02QuotaCalculationAvgTime = _Kpi53QNS02QuotaCalculationAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 12),
    _Kpi53QNS02QuotaCalculationAvgTime_Type()
)
kpi53QNS02QuotaCalculationAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02QuotaCalculationAvgTime.setStatus("current")
_Kpi53QNS02QuotaCalculationSuccess_Type = DisplayString
_Kpi53QNS02QuotaCalculationSuccess_Object = MibScalar
kpi53QNS02QuotaCalculationSuccess = _Kpi53QNS02QuotaCalculationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 13),
    _Kpi53QNS02QuotaCalculationSuccess_Type()
)
kpi53QNS02QuotaCalculationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02QuotaCalculationSuccess.setStatus("current")
_Kpi53QNS02QuotaDepletedRequestAvgTime_Type = DisplayString
_Kpi53QNS02QuotaDepletedRequestAvgTime_Object = MibScalar
kpi53QNS02QuotaDepletedRequestAvgTime = _Kpi53QNS02QuotaDepletedRequestAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 14),
    _Kpi53QNS02QuotaDepletedRequestAvgTime_Type()
)
kpi53QNS02QuotaDepletedRequestAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02QuotaDepletedRequestAvgTime.setStatus("current")
_Kpi53QNS02QuotaDepletedRequestSucccess_Type = DisplayString
_Kpi53QNS02QuotaDepletedRequestSucccess_Object = MibScalar
kpi53QNS02QuotaDepletedRequestSucccess = _Kpi53QNS02QuotaDepletedRequestSucccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 15),
    _Kpi53QNS02QuotaDepletedRequestSucccess_Type()
)
kpi53QNS02QuotaDepletedRequestSucccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02QuotaDepletedRequestSucccess.setStatus("current")
_Kpi53QNS02RadiusAccountingMessageAvgTime_Type = DisplayString
_Kpi53QNS02RadiusAccountingMessageAvgTime_Object = MibScalar
kpi53QNS02RadiusAccountingMessageAvgTime = _Kpi53QNS02RadiusAccountingMessageAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 16),
    _Kpi53QNS02RadiusAccountingMessageAvgTime_Type()
)
kpi53QNS02RadiusAccountingMessageAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02RadiusAccountingMessageAvgTime.setStatus("current")
_Kpi53QNS02RadiusAccountingMessageSuccess_Type = DisplayString
_Kpi53QNS02RadiusAccountingMessageSuccess_Object = MibScalar
kpi53QNS02RadiusAccountingMessageSuccess = _Kpi53QNS02RadiusAccountingMessageSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 17),
    _Kpi53QNS02RadiusAccountingMessageSuccess_Type()
)
kpi53QNS02RadiusAccountingMessageSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02RadiusAccountingMessageSuccess.setStatus("current")
_Kpi53QNS02RetrieveSumAvPairAvgTime_Type = DisplayString
_Kpi53QNS02RetrieveSumAvPairAvgTime_Object = MibScalar
kpi53QNS02RetrieveSumAvPairAvgTime = _Kpi53QNS02RetrieveSumAvPairAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 18),
    _Kpi53QNS02RetrieveSumAvPairAvgTime_Type()
)
kpi53QNS02RetrieveSumAvPairAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02RetrieveSumAvPairAvgTime.setStatus("current")
_Kpi53QNS02RetrieveSumAvPairSuccess_Type = DisplayString
_Kpi53QNS02RetrieveSumAvPairSuccess_Object = MibScalar
kpi53QNS02RetrieveSumAvPairSuccess = _Kpi53QNS02RetrieveSumAvPairSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 19),
    _Kpi53QNS02RetrieveSumAvPairSuccess_Type()
)
kpi53QNS02RetrieveSumAvPairSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02RetrieveSumAvPairSuccess.setStatus("current")
_Kpi53QNS02PolicyCount_Type = DisplayString
_Kpi53QNS02PolicyCount_Object = MibScalar
kpi53QNS02PolicyCount = _Kpi53QNS02PolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 20),
    _Kpi53QNS02PolicyCount_Type()
)
kpi53QNS02PolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02PolicyCount.setStatus("current")
_Kpi53QNS02QueueSize_Type = DisplayString
_Kpi53QNS02QueueSize_Object = MibScalar
kpi53QNS02QueueSize = _Kpi53QNS02QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 21),
    _Kpi53QNS02QueueSize_Type()
)
kpi53QNS02QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02QueueSize.setStatus("current")
_Kpi53QNS02FailedEnqueueCount_Type = DisplayString
_Kpi53QNS02FailedEnqueueCount_Object = MibScalar
kpi53QNS02FailedEnqueueCount = _Kpi53QNS02FailedEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 22),
    _Kpi53QNS02FailedEnqueueCount_Type()
)
kpi53QNS02FailedEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02FailedEnqueueCount.setStatus("current")
_Kpi53QNS02ErrorCount_Type = DisplayString
_Kpi53QNS02ErrorCount_Object = MibScalar
kpi53QNS02ErrorCount = _Kpi53QNS02ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 23),
    _Kpi53QNS02ErrorCount_Type()
)
kpi53QNS02ErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02ErrorCount.setStatus("current")
_Kpi53QNS02SessionCount_Type = DisplayString
_Kpi53QNS02SessionCount_Object = MibScalar
kpi53QNS02SessionCount = _Kpi53QNS02SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 24),
    _Kpi53QNS02SessionCount_Type()
)
kpi53QNS02SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02SessionCount.setStatus("current")
_Kpi53QNS02FreeMemory_Type = DisplayString
_Kpi53QNS02FreeMemory_Object = MibScalar
kpi53QNS02FreeMemory = _Kpi53QNS02FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 42, 25),
    _Kpi53QNS02FreeMemory_Type()
)
kpi53QNS02FreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS02FreeMemory.setStatus("current")
_BroadhopProductsQNSKPI53QNS03_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53QNS03 = _BroadhopProductsQNSKPI53QNS03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43)
)
_Kpi53QNS03CreateEntryAvgTime_Type = DisplayString
_Kpi53QNS03CreateEntryAvgTime_Object = MibScalar
kpi53QNS03CreateEntryAvgTime = _Kpi53QNS03CreateEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 2),
    _Kpi53QNS03CreateEntryAvgTime_Type()
)
kpi53QNS03CreateEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03CreateEntryAvgTime.setStatus("current")
_Kpi53QNS03CreateEntrySuccess_Type = DisplayString
_Kpi53QNS03CreateEntrySuccess_Object = MibScalar
kpi53QNS03CreateEntrySuccess = _Kpi53QNS03CreateEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 3),
    _Kpi53QNS03CreateEntrySuccess_Type()
)
kpi53QNS03CreateEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03CreateEntrySuccess.setStatus("current")
_Kpi53QNS03DeleteEntryAvgTime_Type = DisplayString
_Kpi53QNS03DeleteEntryAvgTime_Object = MibScalar
kpi53QNS03DeleteEntryAvgTime = _Kpi53QNS03DeleteEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 4),
    _Kpi53QNS03DeleteEntryAvgTime_Type()
)
kpi53QNS03DeleteEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03DeleteEntryAvgTime.setStatus("current")
_Kpi53QNS03DeleteEntrySuccess_Type = DisplayString
_Kpi53QNS03DeleteEntrySuccess_Object = MibScalar
kpi53QNS03DeleteEntrySuccess = _Kpi53QNS03DeleteEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 5),
    _Kpi53QNS03DeleteEntrySuccess_Type()
)
kpi53QNS03DeleteEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03DeleteEntrySuccess.setStatus("current")
_Kpi53QNS03GetSessionActionAvgTime_Type = DisplayString
_Kpi53QNS03GetSessionActionAvgTime_Object = MibScalar
kpi53QNS03GetSessionActionAvgTime = _Kpi53QNS03GetSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 6),
    _Kpi53QNS03GetSessionActionAvgTime_Type()
)
kpi53QNS03GetSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03GetSessionActionAvgTime.setStatus("current")
_Kpi53QNS03GetSessionActionSuccess_Type = DisplayString
_Kpi53QNS03GetSessionActionSuccess_Object = MibScalar
kpi53QNS03GetSessionActionSuccess = _Kpi53QNS03GetSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 7),
    _Kpi53QNS03GetSessionActionSuccess_Type()
)
kpi53QNS03GetSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03GetSessionActionSuccess.setStatus("current")
_Kpi53QNS03LockSessionActionAvgTime_Type = DisplayString
_Kpi53QNS03LockSessionActionAvgTime_Object = MibScalar
kpi53QNS03LockSessionActionAvgTime = _Kpi53QNS03LockSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 8),
    _Kpi53QNS03LockSessionActionAvgTime_Type()
)
kpi53QNS03LockSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03LockSessionActionAvgTime.setStatus("current")
_Kpi53QNS03LockSessionActionSuccess_Type = DisplayString
_Kpi53QNS03LockSessionActionSuccess_Object = MibScalar
kpi53QNS03LockSessionActionSuccess = _Kpi53QNS03LockSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 9),
    _Kpi53QNS03LockSessionActionSuccess_Type()
)
kpi53QNS03LockSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03LockSessionActionSuccess.setStatus("current")
_Kpi53QNS03PushQuotaAvgTime_Type = DisplayString
_Kpi53QNS03PushQuotaAvgTime_Object = MibScalar
kpi53QNS03PushQuotaAvgTime = _Kpi53QNS03PushQuotaAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 10),
    _Kpi53QNS03PushQuotaAvgTime_Type()
)
kpi53QNS03PushQuotaAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03PushQuotaAvgTime.setStatus("current")
_Kpi53QNS03PushQuotaSuccess_Type = DisplayString
_Kpi53QNS03PushQuotaSuccess_Object = MibScalar
kpi53QNS03PushQuotaSuccess = _Kpi53QNS03PushQuotaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 11),
    _Kpi53QNS03PushQuotaSuccess_Type()
)
kpi53QNS03PushQuotaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03PushQuotaSuccess.setStatus("current")
_Kpi53QNS03QuotaCalculationAvgTime_Type = DisplayString
_Kpi53QNS03QuotaCalculationAvgTime_Object = MibScalar
kpi53QNS03QuotaCalculationAvgTime = _Kpi53QNS03QuotaCalculationAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 12),
    _Kpi53QNS03QuotaCalculationAvgTime_Type()
)
kpi53QNS03QuotaCalculationAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03QuotaCalculationAvgTime.setStatus("current")
_Kpi53QNS03QuotaCalculationSuccess_Type = DisplayString
_Kpi53QNS03QuotaCalculationSuccess_Object = MibScalar
kpi53QNS03QuotaCalculationSuccess = _Kpi53QNS03QuotaCalculationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 13),
    _Kpi53QNS03QuotaCalculationSuccess_Type()
)
kpi53QNS03QuotaCalculationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03QuotaCalculationSuccess.setStatus("current")
_Kpi53QNS03QuotaDepletedRequestAvgTime_Type = DisplayString
_Kpi53QNS03QuotaDepletedRequestAvgTime_Object = MibScalar
kpi53QNS03QuotaDepletedRequestAvgTime = _Kpi53QNS03QuotaDepletedRequestAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 14),
    _Kpi53QNS03QuotaDepletedRequestAvgTime_Type()
)
kpi53QNS03QuotaDepletedRequestAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03QuotaDepletedRequestAvgTime.setStatus("current")
_Kpi53QNS03QuotaDepletedRequestSucccess_Type = DisplayString
_Kpi53QNS03QuotaDepletedRequestSucccess_Object = MibScalar
kpi53QNS03QuotaDepletedRequestSucccess = _Kpi53QNS03QuotaDepletedRequestSucccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 15),
    _Kpi53QNS03QuotaDepletedRequestSucccess_Type()
)
kpi53QNS03QuotaDepletedRequestSucccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03QuotaDepletedRequestSucccess.setStatus("current")
_Kpi53QNS03RadiusAccountingMessageAvgTime_Type = DisplayString
_Kpi53QNS03RadiusAccountingMessageAvgTime_Object = MibScalar
kpi53QNS03RadiusAccountingMessageAvgTime = _Kpi53QNS03RadiusAccountingMessageAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 16),
    _Kpi53QNS03RadiusAccountingMessageAvgTime_Type()
)
kpi53QNS03RadiusAccountingMessageAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03RadiusAccountingMessageAvgTime.setStatus("current")
_Kpi53QNS03RadiusAccountingMessageSuccess_Type = DisplayString
_Kpi53QNS03RadiusAccountingMessageSuccess_Object = MibScalar
kpi53QNS03RadiusAccountingMessageSuccess = _Kpi53QNS03RadiusAccountingMessageSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 17),
    _Kpi53QNS03RadiusAccountingMessageSuccess_Type()
)
kpi53QNS03RadiusAccountingMessageSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03RadiusAccountingMessageSuccess.setStatus("current")
_Kpi53QNS03RetrieveSumAvPairAvgTime_Type = DisplayString
_Kpi53QNS03RetrieveSumAvPairAvgTime_Object = MibScalar
kpi53QNS03RetrieveSumAvPairAvgTime = _Kpi53QNS03RetrieveSumAvPairAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 18),
    _Kpi53QNS03RetrieveSumAvPairAvgTime_Type()
)
kpi53QNS03RetrieveSumAvPairAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03RetrieveSumAvPairAvgTime.setStatus("current")
_Kpi53QNS03RetrieveSumAvPairSuccess_Type = DisplayString
_Kpi53QNS03RetrieveSumAvPairSuccess_Object = MibScalar
kpi53QNS03RetrieveSumAvPairSuccess = _Kpi53QNS03RetrieveSumAvPairSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 19),
    _Kpi53QNS03RetrieveSumAvPairSuccess_Type()
)
kpi53QNS03RetrieveSumAvPairSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03RetrieveSumAvPairSuccess.setStatus("current")
_Kpi53QNS03PolicyCount_Type = DisplayString
_Kpi53QNS03PolicyCount_Object = MibScalar
kpi53QNS03PolicyCount = _Kpi53QNS03PolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 20),
    _Kpi53QNS03PolicyCount_Type()
)
kpi53QNS03PolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03PolicyCount.setStatus("current")
_Kpi53QNS03QueueSize_Type = DisplayString
_Kpi53QNS03QueueSize_Object = MibScalar
kpi53QNS03QueueSize = _Kpi53QNS03QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 21),
    _Kpi53QNS03QueueSize_Type()
)
kpi53QNS03QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03QueueSize.setStatus("current")
_Kpi53QNS03FailedEnqueueCount_Type = DisplayString
_Kpi53QNS03FailedEnqueueCount_Object = MibScalar
kpi53QNS03FailedEnqueueCount = _Kpi53QNS03FailedEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 22),
    _Kpi53QNS03FailedEnqueueCount_Type()
)
kpi53QNS03FailedEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03FailedEnqueueCount.setStatus("current")
_Kpi53QNS03ErrorCount_Type = DisplayString
_Kpi53QNS03ErrorCount_Object = MibScalar
kpi53QNS03ErrorCount = _Kpi53QNS03ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 23),
    _Kpi53QNS03ErrorCount_Type()
)
kpi53QNS03ErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03ErrorCount.setStatus("current")
_Kpi53QNS03SessionCount_Type = DisplayString
_Kpi53QNS03SessionCount_Object = MibScalar
kpi53QNS03SessionCount = _Kpi53QNS03SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 24),
    _Kpi53QNS03SessionCount_Type()
)
kpi53QNS03SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03SessionCount.setStatus("current")
_Kpi53QNS03FreeMemory_Type = DisplayString
_Kpi53QNS03FreeMemory_Object = MibScalar
kpi53QNS03FreeMemory = _Kpi53QNS03FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 43, 25),
    _Kpi53QNS03FreeMemory_Type()
)
kpi53QNS03FreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS03FreeMemory.setStatus("current")
_BroadhopProductsQNSKPI53QNS04_ObjectIdentity = ObjectIdentity
broadhopProductsQNSKPI53QNS04 = _BroadhopProductsQNSKPI53QNS04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44)
)
_Kpi53QNS04CreateEntryAvgTime_Type = DisplayString
_Kpi53QNS04CreateEntryAvgTime_Object = MibScalar
kpi53QNS04CreateEntryAvgTime = _Kpi53QNS04CreateEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 2),
    _Kpi53QNS04CreateEntryAvgTime_Type()
)
kpi53QNS04CreateEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04CreateEntryAvgTime.setStatus("current")
_Kpi53QNS04CreateEntrySuccess_Type = DisplayString
_Kpi53QNS04CreateEntrySuccess_Object = MibScalar
kpi53QNS04CreateEntrySuccess = _Kpi53QNS04CreateEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 3),
    _Kpi53QNS04CreateEntrySuccess_Type()
)
kpi53QNS04CreateEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04CreateEntrySuccess.setStatus("current")
_Kpi53QNS04DeleteEntryAvgTime_Type = DisplayString
_Kpi53QNS04DeleteEntryAvgTime_Object = MibScalar
kpi53QNS04DeleteEntryAvgTime = _Kpi53QNS04DeleteEntryAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 4),
    _Kpi53QNS04DeleteEntryAvgTime_Type()
)
kpi53QNS04DeleteEntryAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04DeleteEntryAvgTime.setStatus("current")
_Kpi53QNS04DeleteEntrySuccess_Type = DisplayString
_Kpi53QNS04DeleteEntrySuccess_Object = MibScalar
kpi53QNS04DeleteEntrySuccess = _Kpi53QNS04DeleteEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 5),
    _Kpi53QNS04DeleteEntrySuccess_Type()
)
kpi53QNS04DeleteEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04DeleteEntrySuccess.setStatus("current")
_Kpi53QNS04GetSessionActionAvgTime_Type = DisplayString
_Kpi53QNS04GetSessionActionAvgTime_Object = MibScalar
kpi53QNS04GetSessionActionAvgTime = _Kpi53QNS04GetSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 6),
    _Kpi53QNS04GetSessionActionAvgTime_Type()
)
kpi53QNS04GetSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04GetSessionActionAvgTime.setStatus("current")
_Kpi53QNS04GetSessionActionSuccess_Type = DisplayString
_Kpi53QNS04GetSessionActionSuccess_Object = MibScalar
kpi53QNS04GetSessionActionSuccess = _Kpi53QNS04GetSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 7),
    _Kpi53QNS04GetSessionActionSuccess_Type()
)
kpi53QNS04GetSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04GetSessionActionSuccess.setStatus("current")
_Kpi53QNS04LockSessionActionAvgTime_Type = DisplayString
_Kpi53QNS04LockSessionActionAvgTime_Object = MibScalar
kpi53QNS04LockSessionActionAvgTime = _Kpi53QNS04LockSessionActionAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 8),
    _Kpi53QNS04LockSessionActionAvgTime_Type()
)
kpi53QNS04LockSessionActionAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04LockSessionActionAvgTime.setStatus("current")
_Kpi53QNS04LockSessionActionSuccess_Type = DisplayString
_Kpi53QNS04LockSessionActionSuccess_Object = MibScalar
kpi53QNS04LockSessionActionSuccess = _Kpi53QNS04LockSessionActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 9),
    _Kpi53QNS04LockSessionActionSuccess_Type()
)
kpi53QNS04LockSessionActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04LockSessionActionSuccess.setStatus("current")
_Kpi53QNS04PushQuotaAvgTime_Type = DisplayString
_Kpi53QNS04PushQuotaAvgTime_Object = MibScalar
kpi53QNS04PushQuotaAvgTime = _Kpi53QNS04PushQuotaAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 10),
    _Kpi53QNS04PushQuotaAvgTime_Type()
)
kpi53QNS04PushQuotaAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04PushQuotaAvgTime.setStatus("current")
_Kpi53QNS04PushQuotaSuccess_Type = DisplayString
_Kpi53QNS04PushQuotaSuccess_Object = MibScalar
kpi53QNS04PushQuotaSuccess = _Kpi53QNS04PushQuotaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 11),
    _Kpi53QNS04PushQuotaSuccess_Type()
)
kpi53QNS04PushQuotaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04PushQuotaSuccess.setStatus("current")
_Kpi53QNS04QuotaCalculationAvgTime_Type = DisplayString
_Kpi53QNS04QuotaCalculationAvgTime_Object = MibScalar
kpi53QNS04QuotaCalculationAvgTime = _Kpi53QNS04QuotaCalculationAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 12),
    _Kpi53QNS04QuotaCalculationAvgTime_Type()
)
kpi53QNS04QuotaCalculationAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04QuotaCalculationAvgTime.setStatus("current")
_Kpi53QNS04QuotaCalculationSuccess_Type = DisplayString
_Kpi53QNS04QuotaCalculationSuccess_Object = MibScalar
kpi53QNS04QuotaCalculationSuccess = _Kpi53QNS04QuotaCalculationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 13),
    _Kpi53QNS04QuotaCalculationSuccess_Type()
)
kpi53QNS04QuotaCalculationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04QuotaCalculationSuccess.setStatus("current")
_Kpi53QNS04QuotaDepletedRequestAvgTime_Type = DisplayString
_Kpi53QNS04QuotaDepletedRequestAvgTime_Object = MibScalar
kpi53QNS04QuotaDepletedRequestAvgTime = _Kpi53QNS04QuotaDepletedRequestAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 14),
    _Kpi53QNS04QuotaDepletedRequestAvgTime_Type()
)
kpi53QNS04QuotaDepletedRequestAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04QuotaDepletedRequestAvgTime.setStatus("current")
_Kpi53QNS04QuotaDepletedRequestSucccess_Type = DisplayString
_Kpi53QNS04QuotaDepletedRequestSucccess_Object = MibScalar
kpi53QNS04QuotaDepletedRequestSucccess = _Kpi53QNS04QuotaDepletedRequestSucccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 15),
    _Kpi53QNS04QuotaDepletedRequestSucccess_Type()
)
kpi53QNS04QuotaDepletedRequestSucccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04QuotaDepletedRequestSucccess.setStatus("current")
_Kpi53QNS04RadiusAccountingMessageAvgTime_Type = DisplayString
_Kpi53QNS04RadiusAccountingMessageAvgTime_Object = MibScalar
kpi53QNS04RadiusAccountingMessageAvgTime = _Kpi53QNS04RadiusAccountingMessageAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 16),
    _Kpi53QNS04RadiusAccountingMessageAvgTime_Type()
)
kpi53QNS04RadiusAccountingMessageAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04RadiusAccountingMessageAvgTime.setStatus("current")
_Kpi53QNS04RadiusAccountingMessageSuccess_Type = DisplayString
_Kpi53QNS04RadiusAccountingMessageSuccess_Object = MibScalar
kpi53QNS04RadiusAccountingMessageSuccess = _Kpi53QNS04RadiusAccountingMessageSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 17),
    _Kpi53QNS04RadiusAccountingMessageSuccess_Type()
)
kpi53QNS04RadiusAccountingMessageSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04RadiusAccountingMessageSuccess.setStatus("current")
_Kpi53QNS04RetrieveSumAvPairAvgTime_Type = DisplayString
_Kpi53QNS04RetrieveSumAvPairAvgTime_Object = MibScalar
kpi53QNS04RetrieveSumAvPairAvgTime = _Kpi53QNS04RetrieveSumAvPairAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 18),
    _Kpi53QNS04RetrieveSumAvPairAvgTime_Type()
)
kpi53QNS04RetrieveSumAvPairAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04RetrieveSumAvPairAvgTime.setStatus("current")
_Kpi53QNS04RetrieveSumAvPairSuccess_Type = DisplayString
_Kpi53QNS04RetrieveSumAvPairSuccess_Object = MibScalar
kpi53QNS04RetrieveSumAvPairSuccess = _Kpi53QNS04RetrieveSumAvPairSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 19),
    _Kpi53QNS04RetrieveSumAvPairSuccess_Type()
)
kpi53QNS04RetrieveSumAvPairSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04RetrieveSumAvPairSuccess.setStatus("current")
_Kpi53QNS04PolicyCount_Type = DisplayString
_Kpi53QNS04PolicyCount_Object = MibScalar
kpi53QNS04PolicyCount = _Kpi53QNS04PolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 20),
    _Kpi53QNS04PolicyCount_Type()
)
kpi53QNS04PolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04PolicyCount.setStatus("current")
_Kpi53QNS04QueueSize_Type = DisplayString
_Kpi53QNS04QueueSize_Object = MibScalar
kpi53QNS04QueueSize = _Kpi53QNS04QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 21),
    _Kpi53QNS04QueueSize_Type()
)
kpi53QNS04QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04QueueSize.setStatus("current")
_Kpi53QNS04FailedEnqueueCount_Type = DisplayString
_Kpi53QNS04FailedEnqueueCount_Object = MibScalar
kpi53QNS04FailedEnqueueCount = _Kpi53QNS04FailedEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 22),
    _Kpi53QNS04FailedEnqueueCount_Type()
)
kpi53QNS04FailedEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04FailedEnqueueCount.setStatus("current")
_Kpi53QNS04ErrorCount_Type = DisplayString
_Kpi53QNS04ErrorCount_Object = MibScalar
kpi53QNS04ErrorCount = _Kpi53QNS04ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 23),
    _Kpi53QNS04ErrorCount_Type()
)
kpi53QNS04ErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04ErrorCount.setStatus("current")
_Kpi53QNS04SessionCount_Type = DisplayString
_Kpi53QNS04SessionCount_Object = MibScalar
kpi53QNS04SessionCount = _Kpi53QNS04SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 24),
    _Kpi53QNS04SessionCount_Type()
)
kpi53QNS04SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04SessionCount.setStatus("current")
_Kpi53QNS04FreeMemory_Type = DisplayString
_Kpi53QNS04FreeMemory_Object = MibScalar
kpi53QNS04FreeMemory = _Kpi53QNS04FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 3, 53, 44, 25),
    _Kpi53QNS04FreeMemory_Type()
)
kpi53QNS04FreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpi53QNS04FreeMemory.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROADHOP-QNS-MIB",
    **{"broadhopProductsQNS": broadhopProductsQNS,
       "broadhopProductsQNSComponents": broadhopProductsQNSComponents,
       "broadhopProductsQNSComponents53": broadhopProductsQNSComponents53,
       "broadhopProductsQNSComponents53LB01": broadhopProductsQNSComponents53LB01,
       "component53LB01CpuUser": component53LB01CpuUser,
       "component53LB01CpuSystem": component53LB01CpuSystem,
       "component53LB01CpuIdle": component53LB01CpuIdle,
       "component53LB01LoadAverage1": component53LB01LoadAverage1,
       "component53LB01LoadAverage5": component53LB01LoadAverage5,
       "component53LB01LoadAverage15": component53LB01LoadAverage15,
       "component53LB01MemoryTotal": component53LB01MemoryTotal,
       "component53LB01MemoryAvailable": component53LB01MemoryAvailable,
       "component53LB01SwapTotal": component53LB01SwapTotal,
       "component53LB01SwapAvailable": component53LB01SwapAvailable,
       "component53LB01Eth0InOctets": component53LB01Eth0InOctets,
       "component53LB01Eth0OutOctets": component53LB01Eth0OutOctets,
       "component53LB01Eth1InOctets": component53LB01Eth1InOctets,
       "component53LB01Eth1OutOctets": component53LB01Eth1OutOctets,
       "broadhopProductsQNSComponents53LB02": broadhopProductsQNSComponents53LB02,
       "component53LB02CpuUser": component53LB02CpuUser,
       "component53LB02CpuSystem": component53LB02CpuSystem,
       "component53LB02CpuIdle": component53LB02CpuIdle,
       "component53LB02LoadAverage1": component53LB02LoadAverage1,
       "component53LB02LoadAverage5": component53LB02LoadAverage5,
       "component53LB02LoadAverage15": component53LB02LoadAverage15,
       "component53LB02MemoryTotal": component53LB02MemoryTotal,
       "component53LB02MemoryAvailable": component53LB02MemoryAvailable,
       "component53LB02SwapTotal": component53LB02SwapTotal,
       "component53LB02SwapAvailable": component53LB02SwapAvailable,
       "component53LB02Eth0InOctets": component53LB02Eth0InOctets,
       "component53LB02Eth0OutOctets": component53LB02Eth0OutOctets,
       "component53LB02Eth1InOctets": component53LB02Eth1InOctets,
       "component53LB02Eth1OutOctets": component53LB02Eth1OutOctets,
       "broadhopProductsQNSComponents53PortalLB01": broadhopProductsQNSComponents53PortalLB01,
       "component53PortalLB01CpuUser": component53PortalLB01CpuUser,
       "component53PortalLB01CpuSystem": component53PortalLB01CpuSystem,
       "component53PortalLB01CpuIdle": component53PortalLB01CpuIdle,
       "component53PortalLB01LoadAverage1": component53PortalLB01LoadAverage1,
       "component53PortalLB01LoadAverage5": component53PortalLB01LoadAverage5,
       "component53PortalLB01LoadAverage15": component53PortalLB01LoadAverage15,
       "component53PortalLB01MemoryTotal": component53PortalLB01MemoryTotal,
       "component53PortalLB01MemoryAvailable": component53PortalLB01MemoryAvailable,
       "component53PortalLB01SwapTotal": component53PortalLB01SwapTotal,
       "component53PortalLB01SwapAvailable": component53PortalLB01SwapAvailable,
       "component53PortalLB01Eth0InOctets": component53PortalLB01Eth0InOctets,
       "component53PortalLB01Eth0OutOctets": component53PortalLB01Eth0OutOctets,
       "component53PortalLB01Eth1InOctets": component53PortalLB01Eth1InOctets,
       "component53PortalLB01Eth1OutOctets": component53PortalLB01Eth1OutOctets,
       "broadhopProductsQNSComponents53PortalLB02": broadhopProductsQNSComponents53PortalLB02,
       "component53PortalLB02CpuUser": component53PortalLB02CpuUser,
       "component53PortalLB02CpuSystem": component53PortalLB02CpuSystem,
       "component53PortalLB02CpuIdle": component53PortalLB02CpuIdle,
       "component53PortalLB02LoadAverage1": component53PortalLB02LoadAverage1,
       "component53PortalLB02LoadAverage5": component53PortalLB02LoadAverage5,
       "component53PortalLB02LoadAverage15": component53PortalLB02LoadAverage15,
       "component53PortalLB02MemoryTotal": component53PortalLB02MemoryTotal,
       "component53PortalLB02MemoryAvailable": component53PortalLB02MemoryAvailable,
       "component53PortalLB02SwapTotal": component53PortalLB02SwapTotal,
       "component53PortalLB02SwapAvailable": component53PortalLB02SwapAvailable,
       "component53PortalLB02Eth0InOctets": component53PortalLB02Eth0InOctets,
       "component53PortalLB02Eth0OutOctets": component53PortalLB02Eth0OutOctets,
       "component53PortalLB02Eth1InOctets": component53PortalLB02Eth1InOctets,
       "component53PortalLB02Eth1OutOctets": component53PortalLB02Eth1OutOctets,
       "broadhopProductsQNSComponents53PCRFClient01": broadhopProductsQNSComponents53PCRFClient01,
       "component53PCRFClient01CpuUser": component53PCRFClient01CpuUser,
       "component53PCRFClient01CpuSystem": component53PCRFClient01CpuSystem,
       "component53PCRFClient01CpuIdle": component53PCRFClient01CpuIdle,
       "component53PCRFClient01LoadAverage1": component53PCRFClient01LoadAverage1,
       "component53PCRFClient01LoadAverage5": component53PCRFClient01LoadAverage5,
       "component53PCRFClient01LoadAverage15": component53PCRFClient01LoadAverage15,
       "component53PCRFClient01MemoryTotal": component53PCRFClient01MemoryTotal,
       "component53PCRFClient01MemoryAvailable": component53PCRFClient01MemoryAvailable,
       "component53PCRFClient01SwapTotal": component53PCRFClient01SwapTotal,
       "component53PCRFClient01SwapAvailable": component53PCRFClient01SwapAvailable,
       "component53PCRFClient01Eth0InOctets": component53PCRFClient01Eth0InOctets,
       "component53PCRFClient01Eth0OutOctets": component53PCRFClient01Eth0OutOctets,
       "component53PCRFClient01Eth1InOctets": component53PCRFClient01Eth1InOctets,
       "component53PCRFClient01Eth1OutOctets": component53PCRFClient01Eth1OutOctets,
       "broadhopProductsQNSComponents53PCRFClient02": broadhopProductsQNSComponents53PCRFClient02,
       "component53PCRFClient02CpuUser": component53PCRFClient02CpuUser,
       "component53PCRFClient02CpuSystem": component53PCRFClient02CpuSystem,
       "component53PCRFClient02CpuIdle": component53PCRFClient02CpuIdle,
       "component53PCRFClient02LoadAverage1": component53PCRFClient02LoadAverage1,
       "component53PCRFClient02LoadAverage5": component53PCRFClient02LoadAverage5,
       "component53PCRFClient02LoadAverage15": component53PCRFClient02LoadAverage15,
       "component53PCRFClient02MemoryTotal": component53PCRFClient02MemoryTotal,
       "component53PCRFClient02MemoryAvailable": component53PCRFClient02MemoryAvailable,
       "component53PCRFClient02SwapTotal": component53PCRFClient02SwapTotal,
       "component53PCRFClient02SwapAvailable": component53PCRFClient02SwapAvailable,
       "component53PCRFClient02Eth0InOctets": component53PCRFClient02Eth0InOctets,
       "component53PCRFClient02Eth0OutOctets": component53PCRFClient02Eth0OutOctets,
       "component53PCRFClient02Eth1InOctets": component53PCRFClient02Eth1InOctets,
       "component53PCRFClient02Eth1OutOctets": component53PCRFClient02Eth1OutOctets,
       "broadhopProductsQNSComponents53SessionMgr01": broadhopProductsQNSComponents53SessionMgr01,
       "component53SessionMgr01CpuUser": component53SessionMgr01CpuUser,
       "component53SessionMgr01CpuSystem": component53SessionMgr01CpuSystem,
       "component53SessionMgr01CpuIdle": component53SessionMgr01CpuIdle,
       "component53SessionMgr01LoadAverage1": component53SessionMgr01LoadAverage1,
       "component53SessionMgr01LoadAverage5": component53SessionMgr01LoadAverage5,
       "component53SessionMgr01LoadAverage15": component53SessionMgr01LoadAverage15,
       "component53SessionMgr01MemoryTotal": component53SessionMgr01MemoryTotal,
       "component53SessionMgr01MemoryAvailable": component53SessionMgr01MemoryAvailable,
       "component53SessionMgr01SwapTotal": component53SessionMgr01SwapTotal,
       "component53SessionMgr01SwapAvailable": component53SessionMgr01SwapAvailable,
       "component53SessionMgr01Eth0InOctets": component53SessionMgr01Eth0InOctets,
       "component53SessionMgr01Eth0OutOctets": component53SessionMgr01Eth0OutOctets,
       "component53SessionMgr01Eth1InOctets": component53SessionMgr01Eth1InOctets,
       "component53SessionMgr01Eth1OutOctets": component53SessionMgr01Eth1OutOctets,
       "broadhopProductsQNSComponents53SessionMgr02": broadhopProductsQNSComponents53SessionMgr02,
       "component53SessionMgr02CpuUser": component53SessionMgr02CpuUser,
       "component53SessionMgr02CpuSystem": component53SessionMgr02CpuSystem,
       "component53SessionMgr02CpuIdle": component53SessionMgr02CpuIdle,
       "component53SessionMgr02LoadAverage1": component53SessionMgr02LoadAverage1,
       "component53SessionMgr02LoadAverage5": component53SessionMgr02LoadAverage5,
       "component53SessionMgr02LoadAverage15": component53SessionMgr02LoadAverage15,
       "component53SessionMgr02MemoryTotal": component53SessionMgr02MemoryTotal,
       "component53SessionMgr02MemoryAvailable": component53SessionMgr02MemoryAvailable,
       "component53SessionMgr02SwapTotal": component53SessionMgr02SwapTotal,
       "component53SessionMgr02SwapAvailable": component53SessionMgr02SwapAvailable,
       "component53SessionMgr02Eth0InOctets": component53SessionMgr02Eth0InOctets,
       "component53SessionMgr02Eth0OutOctets": component53SessionMgr02Eth0OutOctets,
       "component53SessionMgr02Eth1InOctets": component53SessionMgr02Eth1InOctets,
       "component53SessionMgr02Eth1OutOctets": component53SessionMgr02Eth1OutOctets,
       "broadhopProductsQNSComponents53QNS01": broadhopProductsQNSComponents53QNS01,
       "component53QNS01CpuUser": component53QNS01CpuUser,
       "component53QNS01CpuSystem": component53QNS01CpuSystem,
       "component53QNS01CpuIdle": component53QNS01CpuIdle,
       "component53QNS01LoadAverage1": component53QNS01LoadAverage1,
       "component53QNS01LoadAverage5": component53QNS01LoadAverage5,
       "component53QNS01LoadAverage15": component53QNS01LoadAverage15,
       "component53QNS01MemoryTotal": component53QNS01MemoryTotal,
       "component53QNS01MemoryAvailable": component53QNS01MemoryAvailable,
       "component53QNS01SwapTotal": component53QNS01SwapTotal,
       "component53QNS01SwapAvailable": component53QNS01SwapAvailable,
       "component53QNS01Eth0InOctets": component53QNS01Eth0InOctets,
       "component53QNS01Eth0OutOctets": component53QNS01Eth0OutOctets,
       "component53QNS01Eth1InOctets": component53QNS01Eth1InOctets,
       "component53QNS01Eth1OutOctets": component53QNS01Eth1OutOctets,
       "broadhopProductsQNSComponents53QNS02": broadhopProductsQNSComponents53QNS02,
       "component53QNS02CpuUser": component53QNS02CpuUser,
       "component53QNS02CpuSystem": component53QNS02CpuSystem,
       "component53QNS02CpuIdle": component53QNS02CpuIdle,
       "component53QNS02LoadAverage1": component53QNS02LoadAverage1,
       "component53QNS02LoadAverage5": component53QNS02LoadAverage5,
       "component53QNS02LoadAverage15": component53QNS02LoadAverage15,
       "component53QNS02MemoryTotal": component53QNS02MemoryTotal,
       "component53QNS02MemoryAvailable": component53QNS02MemoryAvailable,
       "component53QNS02SwapTotal": component53QNS02SwapTotal,
       "component53QNS02SwapAvailable": component53QNS02SwapAvailable,
       "component53QNS02Eth0InOctets": component53QNS02Eth0InOctets,
       "component53QNS02Eth0OutOctets": component53QNS02Eth0OutOctets,
       "component53QNS02Eth1InOctets": component53QNS02Eth1InOctets,
       "component53QNS02Eth1OutOctets": component53QNS02Eth1OutOctets,
       "broadhopProductsQNSComponents53QNS03": broadhopProductsQNSComponents53QNS03,
       "component53QNS03CpuUser": component53QNS03CpuUser,
       "component53QNS03CpuSystem": component53QNS03CpuSystem,
       "component53QNS03CpuIdle": component53QNS03CpuIdle,
       "component53QNS03LoadAverage1": component53QNS03LoadAverage1,
       "component53QNS03LoadAverage5": component53QNS03LoadAverage5,
       "component53QNS03LoadAverage15": component53QNS03LoadAverage15,
       "component53QNS03MemoryTotal": component53QNS03MemoryTotal,
       "component53QNS03MemoryAvailable": component53QNS03MemoryAvailable,
       "component53QNS03SwapTotal": component53QNS03SwapTotal,
       "component53QNS03SwapAvailable": component53QNS03SwapAvailable,
       "component53QNS03Eth0InOctets": component53QNS03Eth0InOctets,
       "component53QNS03Eth0OutOctets": component53QNS03Eth0OutOctets,
       "component53QNS03Eth1InOctets": component53QNS03Eth1InOctets,
       "component53QNS03Eth1OutOctets": component53QNS03Eth1OutOctets,
       "broadhopProductsQNSComponents53QNS04": broadhopProductsQNSComponents53QNS04,
       "component53QNS04CpuUser": component53QNS04CpuUser,
       "component53QNS04CpuSystem": component53QNS04CpuSystem,
       "component53QNS04CpuIdle": component53QNS04CpuIdle,
       "component53QNS04LoadAverage1": component53QNS04LoadAverage1,
       "component53QNS04LoadAverage5": component53QNS04LoadAverage5,
       "component53QNS04LoadAverage15": component53QNS04LoadAverage15,
       "component53QNS04MemoryTotal": component53QNS04MemoryTotal,
       "component53QNS04MemoryAvailable": component53QNS04MemoryAvailable,
       "component53QNS04SwapTotal": component53QNS04SwapTotal,
       "component53QNS04SwapAvailable": component53QNS04SwapAvailable,
       "component53QNS04Eth0InOctets": component53QNS04Eth0InOctets,
       "component53QNS04Eth0OutOctets": component53QNS04Eth0OutOctets,
       "component53QNS04Eth1InOctets": component53QNS04Eth1InOctets,
       "component53QNS04Eth1OutOctets": component53QNS04Eth1OutOctets,
       "broadhopProductsQNSComponents53Portal01": broadhopProductsQNSComponents53Portal01,
       "component53Portal01CpuUser": component53Portal01CpuUser,
       "component53Portal01CpuSystem": component53Portal01CpuSystem,
       "component53Portal01CpuIdle": component53Portal01CpuIdle,
       "component53Portal01LoadAverage1": component53Portal01LoadAverage1,
       "component53Portal01LoadAverage5": component53Portal01LoadAverage5,
       "component53Portal01LoadAverage15": component53Portal01LoadAverage15,
       "component53Portal01MemoryTotal": component53Portal01MemoryTotal,
       "component53Portal01MemoryAvailable": component53Portal01MemoryAvailable,
       "component53Portal01SwapTotal": component53Portal01SwapTotal,
       "component53Portal01SwapAvailable": component53Portal01SwapAvailable,
       "component53Portal01Eth0InOctets": component53Portal01Eth0InOctets,
       "component53Portal01Eth0OutOctets": component53Portal01Eth0OutOctets,
       "component53Portal01Eth1InOctets": component53Portal01Eth1InOctets,
       "component53Portal01Eth1OutOctets": component53Portal01Eth1OutOctets,
       "broadhopProductsQNSComponents53Portal02": broadhopProductsQNSComponents53Portal02,
       "component53Portal02CpuUser": component53Portal02CpuUser,
       "component53Portal02CpuSystem": component53Portal02CpuSystem,
       "component53Portal02CpuIdle": component53Portal02CpuIdle,
       "component53Portal02LoadAverage1": component53Portal02LoadAverage1,
       "component53Portal02LoadAverage5": component53Portal02LoadAverage5,
       "component53Portal02LoadAverage15": component53Portal02LoadAverage15,
       "component53Portal02MemoryTotal": component53Portal02MemoryTotal,
       "component53Portal02MemoryAvailable": component53Portal02MemoryAvailable,
       "component53Portal02SwapTotal": component53Portal02SwapTotal,
       "component53Portal02SwapAvailable": component53Portal02SwapAvailable,
       "component53Portal02Eth0InOctets": component53Portal02Eth0InOctets,
       "component53Portal02Eth0OutOctets": component53Portal02Eth0OutOctets,
       "component53Portal02Eth1InOctets": component53Portal02Eth1InOctets,
       "component53Portal02Eth1OutOctets": component53Portal02Eth1OutOctets,
       "broadhopProductsQNSConsolidatedKPIVersion": broadhopProductsQNSConsolidatedKPIVersion,
       "broadhopProductsQNSConsolidatedKPI52": broadhopProductsQNSConsolidatedKPI52,
       "consolidatedKPI52QNS": consolidatedKPI52QNS,
       "consolidatedKPI52QNS01": consolidatedKPI52QNS01,
       "kpi52QNS01RealServerStatus": kpi52QNS01RealServerStatus,
       "kpi52QNS01CreateEntryAvgTime": kpi52QNS01CreateEntryAvgTime,
       "kpi52QNS01CreateEntrySuccess": kpi52QNS01CreateEntrySuccess,
       "kpi52QNS01DeleteEntryAvgTime": kpi52QNS01DeleteEntryAvgTime,
       "kpi52QNS01DeleteEntrySuccess": kpi52QNS01DeleteEntrySuccess,
       "kpi52QNS01GetSessionActionAvgTime": kpi52QNS01GetSessionActionAvgTime,
       "kpi52QNS01GetSessionActionSuccess": kpi52QNS01GetSessionActionSuccess,
       "kpi52QNS01LockSessionActionAvgTime": kpi52QNS01LockSessionActionAvgTime,
       "kpi52QNS01LockSessionActionSuccess": kpi52QNS01LockSessionActionSuccess,
       "kpi52QNS01PushQuotaAvgTime": kpi52QNS01PushQuotaAvgTime,
       "kpi52QNS01PushQuotaSuccess": kpi52QNS01PushQuotaSuccess,
       "kpi52QNS01QuotaCalculationAvgTime": kpi52QNS01QuotaCalculationAvgTime,
       "kpi52QNS01QuotaCalculationSuccess": kpi52QNS01QuotaCalculationSuccess,
       "kpi52QNS01QuotaDepletedRequestAvgTime": kpi52QNS01QuotaDepletedRequestAvgTime,
       "kpi52QNS01QuotaDepletedRequestSucccess": kpi52QNS01QuotaDepletedRequestSucccess,
       "kpi52QNS01RadiusAccountingMessageAvgTime": kpi52QNS01RadiusAccountingMessageAvgTime,
       "kpi52QNS01RadiusAccountingMessageSuccess": kpi52QNS01RadiusAccountingMessageSuccess,
       "kpi52QNS01RetrieveSumAvPairAvgTime": kpi52QNS01RetrieveSumAvPairAvgTime,
       "kpi52QNS01RetrieveSumAvPairSuccess": kpi52QNS01RetrieveSumAvPairSuccess,
       "kpi52QNS01PolicyCount": kpi52QNS01PolicyCount,
       "kpi52QNS01QueueSize": kpi52QNS01QueueSize,
       "kpi52QNS01FailedEnqueueCount": kpi52QNS01FailedEnqueueCount,
       "kpi52QNS01ErrorCount": kpi52QNS01ErrorCount,
       "kpi52QNS01SessionCount": kpi52QNS01SessionCount,
       "kpi52QNS01FreeMemory": kpi52QNS01FreeMemory,
       "consolidatedKPI52QNS02": consolidatedKPI52QNS02,
       "kpi52QNS02RealServerStatus": kpi52QNS02RealServerStatus,
       "kpi52QNS02CreateEntryAvgTime": kpi52QNS02CreateEntryAvgTime,
       "kpi52QNS02CreateEntrySuccess": kpi52QNS02CreateEntrySuccess,
       "kpi52QNS02DeleteEntryAvgTime": kpi52QNS02DeleteEntryAvgTime,
       "kpi52QNS02DeleteEntrySuccess": kpi52QNS02DeleteEntrySuccess,
       "kpi52QNS02GetSessionActionAvgTime": kpi52QNS02GetSessionActionAvgTime,
       "kpi52QNS02GetSessionActionSuccess": kpi52QNS02GetSessionActionSuccess,
       "kpi52QNS02LockSessionActionAvgTime": kpi52QNS02LockSessionActionAvgTime,
       "kpi52QNS02LockSessionActionSuccess": kpi52QNS02LockSessionActionSuccess,
       "kpi52QNS02PushQuotaAvgTime": kpi52QNS02PushQuotaAvgTime,
       "kpi52QNS02PushQuotaSuccess": kpi52QNS02PushQuotaSuccess,
       "kpi52QNS02QuotaCalculationAvgTime": kpi52QNS02QuotaCalculationAvgTime,
       "kpi52QNS02QuotaCalculationSuccess": kpi52QNS02QuotaCalculationSuccess,
       "kpi52QNS02QuotaDepletedRequestAvgTime": kpi52QNS02QuotaDepletedRequestAvgTime,
       "kpi52QNS02QuotaDepletedRequestSucccess": kpi52QNS02QuotaDepletedRequestSucccess,
       "kpi52QNS02RadiusAccountingMessageAvgTime": kpi52QNS02RadiusAccountingMessageAvgTime,
       "kpi52QNS02RadiusAccountingMessageSuccess": kpi52QNS02RadiusAccountingMessageSuccess,
       "kpi52QNS02RetrieveSumAvPairAvgTime": kpi52QNS02RetrieveSumAvPairAvgTime,
       "kpi52QNS02RetrieveSumAvPairSuccess": kpi52QNS02RetrieveSumAvPairSuccess,
       "kpi52QNS02PolicyCount": kpi52QNS02PolicyCount,
       "kpi52QNS02QueueSize": kpi52QNS02QueueSize,
       "kpi52QNS02FailedEnqueueCount": kpi52QNS02FailedEnqueueCount,
       "kpi52QNS02ErrorCount": kpi52QNS02ErrorCount,
       "kpi52QNS02SessionCount": kpi52QNS02SessionCount,
       "kpi52QNS02FreeMemory": kpi52QNS02FreeMemory,
       "consolidatedKPI52QNS03": consolidatedKPI52QNS03,
       "kpi52QNS03RealServerStatus": kpi52QNS03RealServerStatus,
       "kpi52QNS03CreateEntryAvgTime": kpi52QNS03CreateEntryAvgTime,
       "kpi52QNS03CreateEntrySuccess": kpi52QNS03CreateEntrySuccess,
       "kpi52QNS03DeleteEntryAvgTime": kpi52QNS03DeleteEntryAvgTime,
       "kpi52QNS03DeleteEntrySuccess": kpi52QNS03DeleteEntrySuccess,
       "kpi52QNS03GetSessionActionAvgTime": kpi52QNS03GetSessionActionAvgTime,
       "kpi52QNS03GetSessionActionSuccess": kpi52QNS03GetSessionActionSuccess,
       "kpi52QNS03LockSessionActionAvgTime": kpi52QNS03LockSessionActionAvgTime,
       "kpi52QNS03LockSessionActionSuccess": kpi52QNS03LockSessionActionSuccess,
       "kpi52QNS03PushQuotaAvgTime": kpi52QNS03PushQuotaAvgTime,
       "kpi52QNS03PushQuotaSuccess": kpi52QNS03PushQuotaSuccess,
       "kpi52QNS03QuotaCalculationAvgTime": kpi52QNS03QuotaCalculationAvgTime,
       "kpi52QNS03QuotaCalculationSuccess": kpi52QNS03QuotaCalculationSuccess,
       "kpi52QNS03QuotaDepletedRequestAvgTime": kpi52QNS03QuotaDepletedRequestAvgTime,
       "kpi52QNS03QuotaDepletedRequestSucccess": kpi52QNS03QuotaDepletedRequestSucccess,
       "kpi52QNS03RadiusAccountingMessageAvgTime": kpi52QNS03RadiusAccountingMessageAvgTime,
       "kpi52QNS03RadiusAccountingMessageSuccess": kpi52QNS03RadiusAccountingMessageSuccess,
       "kpi52QNS03RetrieveSumAvPairAvgTime": kpi52QNS03RetrieveSumAvPairAvgTime,
       "kpi52QNS03RetrieveSumAvPairSuccess": kpi52QNS03RetrieveSumAvPairSuccess,
       "kpi52QNS03PolicyCount": kpi52QNS03PolicyCount,
       "kpi52QNS03QueueSize": kpi52QNS03QueueSize,
       "kpi52QNS03FailedEnqueueCount": kpi52QNS03FailedEnqueueCount,
       "kpi52QNS03ErrorCount": kpi52QNS03ErrorCount,
       "kpi52QNS03SessionCount": kpi52QNS03SessionCount,
       "kpi52QNS03FreeMemory": kpi52QNS03FreeMemory,
       "consolidatedKPI52QNS04": consolidatedKPI52QNS04,
       "kpi52QNS04RealServerStatus": kpi52QNS04RealServerStatus,
       "kpi52QNS04CreateEntryAvgTime": kpi52QNS04CreateEntryAvgTime,
       "kpi52QNS04CreateEntrySuccess": kpi52QNS04CreateEntrySuccess,
       "kpi52QNS04DeleteEntryAvgTime": kpi52QNS04DeleteEntryAvgTime,
       "kpi52QNS04DeleteEntrySuccess": kpi52QNS04DeleteEntrySuccess,
       "kpi52QNS04GetSessionActionAvgTime": kpi52QNS04GetSessionActionAvgTime,
       "kpi52QNS04GetSessionActionSuccess": kpi52QNS04GetSessionActionSuccess,
       "kpi52QNS04LockSessionActionAvgTime": kpi52QNS04LockSessionActionAvgTime,
       "kpi52QNS04LockSessionActionSuccess": kpi52QNS04LockSessionActionSuccess,
       "kpi52QNS04PushQuotaAvgTime": kpi52QNS04PushQuotaAvgTime,
       "kpi52QNS04PushQuotaSuccess": kpi52QNS04PushQuotaSuccess,
       "kpi52QNS04QuotaCalculationAvgTime": kpi52QNS04QuotaCalculationAvgTime,
       "kpi52QNS04QuotaCalculationSuccess": kpi52QNS04QuotaCalculationSuccess,
       "kpi52QNS04QuotaDepletedRequestAvgTime": kpi52QNS04QuotaDepletedRequestAvgTime,
       "kpi52QNS04QuotaDepletedRequestSucccess": kpi52QNS04QuotaDepletedRequestSucccess,
       "kpi52QNS04RadiusAccountingMessageAvgTime": kpi52QNS04RadiusAccountingMessageAvgTime,
       "kpi52QNS04RadiusAccountingMessageSuccess": kpi52QNS04RadiusAccountingMessageSuccess,
       "kpi52QNS04RetrieveSumAvPairAvgTime": kpi52QNS04RetrieveSumAvPairAvgTime,
       "kpi52QNS04RetrieveSumAvPairSuccess": kpi52QNS04RetrieveSumAvPairSuccess,
       "kpi52QNS04PolicyCount": kpi52QNS04PolicyCount,
       "kpi52QNS04QueueSize": kpi52QNS04QueueSize,
       "kpi52QNS04FailedEnqueueCount": kpi52QNS04FailedEnqueueCount,
       "kpi52QNS04ErrorCount": kpi52QNS04ErrorCount,
       "kpi52QNS04SessionCount": kpi52QNS04SessionCount,
       "kpi52QNS04FreeMemory": kpi52QNS04FreeMemory,
       "consolidatedKPI52SUM": consolidatedKPI52SUM,
       "consolidatedKPI52SUM01": consolidatedKPI52SUM01,
       "kpi52Sum01RealServerStatus": kpi52Sum01RealServerStatus,
       "consolidatedKPI52SUM02": consolidatedKPI52SUM02,
       "kpi52Sum02RealServerStatus": kpi52Sum02RealServerStatus,
       "consolidatedKPI52MYSQL": consolidatedKPI52MYSQL,
       "consolidatedKPI52MYSQL01": consolidatedKPI52MYSQL01,
       "kpi52Mysql01RealServerStatus": kpi52Mysql01RealServerStatus,
       "kpi52Mysql01RealServerUptime": kpi52Mysql01RealServerUptime,
       "kpi52Mysql01SlowQueries": kpi52Mysql01SlowQueries,
       "kpi52Mysql01ThreadCount": kpi52Mysql01ThreadCount,
       "kpi52Mysql01QueriesPerSecond": kpi52Mysql01QueriesPerSecond,
       "consolidatedKPI52MYSQL02": consolidatedKPI52MYSQL02,
       "kpi52Mysql02RealServerStatus": kpi52Mysql02RealServerStatus,
       "kpi52Mysql02RealServerUptime": kpi52Mysql02RealServerUptime,
       "kpi52Mysql02SlowQueries": kpi52Mysql02SlowQueries,
       "kpi52Mysql02ThreadCount": kpi52Mysql02ThreadCount,
       "kpi52Mysql02QueriesPerSecond": kpi52Mysql02QueriesPerSecond,
       "broadhopProductsQNSKPI53": broadhopProductsQNSKPI53,
       "broadhopProductsQNSKPI53LB01": broadhopProductsQNSKPI53LB01,
       "kpi53LB01PCRFProxyExternalCurrentSessions": kpi53LB01PCRFProxyExternalCurrentSessions,
       "kpi53LB01PCRFProxyInternalCurrentSessions": kpi53LB01PCRFProxyInternalCurrentSessions,
       "broadhopProductsQNSKPI53LB02": broadhopProductsQNSKPI53LB02,
       "kpi53LB02PCRFProxyExternalCurrentSessions": kpi53LB02PCRFProxyExternalCurrentSessions,
       "kpi53LB02PCRFProxyInternalCurrentSessions": kpi53LB02PCRFProxyInternalCurrentSessions,
       "broadhopProductsQNSKPI53PortalLB01": broadhopProductsQNSKPI53PortalLB01,
       "kpi53PortalLB01PortalProxyExternalCurrentSessions": kpi53PortalLB01PortalProxyExternalCurrentSessions,
       "broadhopProductsQNSKPI53PortalLB02": broadhopProductsQNSKPI53PortalLB02,
       "kpi53PortalLB02PortalProxyExternalCurrentSessions": kpi53PortalLB02PortalProxyExternalCurrentSessions,
       "broadhopProductsQNSKPI53SessionMgr01": broadhopProductsQNSKPI53SessionMgr01,
       "broadhopProductsQNSKPI53SessionMgr02": broadhopProductsQNSKPI53SessionMgr02,
       "broadhopProductsQNSKPI53QNS01": broadhopProductsQNSKPI53QNS01,
       "kpi53QNS01CreateEntryAvgTime": kpi53QNS01CreateEntryAvgTime,
       "kpi53QNS01CreateEntrySuccess": kpi53QNS01CreateEntrySuccess,
       "kpi53QNS01DeleteEntryAvgTime": kpi53QNS01DeleteEntryAvgTime,
       "kpi53QNS01DeleteEntrySuccess": kpi53QNS01DeleteEntrySuccess,
       "kpi53QNS01GetSessionActionAvgTime": kpi53QNS01GetSessionActionAvgTime,
       "kpi53QNS01GetSessionActionSuccess": kpi53QNS01GetSessionActionSuccess,
       "kpi53QNS01LockSessionActionAvgTime": kpi53QNS01LockSessionActionAvgTime,
       "kpi53QNS01LockSessionActionSuccess": kpi53QNS01LockSessionActionSuccess,
       "kpi53QNS01PushQuotaAvgTime": kpi53QNS01PushQuotaAvgTime,
       "kpi53QNS01PushQuotaSuccess": kpi53QNS01PushQuotaSuccess,
       "kpi53QNS01QuotaCalculationAvgTime": kpi53QNS01QuotaCalculationAvgTime,
       "kpi53QNS01QuotaCalculationSuccess": kpi53QNS01QuotaCalculationSuccess,
       "kpi53QNS01QuotaDepletedRequestAvgTime": kpi53QNS01QuotaDepletedRequestAvgTime,
       "kpi53QNS01QuotaDepletedRequestSucccess": kpi53QNS01QuotaDepletedRequestSucccess,
       "kpi53QNS01RadiusAccountingMessageAvgTime": kpi53QNS01RadiusAccountingMessageAvgTime,
       "kpi53QNS01RadiusAccountingMessageSuccess": kpi53QNS01RadiusAccountingMessageSuccess,
       "kpi53QNS01RetrieveSumAvPairAvgTime": kpi53QNS01RetrieveSumAvPairAvgTime,
       "kpi53QNS01RetrieveSumAvPairSuccess": kpi53QNS01RetrieveSumAvPairSuccess,
       "kpi53QNS01PolicyCount": kpi53QNS01PolicyCount,
       "kpi53QNS01QueueSize": kpi53QNS01QueueSize,
       "kpi53QNS01FailedEnqueueCount": kpi53QNS01FailedEnqueueCount,
       "kpi53QNS01ErrorCount": kpi53QNS01ErrorCount,
       "kpi53QNS01SessionCount": kpi53QNS01SessionCount,
       "kpi53QNS01FreeMemory": kpi53QNS01FreeMemory,
       "broadhopProductsQNSKPI53QNS02": broadhopProductsQNSKPI53QNS02,
       "kpi53QNS02CreateEntryAvgTime": kpi53QNS02CreateEntryAvgTime,
       "kpi53QNS02CreateEntrySuccess": kpi53QNS02CreateEntrySuccess,
       "kpi53QNS02DeleteEntryAvgTime": kpi53QNS02DeleteEntryAvgTime,
       "kpi53QNS02DeleteEntrySuccess": kpi53QNS02DeleteEntrySuccess,
       "kpi53QNS02GetSessionActionAvgTime": kpi53QNS02GetSessionActionAvgTime,
       "kpi53QNS02GetSessionActionSuccess": kpi53QNS02GetSessionActionSuccess,
       "kpi53QNS02LockSessionActionAvgTime": kpi53QNS02LockSessionActionAvgTime,
       "kpi53QNS02LockSessionActionSuccess": kpi53QNS02LockSessionActionSuccess,
       "kpi53QNS02PushQuotaAvgTime": kpi53QNS02PushQuotaAvgTime,
       "kpi53QNS02PushQuotaSuccess": kpi53QNS02PushQuotaSuccess,
       "kpi53QNS02QuotaCalculationAvgTime": kpi53QNS02QuotaCalculationAvgTime,
       "kpi53QNS02QuotaCalculationSuccess": kpi53QNS02QuotaCalculationSuccess,
       "kpi53QNS02QuotaDepletedRequestAvgTime": kpi53QNS02QuotaDepletedRequestAvgTime,
       "kpi53QNS02QuotaDepletedRequestSucccess": kpi53QNS02QuotaDepletedRequestSucccess,
       "kpi53QNS02RadiusAccountingMessageAvgTime": kpi53QNS02RadiusAccountingMessageAvgTime,
       "kpi53QNS02RadiusAccountingMessageSuccess": kpi53QNS02RadiusAccountingMessageSuccess,
       "kpi53QNS02RetrieveSumAvPairAvgTime": kpi53QNS02RetrieveSumAvPairAvgTime,
       "kpi53QNS02RetrieveSumAvPairSuccess": kpi53QNS02RetrieveSumAvPairSuccess,
       "kpi53QNS02PolicyCount": kpi53QNS02PolicyCount,
       "kpi53QNS02QueueSize": kpi53QNS02QueueSize,
       "kpi53QNS02FailedEnqueueCount": kpi53QNS02FailedEnqueueCount,
       "kpi53QNS02ErrorCount": kpi53QNS02ErrorCount,
       "kpi53QNS02SessionCount": kpi53QNS02SessionCount,
       "kpi53QNS02FreeMemory": kpi53QNS02FreeMemory,
       "broadhopProductsQNSKPI53QNS03": broadhopProductsQNSKPI53QNS03,
       "kpi53QNS03CreateEntryAvgTime": kpi53QNS03CreateEntryAvgTime,
       "kpi53QNS03CreateEntrySuccess": kpi53QNS03CreateEntrySuccess,
       "kpi53QNS03DeleteEntryAvgTime": kpi53QNS03DeleteEntryAvgTime,
       "kpi53QNS03DeleteEntrySuccess": kpi53QNS03DeleteEntrySuccess,
       "kpi53QNS03GetSessionActionAvgTime": kpi53QNS03GetSessionActionAvgTime,
       "kpi53QNS03GetSessionActionSuccess": kpi53QNS03GetSessionActionSuccess,
       "kpi53QNS03LockSessionActionAvgTime": kpi53QNS03LockSessionActionAvgTime,
       "kpi53QNS03LockSessionActionSuccess": kpi53QNS03LockSessionActionSuccess,
       "kpi53QNS03PushQuotaAvgTime": kpi53QNS03PushQuotaAvgTime,
       "kpi53QNS03PushQuotaSuccess": kpi53QNS03PushQuotaSuccess,
       "kpi53QNS03QuotaCalculationAvgTime": kpi53QNS03QuotaCalculationAvgTime,
       "kpi53QNS03QuotaCalculationSuccess": kpi53QNS03QuotaCalculationSuccess,
       "kpi53QNS03QuotaDepletedRequestAvgTime": kpi53QNS03QuotaDepletedRequestAvgTime,
       "kpi53QNS03QuotaDepletedRequestSucccess": kpi53QNS03QuotaDepletedRequestSucccess,
       "kpi53QNS03RadiusAccountingMessageAvgTime": kpi53QNS03RadiusAccountingMessageAvgTime,
       "kpi53QNS03RadiusAccountingMessageSuccess": kpi53QNS03RadiusAccountingMessageSuccess,
       "kpi53QNS03RetrieveSumAvPairAvgTime": kpi53QNS03RetrieveSumAvPairAvgTime,
       "kpi53QNS03RetrieveSumAvPairSuccess": kpi53QNS03RetrieveSumAvPairSuccess,
       "kpi53QNS03PolicyCount": kpi53QNS03PolicyCount,
       "kpi53QNS03QueueSize": kpi53QNS03QueueSize,
       "kpi53QNS03FailedEnqueueCount": kpi53QNS03FailedEnqueueCount,
       "kpi53QNS03ErrorCount": kpi53QNS03ErrorCount,
       "kpi53QNS03SessionCount": kpi53QNS03SessionCount,
       "kpi53QNS03FreeMemory": kpi53QNS03FreeMemory,
       "broadhopProductsQNSKPI53QNS04": broadhopProductsQNSKPI53QNS04,
       "kpi53QNS04CreateEntryAvgTime": kpi53QNS04CreateEntryAvgTime,
       "kpi53QNS04CreateEntrySuccess": kpi53QNS04CreateEntrySuccess,
       "kpi53QNS04DeleteEntryAvgTime": kpi53QNS04DeleteEntryAvgTime,
       "kpi53QNS04DeleteEntrySuccess": kpi53QNS04DeleteEntrySuccess,
       "kpi53QNS04GetSessionActionAvgTime": kpi53QNS04GetSessionActionAvgTime,
       "kpi53QNS04GetSessionActionSuccess": kpi53QNS04GetSessionActionSuccess,
       "kpi53QNS04LockSessionActionAvgTime": kpi53QNS04LockSessionActionAvgTime,
       "kpi53QNS04LockSessionActionSuccess": kpi53QNS04LockSessionActionSuccess,
       "kpi53QNS04PushQuotaAvgTime": kpi53QNS04PushQuotaAvgTime,
       "kpi53QNS04PushQuotaSuccess": kpi53QNS04PushQuotaSuccess,
       "kpi53QNS04QuotaCalculationAvgTime": kpi53QNS04QuotaCalculationAvgTime,
       "kpi53QNS04QuotaCalculationSuccess": kpi53QNS04QuotaCalculationSuccess,
       "kpi53QNS04QuotaDepletedRequestAvgTime": kpi53QNS04QuotaDepletedRequestAvgTime,
       "kpi53QNS04QuotaDepletedRequestSucccess": kpi53QNS04QuotaDepletedRequestSucccess,
       "kpi53QNS04RadiusAccountingMessageAvgTime": kpi53QNS04RadiusAccountingMessageAvgTime,
       "kpi53QNS04RadiusAccountingMessageSuccess": kpi53QNS04RadiusAccountingMessageSuccess,
       "kpi53QNS04RetrieveSumAvPairAvgTime": kpi53QNS04RetrieveSumAvPairAvgTime,
       "kpi53QNS04RetrieveSumAvPairSuccess": kpi53QNS04RetrieveSumAvPairSuccess,
       "kpi53QNS04PolicyCount": kpi53QNS04PolicyCount,
       "kpi53QNS04QueueSize": kpi53QNS04QueueSize,
       "kpi53QNS04FailedEnqueueCount": kpi53QNS04FailedEnqueueCount,
       "kpi53QNS04ErrorCount": kpi53QNS04ErrorCount,
       "kpi53QNS04SessionCount": kpi53QNS04SessionCount,
       "kpi53QNS04FreeMemory": kpi53QNS04FreeMemory}
)
