# SNMP MIB module (VARMOUR-HA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/varmour_42825/VARMOUR-HA-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:54 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(varmourMibs,) = mibBuilder.importSymbols(
    "VARMOUR-SMI",
    "varmourMibs")

(VarmourDevice,) = mibBuilder.importSymbols(
    "VARMOUR-TC",
    "VarmourDevice")


# MODULE-IDENTITY

varmour_ha = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VaHighAvail_ObjectIdentity = ObjectIdentity
vaHighAvail = _VaHighAvail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 2, 1)
)
_VaHaGroupId_Type = Integer32
_VaHaGroupId_Object = MibScalar
vaHaGroupId = _VaHaGroupId_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 2, 1, 1),
    _VaHaGroupId_Type()
)
vaHaGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaHaGroupId.setStatus("current")


class _VaHaMgmtVip_Type(OctetString):
    """Custom type vaHaMgmtVip based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaHaMgmtVip_Type.__name__ = "OctetString"
_VaHaMgmtVip_Object = MibScalar
vaHaMgmtVip = _VaHaMgmtVip_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 2, 1, 2),
    _VaHaMgmtVip_Type()
)
vaHaMgmtVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaHaMgmtVip.setStatus("current")


class _VaHaFabLinkIp_Type(OctetString):
    """Custom type vaHaFabLinkIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaHaFabLinkIp_Type.__name__ = "OctetString"
_VaHaFabLinkIp_Object = MibScalar
vaHaFabLinkIp = _VaHaFabLinkIp_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 2, 1, 3),
    _VaHaFabLinkIp_Type()
)
vaHaFabLinkIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaHaFabLinkIp.setStatus("current")


class _VaHaFailoverStatus_Type(OctetString):
    """Custom type vaHaFailoverStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaHaFailoverStatus_Type.__name__ = "OctetString"
_VaHaFailoverStatus_Object = MibScalar
vaHaFailoverStatus = _VaHaFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 2, 1, 4),
    _VaHaFailoverStatus_Type()
)
vaHaFailoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaHaFailoverStatus.setStatus("current")


class _VaHaPreempt_Type(OctetString):
    """Custom type vaHaPreempt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaHaPreempt_Type.__name__ = "OctetString"
_VaHaPreempt_Object = MibScalar
vaHaPreempt = _VaHaPreempt_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 2, 1, 5),
    _VaHaPreempt_Type()
)
vaHaPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaHaPreempt.setStatus("current")


class _VaHaTrackFabDownTime_Type(OctetString):
    """Custom type vaHaTrackFabDownTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaHaTrackFabDownTime_Type.__name__ = "OctetString"
_VaHaTrackFabDownTime_Object = MibScalar
vaHaTrackFabDownTime = _VaHaTrackFabDownTime_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 2, 1, 6),
    _VaHaTrackFabDownTime_Type()
)
vaHaTrackFabDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaHaTrackFabDownTime.setStatus("current")


class _VaHaArpNum_Type(OctetString):
    """Custom type vaHaArpNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaHaArpNum_Type.__name__ = "OctetString"
_VaHaArpNum_Object = MibScalar
vaHaArpNum = _VaHaArpNum_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 2, 1, 7),
    _VaHaArpNum_Type()
)
vaHaArpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaHaArpNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VARMOUR-HA-MIB",
    **{"varmour-ha": varmour_ha,
       "vaHighAvail": vaHighAvail,
       "vaHaGroupId": vaHaGroupId,
       "vaHaMgmtVip": vaHaMgmtVip,
       "vaHaFabLinkIp": vaHaFabLinkIp,
       "vaHaFailoverStatus": vaHaFailoverStatus,
       "vaHaPreempt": vaHaPreempt,
       "vaHaTrackFabDownTime": vaHaTrackFabDownTime,
       "vaHaArpNum": vaHaArpNum}
)
