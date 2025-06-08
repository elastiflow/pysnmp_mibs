# SNMP MIB module (CISCO-CDSTV-AUTHMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-CDSTV-AUTHMGR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:52:32 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLStringOrEmpty,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLStringOrEmpty")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCdstvAuthmgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 751)
)
if mibBuilder.loadTexts:
    ciscoCdstvAuthmgrMIB.setRevisions(
        ("2010-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdstvAuthMgrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdstvAuthMgrMIBNotifs = _CiscoCdstvAuthMgrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 0)
)
_CiscoCdstvAuthMgrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdstvAuthMgrMIBObjects = _CiscoCdstvAuthMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1)
)
_CdstvAuthMgrAddressType_Type = InetAddressType
_CdstvAuthMgrAddressType_Object = MibScalar
cdstvAuthMgrAddressType = _CdstvAuthMgrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1, 1),
    _CdstvAuthMgrAddressType_Type()
)
cdstvAuthMgrAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvAuthMgrAddressType.setStatus("current")
_CdstvAuthMgrAddress_Type = InetAddress
_CdstvAuthMgrAddress_Object = MibScalar
cdstvAuthMgrAddress = _CdstvAuthMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1, 2),
    _CdstvAuthMgrAddress_Type()
)
cdstvAuthMgrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvAuthMgrAddress.setStatus("current")


class _CdstvAuthMgrPort_Type(InetPortNumber):
    """Custom type cdstvAuthMgrPort based on InetPortNumber"""
    defaultValue = 7792


_CdstvAuthMgrPort_Type.__name__ = "InetPortNumber"
_CdstvAuthMgrPort_Object = MibScalar
cdstvAuthMgrPort = _CdstvAuthMgrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1, 3),
    _CdstvAuthMgrPort_Type()
)
cdstvAuthMgrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvAuthMgrPort.setStatus("current")
_CdstvAuthMgrEventIsAddressType_Type = InetAddressType
_CdstvAuthMgrEventIsAddressType_Object = MibScalar
cdstvAuthMgrEventIsAddressType = _CdstvAuthMgrEventIsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1, 4),
    _CdstvAuthMgrEventIsAddressType_Type()
)
cdstvAuthMgrEventIsAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvAuthMgrEventIsAddressType.setStatus("current")
_CdstvAuthMgrEventIsAddress_Type = InetAddress
_CdstvAuthMgrEventIsAddress_Object = MibScalar
cdstvAuthMgrEventIsAddress = _CdstvAuthMgrEventIsAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1, 5),
    _CdstvAuthMgrEventIsAddress_Type()
)
cdstvAuthMgrEventIsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvAuthMgrEventIsAddress.setStatus("current")
_CdstvAuthMgrEventIsPort_Type = InetPortNumber
_CdstvAuthMgrEventIsPort_Object = MibScalar
cdstvAuthMgrEventIsPort = _CdstvAuthMgrEventIsPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1, 6),
    _CdstvAuthMgrEventIsPort_Type()
)
cdstvAuthMgrEventIsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvAuthMgrEventIsPort.setStatus("current")
_CdstvAuthMgrTraxisSoapInterface_Type = CiscoURLStringOrEmpty
_CdstvAuthMgrTraxisSoapInterface_Object = MibScalar
cdstvAuthMgrTraxisSoapInterface = _CdstvAuthMgrTraxisSoapInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1, 7),
    _CdstvAuthMgrTraxisSoapInterface_Type()
)
cdstvAuthMgrTraxisSoapInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvAuthMgrTraxisSoapInterface.setStatus("current")


class _CdstvAuthMgrServerThreadPool_Type(Unsigned32):
    """Custom type cdstvAuthMgrServerThreadPool based on Unsigned32"""
    defaultValue = 5


_CdstvAuthMgrServerThreadPool_Type.__name__ = "Unsigned32"
_CdstvAuthMgrServerThreadPool_Object = MibScalar
cdstvAuthMgrServerThreadPool = _CdstvAuthMgrServerThreadPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1, 8),
    _CdstvAuthMgrServerThreadPool_Type()
)
cdstvAuthMgrServerThreadPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvAuthMgrServerThreadPool.setStatus("current")


