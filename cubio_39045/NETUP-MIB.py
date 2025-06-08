# SNMP MIB module (NETUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cubio_39045/NETUP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:58:54 2025
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

netup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39054)
)
if mibBuilder.loadTexts:
    netup.setRevisions(
        ("1994-04-26 20:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetupHost_ObjectIdentity = ObjectIdentity
netupHost = _NetupHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39054, 1)
)
if mibBuilder.loadTexts:
    netupHost.setStatus("current")
_NetupCpuTable_Object = MibTable
netupCpuTable = _NetupCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 1)
)
if mibBuilder.loadTexts:
    netupCpuTable.setStatus("current")
_NetupCpuEntry_Object = MibTableRow
netupCpuEntry = _NetupCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 1, 1)
)
netupCpuEntry.setIndexNames(
    (0, "NETUP-MIB", "netupCpuIndex"),
)
if mibBuilder.loadTexts:
    netupCpuEntry.setStatus("current")


class _NetupCpuIndex_Type(Integer32):
    """Custom type netupCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetupCpuIndex_Type.__name__ = "Integer32"
_NetupCpuIndex_Object = MibTableColumn
netupCpuIndex = _NetupCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 1, 1, 1),
    _NetupCpuIndex_Type()
)
netupCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupCpuIndex.setStatus("current")


class _NetupCpuLoad_Type(Integer32):
    """Custom type netupCpuLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NetupCpuLoad_Type.__name__ = "Integer32"
_NetupCpuLoad_Object = MibTableColumn
netupCpuLoad = _NetupCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 1, 1, 2),
    _NetupCpuLoad_Type()
)
netupCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupCpuLoad.setStatus("current")


class _NetupCpuTemp_Type(Integer32):
    """Custom type netupCpuTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_NetupCpuTemp_Type.__name__ = "Integer32"
_NetupCpuTemp_Object = MibTableColumn
netupCpuTemp = _NetupCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 1, 1, 3),
    _NetupCpuTemp_Type()
)
netupCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupCpuTemp.setStatus("current")
_NetupMemory_ObjectIdentity = ObjectIdentity
netupMemory = _NetupMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39054, 1, 2)
)
if mibBuilder.loadTexts:
    netupMemory.setStatus("current")
_NetupMemPhisTotal_Type = Integer32
_NetupMemPhisTotal_Object = MibScalar
netupMemPhisTotal = _NetupMemPhisTotal_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 2, 1),
    _NetupMemPhisTotal_Type()
)
netupMemPhisTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupMemPhisTotal.setStatus("current")
if mibBuilder.loadTexts:
    netupMemPhisTotal.setUnits("kB")
_NetupMemPhisFree_Type = Integer32
_NetupMemPhisFree_Object = MibScalar
netupMemPhisFree = _NetupMemPhisFree_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 2, 2),
    _NetupMemPhisFree_Type()
)
netupMemPhisFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupMemPhisFree.setStatus("current")
if mibBuilder.loadTexts:
    netupMemPhisFree.setUnits("kB")
_NetupMemPhisBuffers_Type = Integer32
_NetupMemPhisBuffers_Object = MibScalar
netupMemPhisBuffers = _NetupMemPhisBuffers_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 2, 3),
    _NetupMemPhisBuffers_Type()
)
netupMemPhisBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupMemPhisBuffers.setStatus("current")
if mibBuilder.loadTexts:
    netupMemPhisBuffers.setUnits("kB")
_NetupMemPhisCached_Type = Integer32
_NetupMemPhisCached_Object = MibScalar
netupMemPhisCached = _NetupMemPhisCached_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 2, 4),
    _NetupMemPhisCached_Type()
)
netupMemPhisCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupMemPhisCached.setStatus("current")
if mibBuilder.loadTexts:
    netupMemPhisCached.setUnits("kB")
_NetupMemSwapTotal_Type = Integer32
_NetupMemSwapTotal_Object = MibScalar
netupMemSwapTotal = _NetupMemSwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 2, 5),
    _NetupMemSwapTotal_Type()
)
netupMemSwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupMemSwapTotal.setStatus("current")
if mibBuilder.loadTexts:
    netupMemSwapTotal.setUnits("kB")
_NetupMemSwapFree_Type = Integer32
_NetupMemSwapFree_Object = MibScalar
netupMemSwapFree = _NetupMemSwapFree_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 2, 6),
    _NetupMemSwapFree_Type()
)
netupMemSwapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupMemSwapFree.setStatus("current")
if mibBuilder.loadTexts:
    netupMemSwapFree.setUnits("kB")
_NetupStorageTable_Object = MibTable
netupStorageTable = _NetupStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3)
)
if mibBuilder.loadTexts:
    netupStorageTable.setStatus("current")
_NetupStorageEntry_Object = MibTableRow
netupStorageEntry = _NetupStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3, 1)
)
netupStorageEntry.setIndexNames(
    (0, "NETUP-MIB", "netupStorageIndex"),
)
if mibBuilder.loadTexts:
    netupStorageEntry.setStatus("current")


class _NetupStorageIndex_Type(Integer32):
    """Custom type netupStorageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetupStorageIndex_Type.__name__ = "Integer32"
