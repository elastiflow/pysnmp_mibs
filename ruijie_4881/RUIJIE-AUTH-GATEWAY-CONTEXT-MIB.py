# SNMP MIB module (RUIJIE-AUTH-GATEWAY-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-AUTH-GATEWAY-CONTEXT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:23 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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


# MODULE-IDENTITY

ruijieWebAuthVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67)
)
if mibBuilder.loadTexts:
    ruijieWebAuthVCMIB.setRevisions(
        ("2009-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieWebAuthVCMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWebAuthVCMIBObjects = _RuijieWebAuthVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 1)
)
_RuijieWebAuthUserVCTable_Object = MibTable
ruijieWebAuthUserVCTable = _RuijieWebAuthUserVCTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserVCTable.setStatus("current")
_RuijieWebAuthUserVCEntry_Object = MibTableRow
ruijieWebAuthUserVCEntry = _RuijieWebAuthUserVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 1, 1, 1)
)
ruijieWebAuthUserVCEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-CONTEXT-MIB", "authUserContextNameVC"),
    (0, "RUIJIE-AUTH-GATEWAY-CONTEXT-MIB", "authUserIpAddrVC"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserVCEntry.setStatus("current")


class _AuthUserContextNameVC_Type(DisplayString):
    """Custom type authUserContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AuthUserContextNameVC_Type.__name__ = "DisplayString"
_AuthUserContextNameVC_Object = MibTableColumn
authUserContextNameVC = _AuthUserContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 1, 1, 1, 1),
    _AuthUserContextNameVC_Type()
)
authUserContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserContextNameVC.setStatus("current")
_AuthUserIpAddrVC_Type = IpAddress
_AuthUserIpAddrVC_Object = MibTableColumn
authUserIpAddrVC = _AuthUserIpAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 1, 1, 1, 2),
    _AuthUserIpAddrVC_Type()
)
authUserIpAddrVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserIpAddrVC.setStatus("current")
_AuthUserOnlineFlagVC_Type = Gauge32
_AuthUserOnlineFlagVC_Object = MibTableColumn
authUserOnlineFlagVC = _AuthUserOnlineFlagVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 1, 1, 1, 3),
    _AuthUserOnlineFlagVC_Type()
)
authUserOnlineFlagVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserOnlineFlagVC.setStatus("current")
_AuthUserTimeLimitVC_Type = Gauge32
_AuthUserTimeLimitVC_Object = MibTableColumn
authUserTimeLimitVC = _AuthUserTimeLimitVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 1, 1, 1, 4),
    _AuthUserTimeLimitVC_Type()
)
authUserTimeLimitVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserTimeLimitVC.setStatus("current")
_AuthUserTimeUsedVC_Type = Gauge32
_AuthUserTimeUsedVC_Object = MibTableColumn
authUserTimeUsedVC = _AuthUserTimeUsedVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 1, 1, 1, 5),
    _AuthUserTimeUsedVC_Type()
)
authUserTimeUsedVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserTimeUsedVC.setStatus("current")
_AuthUserStatusVC_Type = RowStatus
_AuthUserStatusVC_Object = MibTableColumn
authUserStatusVC = _AuthUserStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 1, 1, 1, 6),
    _AuthUserStatusVC_Type()
)
authUserStatusVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserStatusVC.setStatus("current")
_RuijieWebAuthVCMIBConformance_ObjectIdentity = ObjectIdentity
ruijieWebAuthVCMIBConformance = _RuijieWebAuthVCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 3)
)
_RuijieWebAuthVCMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieWebAuthVCMIBCompliances = _RuijieWebAuthVCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 3, 1)
)
_RuijieWebAuthVCMIBGroups_ObjectIdentity = ObjectIdentity
ruijieWebAuthVCMIBGroups = _RuijieWebAuthVCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 3, 2)
)

# Managed Objects groups

ruijieWebAuthVCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 3, 2, 1)
)
ruijieWebAuthVCMIBGroup.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-CONTEXT-MIB", "authUserContextNameVC"),
        ("RUIJIE-AUTH-GATEWAY-CONTEXT-MIB", "authUserIpAddrVC"),
        ("RUIJIE-AUTH-GATEWAY-CONTEXT-MIB", "authUserOnlineFlagVC"),
        ("RUIJIE-AUTH-GATEWAY-CONTEXT-MIB", "authUserTimeLimitVC"),
        ("RUIJIE-AUTH-GATEWAY-CONTEXT-MIB", "authUserTimeUsedVC"),
        ("RUIJIE-AUTH-GATEWAY-CONTEXT-MIB", "authUserStatusVC"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthVCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieWebAuthVCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 67, 3, 1, 1)
)
ruijieWebAuthVCMIBCompliance.setObjects(
    ("RUIJIE-AUTH-GATEWAY-CONTEXT-MIB", "ruijieWebAuthVCMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieWebAuthVCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-AUTH-GATEWAY-CONTEXT-MIB",
    **{"ruijieWebAuthVCMIB": ruijieWebAuthVCMIB,
       "ruijieWebAuthVCMIBObjects": ruijieWebAuthVCMIBObjects,
       "ruijieWebAuthUserVCTable": ruijieWebAuthUserVCTable,
       "ruijieWebAuthUserVCEntry": ruijieWebAuthUserVCEntry,
       "authUserContextNameVC": authUserContextNameVC,
       "authUserIpAddrVC": authUserIpAddrVC,
       "authUserOnlineFlagVC": authUserOnlineFlagVC,
       "authUserTimeLimitVC": authUserTimeLimitVC,
       "authUserTimeUsedVC": authUserTimeUsedVC,
       "authUserStatusVC": authUserStatusVC,
       "ruijieWebAuthVCMIBConformance": ruijieWebAuthVCMIBConformance,
       "ruijieWebAuthVCMIBCompliances": ruijieWebAuthVCMIBCompliances,
       "ruijieWebAuthVCMIBCompliance": ruijieWebAuthVCMIBCompliance,
       "ruijieWebAuthVCMIBGroups": ruijieWebAuthVCMIBGroups,
       "ruijieWebAuthVCMIBGroup": ruijieWebAuthVCMIBGroup}
)