class _CdstvAuthMgrDebugLevel_Type(Integer32):
    """Custom type cdstvAuthMgrDebugLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("low", 2),
          ("high", 3))
    )


_CdstvAuthMgrDebugLevel_Type.__name__ = "Integer32"
_CdstvAuthMgrDebugLevel_Object = MibScalar
cdstvAuthMgrDebugLevel = _CdstvAuthMgrDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 1, 9),
    _CdstvAuthMgrDebugLevel_Type()
)
cdstvAuthMgrDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvAuthMgrDebugLevel.setStatus("current")
_CiscoCdstvAuthMgrMIBConform_ObjectIdentity = ObjectIdentity
ciscoCdstvAuthMgrMIBConform = _CiscoCdstvAuthMgrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 2)
)
_CiscoCdstvAuthMgrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdstvAuthMgrMIBCompliances = _CiscoCdstvAuthMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 2, 1)
)
_CiscoCdstvAuthMgrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdstvAuthMgrMIBGroups = _CiscoCdstvAuthMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 2, 2)
)

# Managed Objects groups

ciscoCdstvAuthMgrMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 2, 2, 1)
)
ciscoCdstvAuthMgrMIBMainObjectGroup.setObjects(
      *(("CISCO-CDSTV-AUTHMGR-MIB", "cdstvAuthMgrAddress"),
        ("CISCO-CDSTV-AUTHMGR-MIB", "cdstvAuthMgrPort"),
        ("CISCO-CDSTV-AUTHMGR-MIB", "cdstvAuthMgrEventIsPort"),
        ("CISCO-CDSTV-AUTHMGR-MIB", "cdstvAuthMgrTraxisSoapInterface"),
        ("CISCO-CDSTV-AUTHMGR-MIB", "cdstvAuthMgrServerThreadPool"),
        ("CISCO-CDSTV-AUTHMGR-MIB", "cdstvAuthMgrDebugLevel"),
        ("CISCO-CDSTV-AUTHMGR-MIB", "cdstvAuthMgrAddressType"),
        ("CISCO-CDSTV-AUTHMGR-MIB", "cdstvAuthMgrEventIsAddressType"),
        ("CISCO-CDSTV-AUTHMGR-MIB", "cdstvAuthMgrEventIsAddress"))
)
if mibBuilder.loadTexts:
    ciscoCdstvAuthMgrMIBMainObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdstvAuthMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 751, 2, 1, 1)
)
ciscoCdstvAuthMgrMIBCompliance.setObjects(
    ("CISCO-CDSTV-AUTHMGR-MIB", "ciscoCdstvAuthMgrMIBMainObjectGroup")
)
if mibBuilder.loadTexts:
    ciscoCdstvAuthMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDSTV-AUTHMGR-MIB",
    **{"ciscoCdstvAuthmgrMIB": ciscoCdstvAuthmgrMIB,
       "ciscoCdstvAuthMgrMIBNotifs": ciscoCdstvAuthMgrMIBNotifs,
       "ciscoCdstvAuthMgrMIBObjects": ciscoCdstvAuthMgrMIBObjects,
       "cdstvAuthMgrAddressType": cdstvAuthMgrAddressType,
       "cdstvAuthMgrAddress": cdstvAuthMgrAddress,
       "cdstvAuthMgrPort": cdstvAuthMgrPort,
       "cdstvAuthMgrEventIsAddressType": cdstvAuthMgrEventIsAddressType,
       "cdstvAuthMgrEventIsAddress": cdstvAuthMgrEventIsAddress,
       "cdstvAuthMgrEventIsPort": cdstvAuthMgrEventIsPort,
       "cdstvAuthMgrTraxisSoapInterface": cdstvAuthMgrTraxisSoapInterface,
       "cdstvAuthMgrServerThreadPool": cdstvAuthMgrServerThreadPool,
       "cdstvAuthMgrDebugLevel": cdstvAuthMgrDebugLevel,
       "ciscoCdstvAuthMgrMIBConform": ciscoCdstvAuthMgrMIBConform,
       "ciscoCdstvAuthMgrMIBCompliances": ciscoCdstvAuthMgrMIBCompliances,
       "ciscoCdstvAuthMgrMIBCompliance": ciscoCdstvAuthMgrMIBCompliance,
       "ciscoCdstvAuthMgrMIBGroups": ciscoCdstvAuthMgrMIBGroups,
       "ciscoCdstvAuthMgrMIBMainObjectGroup": ciscoCdstvAuthMgrMIBMainObjectGroup}
)