_NetupStorageIndex_Object = MibTableColumn
netupStorageIndex = _NetupStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3, 1, 1),
    _NetupStorageIndex_Type()
)
netupStorageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupStorageIndex.setStatus("current")
_NetupStorageDevice_Type = OctetString
_NetupStorageDevice_Object = MibTableColumn
netupStorageDevice = _NetupStorageDevice_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3, 1, 2),
    _NetupStorageDevice_Type()
)
netupStorageDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupStorageDevice.setStatus("current")
_NetupStorageMountPoint_Type = OctetString
_NetupStorageMountPoint_Object = MibTableColumn
netupStorageMountPoint = _NetupStorageMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3, 1, 3),
    _NetupStorageMountPoint_Type()
)
netupStorageMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupStorageMountPoint.setStatus("current")
_NetupStorageFilesystem_Type = OctetString
_NetupStorageFilesystem_Object = MibTableColumn
netupStorageFilesystem = _NetupStorageFilesystem_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3, 1, 4),
    _NetupStorageFilesystem_Type()
)
netupStorageFilesystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupStorageFilesystem.setStatus("current")


class _NetupStorageBlockSize_Type(Integer32):
    """Custom type netupStorageBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetupStorageBlockSize_Type.__name__ = "Integer32"
_NetupStorageBlockSize_Object = MibTableColumn
netupStorageBlockSize = _NetupStorageBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3, 1, 5),
    _NetupStorageBlockSize_Type()
)
netupStorageBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupStorageBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    netupStorageBlockSize.setUnits("Bytes")


class _NetupStorageFragmentSize_Type(Integer32):
    """Custom type netupStorageFragmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetupStorageFragmentSize_Type.__name__ = "Integer32"
_NetupStorageFragmentSize_Object = MibTableColumn
netupStorageFragmentSize = _NetupStorageFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3, 1, 6),
    _NetupStorageFragmentSize_Type()
)
netupStorageFragmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupStorageFragmentSize.setStatus("current")
if mibBuilder.loadTexts:
    netupStorageFragmentSize.setUnits("Bytes")


class _NetupStorageSize_Type(Integer32):
    """Custom type netupStorageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetupStorageSize_Type.__name__ = "Integer32"
_NetupStorageSize_Object = MibTableColumn
netupStorageSize = _NetupStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3, 1, 7),
    _NetupStorageSize_Type()
)
netupStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupStorageSize.setStatus("current")
if mibBuilder.loadTexts:
    netupStorageSize.setUnits("fragments")


class _NetupStorageFree_Type(Integer32):
    """Custom type netupStorageFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetupStorageFree_Type.__name__ = "Integer32"
_NetupStorageFree_Object = MibTableColumn
netupStorageFree = _NetupStorageFree_Object(
    (1, 3, 6, 1, 4, 1, 39054, 1, 3, 1, 8),
    _NetupStorageFree_Type()
)
netupStorageFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupStorageFree.setStatus("current")
if mibBuilder.loadTexts:
    netupStorageFree.setUnits("blocks")
_NetupIptv_ObjectIdentity = ObjectIdentity
netupIptv = _NetupIptv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39054, 2)
)
if mibBuilder.loadTexts:
    netupIptv.setStatus("current")
_NetupConnectedClients_ObjectIdentity = ObjectIdentity
netupConnectedClients = _NetupConnectedClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39054, 2, 1)
)
if mibBuilder.loadTexts:
    netupConnectedClients.setStatus("current")


class _NetupStbClients_Type(Integer32):
    """Custom type netupStbClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetupStbClients_Type.__name__ = "Integer32"
_NetupStbClients_Object = MibScalar
netupStbClients = _NetupStbClients_Object(
    (1, 3, 6, 1, 4, 1, 39054, 2, 1, 1),
    _NetupStbClients_Type()
)
netupStbClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupStbClients.setStatus("current")


class _NetupPcClients_Type(Integer32):
    """Custom type netupPcClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetupPcClients_Type.__name__ = "Integer32"
_NetupPcClients_Object = MibScalar
netupPcClients = _NetupPcClients_Object(
    (1, 3, 6, 1, 4, 1, 39054, 2, 1, 2),
    _NetupPcClients_Type()
)
netupPcClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupPcClients.setStatus("current")


class _NetupTotalClients_Type(Integer32):
    """Custom type netupTotalClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetupTotalClients_Type.__name__ = "Integer32"
_NetupTotalClients_Object = MibScalar
netupTotalClients = _NetupTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 39054, 2, 1, 3),
    _NetupTotalClients_Type()
)
netupTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netupTotalClients.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETUP-MIB",
    **{"netup": netup,
       "netupHost": netupHost,
       "netupCpuTable": netupCpuTable,
       "netupCpuEntry": netupCpuEntry,
       "netupCpuIndex": netupCpuIndex,
       "netupCpuLoad": netupCpuLoad,
       "netupCpuTemp": netupCpuTemp,
       "netupMemory": netupMemory,
       "netupMemPhisTotal": netupMemPhisTotal,
       "netupMemPhisFree": netupMemPhisFree,
       "netupMemPhisBuffers": netupMemPhisBuffers,
       "netupMemPhisCached": netupMemPhisCached,
       "netupMemSwapTotal": netupMemSwapTotal,
       "netupMemSwapFree": netupMemSwapFree,
       "netupStorageTable": netupStorageTable,
       "netupStorageEntry": netupStorageEntry,
       "netupStorageIndex": netupStorageIndex,
       "netupStorageDevice": netupStorageDevice,
       "netupStorageMountPoint": netupStorageMountPoint,
       "netupStorageFilesystem": netupStorageFilesystem,
       "netupStorageBlockSize": netupStorageBlockSize,
       "netupStorageFragmentSize": netupStorageFragmentSize,
       "netupStorageSize": netupStorageSize,
       "netupStorageFree": netupStorageFree,
       "netupIptv": netupIptv,
       "netupConnectedClients": netupConnectedClients,
       "netupStbClients": netupStbClients,
       "netupPcClients": netupPcClients,
       "netupTotalClients": netupTotalClients}
)
