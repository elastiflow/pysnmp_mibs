# SNMP MIB module (ZYXEL-ANTI-ARPSCAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ANTI-ARPSCAN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:30:51 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelAntiArpscan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelAntiArpscanSetup_ObjectIdentity = ObjectIdentity
zyxelAntiArpscanSetup = _ZyxelAntiArpscanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1)
)
_ZyAntiArpscanState_Type = EnabledStatus
_ZyAntiArpscanState_Object = MibScalar
zyAntiArpscanState = _ZyAntiArpscanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 1),
    _ZyAntiArpscanState_Type()
)
zyAntiArpscanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAntiArpscanState.setStatus("current")


class _ZyAntiArpscanPortThreshold_Type(Integer32):
    """Custom type zyAntiArpscanPortThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ZyAntiArpscanPortThreshold_Type.__name__ = "Integer32"
_ZyAntiArpscanPortThreshold_Object = MibScalar
zyAntiArpscanPortThreshold = _ZyAntiArpscanPortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 2),
    _ZyAntiArpscanPortThreshold_Type()
)
zyAntiArpscanPortThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAntiArpscanPortThreshold.setStatus("current")


class _ZyAntiArpscanHostThreshold_Type(Integer32):
    """Custom type zyAntiArpscanHostThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_ZyAntiArpscanHostThreshold_Type.__name__ = "Integer32"
_ZyAntiArpscanHostThreshold_Object = MibScalar
zyAntiArpscanHostThreshold = _ZyAntiArpscanHostThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 3),
    _ZyAntiArpscanHostThreshold_Type()
)
zyAntiArpscanHostThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAntiArpscanHostThreshold.setStatus("current")
_ZyxelAntiArpscanPortTable_Object = MibTable
zyxelAntiArpscanPortTable = _ZyxelAntiArpscanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelAntiArpscanPortTable.setStatus("current")
_ZyxelAntiArpscanPortEntry_Object = MibTableRow
zyxelAntiArpscanPortEntry = _ZyxelAntiArpscanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 4, 1)
)
zyxelAntiArpscanPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelAntiArpscanPortEntry.setStatus("current")


class _ZyAntiArpscanPortTrustState_Type(Integer32):
    """Custom type zyAntiArpscanPortTrustState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_ZyAntiArpscanPortTrustState_Type.__name__ = "Integer32"
_ZyAntiArpscanPortTrustState_Object = MibTableColumn
zyAntiArpscanPortTrustState = _ZyAntiArpscanPortTrustState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 4, 1, 1),
    _ZyAntiArpscanPortTrustState_Type()
)
zyAntiArpscanPortTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAntiArpscanPortTrustState.setStatus("current")
_ZyAntiArpscanMaxNumberOfTrustHosts_Type = Integer32
_ZyAntiArpscanMaxNumberOfTrustHosts_Object = MibScalar
zyAntiArpscanMaxNumberOfTrustHosts = _ZyAntiArpscanMaxNumberOfTrustHosts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 5),
    _ZyAntiArpscanMaxNumberOfTrustHosts_Type()
)
zyAntiArpscanMaxNumberOfTrustHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAntiArpscanMaxNumberOfTrustHosts.setStatus("current")
_ZyxelAntiArpscanTrustHostTable_Object = MibTable
zyxelAntiArpscanTrustHostTable = _ZyxelAntiArpscanTrustHostTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelAntiArpscanTrustHostTable.setStatus("current")
_ZyxelAntiArpscanTrustHostEntry_Object = MibTableRow
zyxelAntiArpscanTrustHostEntry = _ZyxelAntiArpscanTrustHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 6, 1)
)
zyxelAntiArpscanTrustHostEntry.setIndexNames(
    (0, "ZYXEL-ANTI-ARPSCAN-MIB", "zyAntiArpscanTrustHostIpAddress"),
    (0, "ZYXEL-ANTI-ARPSCAN-MIB", "zyAntiArpscanTrustHostMask"),
)
if mibBuilder.loadTexts:
    zyxelAntiArpscanTrustHostEntry.setStatus("current")
_ZyAntiArpscanTrustHostIpAddress_Type = IpAddress
_ZyAntiArpscanTrustHostIpAddress_Object = MibTableColumn
zyAntiArpscanTrustHostIpAddress = _ZyAntiArpscanTrustHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 6, 1, 1),
    _ZyAntiArpscanTrustHostIpAddress_Type()
)
zyAntiArpscanTrustHostIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAntiArpscanTrustHostIpAddress.setStatus("current")
_ZyAntiArpscanTrustHostMask_Type = IpAddress
_ZyAntiArpscanTrustHostMask_Object = MibTableColumn
zyAntiArpscanTrustHostMask = _ZyAntiArpscanTrustHostMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 6, 1, 2),
    _ZyAntiArpscanTrustHostMask_Type()
)
zyAntiArpscanTrustHostMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAntiArpscanTrustHostMask.setStatus("current")
_ZyAntiArpscanTrustHostName_Type = DisplayString
_ZyAntiArpscanTrustHostName_Object = MibTableColumn
zyAntiArpscanTrustHostName = _ZyAntiArpscanTrustHostName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 6, 1, 3),
    _ZyAntiArpscanTrustHostName_Type()
)
zyAntiArpscanTrustHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAntiArpscanTrustHostName.setStatus("current")
_ZyAntiArpscanTrustHostRowStatus_Type = RowStatus
_ZyAntiArpscanTrustHostRowStatus_Object = MibTableColumn
zyAntiArpscanTrustHostRowStatus = _ZyAntiArpscanTrustHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 1, 6, 1, 4),
    _ZyAntiArpscanTrustHostRowStatus_Type()
)
zyAntiArpscanTrustHostRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAntiArpscanTrustHostRowStatus.setStatus("current")
_ZyxelAntiArpscanStatus_ObjectIdentity = ObjectIdentity
zyxelAntiArpscanStatus = _ZyxelAntiArpscanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 2)
)
_ZyAntiArpscanHostClear_Type = Integer32
_ZyAntiArpscanHostClear_Object = MibScalar
zyAntiArpscanHostClear = _ZyAntiArpscanHostClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 2, 1),
    _ZyAntiArpscanHostClear_Type()
)
zyAntiArpscanHostClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAntiArpscanHostClear.setStatus("current")
_ZyxelAntiArpscanHostTable_Object = MibTable
zyxelAntiArpscanHostTable = _ZyxelAntiArpscanHostTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelAntiArpscanHostTable.setStatus("current")
_ZyxelAntiArpscanHostEntry_Object = MibTableRow
zyxelAntiArpscanHostEntry = _ZyxelAntiArpscanHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 2, 2, 1)
)
zyxelAntiArpscanHostEntry.setIndexNames(
    (0, "ZYXEL-ANTI-ARPSCAN-MIB", "zyAntiArpscanHostMacAddress"),
    (0, "ZYXEL-ANTI-ARPSCAN-MIB", "zyAntiArpscanHostVid"),
)
if mibBuilder.loadTexts:
    zyxelAntiArpscanHostEntry.setStatus("current")
_ZyAntiArpscanHostMacAddress_Type = MacAddress
_ZyAntiArpscanHostMacAddress_Object = MibTableColumn
zyAntiArpscanHostMacAddress = _ZyAntiArpscanHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 2, 2, 1, 1),
    _ZyAntiArpscanHostMacAddress_Type()
)
zyAntiArpscanHostMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAntiArpscanHostMacAddress.setStatus("current")


class _ZyAntiArpscanHostVid_Type(Integer32):
    """Custom type zyAntiArpscanHostVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyAntiArpscanHostVid_Type.__name__ = "Integer32"
_ZyAntiArpscanHostVid_Object = MibTableColumn
zyAntiArpscanHostVid = _ZyAntiArpscanHostVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 2, 2, 1, 2),
    _ZyAntiArpscanHostVid_Type()
)
zyAntiArpscanHostVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAntiArpscanHostVid.setStatus("current")
_ZyAntiArpscanHostPort_Type = Integer32
_ZyAntiArpscanHostPort_Object = MibTableColumn
zyAntiArpscanHostPort = _ZyAntiArpscanHostPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 2, 2, 1, 3),
    _ZyAntiArpscanHostPort_Type()
)
zyAntiArpscanHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAntiArpscanHostPort.setStatus("current")
_ZyAntiArpscanHostIpAddress_Type = IpAddress
_ZyAntiArpscanHostIpAddress_Object = MibTableColumn
zyAntiArpscanHostIpAddress = _ZyAntiArpscanHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 2, 2, 1, 4),
    _ZyAntiArpscanHostIpAddress_Type()
)
zyAntiArpscanHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAntiArpscanHostIpAddress.setStatus("current")


class _ZyAntiArpscanHostStatus_Type(Integer32):
    """Custom type zyAntiArpscanHostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("errDisable", 2)
    )


_ZyAntiArpscanHostStatus_Type.__name__ = "Integer32"
_ZyAntiArpscanHostStatus_Object = MibTableColumn
zyAntiArpscanHostStatus = _ZyAntiArpscanHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 106, 2, 2, 1, 5),
    _ZyAntiArpscanHostStatus_Type()
)
zyAntiArpscanHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAntiArpscanHostStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ANTI-ARPSCAN-MIB",
    **{"zyxelAntiArpscan": zyxelAntiArpscan,
       "zyxelAntiArpscanSetup": zyxelAntiArpscanSetup,
       "zyAntiArpscanState": zyAntiArpscanState,
       "zyAntiArpscanPortThreshold": zyAntiArpscanPortThreshold,
       "zyAntiArpscanHostThreshold": zyAntiArpscanHostThreshold,
       "zyxelAntiArpscanPortTable": zyxelAntiArpscanPortTable,
       "zyxelAntiArpscanPortEntry": zyxelAntiArpscanPortEntry,
       "zyAntiArpscanPortTrustState": zyAntiArpscanPortTrustState,
       "zyAntiArpscanMaxNumberOfTrustHosts": zyAntiArpscanMaxNumberOfTrustHosts,
       "zyxelAntiArpscanTrustHostTable": zyxelAntiArpscanTrustHostTable,
       "zyxelAntiArpscanTrustHostEntry": zyxelAntiArpscanTrustHostEntry,
       "zyAntiArpscanTrustHostIpAddress": zyAntiArpscanTrustHostIpAddress,
       "zyAntiArpscanTrustHostMask": zyAntiArpscanTrustHostMask,
       "zyAntiArpscanTrustHostName": zyAntiArpscanTrustHostName,
       "zyAntiArpscanTrustHostRowStatus": zyAntiArpscanTrustHostRowStatus,
       "zyxelAntiArpscanStatus": zyxelAntiArpscanStatus,
       "zyAntiArpscanHostClear": zyAntiArpscanHostClear,
       "zyxelAntiArpscanHostTable": zyxelAntiArpscanHostTable,
       "zyxelAntiArpscanHostEntry": zyxelAntiArpscanHostEntry,
       "zyAntiArpscanHostMacAddress": zyAntiArpscanHostMacAddress,
       "zyAntiArpscanHostVid": zyAntiArpscanHostVid,
       "zyAntiArpscanHostPort": zyAntiArpscanHostPort,
       "zyAntiArpscanHostIpAddress": zyAntiArpscanHostIpAddress,
       "zyAntiArpscanHostStatus": zyAntiArpscanHostStatus}
)
